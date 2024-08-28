class Category:
    def __init__(self, name):
        self.ledger = []
        self.name = name

    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=''):
        is_enough_funds = self.check_funds(amount)
        if is_enough_funds:
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        else:
            return False

    def get_balance(self):
        balance = 0
        for entry in self.ledger:
            balance += entry['amount']
        return balance

    def transfer(self, amount, destination):
        is_enough_funds = self.withdraw(
            amount, f'Transfer to {destination.name}')
        if is_enough_funds:
            destination.deposit(amount, f'Transfer from {self.name}')
            return True
        else:
            return False

    def __str__(self):
        title = fill_centered(self.name, width=30, symbol='*')
        list = [
            f'{entry["description"] if len(entry["description"]) <= 23 else entry["description"][:23]:<23}{entry["amount"]:>7.2f}' for entry in self.ledger]

        total = 'Total: ' + str(self.get_balance())
        return title + '\n' + '\n'.join(list) + '\n' + total

    def __repr__(self):
        return self.__str__()

    def check_funds(self, amount):
        sum = 0
        for entry in self.ledger:
            sum += entry['amount']
            if sum >= amount:
                return True
        return False

    def get_spend(self):
        return sum(entry['amount']
                   for entry in self.ledger if entry['amount'] < 0)


def create_spend_chart(categories):
    title_text = 'Percentage spent by category'
    chart = [[f'{level:>3}|'] for level in range(100, -10, -10)]
    horizontal_line = '    ' + '-' * len(categories) * 3 + '-'
    max_name_len = max(len(category.name) for category in categories)
    total_spent = sum(category.get_spend() for category in categories)

    for category in categories:
        spent_by_category = category.get_spend()
        percentage = abs(100 * spent_by_category / total_spent)
        for i in range(100, -10, -10):
            if percentage >= i:
                chart[int((100-i)/10)].append(' o ')
            else:
                chart[int((100-i)/10)].append('   ')

    for i in range(len(chart)):
        chart[i].append(' ')
    categories_names = []
    for i in range(max_name_len):
        categories_names.append('')
        for j in range(len(categories)):
            if len(categories[j].name) > i:
                categories_names[i] += ' ' + categories[j].name[i] + ' '
            else:
                categories_names[i] += '   '
            categories_names[i] = f'{categories_names[i]:>7}'
        categories_names[i] = categories_names[i] + ' '

    return title_text + '\n' + '\n'.join(''.join(row) for row in chart) + '\n' + horizontal_line + '\n' + '\n'.join(categories_names)


def fill_centered(text, width, symbol=' '):
    spaces_to_add = symbol * int((width - len(text)) / 2)
    return spaces_to_add + text + spaces_to_add


food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)

print(food)
print(create_spend_chart([food, clothing]))

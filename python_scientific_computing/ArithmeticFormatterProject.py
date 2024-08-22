def arithmetic_arranger(problems, show_answers=False):
    line_a = []
    line_b = []
    line_c = []
    line_d = []

    if len(problems) > 5:
        return 'Error: Too many problems.'

    for i in range(0, len(problems)):
        error, a, operator, b = validate_problem(problems[i])
        if error:
            return error
        result = operate(a, operator, b)
        operands_to_fill = [a, b]
        filled_operands, result = fill_if_necessary(operands_to_fill, result)
        a = filled_operands[0]
        b = filled_operands[1]
        append_to_line(line_a, ' ', a)
        append_to_line(line_b, operator, b)
        append_bar_to_line(line_c, len(a))
        append_to_line(line_d, '', result)

    lines = [line_a, line_b, line_c]

    if show_answers:
        lines.append(line_d)

    text = create_text(lines)
    return text


def validate_problem(problem):
    problem_error = None
    a, operator, b = problem.split(' ')

    if operator != '+' and operator != '-':
        problem_error = "Error: Operator must be '+' or '-'."

    if not a.isdigit() or not b.isdigit():
        problem_error = 'Error: Numbers must only contain digits.'

    if len(a) > 4 or len(b) > 4:
        problem_error = 'Error: Numbers cannot be more than four digits.'

    return problem_error, a, operator, b


def fill_if_necessary(operands, result):
    max_size = get_max_size(operands)
    filled_operands = fill_operands(operands, max_size)
    filled_result = fill_string(str(result), max_size + 1)
    return filled_operands, filled_result


def get_max_size(operands):
    return max(map(lambda op: len(op),  operands))


def fill_operands(operands, max_size):
    filled_operands = []
    for i in range(0, len(operands)):
        operand = operands[i]
        spaces_to_add = ' ' * (max_size - len(operand))
        filled_operands.append(spaces_to_add + operand)
    return filled_operands


def fill_string(string, max_size):
    spaces_to_add = ' ' * (max_size - len(string))
    return spaces_to_add + string


def operate(operand_a, operator, operand_b):
    result = 0
    if operator == '+':
        result = int(operand_a) + int(operand_b)
    else:
        result = int(operand_a) - int(operand_b)
    return result


def append_to_line(line, operator, operand):
    line.append(operator + ' ' + operand + '    ')


def append_bar_to_line(line, length):
    line.append('-'*(length+2) + '    ')


def create_text(lines):
    text = ''
    for i in range(0, len(lines)):
        text = text + ''.join(lines[i])[:-4] + '\n'
    return text[:-1]


print(
    f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}'
)

print(
    f'\n{arithmetic_arranger(["3 + 8557", "988 + 4000"], True)}')

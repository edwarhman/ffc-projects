def arithmetic_arranger(problems, show_answers=False):
    error, lines = construct_text_lines(problems)
    if error:
        return error
    hide_last_line_if_needed(lines, show_answers)
    return format_text(lines)


def construct_text_lines(problems):
    lines = [[], [], [], []]
    if len(problems) > 5:
        return 'Error: Too many problems.', None
    for i in range(0, len(problems)):
        error, operands, operator = validate_problem(problems[i])
        if error:
            return error, None
        result = calc_problem_result(operands, operator)
        operands, result = fill_if_needed(operands, result)
        append_data_to_lines(lines, operator, operands, result)
    return None, lines


def validate_problem(problem):
    problem_error = None
    a, operator, b = problem.split(' ')

    if operator != '+' and operator != '-':
        problem_error = "Error: Operator must be '+' or '-'."

    if not a.isdigit() or not b.isdigit():
        problem_error = 'Error: Numbers must only contain digits.'

    if len(a) > 4 or len(b) > 4:
        problem_error = 'Error: Numbers cannot be more than four digits.'

    return problem_error, [a, b], operator


def fill_if_needed(operands, result):
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


def calc_problem_result(operands, operator):
    result = 0
    if operator == '+':
        result = int(operands[0]) + int(operands[1])
    else:
        result = int(operands[0]) - int(operands[1])
    return result


def append_data_to_lines(lines, operator, operands, result):
    a, b = operands
    append_operation_to_line(lines[0], ' ', a)
    append_operation_to_line(lines[1], operator, b)
    append_bar_to_line(lines[2], len(a))
    append_result_line(lines[3], result)


def append_operation_to_line(line, operator, operand):
    line.append(operator + ' ' + operand + '    ')


def append_result_line(line, result):
    append_operation_to_line(line, '', result)


def append_bar_to_line(line, length):
    line.append('-'*(length+2) + '    ')


def hide_last_line_if_needed(lines, show_answers):
    if not show_answers:
        lines.pop()


def format_text(lines):
    text = ''
    for i in range(0, len(lines)):
        text = text + ''.join(lines[i])[:-4] + '\n'
    return text[:-1]


print(
    f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}'
)

print(
    f'\n{arithmetic_arranger(["3 + 8557", "988 + 4000"], True)}')

def calculate(operands, operators):
    result = operands[0]
    for i, operator in enumerate(operators):
        if operator == '+':
            result += operands[i + 1]
        elif operator == '-':
            result -= operands[i + 1]
        elif operator == '*':
            result *= operands[i + 1]
        elif operator == '/':
            if result < 0:
                result = -(-result // operands[i + 1])
            else:
                result //= operands[i + 1]
    return result


def backtrack(operators, current_operators, counts, results, operands):
    if len(current_operators) == len(operands) - 1:
        result = calculate(operands, current_operators)
        results['max'] = max(results['max'], result)
        results['min'] = min(results['min'], result)
        return

    for i in range(4):
        if counts[i] > 0:
            counts[i] -= 1
            current_operators.append(operators[i])
            backtrack(operators, current_operators, counts, results, operands)
            counts[i] += 1
            current_operators.pop()


def solve(numbers, operator_count):
    operators = ['+', '-', '*', '/']
    results = {'max': -float('inf'), 'min': float('inf')}
    backtrack(operators, [], operator_count, results, numbers)
    return results['max'], results['min']


N = int(input())
numbers = list(map(int, input().split()))
operator_count = list(map(int, input().split()))

max_val, min_val = solve(numbers, operator_count)
print(max_val)
print(min_val)

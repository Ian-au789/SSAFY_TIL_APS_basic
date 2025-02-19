import sys
sys.stdin = open("input.txt")


def back_expression(formula):
    top = -1
    stack = [0]*len(formula)
    new_formula = []

    weight = {0: ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"], 1: ["+", "-"], 2: ["*", "/"]}

    for i in range(len(formula)):
        if formula[i] in weight[0]:
            new_formula.append(formula[i])

        elif formula[i] in weight[1]:
            if stack[top] in weight[2]:
                new_formula.append(stack[top])
                top -= 1

            top += 1
            stack[top] = formula[i]

        else:
            if stack[top] in weight[2]:
                new_formula.append(stack[top])
                top -= 1

            top += 1
            stack[top] = formula[i]

    while top > -1:
        new_formula.append(stack[top])
        top -= 1

    return "".join(new_formula)


def calculator(size, string):
    top = -1
    stack = [""] * size
    pass





for t in range(1, 11):
    N = int(input())
    expression_str = input()
    expression = back_expression(expression_str)

    print(expression)
    # print(f"#{t} {calculator(N, expression)}")

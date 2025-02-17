# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AZEvJfCqa1MDFAVs&probBoxId=AZTP3wYKXqvHBIRD&type=USER&problemBoxTitle=%2802.17%29+Stack2-1&problemBoxCnt=5

import sys
sys.stdin = open("4874_input.txt")


def forth_calculator(formula):
    stack = [""] * len(formula)
    top = -1
    operator = ["+", "-", "*", "/"]

    for n in formula:
        if n in operator:
            if type(stack[top]) == int and type(stack[top-1]) == int:    # 스택에 제일 마지막에 저장된 2개 값이 정수인지 확인
                # 각 연산자에 맞는 계산 실행하고 top -1
                if n == "+":
                    stack[top - 1] += stack[top]
                    top -= 1

                elif n == "-":
                    stack[top - 1] -= stack[top]
                    top -= 1

                elif n == "*":
                    stack[top-1] *= stack[top]
                    top -= 1

                else:
                    stack[top - 1] //= stack[top]
                    top -= 1

            else:                # 연산이 불가한 경우 에러
                return "error"

        elif n == ".":
            if top == 0:         # 모든 연산이 끝났을 때 저장된 정수를 모두 썼으므로 top = 0이어야 함
                return stack[top]
            else:                # 1 2 + 3 . 처럼 숫자만 주어지고 끝나는 연산도 있음 (에러)
                return "error"

        else:                    # 숫자는 스택에 저장
            top += 1
            stack[top] = int(n)


T = int(input())
for t in range(1, T+1):
    expression = list(map(str, input().split()))
    print(f"#{t} {forth_calculator(expression)}")

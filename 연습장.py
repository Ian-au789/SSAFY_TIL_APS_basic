def which_day(a, b):
    cnt = b-1
    for i in range(a):
        cnt += days_in_month[i]

    return day[cnt % 7]


day = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
days_in_month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

print(which_day(5, 24))


def press_keypad(numbers, hand):
    keypad = [[1, 4, 7], [2, 5, 8, 0], [3, 6, 9]]
    thumb = []
    left_thumb = [0, 3]
    right_thumb = [2, 3]

    for number in numbers:
        if number in keypad[0]:
            thumb.append("L")
            left_thumb = [0, (number - 1) // 3]

        elif number in keypad[2]:
            thumb.append("R")
            right_thumb = [2, (number // 3) - 1]

        else:
            for i in range(4):
                if number == keypad[1][i]:
                    left_distance = abs(left_thumb[1] - i) + abs(1 - left_thumb[0])
                    right_distance = abs(right_thumb[1] - i) + abs(1 - right_thumb[0])

                    if left_distance > right_distance:
                        thumb.append("R")
                        right_thumb = [1, i]

                    elif left_distance < right_distance:
                        thumb.append("L")
                        left_thumb = [1, i]

                    else:
                        if hand == "left":
                            thumb.append("L")
                            left_thumb = [1, i]
                        else:
                            thumb.append("R")
                            right_thumb = [1, i]

                    break

    return "".join(thumb)


print(press_keypad([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
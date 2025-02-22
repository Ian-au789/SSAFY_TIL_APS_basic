def back_to_room(rooms):
    corridor = [0] * 201  # 복도 번호는 1~200까지 사용

    for room in rooms:
        start = (room[0] + 1) // 2
        end = (room[1] + 1) // 2

        for i in range(start, end + 1):
            corridor[i] += 1  # 해당 복도를 이용하는 학생 증가

    return max(corridor)  # 가장 많이 사용된 복도의 횟수가 최소 시간


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    rooms = []

    for _ in range(N):
        room1, room2 = map(int, input().split())
        rooms.append((min(room1, room2), max(room1, room2)))  # 항상 작은 번호가 앞에 오도록 정렬

    print(f"#{t} {back_to_room(rooms)}")

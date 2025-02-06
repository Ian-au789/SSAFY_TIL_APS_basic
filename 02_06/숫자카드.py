
n = "49679"


def many_cards(card):

    card_list = []

    for i in range(len(card)):
        card_list.append(int(card[i]))

    counts = [0]*10

    for number in card_list:
        counts[number] += 1

    for i in range(9, -1, -1):
        if counts[i] == max(counts):
            return i, max(counts)


print(many_cards(n))

def all_subset(depth, included):
    if depth == len(input_list):
        subset = [input_list[i] for i in range(len(input_list)) if included[i]]
        subsets.append(subset)
        return

    included[depth] = True
    all_subset(depth+1, included)

    included[depth] = False
    all_subset(depth+1, included)

input_list = [1, 2, 3]
subsets = []
init_included = [False]*len(input_list)
all_subset(0, init_included)
print(subsets)
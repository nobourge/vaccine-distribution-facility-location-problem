def best_assigment(demand, capacity):
    total_demand = sum(demand)
    x = len(capacity)
    masks = [1 << i for i in range(x)]
    subsets = []
    for i in range(1, 1 << x):
        subset = []
        for mask, sss in zip(masks, capacity):

            if i & mask:

                subset.append(sss)
            else:
                subset.append(0)
        if total_demand <= sum(subset):
            for center in subset:
                # todo
        subsets.append(subset)


    return subsets


print(best_assigment(demand=[8, 13, 8, 9, 11, 9, 7],
                     capacity=[45, 30, 25, 20]
                     ))

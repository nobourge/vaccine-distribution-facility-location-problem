def get_assignements(capacity_subset,
                     demand,
                     travel_cost,
                     cost,
                     current_cost,
                     assigning=None,
                     i=0,
                     a = 0):
    global n
    global l
    global assignments

    if assigning is None:
        l = len(capacity_subset)
        n = len(demand)
        assigning = [-1] * n

    if i == n:
        if current_cost < cost:
            assignments = assigning
            cost = current_cost

            print('.')

    else:
        for c in range(l):
            for d in range(n):
                cap, index = capacity_subset[c]
                f = (d + i) % n
                ca = c + a
                if ca < l:
                    if demand[f] <= cap:
                        if current_cost + travel_cost[f][index] <= cost:
                            assigning[i] = index

                            current_cost += travel_cost[f][index]
                            cap -= demand[f]
                            capacity_subset[ca] = [cap, index]

                get_assignements(capacity_subset,
                                 demand,
                                 travel_cost,
                                 cost,
                                 current_cost,
                                 assigning,
                                 i, a + 1)
        get_assignements(capacity_subset,
                         demand,
                         travel_cost,
                         cost,
                         current_cost,
                         assigning,
                         i + 1, a)

    return cost, assignments


demand = [8, 13, 8, 9, 11, 9, 7]
capacity_subset = [[30, 1], [25, 2], [20, 3]]
travel_cost = [[1, 3, 3, 6],
               [2, 1, 3, 5],
               [2, 4, 1, 6],
               [2, 1, 2, 2],
               [5, 3, 6, 2],
               [4, 6, 2, 4],
               [5, 6, 4, 2]]
sols = []
total_demand: 65
MinTravelCostAssigments: [[45, 30, 25, 20], [45, 30, 25, 0],
                          [45, 30, 0, 20], [45, 30, 0, 0],
                          [45, 0, 25, 20], [45, 0, 25, 0],
                          [45, 0, 0, 20], [0, 30, 25, 20]]
cost = 1000
assignment = []

print(get_assignements(capacity_subset,
                       demand,
                       travel_cost,
                       cost,
                       current_cost=0,
                       assigning=None, i=0))

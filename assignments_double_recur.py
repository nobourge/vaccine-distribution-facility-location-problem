def get_assignements(capacity_subset,
                     demand,
                     travel_cost,
                     cost,
                     current_cost,
                     assigning=None,
                     i=0,
                     a=0,
                     assigned=0):
    global n
    global l
    global assignments
    global cheapest

    if assigning is None:
        l = len(capacity_subset)
        n = len(demand)
        assigning = [-1] * n
        cheapest = 1000

    if (n == i) or (l == a):
        if assigned == n:
            if current_cost < cheapest:
                assignments = assigning
                cheapest = current_cost

                print('.')
        return

    else:
        for c in range(l):
            for d in range(n):
                f = (d + i) % n
                ca = (c + a) % l
                cap, index = capacity_subset[ca]
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
                                             i + 1,
                                             a,
                                             assigned+1)
                get_assignements(capacity_subset,
                                 demand,
                                 travel_cost,
                                 cost,
                                 current_cost,
                                 assigning,
                                 i,
                                 a + 1,
                                 assigned)
        """get_assignements(capacity_subset,
                         demand,
                         travel_cost,
                         cost,
                         current_cost,
                         assigning,
                         i + 1, 
                         a)"""

    if cheapest < 1000:
        return cheapest, assignments


demand = [8, 1, 3, 1]
capacity_subset = [[9, 1], [5, 2], [1, 3]]
travel_cost = [[1, 3, 3, 6],
               [2, 1, 3, 5],
               [2, 4, 1, 6],
               [2, 1, 3, 5]
               ]
sols = []
total_demand: 65

cost = 1000
assignment = []

print(get_assignements(capacity_subset,
                       demand,
                       travel_cost,
                       cost,
                       current_cost=0,
                       assigning=None,
                       i=0,
                       a=0))

def generationMots(self, i):
    if i == self.taille:
        self.affiche()
    else:
        for c in "abcdefghijklmnopqrstuvwxyz":
            self.s[i] = c
            self.generationMots(i + 1)


def get_assignements(capacity_subset,
                     demand,
                     travel_cost,
                     cost,
                     assignments,
                     current_cost,
                     assigning=None,
                     i=0):
    global n
    global capacity_indexes
    global l

    if assigning is None:
        capacity_subset = sorted(capacity_subset)
        n = len(demand)

        capacity_indexes = []
        for s in range(len(capacity_subset)):
            if 0 < capacity_subset[s]:
                capacity_indexes.append(s)
        l = len(capacity_indexes)
        assigning = [-1] * n

    if i == n:
        assignments = assigning
        cost = current_cost

    else:
        for c in range(l):
            for d in range(n):

                f = (d + i) % n
                assigned = False
                while (not assigned) & (c < l):
                    ci = capacity_indexes[c]
                    if (demand[f] <= capacity_subset[ci]) \
                            and (
                            current_cost + travel_cost[f][ci] <= cost):
                        assigning[i] = ci
                        assigned = True
                        current_cost += travel_cost[f][ci]
                        capacity_subset[ci] -= demand[f]

                        get_assignements(capacity_subset,
                                         demand,
                                         travel_cost,
                                         cost,
                                         assignment,
                                         current_cost,
                                         assigning,
                                         i + 1)
                    else:
                        c += 1

                assigning[-1] = -1
                current_cost -= travel_cost[d][ci]
                capacity_subset[ci] += demand[f]

    return cost, assignments


demand = [8, 13, 8, 9, 11, 9, 7]
capacity_subset = [45, 30, 0, 20]
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
                       assignment,
                       current_cost=0,
                       assigning=None, i=0))

def generationMots(self, i):
    if i == self.taille:
        self.affiche()
    else:
        for c in "abcdefghijklmnopqrstuvwxyz":
            self.s[i] = c
            self.generationMots(i + 1)


def get_assignements(capacity_subset, demand, travel_cost,
                     current_cost, cost=-1,
                     assigning=None, d=0, c=0):
    global n
    global capacity_indexes
    if assigning is None:
        assigning = []
        n = 0
        capacity_indexes = []
        for i in range(len(capacity_subset)):
            if 0 < capacity_subset[i]:
                capacity_indexes.append(i)
                n += 1
        c = capacity_indexes[0]

    if c == n:
        assignments = assigning

    else:
        for d in range(len(demand)):
            if (demand[d] <= capacity_subset[capacity_indexes[c]]) \
                    and (
                    current_cost + travel_cost[d][c] <= cost):
                assigning.append(capacity_indexes[c])
                current_cost += travel_cost[d][c]
                capacity_subset[capacity_indexes[c]] -= demand[d]
                get_assignements(capacity_subset, demand, travel_cost,
                                 current_cost, cost,
                                 assigning, d, c + 1)
            del assigning[-1]
            current_cost -= travel_cost[d][c]
            capacity_subset[capacity_indexes[c]] += demand[d]

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
sols=[]
total_demand: 65
MinTravelCostAssigments :  [[45, 30, 25, 20], [45, 30, 25, 0], [45, 30, 0, 20], [45, 30, 0, 0], [45, 0, 25, 20], [45, 0, 25, 0], [45, 0, 0, 20], [0, 30, 25, 20]]

print(get_assignements(capacity_subset, demand, travel_cost,
                     current_cost=0, cost=1000,
                     assigning=None, d=0, c=0))
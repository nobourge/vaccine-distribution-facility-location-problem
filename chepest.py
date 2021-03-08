from copy import deepcopy


def get_possible_assigns(capacity_subset, dem):
    possible_assigns = []
    for c in capacity_subset:
        if dem <= c[0]:
            f = deepcopy(c)
            possible_assigns.append(f)
    return possible_assigns


def getSubsetAssignements(capacity_subset,
                          demand,
                          travel_cost,
                          cost,
                          current_cost,
                          assigning,
                          i,
                          a,
                          assigned,
                          profondeur):
    global n
    global origin
    if assigning is None:
        origin = capacity_subset
        n = len(demand)
        assignments = []
        assigning = [-1] * n
        if cost == -1:
            cost = 10000

    best = []

    if profondeur == 0:
        if assigned == len(demand):
            return (True, current_cost, assigning)
        else:
            return (False, current_cost, assigning)


    possible_assigns = get_possible_assigns(capacity_subset, dem)
    # simule coups possibles
    for possible_assign in possible_assigns:
        assigning[f] = possible_assign[1]
        current_cost += travel_cost[d][possible_assign[1]]
        capacity_subset[capacity_subset.index(possible_assign)][0] \
            -= dem
        # recursion pour simuler

        all_assigned = getSubsetAssignements(capacity_subset,
                                      demand,
                                      travel_cost,
                                      cost,
                                      current_cost,
                                      assigning,
                                      i+1,
                                      a,
                                      assigned+1,
                                      profondeur - 1)[0]
        if all_assigned:
            print(current_cost)
            if current_cost < cost:
                cost = current_cost
                assignments = deepcopy(assigning)
                best = [(cost, assignments)]

        assigning[f] = -1
        current_cost -= travel_cost[d][possible_assign[1]]
        possible_assign[0] -= dem
        capacity_subset[capacity_subset.index(possible_assign)][0] \
            += dem
        possible_assign[0] += dem



    return best

def getSubsetAssignements(capacity_subset,
                          demand,
                          travel_cost,
                          cost,
                          current_cost,
                          assigning,
                          i,
                          a,
                          assigned,
                          profondeur):
    for f in range(len(demand)):
        """dem = demand[f]
        assigning = [-1] * len_capacity
        assigned = 0
        current_cost = 0
        capacity_subset = origin"""
        possible_assigns = get_possible_assigns(capacity_subset, dem)



demand = [8, 1, 3, 1]
capacity_subset = [[9, 1], [5, 2], [1, 3]]
travel_cost = [[1, 3, 3, 6],
               [2, 1, 3, 5],
               [2, 4, 1, 6],
               [2, 1, 3, 5]
               ]
sols = []
total_demand: 65

assignment = []


print(getSubsetAssignements(capacity_subset,
                            demand,
                            travel_cost,
                            cost=-1,
                            current_cost=0,
                            assigning=None,
                            i=0,
                            a=0,
                            assigned=0,
                            profondeur=len(demand)))

from projet1 import *


def permutations(lst):
    # If lst is empty then there are no permutations
    if len(lst) == 0:
        return []

        # If there is only one element in lst then, only
    # one permuatation is possible
    if len(lst) == 1:
        return [lst]

        # Find the permutations for lst if there are
    # more than 1 characters

    building_permutation = []

    # Iterate the input(lst) and calculate the permutation
    for i in range(len(lst)):
        m = lst[i]

        # Extract lst[i] or m from the list
        remaining_list = lst[:i] + lst[i + 1:]

        # Generating all permutations where m is first element
        for p in permutations(remaining_list):
            building_permutation.append([m] + p)
    return building_permutation


def assign(dp,
           permuted_capacity,
           travel_cost,
           cost,
           i
           ):
    # print(i, dp, capacity)
    current_cost = 0
    assigning = [-1] * len(dp)
    for d in dp:
        assigned = False
        i = 0
        c = 0
        while not assigned and c < len(permuted_capacity):

            if d[0] <= permuted_capacity[c][0]:
                if (current_cost + travel_cost[d[1]][
                     permuted_capacity[c][1]]) < cost:
                    assigning[d[1]] = permuted_capacity[c][1]
                    permuted_capacity[c][0] -= d[0]
                    assigned = True
                    current_cost += travel_cost[d[1]][
                        permuted_capacity[c][1]]
                else:
                    # print(cost, '< assigning', permuted_capacity[c],
                    #    'to', assigning,)
                    return -1, []
            else:
                if (c + 1) < len(permuted_capacity):
                    c += 1
                else:
                    return -1, []
    cost = current_cost

    return cost, assigning


def minimum_travel_cost(demand,
                        capacity,
                        travel_cost):
    """
     trouve une affectation des familles aux centres de vaccination
     minimisant les coûts de déplacements en considérant que ceux-ci
     sont déjà construits.
     tient compte d’aucun coût de construction.
    :param demand: list tel que demand[i] = di pour i ∈ I.
    :param capacity:list tel que capacity[j]= cj j ∈ J
    si un centre len_capacity’est pas construit sur un site j, alors
    capacity[j]=0
    :param travel_cost: tableau tel que travel_cost[i][j] = ti j
    :return:(cost,assignments)
            (-1,[]) Si aucune affectation ne permet de satisfaire les
            demandes
    """
    print(capacity)
    if isinstance(capacity[0], int):
        indexed_capacities = []
        for i in range(len(capacity)):
            indexed_capacities.append([capacity[i], i])
        # sortedescending_indexed_capacities = sorted(
        # indexed_capacities,reverse=True)
        capacity = indexed_capacities
    assignments = []
    indexed_demand = []

    for i in range(len(demand)):
        indexed_demand.append([demand[i], i])
    indexed_demand_permutations = permutations(indexed_demand)
    cost = -1
    i = 0
    for permuted_capacity in permutations(capacity):

        for dp in indexed_demand_permutations:
            if cost == -1:
                cost = 1000
            i += 1
            permuted_subset_assignments_cost, \
            permuted_subset_assignments = \
                assign(dp,
                       deepcopy(permuted_capacity),
                       travel_cost,
                       cost,
                       i
                       )
            """get_subset_assignments(capacity,
                                       dp,
                                       travel_cost,
                                       cost,
                                       current_cost=0,
                                       assigning=None,
                                       i=0,
                                       a=0)"""
            if len(permuted_subset_assignments) == len(demand):
                if permuted_subset_assignments_cost < cost:
                    cost = permuted_subset_assignments_cost
                    assignments = permuted_subset_assignments
    if len(assignments) == len(demand):
        return (cost, assignments)
    else:
        return -1, []


demand = [8, 13, 8, 9, 11, 9, 7]
capacity = [45, 30, 25, 20]
travel_cost = [[1, 3, 3, 6],
               [2, 1, 3, 5],
               [2, 4, 1, 6],
               [2, 1, 2, 2],
               [5, 3, 6, 2],
               [4, 6, 2, 4],
               [5, 6, 4, 2]]

print(minimum_travel_cost(demand, capacity, travel_cost))

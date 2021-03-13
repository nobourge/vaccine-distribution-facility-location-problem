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


def assign_family(cost,
                  demand,
                  d,
                  family_min_travel_cost,
                  assignments,
                  assigned_families,
                  built,
                  nearest_built):

    print(' site', nearest_built[1],
          'stock:', nearest_built[0],
          'satifies family', d,
          'demand :', demand[d])
    assignments[d] = nearest_built[1]
    assigned_families += 1
    cost += family_min_travel_cost
    # print(built, nearest_built)
    built[built.index(nearest_built)][0] -= demand[d]
    family_min_travel_cost = -1


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
    len_demand = len(demand)
    len_capacity = len(capacity)

    cost = 0
    assignments = [-1] * len_demand
    assigned_families = 0
    to_assign_index_list = [[i] for i in range(len_demand)]
    len_to_assign = len(to_assign_index_list)
    built = []
    for j in range(len_capacity):
        if 0 < capacity[j]:
            built.append([capacity[j], j])

    nearest_built_potential = None
    # built site with lowest current family travel_cost
    to_assign_idx = 0
    while 0 < len_to_assign:
        family_min_travel_cost = -1
        assigned = False
        potential_sites = deepcopy(built)
        while (not assigned) & (0 < len(potential_sites)):
            # search of the nearest built
            for b in potential_sites:
                if travel_cost[to_assign_idx][b[1]] < family_min_travel_cost or \
                        family_min_travel_cost == -1:
                    family_min_travel_cost = travel_cost[to_assign_idx][b[1]]
                    nearest_built = b
                    nearest_built_potential = b


            if demand[to_assign_idx] <= nearest_built_potential[0]:
                print(' site', nearest_built_potential[1],
                      'stock:', nearest_built_potential[0],
                      'satifies family', to_assign_idx,
                      'demand :', demand[to_assign_idx])
                assignments[to_assign_idx] = nearest_built_potential[1]
                assigned = True
                cost += family_min_travel_cost
                # print(built, nearest_built_potential)
                built[built.index(nearest_built_potential)][0] -= demand[to_assign_idx]
                family_min_travel_cost = -1

                del to_assign_index_list[0]

            else:  # search in remaining potentials
                if 0 < len(potential_sites):
                    del potential_sites[
                        potential_sites.index(nearest_built_potential)]
                family_min_travel_cost = -1

        if not assigned:
            # replace nearest built min with current family equal or
            # above demand already assigned families with current family
            pass

    if assigned_families == len_demand:
        return cost, assignments
    else:
        return -1, []  # minimum_travel_cost(demand,
        # capacity,
        # travel_cost)


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

# Nom : Bourgeois
# Prénom : Noé
# Matricule : 000496667

import sys
from copy import deepcopy


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

    l = []  # empty list that will store current permutation

    # Iterate the input(lst) and calculate the permutation
    for i in range(len(lst)):
        m = lst[i]

        # Extract lst[i] or m from the list.  remLst is
        # remaining list
        remLst = lst[:i] + lst[i + 1:]

        # Generating all permutations where m is first
        # element
        for p in permutations(remLst):
            l.append([m] + p)
    return l


def assign(dp,
           sp,
           travel_cost,
           cost,
           ):
    # print(dp, sp)
    current_cost = 0
    assigning = [-1] * len(dp)
    for d in dp:
        assigned = False
        i = 0
        c = 0
        while not assigned and c < len(sp):

            if d[0] <= sp[c][0]:
                if (current_cost + travel_cost[d[1]][sp[c][1]]) < cost:
                    assigning[d[1]] = sp[c][1]
                    sp[c][0] -= d[0]
                    assigned = True
                    current_cost += travel_cost[d[1]][sp[c][1]]
                else:
                    return -1, []
            else:
                if (c + 1) < len(sp):
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
    """
    indexed_capacities = []
    for i in range(len(capacity)):
        indexed_capacities.append([capacity[i], i])
    sortedescending_indexed_capacities = sorted(indexed_capacities,
                                                reverse=True)"""
    assignments = []
    indexed_demand = []
    for i in range(len(demand)):
        indexed_demand.append([demand[i], i])
    indexed_demand_permutations = permutations(indexed_demand)
    cost = -1
    indexed_capacity_permutations = permutations(capacity)
    for sp in indexed_capacity_permutations[:-1]:
        for dp in indexed_demand_permutations:
            if cost == -1:
                cost = 1000
            permuted_subset_assignments_cost, \
            permuted_subset_assignments = \
                assign(dp,
                       deepcopy(sp),
                       travel_cost,
                       cost
                       )
            """get_subset_assignments(sp,
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


def get_subset(values, choices=None):
    subset = []
    for i in range(len(values)):
        if choices[i]:
            subset.append(values[i])

    return subset


def get_min_cost_assignments(sortedescending_indexed_capacities,
                             choices,
                             demand,
                             opening_cost, start, current):
    """

    :param cost:
    :param assignments:
    :param sortedescending_indexed_capacities:
    :param demand:
    :param current:
    :param subsets:
    :return:
    """
    # using a mask of size len(sortedescending_indexed_capacities)
    global len_capacity
    global len_demand
    global total_demand

    global cost
    global min_cost_assignments

    if start:
        len_demand = len(demand)
        total_demand = sum(demand)
        print('total_demand:', total_demand)

        cost = 1000
        min_cost_assignments = []
        start = False

    if current == 0:
        len_capacity = len(sortedescending_indexed_capacities)
        choices = [True] * len_capacity

    if current == len_capacity:
        current_capacity_sum = 0
        for i in range(len(choices)):
            if choices[i]:
                v = sortedescending_indexed_capacities[i][0]
                current_capacity_sum += v
        if total_demand <= current_capacity_sum:

            subset = get_subset(sortedescending_indexed_capacities,
                                choices)
            print(subset)
            subset_travel_cost, subset_assignments = \
                minimum_travel_cost(demand, subset, travel_cost)

            if len(subset_assignments) == len_demand:
                subset_build_cost = 0
                for i in subset:
                    subset_build_cost += opening_cost[i[1]]



                subset_tot_cost = subset_build_cost + subset_travel_cost
                if subset_tot_cost < cost:
                    cost = subset_tot_cost
                    min_cost_assignments = subset_assignments

    else:
        # try with
        choices[current] = True
        get_min_cost_assignments(sortedescending_indexed_capacities, choices,
                                 demand, opening_cost, start, current + 1)

        # try without
        if current == 0:
            del sortedescending_indexed_capacities[current]
            del choices[current]
            test_cap = 0
            for c in range(len(sortedescending_indexed_capacities)):
                test_cap += sortedescending_indexed_capacities[c][0]
            if total_demand <= test_cap:
                get_min_cost_assignments(sortedescending_indexed_capacities,
                                         choices, demand, opening_cost, start,
                                         current)
        else:
            choices[current] = False
            get_min_cost_assignments(sortedescending_indexed_capacities,
                                     choices, demand, opening_cost, start,
                                     current + 1)
    return cost, min_cost_assignments


def facility_location(opening_cost, demand, capacity, travel_cost):
    """
    resolves FLP
    :param opening_cost: liste où opening_cost[j] = fj
    :param demand:
    :param capacity:
    :param travel_cost:
    :return: if no solution: tuple (-1,[],[])
            else: tuple (cost, centers, assigning)
    """
    cost = -1
    centers = []
    assignments = []
    indexed_capacities = []
    for i in range(len(capacity)):
        indexed_capacities.append([capacity[i], i])
    sortedescending_indexed_capacities = sorted(indexed_capacities,
                                                reverse=True)
    print('sortedescending_indexed_capacities:',
          sortedescending_indexed_capacities)
    choices = [True] * len(capacity)
    cost, assignments = get_min_cost_assignments(
        sortedescending_indexed_capacities, choices,
        demand, opening_cost, start=True, current=0)
    if 0 < len(assignments):
        subset_travel_cost, assignments = minimum_travel_cost(demand,
                                                              assignments,
                                                              travel_cost)

        cost += subset_travel_cost
        for i in assignments:
            centers.append(i[1])

        return (cost, centers, assignments)
    else:
        return (-1,[],[])


def read_instance(file_name):
    """
    Fonction retournant les données
    (opening_cost,travel_cost,demand,capacity) de l'instance file_name
    dont le fichier doit être situé dans le même dossier
    :param file_name: String
    :return: (opening_cost,travel_cost,demand,capacity)
    """
    opening_cost = []
    demand = []
    capacity = []
    travel_cost = []
    try:
        file = open(file_name, 'r')
        info = file.readline().split(" ")
        I = int(info[0])
        J = int(info[1])
        info = file.readline().split(" ")
        for j in range(J):
            opening_cost.append(int(info[j]))
        info = file.readline().split(" ")
        for i in range(I):
            demand.append(int(info[i]))
        info = file.readline().split(" ")
        for j in range(J):
            capacity.append(int(info[j]))
        for i in range(I):
            travel_cost.append([])
            info = file.readline().split(" ")
            for j in range(J):
                travel_cost[i].append(round(float(info[j])))
    except:
        print(
            "Erreur lors de la lecture des données, "
            "vérifiez que le fichier de l'instance "
            "est dans le même dossier que ce fichier")
    return opening_cost, demand, capacity, travel_cost


# Résolution du FLP sur l'instance passée en ligne de commande
if __name__ == "__main__":
    opening_cost, demand, capacity, travel_cost = read_instance(
        'FLP-7-4.txt')
    print("Instance : {}".format('FLP-7-4.txt'))
    print("Opening costs : {}".format(opening_cost))
    print("Demand : {}".format(demand))
    print("Capacity : {}".format(capacity))
    print("Travel costs : {}".format(travel_cost))
    print("Résultats : {}".format(
        facility_location(opening_cost, demand, capacity,
                          travel_cost)))
"""   
    if len(sys.argv) == 2:

        opening_cost, demand, capacity, travel_cost = read_instance(
           sys.argv[1])
        
        print("Instance : {}".format(sys.argv[1]))
        print("Opening costs : {}".format(opening_cost))
        print("Demand : {}".format(demand))
        print("Capacity : {}".format(capacity))
        print("Travel costs : {}".format(travel_cost))
        print("Résultats : {}".format(
            facility_location(opening_cost, demand, capacity,
                              travel_cost)))
    else:
        print("Veuillez fournir un nom d'instance")
"""

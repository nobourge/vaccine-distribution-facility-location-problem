# Nom : Bourgeois
# Prénom : Noé
# Matricule : 000496667

import sys
import time
from copy import deepcopy


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

    built = []
    for j in range(len_capacity):
        if 0 < capacity[j]:
            built.append([capacity[j], j])

    nearest_built = None

    for d in range(len_demand):
        family_min_travel_cost = -1
        assigned = False
        potential_sites = deepcopy(built)
        while (not assigned) & (0 < len(potential_sites)):

            for b in potential_sites:
                if travel_cost[d][b[1]] < family_min_travel_cost or \
                        family_min_travel_cost == -1:
                    family_min_travel_cost = travel_cost[d][b[1]]
                    nearest_built = b

            if demand[d] <= nearest_built[0]:
                print(' site', nearest_built[1],
                      'stock:', nearest_built[0],
                      'satifies family', d,
                      'demand :', demand[d])
                assignments[d] = nearest_built[1]
                assigned = True
                assigned_families += 1
                cost += family_min_travel_cost
                # print(built, nearest_built)
                built[built.index(nearest_built)][0] -= demand[d]
                family_min_travel_cost = -1

            else:
                if 0 < len(potential_sites):
                    del potential_sites[
                        potential_sites.index(nearest_built)]
                family_min_travel_cost = -1

    if assigned_families == len_demand:
        return cost, assignments
    else:
        return -1, []  # minimum_travel_cost(demand,
        # capacity,
        # travel_cost)


def get_min_cost_assignments(sortedescending_indexed_capacities,
                             choices,
                             demand,
                             opening_cost,
                             travel_cost,
                             start, current):
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
            # print(sortedescending_indexed_capacities, choices)

            subset = [0] * len(capacity)
            for i in range(len(sortedescending_indexed_capacities)):
                if choices[i]:
                    subset[sortedescending_indexed_capacities[i][
                        1]] = sortedescending_indexed_capacities[i][0]

            print('subset :', subset)
            subset_travel_cost, subset_assignments = \
                minimum_travel_cost(demand, subset, travel_cost)
            print(' travel_cost :', subset_travel_cost)
            print(' assignments :', subset_assignments)

            if len(subset_assignments) == len_demand:
                subset_build_cost = 0
                for i in range(len(subset)):
                    if subset[i] != 0:
                        subset_build_cost += opening_cost[i]
                print(' build_cost :', subset_build_cost)

                subset_tot_cost = subset_build_cost + subset_travel_cost
                if subset_tot_cost < cost:
                    print(subset_tot_cost, '<', cost)
                    cost = subset_tot_cost
                    min_cost_assignments = subset_assignments

    else:
        # try with
        choices[current] = True
        get_min_cost_assignments(sortedescending_indexed_capacities,
                                 choices,
                                 demand, opening_cost,
                                 travel_cost, start, current + 1)

        # try without
        if current == 0:
            del sortedescending_indexed_capacities[current]
            del choices[current]
            test_cap = 0
            for c in range(len(sortedescending_indexed_capacities)):
                test_cap += sortedescending_indexed_capacities[c][0]
            if total_demand <= test_cap:
                get_min_cost_assignments(
                    sortedescending_indexed_capacities,
                    choices, demand, opening_cost,
                    travel_cost, start,
                    current)
        else:
            choices[current] = False
            get_min_cost_assignments(sortedescending_indexed_capacities,
                                     choices, demand, opening_cost,
                                     travel_cost,
                                     start,
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
    centers = set()
    assignments = []
    indexed_capacities = []
    for i in range(len(capacity)):
        indexed_capacities.append([capacity[i], i])
    sortedescending_indexed_capacities = sorted(indexed_capacities,
                                                reverse=True)

    # print('sortedescending_indexed_capacities:',
    # sortedescending_indexed_capacities)

    choices = [True] * len(capacity)
    cost, assignments = get_min_cost_assignments(
        sortedescending_indexed_capacities, choices,
        demand, opening_cost, travel_cost, start=True, current=0)
    if 0 < len(assignments):
        for i in assignments:
            centers.add(i)
        centers = list(centers)

        return (cost, centers, assignments)
    else:
        return (-1, [], [])


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
    start = time.time()

    opening_cost, demand, capacity, travel_cost = read_instance(
        'FLP-20-7-4.txt')
    print("Instance : {}".format('FLP-7-4.txt'))
    print("Opening costs : {}".format(opening_cost))
    print("Demand : {}".format(demand))
    print("Capacity : {}".format(capacity))
    print("Travel costs : {}".format(travel_cost))
    print("Résultats : {}".format(
        facility_location(opening_cost, demand, capacity,
                          travel_cost)))

    end = time.time()
    print(end - start)
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

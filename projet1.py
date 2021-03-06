# Nom : Bourgeois
# Prénom : Noé
# Matricule : 000496667

import sys


def get_assignements(capacitySubset, demand, travel_cost, cost=-1,
                               assignments=None):
    for capacity in capacitySubset:
        if 0 < capacity:
            pass
            # todo


def get_subset(values, choices=None):
    subset = []
    for i in range(len(values)):
        if choices[i]:
            subset.append(values[i])

    return subset


def getMinTravelCostAssigments(sortedescending_indexed_capacities, choices, demand, travel_cost,
                               current=0, subsets=None, cost=-1,
                               assignments=None):
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
    if assignments is None:
        assignments = []

    global n
    global total_demand

    if subsets is None:
        subsets = []
        total_demand = sum(demand)
        print('total_demand:', total_demand)

    if current == 0:
        n = len(sortedescending_indexed_capacities)
        choices = [True] * n

    if current == n:
        current_sum = 0
        for i in range(len(choices)):
            if choices[i]:
                v = sortedescending_indexed_capacities[i][0]
                current_sum += v
        if total_demand <= current_sum:
            subsets.append(get_subset(
                sortedescending_indexed_capacities, choices))

    else:
        # try with
        choices[current] = True
        getMinTravelCostAssigments(sortedescending_indexed_capacities, choices, demand, travel_cost,
                                   current + 1, subsets)
        # try without
        if current == 0:
            del sortedescending_indexed_capacities[current]
            del choices[current]
            test_cap = 0
            for c in range(len(sortedescending_indexed_capacities)):
                test_cap += sortedescending_indexed_capacities[c][0]
            if total_demand <= test_cap:
                getMinTravelCostAssigments(sortedescending_indexed_capacities, choices, demand,
                                           travel_cost, current,
                                           subsets)
        else:
            choices[current] = False
            getMinTravelCostAssigments(sortedescending_indexed_capacities, choices, demand,
                                       travel_cost, current + 1,
                                       subsets)
    return subsets


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
    si un centre n’est pas construit sur un site j, alors
    capacity[j]=0
    :param travel_cost: tableau tel que travel_cost[i][j] = ti j
    :return:
    """
    cost = -1
    assignments = []
    indexed_capacities = []
    for i in range(len(capacity)):
        indexed_capacities.append([capacity[i], i])
    sortedescending_indexed_capacities = sorted(indexed_capacities, reverse=True)
    print('sortedescending_indexed_capacities:',
          sortedescending_indexed_capacities)
    choices = [True] * len(capacity)
    print('MinTravelCostAssigments : ')
    print(getMinTravelCostAssigments(
        sortedescending_indexed_capacities, choices, demand,
        travel_cost))
    return (cost, assignments)


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
    minimum_travel_cost(demand, capacity, travel_cost)

    return (cost, centers, assignments)


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

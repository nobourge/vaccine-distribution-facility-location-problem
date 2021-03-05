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
        else:
            subset.append(0)
    return subset


def getMinTravelCostAssigments(values, choices, demand, travel_cost,
                               current=0, subsets=None, cost=-1,
                               assignments=None):
    """

    :param cost:
    :param assignments:
    :param values:
    :param demand:
    :param current:
    :param subsets:
    :return:
    """
    # using a mask of size len(values)
    if assignments is None:
        assignments = []
    global n
    global total_demand
    global Noned

    if subsets is None:
        subsets = []
        total_demand = sum(demand)
        print('total_demand:', total_demand)

    if current == 0:
        n = 0
        Noned = 0
        for i in range(len(choices)):
            if choices[i] is not None:
                choices[i] = True
                n += 1
            else:
                Noned += 1

    if current == n:
        current_sum = 0
        for i in range(len(choices)):
            if choices[i]:
                current_sum += values[i]
        if total_demand <= current_sum:
            subsets.append(get_subset(values, choices))

    else:
        # try with
        choices[current + Noned] = True
        getMinTravelCostAssigments(values, choices, demand, travel_cost,
                                   current + 1, subsets)
        # try without
        if current == 0:
            values[current + Noned] = 0
            choices[current + Noned] = None
            if total_demand <= sum(values):
                getMinTravelCostAssigments(values, choices, demand,
                                           travel_cost, current,
                                           subsets)
        else:
            choices[current + Noned] = False
            getMinTravelCostAssigments(values, choices, demand,
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
    sortedescending_capacity = sorted(capacity, reverse=True)
    print(sortedescending_capacity)
    choices = [True] * len(capacity)
    MinTravelCostAssigments = getMinTravelCostAssigments(
        sortedescending_capacity, choices, demand, travel_cost)
    print('MinTravelCostAssigments : ',
          MinTravelCostAssigments)

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

    if len(sys.argv) == 2:

        opening_cost, demand, capacity, travel_cost = read_instance(
            sys.argv[1])
        # opening_cost, demand, capacity, travel_cost = read_instance(
        #   'FLP-7-4.txt')
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

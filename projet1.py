# Nom : Bourgeois
# Prénom : Noé
# Matricule : 000496667

import sys

def get_assignements(capacitySubset, demand, travel_cost):
    for capacity in capacitySubset:
        if 0 < capacity:
            
            # todo

def minimum_travel_cost(demand, capacity, travel_cost):
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

    total_demand = sum(demand)
    capacities_satisfying_total_demand = getCapacitySubSets_satisfying(
        total_demand,
        sorted(capacity, reverse=True))
    print('capacities_satisfying_total_demand : ',
          capacities_satisfying_total_demand)
    for capacitySubset in capacities_satisfying_total_demand:
        get_assignements(capacitySubset, demand, travel_cost)

        return (cost, assignments)


def get_subset(values, choices=None):
    subset = []
    if choices == None:
        choices = [True] * len(values)
    for i in range(len(choices)):
        if choices[i]:
            subset.append(values[i])
        else:
            subset.append(0)
    return subset


def getCapacitySubSets_satisfying(total_demand,
                                  capacity,
                                  current=0,
                                  capacities_satisfying_total_demand=None):

    if capacities_satisfying_total_demand is None:
        capacities_satisfying_total_demand = []
    global choices
    global n
    global totaldemand
    global totalcapacity


    if current == 0:
        n = len(capacity)
        totalCapacity = sum(capacity)
        choices = [False] * n
        # using a mask of size len(capacity)

    elif current == n:  # print un sousEnsemble
        subset = get_subset(capacity, choices)
        if sum(subset) >= total_demand:
            capacities_satisfying_total_demand.append(subset)

    else:
        # try with
        choices[current] = True
        getCapacitySubSets_satisfying(total_demand,
                                      capacity,
                                      current + 1,
                                      capacities_satisfying_total_demand)

        # try without
        choices[current] = False
        if totaldemand < totalcapacity - capacity[current]:
            getCapacitySubSets_satisfying(total_demand,
                                          capacity,
                                          current + 1,
                                          capacities_satisfying_total_demand)

    return capacities_satisfying_total_demand


def facility_location(opening_cost, demand, capacity, travel_cost):
    """
    resolves FLP
    :param opening_cost: liste où opening_cost[j] = fj
    :param demand:
    :param capacity:
    :param travel_cost:
    :return: if no solution: tuple (-1,[],[])
            else: tuple (cost, centers, assignments)
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
        print("Traval costs : {}".format(travel_cost))
        print("Résultats : {}".format(
            facility_location(opening_cost, demand, capacity,
                              travel_cost)))
    else:
        print("Veillez fournir un nom d'instance")

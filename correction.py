# Placez ce fichier dans le même dossier que projet1.py et FLP-7-4.txt

from projet1 import facility_location
from projet1 import minimum_travel_cost

INSTANCE = "FLP-7-4.txt"
OPT = 43
CENTERS = [0, 3]
MIN_TRAVEL_OPT = 44


def read_instance(file_name):
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
                travel_cost[i].append(int(info[j]))
    except:
        print(
            "Erreur lors de la lecture des données, vérifiez que le fichier de l'instance est dans le même dossier que ce fichier")
    return opening_cost, demand, capacity, travel_cost


def solution_value(opening_cost, demand, capacity, travel_cost, centers,
                   assignments):
    flag = True
    if len(assignments) != len(demand):
        flag = False
    cent = []
    for i in range(len(demand)):
        if assignments[i] < 0 or assignments[i] >= len(capacity):
            flag = False
        elif assignments[i] not in cent:
            cent.append(assignments[i])
    for j in centers:
        if j < 0 or j >= len(capacity):
            flag = False
    for j in cent:
        if not (j in centers):
            flag = False
    for j in range(len(capacity)):
        if j in centers:
            tmp = 0
            for i in range(len(demand)):
                if assignments[i] == j:
                    tmp += demand[i]
            if tmp > capacity[j]:
                flag = False
    sol = -1
    if flag:
        sol = 0
        for j in centers:
            sol += opening_cost[j]
        for i in range(len(demand)):
            sol += travel_cost[i][assignments[i]]
    return sol


def adapt_capacity(centers, capacity):
    res = []
    for j in range(len(capacity)):
        if j in centers:
            res.append(capacity[j])
        else:
            res.append(0)
    return res


def centers_cost(opening_cost):
    res = 0
    for j in range(len(opening_cost)):
        if j in CENTERS:
            res += opening_cost[j]
    return res


def check_functions():
    opening_cost, demand, capacity, travel_cost = read_instance(
        INSTANCE)
    sol1 = minimum_travel_cost(demand,
                               adapt_capacity(CENTERS, capacity),
                               travel_cost)
    print("Solution minimum_travel_cost {}".format(sol1))
    if len(sol1[1]) == 0:
        print("Erreur, pas de solution retournée")
    else:
        sol1_check = solution_value(opening_cost, demand, capacity,
                                    travel_cost, CENTERS, sol1[1])
        print("Fonction minimum_travel_cost : ")
        if sol1_check == -1:
            print("Solution non valide")
        else:
            if sol1[0] + centers_cost(opening_cost) != sol1_check:
                print("Erreur dans le cout de la solution")
            elif sol1_check > MIN_TRAVEL_OPT:
                print("Solution non optimale")
            elif sol1_check < MIN_TRAVEL_OPT:
                print(
                    "Solution trouvée meilleure que la solution optimale prévue... contactez l'assistant")
            else:
                print("Solution optimale trouvé")

    sol2 = facility_location(opening_cost, demand, capacity,
                             travel_cost)
    print("Solution facility_location {}".format(sol2))
    if len(sol2[2]) == 0:
        print("Erreur, pas de solution retournée")
    else:
        sol2_check = solution_value(opening_cost, demand, capacity,
                                    travel_cost, sol2[1], sol2[2])
        print("Fonction facility_location : ")
        if sol2_check == -1:
            print("Solution non valide")
        else:
            if sol2[0] != sol2_check:
                print("Erreur dans le cout de la solution")
            elif sol2_check > OPT:
                print("Solution non optimale")
            elif sol2_check < OPT:
                print(
                    "Solution trouvée meilleure que la solution optimale prévue... contactez l'assistant")
            else:
                print("Solution optimale trouvé")


check_functions()

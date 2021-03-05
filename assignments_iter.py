def get_assignements(capacity_subset, demand, travel_cost, cost=-1,
                     assigning=None, current=0):
    current_cost = 0
    assigning = []
    for i in capacity_subset:
        if 0 < i:
            pass
    c = 0
    d = 0
    while current_cost <= cost:
        if demand[d] <= capacity_subset[c]:


        current_family_site_travel_cost = travel_cost[d][c]
        current_cost += current_family_site_travel_cost
        if current_cost <= cost:
            assigning.append(capacity_subset_index)
        else:
            current_cost -= current_family_site_travel_cost

    return cost, assigning


demand = [8, 13, 8, 9, 11, 9, 7]
capacity_subset = [45, 30, 0, 20]
travel_cost = [[1, 3, 3, 6],
               [2, 1, 3, 5],
               [2, 4, 1, 6],
               [2, 1, 2, 2],
               [5, 3, 6, 2],
               [4, 6, 2, 4],
               [5, 6, 4, 2]]
sols = []
total_demand: 65
MinTravelCostAssigments: [[45, 30, 25, 20], [45, 30, 25, 0],
                          [45, 30, 0, 20], [45, 30, 0, 0],
                          [45, 0, 25, 20], [45, 0, 25, 0],
                          [45, 0, 0, 20], [0, 30, 25, 20]]

get_assignements(capacity_subset, demand, travel_cost, cost=10000,
                 assigning=None, current=0)

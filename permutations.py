def all_perms(elements):
    if len(elements) <= 1:
        print(elements)
    else:
        for perm in all_perms(elements[1:]):
            permutation = []
            for i in range(len(elements)):
                # nb elements[0:1] works in both string and list contexts
                permutation.append(perm[:i] + elements[0:1] + perm[i:])
            print(permutation)


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


# Driver program to test above function
data = [8, 1, 3, 1]
for p in permutations(data):
    print(p)

demand = [8, 1, 3, 1]

# print(all_perms(demand))
# permutations(demand)

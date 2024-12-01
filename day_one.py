def question_one(left_list, right_list):
    # Sort the lists small -> high
    a = sorted(left_list)
    b = sorted(right_list)
    
    distance = 0
    for i in range(len(a)):
        # non-negative result -> as with example 
        distance += abs(a[i] - b[i])
    return distance


with open("input.txt", "r") as file:
    # declare lists
    left_list = []
    right_list = []
    # now we need to read the input
    for n in file:
        # -> find the separate ' ' -> then it unloads to left then goes to right
        left, right = map(int, n.split())
        # self-declares itself here really
        left_list.append(left)
        right_list.append(right)


result = question_one(left_list, right_list)
print("total Distance:", result)

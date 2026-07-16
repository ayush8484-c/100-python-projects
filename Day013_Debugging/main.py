import random

# Bugged code
# def mutate(a_list):
#     b_list = []
#     new_item = 0
#     for item in a_list:
#         new_item = item * 2
#         new_item += random.randint(1, 3)
#         new_item = maths.add(new_item, item)
#
#     b_list.append(new_item)
#     print(b_list)
#
# mutate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


#Debugged code

def add(n1, n2):
    return n1 + n2
def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1, 3)
        new_item = add(new_item, item)
        b_list.append(new_item)
    print(b_list)
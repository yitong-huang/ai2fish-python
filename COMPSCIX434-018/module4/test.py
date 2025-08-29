# original_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
#
# reversed_dict_1 = {}
# for k, v in original_dict.items():
#     reversed_dict_1[v] = k
# print(reversed_dict_1)
#
# reversed_dict_2 = {}
# for k in original_dict.keys():
#     reversed_dict_2[original_dict[k]] = k
# print(reversed_dict_2)

# s = "A fool thinks himself to be wise, but a wise man knows himself to be a fool"
# d = {}
# for w in s.lower().replace(",", " ").split():
#     if w in d:
#         d[w] += 1
#     else:
#         d[w] = 1
# print(d)

# d1 = {'a': 1, 'b': 2, 'c': 3}
# d2 = {'a': 10, 'c': 30, 'f': 50}
# added_dict = {}
#
# for k, v in d1.items():
#     added_dict[k] = v
#
# for k, v in d2.items():
#     if k in added_dict:
#         added_dict[k] += v
#     else:
#         added_dict[k] = v
#
# print(added_dict)

# lol = [['C++', 'Java', 'Python', 'Swift'],
# ['San Francisco','Berkeley','Oakland'],
# ['Apple', 'Banana', 'Cherry', 'Dragonfruit', 'Grape']]
# length = []
#
# for l in lol:
#     inner = []
#     for s in l:
#         inner.append(len(s))
#     length.append(inner)
#
# print(length)
#

students = [{'name': 'Lisa', 'score': 93},
{'name': 'Jeff', 'score': 85},
{'name': 'Elon', 'score': 89},
{'name': 'Satya', 'score': 90},
{'name': 'Tim', 'score': 82}]

if len(students) > 0:
    num_students = len(students)
    sum_score = 0
    for student in students:
        sum_score += student["score"]
    avg_score = sum_score / num_students
    print("average score: ", avg_score)
else:
    print("no students")


if len(students) > 0:
    highest_score = students[0]["score"]
    highest_name = students[0]["name"]
    for student in students:
        if student["score"] > highest_score:
            highest_score = student["score"]
            highest_name = student["name"]
    print(f"highest student: {highest_name}, score: {highest_score}")
else:
    print("no students")
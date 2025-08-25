def mean(data):
    if len(data) == 0:
        return None
    return sum(data) / len(data)

m = mean([1, 2, 3, 4, 5, 6])
print(m)
m = mean([])
print(m)

def median(data):
    if len(data) == 0:
        return None
    sorted_data = sorted(data)
    if len(sorted_data) % 2 == 0:
        return (data[int(len(sorted_data) / 2)] + data[int(len(sorted_data) / 2 - 1)]) / 2
    else:
        return data[int((len(sorted_data) - 1) / 2)]


m = median([1, 3, 24, 57, 79, 88])
print(m)
m = median([])
print(m)


def mode(data):
    if len(data) == 0:
        return None
    number_occurrence = {}
    for number in data:
        if number in number_occurrence:
            number_occurrence[number] += 1
        else:
            number_occurrence[number] = 1

    max_occurrence = 0
    max_occurrence_number = None
    for number, number_occurrence in number_occurrence.items():
        if number_occurrence > max_occurrence:
            max_occurrence = number_occurrence
            max_occurrence_number = number

    return max_occurrence_number

m = mode([1, 2, 3, 1, 3, 1])
print(m)
m = mode([])
print(m)

def rank(data, number):
    sorted_data = sorted(data)
    for i in range(len(sorted_data)):
        if number == sorted_data[i]:
            return i
    return None

m = rank([1, 2, 3, 1, 3, 1], 5)
print(m)
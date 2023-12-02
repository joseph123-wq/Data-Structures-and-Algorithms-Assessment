def remove_duplicates(sequence):
    view = set()
    result = []

    for item in sequence:
        if item not in view:
            view.add(item)
            result.append(item)

    return result

input_sequence = [1,2,3,2,4,5,3,6,5,7]
result = remove_duplicates(input_sequence)
print(result)



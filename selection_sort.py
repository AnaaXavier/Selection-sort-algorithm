def selection_sort(array):
    # It traverses the array using its indexes, except the last element.
    for current_index in range(len(array)-1):
        minimum_index = current_index
        # Then it tranverses the whole array, this time iterating the current index.
        for next_minimum_index in range(current_index, len(array)):
            if array[next_minimum_index] < array[minimum_index]:
                minimum_index = next_minimum_index
        # Verifies if it's a small number, if it is, it updates its index.
        if array[current_index] > array[minimum_index]:
            temp = array[current_index]
            array[current_index] = array[minimum_index]
            array[minimum_index] = temp
    
    return array

numbers_list = [7, 3, 5, 2, 4, 1]
sorted_numbers = selection_sort(numbers_list)
print(sorted_numbers)

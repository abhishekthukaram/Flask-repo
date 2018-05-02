def elementsearch(input_list, element):
    index_start = 0
    index_end = len(input_list)
    while (True):
        mid_index = int((index_start + index_end)) / 2
        if mid_index < index_start or mid_index > index_end or element < 0:
            return False
        elif element not in input_list:
            return False
        if input_list[mid_index] == element:
            return True
        elif input_list[mid_index] < element:
            index_start = mid_index
        else:
            index_end = mid_index


print elementsearch([1, 2, 4, 6, 8], 8)
print elementsearch([2, 4, 6, 7, 8, 9], 2)
print elementsearch([1, 2, 3, 4, 5, 10, 15], 25)
print elementsearch([5, 10, 15, 20, 25, 30], -1)
print elementsearch([10, 20, 21, 22, 23, 24], 20)

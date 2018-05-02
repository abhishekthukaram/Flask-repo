def searchelement(given_list, number_search):
    for number in given_list:
        if number == number_search:
            return True
    return False


print searchelement([1, 2, 3, 4, 5], 1)
print searchelement([1, 2, 3, 4, 5], -1)
print searchelement([1, 2, 3, 4, 8], 8)

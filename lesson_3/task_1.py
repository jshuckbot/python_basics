def find_list_duplicate_elements(numbers):
    """Ищет повторяющие элементы"""
    double_numbers = []
    tmp_lst = []
    
    for number in numbers:
        if number not in tmp_lst:
            tmp_lst.append(number)
        else:
            double_numbers.append(number)
            
    return double_numbers


lst = [1, 3, 1, 2, 6, 9, 8, 3, 2, 9]

print(find_list_duplicate_elements(lst))

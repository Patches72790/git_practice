def nb_dig(n, d):
    count = 0
    k_list = []
    k_list_string = []
    for i in range(0, n+1):
        k_list.append(i**2)
    for i in k_list:
        k_list_string.append(str(i))
    for i in k_list_string:
        if len(str(i)) == 1 and str(i) == str(d):
            count += 1
        elif len(str(i)) > 1:
            for digit in i:
                if str(digit) == str(d):
                    count += 1
    return count + " is the number of occurrences of this digit."

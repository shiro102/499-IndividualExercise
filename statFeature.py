def stat(string):
    list_of_word = list(set(string))
    result = []
    for a in list_of_word:
        result.append('The occurrence of "{:s}" is {:d}'.format(a, string.count(a)))

    return result

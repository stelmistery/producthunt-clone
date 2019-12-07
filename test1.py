def drob(a, b, c, d):
    list_vars_str = []
    list_vars_in = [a,b,c,d]
    list_vars_in = list_vars_in.sort()
    for i in list_vars_in:
        for j in list_vars_in:
            list_vars_str = list_vars_str.append(str(i) + '/' + str(j))

    return list_vars_str

drob(1,2,3,4)        

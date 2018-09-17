from itertools import groupby

def count_occurrences(f):
    
    f_dic = {}
    
    f.sort()

    f_values = [len(list(group)) for key, group in groupby(f)]

    f_set = set(f)
    f_unique = list(f_set)
    
    f_unique.sort()
    
    for x in range(0,len(f_unique)):
                   
        f_dic[f_unique[x]] = f_values[x]
    
    #print(f_dic)
    return f_dic
    
    
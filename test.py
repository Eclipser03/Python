s = ['-2' '-1' '8' '11' '4' '5']

s = [int(i) for i in s.split()]
lst = s.sort()
tp_lst = sorted(tuple(lst))
print(s)
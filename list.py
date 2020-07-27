a_list=list(range(1,10))
a_list=a_list[1:8]
a_list.append(9)
a_list.insert(0,5)
a_list.remove(5)
a_list.pop()
print(a_list)
a_list=[x*2+1 for x in range(5)]
print(a_list)
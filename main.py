#list operattions
my_ips = ['192.168.0.1' , '192.168.0.2' , '192.168.0.3']
for ip in my_ips:
    print(f'Connecting to {ip}')

#concatenation of lists

list1 = [1,2]
list2 = [4,5]

full_list = list1 + list2
full_list.append(7)
print(full_list)

sq = lambda x: x**2
print(sq(5))

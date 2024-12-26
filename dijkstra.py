def find_min_distance():
    min_distance = float('inf')
    min_distance_index = None
    for index in range(num):
        if not is_visited[index]:
            if min_distance > len_table[index][0]:
                min_distance = len_table[index][0]
                min_distance_index = index
    return min_distance_index

def print_table():
    print("--------------------------------------------")
    print("node       | ", end=" ")
    for i in range(num): 
        print(f"{chr(ord('A') + i):3s}", end="") 
    print() 

    print("min dis    |", end="")
    for each_end in range(num): 
        if len_table[each_end][0] == float('inf'): 
            print("-  ", end="")
        else:
            print(f"{len_table[each_end][0]:3d}", end="")
    print()

    print("Last node  | ", end=" ")
    for each_end in range(num):
        if len_table[each_end][1] == None: last_hop = '-  '
        else: last_hop = chr(ord('A') + len_table[each_end][1])
        print(f"{last_hop:3s}", end="")
    print()
    
 

num = int(input("Number of Nodes: "))

route = list()    
# 記錄到每一條邊的距離

len_table = [[float('inf'), None] for _ in range(num)]    
# 記錄到起點的長度

is_visited = [False] * num    
# 紀錄是否有訪問過

print("Please input edges (node1, node2, distance): ")
print("Input \"0\" for end.")
while True:
    content = input()
    if content == '0': break
    route.append(list(map(int, content.split())))

start = int(input("Please input start: "))
destination = int(input("Please input destination: "))
len_table[start] = [0, start]
times = 0

for end in range(num):
    if end == start: continue
    node = start

    while True:
        for each_route in route:
            if node == each_route[0]: next = each_route[1]
            elif node == each_route[1]: next = each_route[0]  
            else: continue

            if len_table[next][0] > each_route[2] + len_table[node][0]:
                len_table[next][0] = each_route[2] + len_table[node][0]
                len_table[next][1] = node
            times += 1

        is_visited[node] = True

        node = find_min_distance()
        if node == end or node == None:
            break

# If you try Chiao_Tung_graph.txt data, then don't use print_table()
# print_table()
print("--------------------------------------------")
print(f"Smallest distance from {start} to {destination}: {len_table[destination][0]}m")
print(f"Complete with {times} rounds.")
import numpy as np

def find_min_distance(num, is_visited, len_table, A_star_table):
    min_distance = float('inf')
    min_distance_index = None
    for index in range(num):
        if not is_visited[index]:
            if min_distance > len_table[index][0] + A_star_table[index]:
                min_distance = len_table[index][0] + A_star_table[index]
                min_distance_index = index
    return min_distance_index

def init_A_star(num, coordinate):
    print("Please input the coordinates: ")
    for i in range(num):
        input_coordinate = list(map(int, input().split()))
        coordinate.append(np.array(input_coordinate))

def build_A_star_table(num, end, A_star_table, coordinate):
    for each_node in range(num):
        distance = np.linalg.norm(coordinate[end] - coordinate[each_node])
        A_star_table[each_node] = distance

def print_table(num, len_table):
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
    print("\n--------------------------------------------")
    


num = int(input("Number of Nodes: "))
route = list()    
# 記錄到每一條邊的距離

len_table = [[float('inf'), None] for _ in range(num)]    
# 記錄到起點的長度

is_visited = [False] * num    
# 紀錄是否有訪問過

coordinate = list()    
# 記錄每一個點的幾何位置(A* 使用)

A_star_table = [0] * num
# 每一個點的評價分數(離終點的幾何距離)

print("Please input edges (node1, node2, distance): ")
print("Input \"0\" for end.")
while True:
    content = input()
    if content == '0': break
    route.append(list(map(int, content.split())))

init_A_star(num, coordinate)

start = int(input("Please input start: "))
len_table[start] = [0, start]



times = 0
for end in range(num):
    if end == start: continue
    node = start
    build_A_star_table(num, end, A_star_table, coordinate)

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

        node = find_min_distance(num, is_visited, len_table, A_star_table)
        if node == end or node == None: 
            break
        

print_table(num, len_table)  
print(f"Complete with {times} rounds.")
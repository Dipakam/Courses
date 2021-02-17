import sys

input1 = sys.argv[1]
file = open(input1,"r")
input = file.read().split('\n')
# print(input)
j = 1
graph = {}
connectivity = {}
number_of_graphs = int(input[0])
spanning_tree_packet = {}

def populate_link(graph,link):
    # print(graph)
    # print(link)
    # print(link)
    ports = link.split(' ')
    switch1 = ports[0].split(',')
    switch2 = ports[1].split(',')
    # print(switch1)
    # print(switch2)
    conn1 = switch1[0] + switch2[0]
    conn2 = switch2[0] + switch1[0]
    spanning_tree_packet[switch1[0]] = (switch1[0],switch1[0],0)
    spanning_tree_packet[switch2[0]] = (switch2[0],switch2[0],0)
    connectivity[conn1] = (switch1[1],switch2[1])
    connectivity[conn2] = (switch2[1],switch1[1])
    if(switch1[0] in graph):
        if(switch2[0] in graph):
            if(isinstance(graph[switch1[0]],dict)):
                graph[switch1[0]][switch1[1]] = switch2[0]
            else:
                graph[switch1[0]] = {switch1[1] : switch2[0]}
            if(isinstance(graph[switch2[0]],dict)):
                graph[switch2[0]][switch2[1]] = switch1[0]
            else:
                graph[switch2[0]] = {switch2[1] : switch1[0]}
        else:
            if(isinstance(graph[switch1[0]],dict)):
                graph[switch1[0]][switch1[1]] = switch2[0]
            else:
                graph[switch1[0]] = {switch1[1] : switch2[0]}
            graph[switch2[0]] = {switch2[1] : switch1[0]}
    else:
        if(switch2[0] in graph):
            graph[switch1[0]] = {switch1[1] : switch2[0]}
            if(isinstance(graph[switch2[0]],dict)):
                graph[switch2[0]][switch2[1]] = switch1[0]
            else:
                graph[switch2[0]] = {switch2[1] : switch1[0]}
        else:
            graph[switch1[0]] = {switch1[1] : switch2[0]}
            graph[switch2[0]] = {switch2[1] : switch1[0]}
    # print(graph)


def small_address(sw1,sw2):
    if(int(sw1[1]) < int(sw2[1])):
        return sw1
    else:
        return sw2

def populate_graph(graph,number_of_links,links):
    for i in range(len(links)):
        populate_link(graph,links[i])

for i in range(number_of_graphs):
    number_of_links = int(input[j])
    links = input[j+1:j+number_of_links+1]
    print(number_of_links,links)
    j = j + number_of_links + 1
    populate_graph(graph,number_of_links,links)
    print(graph)
    print(connectivity)
    print(spanning_tree_packet)
    #assume that the order of the input is ascending in the switch address

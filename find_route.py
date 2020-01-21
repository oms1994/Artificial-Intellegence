
#Variable Declarataions

import sys
from queue import*
flag=0;
#maincode

#opens input file and format it accordingly
#mode is for selecting heuristicoption
def format_inputfile_data(inpfile,mode):
    if(mode==0):
        inputnodes = {}
        inputfile = open(inpfile,'r')
        lines = inputfile.readlines()
        inputfile.close()
        for line in lines[:-1]:
            data = line.split()
            
            if(data[0] in inputnodes):
                inputnodes[data[0]][data[1]] = int(data[2])
            else:
                inputnodes[data[0]] = {data[1]:int(data[2])}
            if(data[1] in inputnodes):
                inputnodes[data[1]][data[0]] = int(data[2])
            else:
                inputnodes[data[1]] = {data[0]:int(data[2])}
        return inputnodes
    elif(mode==1):
        h_values = {}
        inputfile = open(inpfile,'r')
        lines = inputfile.readlines()
        inputfile.close()
        for line in lines[:-1]:
            data = line.split()
            h_values[data[0]] = int(data[1])
        return h_values

# if informed search 

def search_informed(start_node, desnode, inputnodes, h_values):
    node_gen = 0
    node_exp = 0
    node_fringe = PriorityQueue()
    node_fringe.put((0,start_node))
    visited = {}
    visited[start_node] = ("",0)
    node_found_arr = []
    max_node = 0
    while not node_fringe.empty():
        if len(node_fringe.queue) > max_node:
            max_node = len(node_fringe.queue)
        _,temp_node = node_fringe.get()
        node_exp+=1
        if temp_node==desnode:
            break
        if temp_node in node_found_arr:
            continue
        node_found_arr.append(temp_node)
        for i in inputnodes[temp_node]:
            node_gen+=1  
            if i not in visited:
                visited[i]=(temp_node,inputnodes[temp_node][i]+visited[temp_node][1])
            node_fringe.put((inputnodes[temp_node][i]+visited[temp_node][1]+h_values[i],i))
    route = []
    distance = "infinity"
    if desnode in visited:
        distance = 0.0
        temp_node = desnode
        while temp_node != start_node:
            distance += inputnodes[visited[temp_node][0]][temp_node]
            route.append(temp_node)
            temp_node = visited[temp_node][0]
    return route,node_exp,node_gen,distance,max_node

#if uninformed search

def search_un_informed(start_node, desnode, inputnodes):
    node_gen = 0
    node_exp = 0
    node_fringe = PriorityQueue()
    node_fringe.put((0,start_node))
    visited = {}
    visited[start_node] = ("",0)
    node_found_arr = []
    max_node = 0
    while not node_fringe.empty():
        if len(node_fringe.queue) > max_node:
            max_node = len(node_fringe.queue)
        _,temp_node = node_fringe.get()
        node_exp+=1
        if temp_node==desnode:
            break
        if temp_node in node_found_arr:
            continue
        node_found_arr.append(temp_node)
        for i in inputnodes[temp_node]:    
            node_gen+=1
            # node_found_arr.append(i)
            node_fringe.put((inputnodes[temp_node][i]+visited[temp_node][1],i))
            if i not in visited:
                visited[i]=(temp_node,inputnodes[temp_node][i]+visited[temp_node][1])
    route = []
    distance = "infinity"
    if desnode in visited:
        distance = 0.0
        temp_node = desnode
        while temp_node != start_node:
            distance += inputnodes[visited[temp_node][0]][temp_node]
            route.append(temp_node)
            temp_node = visited[temp_node][0]
    return route,node_exp,node_gen,distance,max_node



if len(sys.argv)==5:
    inpfile = sys.argv[1]
    noderoot = sys.argv[2]
    nodedes = sys.argv[3]
    inpfile_h = sys.argv[4]
    inputnodes = format_inputfile_data(inpfile,0)
    h_values = format_inputfile_data(inpfile_h,1)
    route,node_exp, node_gen, distance, max_node = search_informed(noderoot,nodedes,inputnodes,h_values)
    print("nodes expanded: {}".format(node_exp))
    print("nodes generated: {}".format(node_gen))
    print("maximum nodes in m/m: {}".format(max_node))
    print("total distance: {}".format(distance))
    if(str(distance)=="infinity"):
        print("route: none")
    else:
        print("route:")   
    temp_node = noderoot
    for path in route[::-1]:
        print("{} to {}, {} km".format(temp_node,path,inputnodes[temp_node][path]))
        temp_node = path

elif len(sys.argv)==4:
    inpfile = sys.argv[1]
    noderoot = sys.argv[2]
    nodedes = sys.argv[3]
    inputnodes = format_inputfile_data(inpfile,0)
    route,node_exp, node_gen, distance,max_node = search_un_informed(noderoot,nodedes,inputnodes)

    print("nodes generated: {}".format(node_exp))
    print("nodes expoanded: {}".format(node_gen))
    print("maximum nodes in m/m: {}".format(max_node))
    print("total distance: {}".format(distance))
    if(str(distance)=="infinity"):
        print("route: none")
    else:
        print("route:")    
    temp_node = noderoot
    for path in route[::-1]:
        print("{} to {}, {} km".format(temp_node,path,inputnodes[temp_node][path]))
        temp_node = path        
else:
    print("enter valid arguments")

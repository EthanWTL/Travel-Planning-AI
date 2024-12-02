def getHotelIndex(day,cordinates):
    hotel_index = 0
    if day > 0:
        for j in range(day):
            hotel_index += len(cordinates[j])
    return hotel_index

def totalCost_multiday(mask, pos, day, cordinates, n, visited, cost, info_lists):
    visit_requirement = len(cordinates[day])
    distance_list = []
    i_list = []

    hotel_index = getHotelIndex(day,cordinates)
    # Base case: if all cities are visited, return the
    # cost to return to the starting city (0)

    if mask == (1 << n) - 1:
        return cost[pos][hotel_index]

    if visit_requirement == visited:
        for i in range(n):
            if (mask & (1 << i)) == 0: 
                i_list.append(i)
                distance_list.append(cost[pos][i] + totalCost_multiday(mask | (1 << i), hotel_index, day + 1, cordinates, n, 1, cost, info_lists))
        
        info_list = [i_list, distance_list]
        info_lists.append(info_list)
        
        return min(distance_list) + cost[pos][hotel_index] # change this to the old hotel position
    
    # Try visiting every city that has not been visited yet
    for i in range(n):
        if (mask & (1 << i)) == 0: 

            i_list.append(i)
            # If city i is not visited, visit it and 
             #  update the mask
            distance_list.append(cost[pos][i] +
                      totalCost_multiday(mask | (1 << i), i, day, cordinates, n, visited + 1, cost, info_lists))
        

    info_list = [i_list, distance_list]
    info_lists.append(info_list)
  
    return min(distance_list)



#test
cordinates = [[(0,0),(0,0),(0,0)], [(0,0),(0,0),(0,0),(0,0)]]
distance_matrix = [
    [0,10,12, 1000, 13, 1000,1000],
    [10,0,11,1000,1000,1000,1000],
    [12,11,0,1000,1000,1000,1000],
    [1000,1000,1000,0,14,1000,17],
    [1000,1000,1000,14,0,15,1000,],
    [1000,1000,1000,1000,15,0,16],
    [1000,1000,1000,17,1000,16,0]
]

n = len(distance_matrix)
info_list = []
#newMask will have all the hotels as 1 before the function.
newMask = 1
index_list = list(range(len(cordinates) - 1))
index_list = index_list[::-1]
newMask = 1
for i in index_list:
    newMask = (newMask << (len(cordinates[i]))) + 1

optimized_distance = totalCost_multiday(newMask,0,0,cordinates,n,1,distance_matrix, info_list)
optimized_distance
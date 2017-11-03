#!/usr/bin/env python3

# Report
# (1) As the problem was considered, several aspects were taken into consideration. The most important factor in my case
# was to assume that the value of k(time to check a group assignment) exceeds m and n by a large degree which makes it
# more logical to assume all group sizes as 3 unless there were not enough students fill the group. If we do assume that
# k exceeds m and n by a large amount we understand that the lesser the number of groups, the lesser time needs to be
# given. The converse also holds true.
# The state space for this problem includes all possible combinations of all group sizes ranging 0-3. The successor
# function is any student that is switched with another student in a group according to the preferred list. Edge weights
# is not applicable in this case. Goal state is not defined. Heuristic function is also not applicable.
# (2) The algorithm used in this program uses list of lists to create a set of all groups in one big list. Then we start
# by swapping the first element of the first list with elements of other list to check if overall cost reduces. If it
# does reduce, we update the cost and then check for the best replacement of the next element. After we have checked the
# best replacements for all lists, the final output with the least cost is displayed.
# (3) Several problems were faced. The first problem is how to determine the data structure to be used. Since I am not
# very efficient in Data Structures, I had several problems assigning the appropriate data structure. The next problem
# was the right algorithm. There was no goal state or right answer, there were best possible answers. The primitive way
# to go about it is to use brute force method which involved searching for all possible cases of all solutions. Then we
# needed to evolve the then current solution to find a better solution. What we assumed in this problem is the value of
# k will be large since time taken to check an assignment will be much greater than time taken to hold a meeting or
# reply to a mail.

import json
import string
import sys
import random
import math

filename = sys.argv[1]
kvalue = int(sys.argv[2])
m = int(sys.argv[3])
n = int(sys.argv[4])


def matchmaker(data):

    length_data = len(data)
    students = []
    
    for i in range(0,length_data):
        students.append(data[i]["userID"])
    length_stud = len(students)

    count = 0
    if (length_stud%3 !=0):
        count = 1
    length_init = int(length_stud/3)+ count

    #actual logical part

    initial=[]
    index1=0
    for k in range(length_init):
        temp = []
        end=index1+3
        if end >len(students):
            end =len(students)
        for j in range(index1,end):
            temp.append(students[j])
        initial.append(temp)
        index1+=3

    originalcost = costcheck(initial,data)

    newcost = 0

    # Now we swap elements required number of times to check for a better cost
    for i in range(len(initial)-1):
        for p in range(i+1,len(initial)-1):
            for j in range(3):

            #if():# should contain searching for preferredlist
                initial[i][j], initial[p][j] = initial[p][j], initial[i][j]
                newcost = costcheck(initial, data)
                if(newcost >= originalcost):
                    initial[i][j], initial[p][j] = initial[p][j], initial[i][j]
                else:
                    originalcost = newcost

    # Swap for last list
    last_index=len(initial)-1
    for i in range(0, len(initial)-1):
        for j in range(len(initial[last_index])):
            initial[i][j], initial[last_index][j] = initial[last_index][j], initial[i][j]
            newcost = costcheck(initial, data)
            if (newcost >= originalcost):
                initial[i][j], initial[last_index][j] = initial[last_index][j], initial[i][j]
            else:
                originalcost = newcost


    originalcost = originalcost + kvalue*len(initial)
    for group in initial:
        print( " ".join([element for element in group]))
    print(originalcost)

    return 0

#def assignteam(data)

def costcheck(list1,data):
    cost = 0
    for users in list1:
        for user in users:
            userpref = checkelement(data, user)
            for c in range(len(users)):
                if users[c]!= user:
                    if(users[c] in userpref['prefer']):
                        continue
                    else:
                        cost = cost+n


    for users in list1:
        for user in users:
            userpref = checkelement(data, user)
            for c in range(len(users)):
                if users[c]!= user :
                    if(users[c] in userpref['nonPrefer']):
                        cost = cost + m

    

    for users in list1:
        for user in users:
            userpref = checkelement(data, user)
            if(userpref['preferNumber'] != 3 and userpref['preferNumber'] != 0):
                cost+=1


    size = len(list1)


    return cost  
            

def checkelement(data, userID):
    for element in data:
        if element['userID']==userID:
            return element

data = []
with open(filename) as f:
    for line in f:
        line = line.replace("\n", "")
        lineData = line.split(" ")
        preferenceList = []
        nonPreferenceList = []
        if (not (lineData[2] is "_" )):
            seperated = lineData[2].split(",")
            preferenceList = [preferName for preferName in seperated]

        if (not (lineData[3] is "_" )):
            seperated = lineData[3].split(",")
            nonPreferenceList = [nonPreferName for nonPreferName in seperated]
      
        currentData = {
            'userID': lineData[0],
            'preferNumber': lineData[1],
            'prefer': preferenceList,
            'nonPrefer': nonPreferenceList,
            'team_index': 0
        }
        data.append(currentData)

matchmaker(data)




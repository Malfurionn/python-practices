# print first item of each list then second item and ....
def character_picture(myList):
#     loop through all indexes
    for i in range(len(myList[0])):
#         loop through all lists
        for j in range(len(myList)):
#         print myList[0][0] then [1][0] then [2][0] 
            print(myList[j][i], end="")
# Print new line
        print()
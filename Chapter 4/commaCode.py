#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Solution for first practice project
def list_to_string(myList):
#    empty string as a placeholder
    b = ""
#    Check if the list is not empty
    if len(myList) != 0:
#        Loop through the list until the second-last item of the list and add the items to giant string
        for i in range(len(myList)-1):
            b += str(myList[i]) + ", "
#        adds the last item to the giant string  
        b = b + ", and " + str(myList[-1])
        return b
#     return emty if the list is emty
    else:
        return ""


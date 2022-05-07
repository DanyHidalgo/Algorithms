'''
Merge 2 ordered lists into 1 ordered list
'''


def merge_list(a, b):
    
    c = []
    min = []
    max = []
    
    for i in range(len(b)):
    
        if (a[i] < b[i]):
        
            min.insert(i, a[i])
            max.insert (i, b[i])

            c.insert(i + (i + 1), max[i])
            c.insert(i - (i + 1), min[i])
        
        elif (a[i] > b[i]):
        
            min.insert(i, b[i])
            max.insert(i, a[i])

            c.insert(i + (i + 1), max[i])
            c.insert(i - (i + 1), min[i])
      
    

    print(c)

# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    merged = []
    # TO-DO

   
    

    #compare items in each array
    #elements
    #merged array
    #indices
    #divide and conquer
    #element before, element after
    #different array lengths

    #we want to *compare two *sorted arrays for which we *do not know the lengths ahead of time
    #we want to *merge them into a new array in sorted order in O(n) fashion

    #we want our loop to be determined by the total number of list elements processed by the merge function
    #we want to have one for loop that sorts when necessary



    # [0,10,11]
    # [4,7,8,9,10,45]


        # i run out of roadway so to speak with lists of different lengths
      # if first element lt second array first elemnet add to merge
      # else add second array first to merge
      #need more variables when you are at a standstill!!!
      #can more be added at each step
      #slices?
      #total train of thought lost
      #never thought of conditions (empty arrs eval to false) in python if using an IF expression

    while(arrA or arrB):
        if not arrB or (arrA and arrA[0] < arrB[0]):
            merged.append(arrA.pop(0))
        
        else:
            merged.append(arrB.pop(0))

    



        
   
    
    
        

        


       
            






    
    return merged


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    

    

    # if len(arr) == 0:
    #     return merged_list

  

    if len(arr) <= 1:
       

        return  arr #where does this returned value go?
        
    
    

    else:
        split = len(arr)//2
        a1, a2 = arr[0:split], arr[split:]
            
        return merge(merge_sort(a1),merge_sort(a2))


    


   


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr

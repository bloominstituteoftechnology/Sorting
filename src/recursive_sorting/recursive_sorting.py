# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    smallA=0
    smallB=0
    sorted=0
    Aend=False
    Bend=False
    while sorted<elements:
        if (Aend==False) and (Bend==False):
            if arrA[smallA] < arrB[smallB]:
                merged_arr[sorted] = arrA [smallA]
                sorted = sorted +1
                if smallA < len(arrA)-1:
                    smallA=smallA+1
                else:
                    Aend=True

         #   else:
         #       print(sorted, smallB)
         #       merged_arr[sorted] = arrB[smallB]
         #       smallB = smallB+1
         #       sorted = sorted +1
            else:
                merged_arr[sorted] = arrB[smallB]
                sorted = sorted + 1
                if smallB < len(arrB)-1:
                    smallB=smallB+1
                else:
                    Bend=True

         #   else:
         #       merged_arr[sorted] = arrA[smallA]
         #       smallA=smallA+1
         #       sorted = sorted +1

        elif Aend==True:
            merged_arr[sorted]=arrB[smallB]
            sorted=sorted+1
            smallB=smallB+1
        elif Bend==True:
            merged_arr[sorted]=arrA[smallA]
            sorted=sorted+1
            smallA=smallA+1

    
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    if len(arr)<=1:
        print("done")
        return arr
    else:
        middle_index = len(arr)//2
        print("Original arr : ",len(arr))
        print("1st  arr : ", len(arr[:middle_index]))
        print("2nd arr : ", len(arr[middle_index:]))
        print("---------------------------")

        return merge(merge_sort(arr[:middle_index]),merge_sort(arr[middle_index:]))
    # TO-DO



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

a=[1,5,100,80,8,60,9,15,2,50,20,7,30,45,3]
b=[2,7]
c=[3,1,5,10,2]
d=[5]
f=[1,3]
g=[5,10]
e= merge_sort(a)
print(e)


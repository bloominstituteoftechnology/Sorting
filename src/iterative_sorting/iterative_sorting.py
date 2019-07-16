# TO-DO: Complete the selection_sort() function below 

#all in all 6n^2 +1 ??
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1): #O(n)
        cur_index = i# O(1)

        for i in range(cur_index +1, len(arr)):#0(n) current index will change and give range(3, 10) , range(4 10)
            comparison_index = i#(O(1))

            if arr[cur_index] < arr[comparison_index]:#O(1))
                pass#O(1))
            
            elif arr[cur_index] >= arr[comparison_index ]:#O(1))
                arr[cur_index], arr[comparison_index] =  arr[comparison_index], arr[cur_index]#O(2))?

            
                

    return arr#O(1))


# TO-DO:  implement the Bubble Sort function below

#unknown how many loops, 
#find connection betwen data and unknown
#how do I know how many swaps are still needed?
def bubble_sort( arr ):

    swap_count = 0
    restart = True
    
    while restart == True:
        
        for i in range(0, len(arr) - 1):

            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

                
                print(arr,i,swap_count,len(arr))
                swap_count = 0
                break
            

            if arr[i] < arr[i + 1]:
                swap_count = swap_count + 1
                print(arr,i,swap_count,len(arr))
                
    
            if swap_count == len(arr) - 1:
                print("FINALLY",arr)
                
                
                return arr

    
        

                

       

       
    


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr
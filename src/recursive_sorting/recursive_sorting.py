# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    l = len(arrA) + len(arrB)
    merged_sorted = []

    for _ in range(l):
        if len(arrA) > 1:
            smallestA = arrA[0]
            smallestIndexA = 0
            for count, _ in enumerate(arrA):
                if smallestA > arrA[count]:
                    smallestA = arrA[count]
                    smallestIndexA = count
        elif len(arrA) == 1:
            smallestA = arrA[0]
            smallestIndexA = 0
        else:
            smallestA = None

        if len(arrB) > 1:
            smallestB = arrB[0]
            smallestIndexB = 0
            for count, _ in enumerate(arrB):
                if smallestB > arrB[count]:
                    smallestB = arrB[count]
                    smallestIndexB = count
        elif len(arrB) == 1:
            smallestB = arrB[0]
            smallestIndexB = 0
        else:
            smallestB = None

        if smallestA != None and smallestB != None:
            if smallestA > smallestB:
                arrB.pop(smallestIndexB)
                merged_sorted.append(smallestB)
            else:
                arrA.pop(smallestIndexA)
                merged_sorted.append(smallestA)

        elif smallestA != None:
            arrA.pop(smallestIndexA)
            merged_sorted.append(smallestA)
            pass
        elif smallestB != None:
            arrB.pop(smallestIndexB)
            merged_sorted.append(smallestB)
    return merged_sorted


# TO-DO: implement the Merge Sort function below USING RECURSION

def merge_sort(arr):
    newArr = []
    if len(arr) > 1:
        middle = len(arr) // 2
        left = merge_sort(arr[:middle])
        right = merge_sort(arr[middle:])
        newArr = merge(left, right)
        return newArr
    return arr


print(merge_sort([5, 3, 8, 6, 7, 1]))


"""
function merge(arrA, arrB) {
  let mergedsorted = []
  let len = arrA.length + arrB.length
  let smallestA
  let smallestIndexA
  let smallestB
  let smallestIndexB


  for (let tracker = 0; tracker < len; tracker++) {
    if (arrA.length > 1) {
      smallestA = arrA[0]
      smallestIndexA = 0
      for (let i = 0; i < arrA.length; i++) {
        if (smallestA > arrA[i]) {
          smallestA = arrA[i]
          smallestIndexA = i
        }
      }
    } else if (arrA.length === 1) {
      smallestA = arrA[0]
      smallestIndexA = 0
    } else {
      smallestA = null
    }

    if (arrB.length > 1) {
      smallestB = arrB[0]
      smallestIndexB = 0
      for (let i = 0; i < arrB.length; i++) {
        if (smallestB > arrB[i]) {
          smallestB = arrB[i]
          smallestIndexB = i
        }
      }
    } else if (arrB.length === 1) {
      smallestB = arrB[0]
      smallestIndexB = 0
    } else {
      smallestB = null
    }

    if (smallestA !== null && smallestB !== null) {
      if (smallestA > smallestB) {
        arrB.splice(smallestIndexB, 1);
        mergedsorted.push(smallestB)  
      } else {
        arrA.splice(smallestIndexA, 1);
        mergedsorted.push(smallestA)
      }

    } else if (smallestA !== null) {
      arrA.splice(smallestIndexA, 1);
      mergedsorted.push(smallestA)
      
    } else if (smallestB !== null) {
      arrB.splice(smallestIndexB, 1);
      mergedsorted.push(smallestB)
    }
  }
  return mergedsorted
}


function mergeSort(arr) {
  let middle
  let left
  let right
  let newArr = []
  
  if (arr.length > 1) {
    middle = Math.floor(arr.length / 2)
    left = mergeSort(arr.slice(0, middle))
    right = mergeSort(arr.slice(middle))
    newArr = merge(left, right)
    return newArr
  }
  return arr
}

"""


# STRETCH: implement an in-place merge sort algorithm

def merge_in_place(arr, start, mid, end):
        # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr

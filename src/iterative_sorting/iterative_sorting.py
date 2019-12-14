# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    for count, _ in enumerate(arr):
        smallest = arr[count]
        smallestIndex = count
        inner_count = count + 1
        while inner_count < len(arr):
            if smallest > arr[inner_count]:
                smallest = arr[inner_count]
                smallestIndex = inner_count
            inner_count += 1
        if smallestIndex != count:
            arr[smallestIndex] = arr[count]
            arr[count] = smallest
    return arr


#print(selection_sort([8, 250, 8000, 135, 6584, 23, 7, 63, 8, 3, 4, 3, 2, 6, 5, 20, 50, 8, 3, 9, 4]))


"""
function SelectionSort(list) {
  let temp;
  let smallest;
  let smallestIndex;
  for (let i = 0; i <= list.length - 1; i++) {
    temp = list[i]
    smallest = list[i]
    smallestIndex = i
    for (let j = i + 1; j <= list.length - 1; j++) {
      if (smallest > list[j]) {
        smallest = list[j]
        smallestIndex = j
      }
    }
    if (smallestIndex !== i) {
      list[smallestIndex] = list[i]
      list[i] = smallest
    }
  }
  return list;
}

console.log("====SELECTION=====")
console.log(SelectionSort([8, 250, 8000, 135, 6584, 23, 7, 1.6, 8, 1.8, 2, 20.8, 6, 5, 20, 50, 8, 3, 9, 4]))
"""


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    for _ in arr:
        for inner_count, _ in enumerate(range(len(arr) - 1)):
            if arr[inner_count + 1] < arr[inner_count]:
                temp = arr[inner_count + 1]
                arr[inner_count + 1] = arr[inner_count]
                arr[inner_count] = temp
    return arr

#print(bubble_sort([8, 250, 8000, 135, 6584, 23, 7, 63, 8, 3, 4, 3, 2, 6, 5, 20, 50, 8, 3, 9, 4]))


"""
function bubbleSort(list) {
  let temp;
  for (let i = 0; i < list.length - 1; i++) {
    for (let j = 0; j < list.length -1; j++) {
      if (list[j + 1] < list[j]) {
        temp = list[j + 1]
        list[j + 1] = list[j]
        list[j] = temp
      }
    }
  }
  return list
}

console.log("====BUBBLE=====")
console.log(bubbleSort([8, 250, 8000, 135, 6584, 23, 7, 1.6, 8, 1.8, 2, 20.8, 6, 5, 20, 50, 8, 3, 9, 4]))
"""


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr

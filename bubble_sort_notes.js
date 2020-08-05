// Solution 1
function bubbleSort(arr) {
 for (let i = 0; i < arr.length; i++) {
   for (let j = 0; j < arr.length; j++) {
      if (arr[j] > arr[j+1]) {
        [arr[j], arr[j+1]] = [arr[j+1], arr[j]]
        break;
      }
   }
 }
return arr
}
 
// Lambda Model Solution from Web12
function bubbleSort(arr) {
  let swappedValue;
  do {
    swappedValue = false;
    for (let i = 0; i < arr.length - 1; i++) {
      if (arr[i] > arr[i + 1]) {
        let temp = arr[i];
        arr[i] = arr[i + 1];
        arr[i + 1] = temp;
        swappedValue = true;
      }
    }
  } while (swappedValue);
  return arr;
}


// A somewhat similar solution  with a while loop.......
function bubbleSort(arr) {
  let results = [];
  let temp;
  let move = true;
  
  while (move) {
    move = false;
    for (let i = 0; i < arr.length - 1; i++) {
      if (arr[i] > arr[i + 1]) {
        arr = swap(arr, i, i+1);
        move = true;
      }
    }
  }
  return arr;
}
function swap(arr, a, b) {
  let temp = arr[a];
  arr[a] = arr[b];
  arr[b] = temp;
  return arr;
}
 
 bubbleSort([13, 2, 7, 42, 9, 78, 190]); 

 // Sam Ko Solutions

 function bubbleSortOld(arr) {
  let swappedValue;
  let len = arr.length - 1;
  
  do {
    swappedValue = false;
    
    for (let i = 0; i < len; i++) {
      if (arr[i] > arr[i + 1]) {
        [arr[i], arr[i + 1]] = [arr[i + 1], arr[i]];
        swappedValue = true;
      }
    }
​
    len--;
  } while (swappedValue);
​
  return arr;
}
​
function bubbleSortNew(arr) {
  let swappedValue;
  let len = arr.length - 1;
  
  for (let i = 0; i < arr.length; i++) {
    swappedValue = false;
​
    for (let j = 0; j < len; j++) {
      if (arr[j] > arr[j + 1]) {
        [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]];
        swappedValue = true;
      }
    }
​
    if (swappedValue) {
      len--;
      continue;
    } else {
      break;
    }
  }
​
  return arr;
}
​
console.log(bubbleSortOld([13, 2, 7, 42, 9, 78, 190, 3, 4]));
console.log(bubbleSortNew([13, 2, 7, 42, 9, 78, 190, 3, 4]));
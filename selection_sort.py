def selection_sort(arr):
  for i in range(len(arr)):

    min_index = i
    for j in range(i+1,len(arr)):
      if arr[j]< arr[min_index]:
        min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]

  return arr


n = int(input("enter number of elements in array: "))
arr = []

for i in range(n):
  element = int(input())
  arr.append(element)

print("unsorted array is: ", arr)
sorted_arr = selection_sort(arr)
print("sorted array is: ", sorted_arr)




"""
Output:


enter number of elements in array: 5
23
6
112
46
3
unsorted array is:  [23, 6, 112, 46, 3]
sorted array is:  [3, 6, 23, 46, 112]
"""

#Quick Sort Code
#Sort an array A using Quick Sort.
#Change in the input array itself. So no need to return or print anything.


#Input format :
#Line 1 : Integer n i.e. Array size
#Line 2 : Array elements (separated by space)
#Output format :
#Array elements in increasing order (separated by space)
#Constraints :
#1 <= n <= 10^3

def partition(arr,start,end):
 pivot = arr[start]
 c = 0
 for i in range(start,end+1):
  if arr[i]<pivot:
   c = c+1
 arr[start+c],arr[start] = arr[start],arr[start+c]
 pivotIndex = start+c
 i = start
 j = end
 while i < j:
  while i<pivotIndex and arr[i] < pivot:
   i = i+1
  while j>pivotIndex and arr[j] >= pivot:
   j = j-1
  arr[i],arr[j]=arr[j],arr[i]
 return pivotIndex


def quickSort(arr, start, end):
 if start >= end:
  return
 pivotIndex = partition(arr,start,end)
 quickSort(arr,start,pivotIndex-1)
 quickSort(arr,pivotIndex+1,end)
    

n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
quickSort(arr, 0, n-1)
print(*arr)
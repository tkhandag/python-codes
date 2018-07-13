def binary_search_recursive(arr, elem, start=0, end=None):
    if end is None:
        end = len(arr) - 1
    if start > end:
        return False

    mid = (start + end) // 2
    if elem == arr[mid]:
        return mid
    if elem < arr[mid]:
        return binary_search_recursive(arr, elem, start, mid-1)
    # elem > arr[mid]
    return binary_search_recursive(arr, elem, mid+1, end)
n=input("enter no of element")
arr=[]
for v in n:
    arr.append(int(input("enter vth element")))
ele=int(input("enter element you want to search"))    
binary_search_recursive(arr, ele, start=0, end=None)
    
    
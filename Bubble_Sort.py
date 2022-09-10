def Bubble_Sort(arr: list) -> list:
    for _ in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print(arr)

arr = [6,3,7,5, 3,6,3,7,5, 3,6,3,7,5, 3,6,3,7,5, 3,]

Bubble_Sort(arr=arr)
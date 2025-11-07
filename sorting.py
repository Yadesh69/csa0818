arr = list(map(int, input("Enter numbers separated by space: ").split()))
arr.sort()
n = len(arr)
mid = n // 2
if n % 2 == 0:
     middle = (arr[mid - 1] + arr[mid]) / 2
else:
    middle = arr[mid]

print("Sorted array:", arr)
print("Middle element:", middle)

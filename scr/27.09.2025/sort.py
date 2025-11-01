arr = input()
arr = [int(x) for x in arr.split()]
n = len(arr)


for j in range(n):
    flag = False
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            flag = True
    if flag == False:
        print(arr)
        break
print(arr)
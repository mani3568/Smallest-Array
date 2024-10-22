arr=[2,5,1,3,0]
min=arr[0]
n=len(arr)
for i in range(1,n):
    if arr[i]<min:
        min=arr[i]
print(min)
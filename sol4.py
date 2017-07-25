num=int(input())

arr1=input().split(' ')
arr2=input().split(' ')
arr3=[]
for i in range(num):
    arr3.append(int(arr1[i])+int(arr2[i]))

print (*arr3)

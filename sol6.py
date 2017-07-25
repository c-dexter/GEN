case=int(raw_input())
lis=[]
ans=[]
for i in range(case):
    lis.append(raw_input())

for i in range(case):
    num=0
    for j in range(0,i):
        if(lis[i]>lis[j]):
            num+=1
    ans.append(num)

for i in range(case):
    print ans[i]
    

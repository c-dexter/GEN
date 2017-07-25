case=int(input())
l_cost=[]

for i in range(case):
    
    check_p=input()
    
    c_array=[]
    l_array=[]
    c_petrol=0
    m_cost=0
    petrol=0
    
    
    temp=raw_input()
    c_array=temp.split(' ')
        
    
    temp1=raw_input()
    l_array=temp1.split(' ')

    for j in range(check_p):

        if(petrol<(int(l_array[j]))):
            k=j
            while(k<check_p):
                if(int(c_array[k])<int(c_array[j])):
                    break
                k=k+1
            x=j
            while(x<k):
                m_cost=m_cost+int(c_array[j])*(int(l_array[x]))
                petrol=petrol+int(l_array[x])
                x=x+1
        petrol=petrol-int(l_array[j])
    print(m_cost)
              


    

    
    

        

case=int(input())

for i in range(case):
    val=raw_input()
    data=raw_input().split(' ')
    #data=dat.split(' ')
    while(len(data)!=1):
        index=0
        j=0
      #  print 'hi'
        while(j<len(data)):
            if((j+1)==len(data)):
                #print 'lol123'
                xor=int(data[j])
               # print (' %d jth %d j') %(int(data[j]),j)
                data.pop()
                data.insert(index,xor)
            else:
               # print 'lol'
               # print j,len(data)
                xor=int(data[j])^int(data[j+1])
              #  print data[j],data[j+1]
                data.pop(j)
                data.pop(j)
                data.insert(index,xor)
               # print ('%d j %d index %d length') %(j,index,len(data))
               # print data
            index=index+1
            #print index
            j=j+1
    print int(data[0])
              
             
           
        





   
        

cases=int(raw_input())

for i in range(cases):
    pal=raw_input()
    default='YES'
    if((len(pal)%2)==0):
        dom='EVEN'
        for j in range((len(pal)+1)/2):
            if (pal[j]!=pal[len(pal)-1-j]):
                default='NO'
                break
    else:
        dom='ODD'
        for j in range((len(pal)/2)):
                       if (pal[j]!=pal[len(pal)-1-j]):
                       
                           default='NO'
                           break
        
    if(default=='NO'):
                       print default
    else:
                       print default,dom

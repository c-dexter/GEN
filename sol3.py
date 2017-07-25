case=int(input())

for i in range(case):
    dim=int(input())
    mat=[]
    inv=0
    for j in range(dim):
        mat +=raw_input().split(' ')

    for r in range(dim):
        for c in range(dim):

            for r_d in range(r,dim):
                for c_d in range(c,dim):

                    if((int(mat[r*dim+c]))>(int(mat[r_d*dim+c_d]))):
                        inv=inv+1

    print inv

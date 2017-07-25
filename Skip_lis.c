#include<stdlib.h>
#include<stdio.h>

struct sl{
int a;
struct sl *lt;
struct sl *dn;
}demo;

int level=4;

void main()
{
    struct sl *a[level];
    int i,flag,val,forw=1;
    struct sl *t=(struct sl *)malloc(sizeof(demo));

    for(i=0;i<level;i++)
    a[i]=(struct sl *)malloc(sizeof(demo));

    for(i=0;i<level;i++)
    {
        flag=10;
        forw=1;
        while(forw)
        {
            printf("Enter the Val:\t");
            scanf("%d",&val);
            t->a=val;
            printf("1/0:\t");
            scanf("%d",&forw);
                if(forw)
                {
                   t->lt=(struct sl *)malloc(sizeof(demo));
                }
                else
                    t->lt=NULL;

                if(flag==10)
                    a[i]=t;

            flag=0;
            t=t->lt;
        }
        t=(struct sl *)malloc(sizeof(demo));
    }


    for(i=0;i<level;i++)
    {
        while(1)
        {
            if((a[i])==NULL)
            break;

            else
            {
            printf("%d \t",(a[i])->a);
            (a[i])=(a[i])->lt;
            }
        }
        printf("\n");
    }

}

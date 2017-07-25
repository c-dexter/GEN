#include<stdio.h>
#include<stdlib.h>

struct hash{
int a;
struct hash *ptr;
}demo;


void main()
{
    struct hash *pt;
    struct hash h_t[7];
    int arr[7]={50,790,76,85,92,70,99};
    int i,val;

    for(i=0;i<7;i++)
    {
        h_t[i].ptr=NULL;
        h_t[i].a=0;
    }

    for(i=0;i<7;i++)
    {
        val=arr[i]%7;

        if((h_t[val].a)==0)
            (h_t[val].a)=arr[i];

        else
            {
               pt=h_t[val].ptr;
               if(pt==NULL)
               {
                   h_t[val].ptr=(struct hash *)malloc(sizeof(demo));
                   pt=h_t[val].ptr;

               }
               else
               {
                    while(pt->ptr!=NULL)
                        {
                            pt=pt->ptr;
                        }

                    pt->ptr=(struct hash *)malloc(sizeof(demo));
                    pt=pt->ptr;
                }

                pt->a=arr[i];
                pt->ptr=NULL;

            }
        }

   for(i=0;i<7;i++)
    {
        printf("%d\t",h_t[i].a);

        if(((h_t[i].ptr))==NULL)
        {
            printf("\n");
             continue;
        }
        else
        {
            pt=(h_t[i].ptr);
            while(pt!=NULL)
            {
                printf("%d\t",pt->a);
                pt=pt->ptr;
            }
        }
        printf("\n");
    }
}

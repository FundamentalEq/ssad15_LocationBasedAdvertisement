#include<stdio.h>
#include<stdlib.h>
int main()
{
int j,jj,ini,inii,aa,jjj;
printf("efhgeuhgreughru");
int N=1234;
int i;
float array[1000000];
printf("efhgeuhgreughru");
for(i=0;i<10000;i=i+1)
{
printf("efhgeuhgreughru");
long long int Nt=rand();
printf("efhgeuhgreughru");
Nt=(Nt%1000001);
printf("efhgeuhgreughru");
aa=0;
printf("efhgeuhgreughru");
printf("value trail %lld",Nt);
for(jjj=0;jjj<Nt;jjj=jjj+1)
{
j=0;
jj=0;
ini=0;
inii=0;
while (j<N)
{
long long int z=rand();
z=z%1000000;
double q=z/(1000000*1.0);
if (q<0.5)
ini=ini+1;
else
ini=ini-1;
j=j+1;
}
while (jj<N)
{
 long long int z=rand();
                z=z%1000000;
                double q=z/(1000000*1.0);

                if (q<0.5)
                        inii=inii+1;
                else
                        inii=inii-1;
jj=jj+1;
}
if (ini==inii)
aa=aa+1;
}
array[Nt]=aa/Nt;
printf("value od prob %lf at a trail %lld",array[Nt],Nt);
}
return 0;
}

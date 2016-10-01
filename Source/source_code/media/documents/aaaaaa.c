#include<stdio.h>
#include<stdlib.h>
int main()
{
	int j,jj,ini,inii,aa,jjj;
	int N=0;
         int Nt;
        scanf("%d",&Nt);
	int i;
        double array[1000000];
	for(i=200;i<1000;i=i+1,N=N+1)
	{
                double k=1;
                 int mmm;
                 for(mmm=1;mmm<=2*N-1;mmm=mmm+2)
                   {
                     k=k*(mmm/((mmm+1)*1.0));
                   }
                  int mm;
                  aa=0;
                  for(mm=0;mm<Nt;mm=mm+1)
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
			while(jj<N)
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
                  array[N]=(aa/(Nt*1.0))-k;
     }
int p;
for(p=0;p<1000;p=p+1)
{
if (array[p] >= 0)
printf("%d      %lf\n",p,array[p]);
if (array[Nt] < 0)
printf("%d     %lf\n",p,-1*array[p]);
}

return 0;
}


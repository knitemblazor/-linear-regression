//linear regression using gradient descend 


#include<stdio.h>

float gradient_descent(float x[10],float w[10],float y[10],float yp[10])
{ float dw,d1;

for(int j=1;j<10;j++)
   { dw=0;
     for(int i=0;i<10;i++)
      {
        yp[i]=w[j-1]*x[i];
        d1=((yp[i]-y[i])*x[i]);
        dw=(d1+dw)/10;
       // printf("%f\n",dw);

      }
       ;
       w[j]=w[j-1]-0.1*dw;
   }
return(printf("%f",w[9]));
 }



void main()

{ float x[10]={1,2,3,4,5,6,7,8,9,10},yp[10],d1;
  float y[10]={1,2,3,4,5,6,7,8,9,10},w[10],dw=0;
  int i,j;
  w[0]=0.1;
gradient_descent(x,w,y,yp);

}

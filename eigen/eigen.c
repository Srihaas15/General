//only for symmetric matrices
#include<stdio.h>
#include<math.h>

void findpq(int n, double a[n][n], int *p, int *q) {
   *p=-1;
   *q=-1;
    double maxvalue = 0.0;
    for (int i = 0; i < n; i++) {
      for (int j = i + 1; j < n; j++) {  
         if (fabs(a[i][j]) > maxvalue) {
             maxvalue = fabs(a[i][j]);
               *p = i;
               *q = j;
            }
        }
    }
}

void jacobi(int n,double a[n][n],double P[n][n],int p,int q){
     double t;
     double temp1[n][n],temp2[n][n];
    t=0.5*atan((2*a[p][q])/(a[p][p]-a[q][q]));     
     double c,s;
     c=cos(t);
     s=sin(t);
      for(int i = 0;i<n;i++){
       for(int j=0;j<n;j++){
        if(i==j){
            P[i][j]=1.0;
            }
         else{
            P[i][j]=0.0;
            }    
     }
    }
     P[p][p]=c;
     P[q][q]=c;
     P[p][q]=-s;
     P[q][p]=s;
   for(int i = 0;i<n;i++){
     for(int j=0;j<n;j++) {
       temp1[i][j] = 0.0;
         for (int k=0;k<n;k++) {
           temp1[i][j]+=P[k][i]*a[k][j];
        }
      }
    }
   for(int i=0;i<n;i++){
     for(int j = 0; j < n;j++){
       temp2[i][j]=0.0;
          for(int k=0;k<n;k++){
            temp2[i][j]+=temp1[i][k]*P[k][j];
      }
     }
    }
   
   for(int i = 0;i<n;i++){
      for(int j=0;j<n;j++){
            a[i][j]=temp2[i][j];
     }
    }
   
 
}
 
int main(){
   int n;
   double tolerance =0.00001;
   int maxpass=100;
   int pass; 
   printf("Enter the order of the matrix:\n");
   scanf("%d",&n);
   double a[n][n],P[n][n];
   printf("Enter the elements of the symmetric matrix:\n");
   for(int i=0;i<n;i++){
    for(int j=0;j<n;j++){
    scanf("%lf",&a[i][j]);
    }
   } 
   for(int i=0;i<n;i++){
    for(int j=0;j<n;j++){
       if(a[i][j] != a[j][i]){
        printf("Enter a proper symmetric matrix\n");
        return 0;
       }
      }
     }
     
   for(pass=0;pass<=maxpass;pass++){
     int p=0,q=0;
      findpq(n,a,&p,&q);
      if (fabs(a[p][q]) < tolerance) {
      break;
      }
     jacobi(n,a,P,p,q);
    }

   printf("Eigen values of a are:\n");
     for(int i=0;i<n;i++){
          printf("%.5lf\n",a[i][i]);
   } 
     
     
   
   return 0;
}

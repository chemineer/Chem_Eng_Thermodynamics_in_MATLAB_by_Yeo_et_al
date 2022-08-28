%dblinterp.m : 이중안짐작
function s=dblinterp(x,y,z1,z2,w)
%x :독립변수1, 원소수2인 벡터 (예:온도)
%y :독립변수2, 원소수2인 벡터 (예:압력)
%z1 :독립변수1과 2에서의 종속변수 1의 값, 2x2 행렬 (예:엔탈피)
%z2 :독립변수1과 2에서의 종속변수 2의 값, 2x2 행렬 (예:부피)
%w : 미지의 x와 y에서의 종속변수, 원소수2인 벡터

clear out;
x1=x(1);
x2=x(2);
y1=y(1);
y2=y(2);
dx=x2-x1;
dy=y2-y1;

z11=z1(1,1);
z12=z1(1,2);
z21=z1(2,1);
z22=z1(2,2);
z=w(1);

v11=z2(1,1);
v12=z2(1,2);
v21=z2(2,1);
v22=z2(2,2);
v=w(2);

dz=z11+z22-z12-z21;
dz1=z12-z11;
dz2=z21-z11;
a1=dz/dx/dy;
b1=dz2/dx-y1*dz/dx/dy;
c1=dz1/dy-x1*dz/dx/dy;
d1=z11-x1*dz2/dx-y1*dz1/dy+x1*y1*dz/dx/dy-z;

dv=v11+v22-v12-v21;
dv1=v12-v11;
dv2=v21-v11;
a2=dv/dx/dy;
b2=dv2/dx-y1*dv/dx/dy;
c2=dv1/dy-x1*dv/dx/dy;
d2=v11-x1*dv2/dx-y1*dv1/dy+x1*y1*dv/dx/dy-v;

A=a1*b2-a2*b1;
B=a1*d2-a2*d1+c1*b2-c2*b1;
C=c1*d2-c2*d1;
s1=(-B+sqrt(B*B-4.*A*C))/2./A;
s2=(-b1*s1-d1)/(a1*s1+c1);
s=[s1 s2];
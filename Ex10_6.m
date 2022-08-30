%Ex10_6.m

clear out;

nc=2;          %성분수
x(1)=0.5;   %액상몰분율
yi(1)=0.958;   %기상몰분율(가정값)
Pc(1)=33.94;  %임계압력(bar)
Tc(1)=126.1;   %임계온도(K)
w(1)=0.04;    %이심인자

x(2)=0.5;   %액상몰분율
yi(2)=0.042;   %기상몰분율(가정값)
Pc(2)=46.04;  %임계압력(bar)
Tc(2)=190.6;   %임계온도(K)
w(2)=0.011;    %이심인자

T=100;         %system온도(K)
Pi=4.119;           %기포점 압력(bar, 가정값)

%기포점 압력 및 기상조성 계산
[bp,y]=BP_PR(nc,Pc,Tc,w,x,T,Pi,yi);

%기상 조성의 합
sy=0.0;
for i=1:nc
    sy=sy+y(i);
end

%print results
fprintf('\n기포점 압력= %10.5f MPa \n', bp/10.0);

for i=1:nc
    fprintf('\n기상몰분율(y %2.0f)= %10.5f \n', i, y(i));
end

fprintf('\n기상몰분율의 합= %10.5f \n', sy )
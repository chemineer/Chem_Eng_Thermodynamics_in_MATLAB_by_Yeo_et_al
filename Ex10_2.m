%Ex10_2.m

clear out;

nc=2;          %성분수
x(1)=0.5;   %액상몰분율
y(1)=0.958;   %기상몰분율(가정값)
Pc(1)=33.94;  %임계압력(bar)
Tc(1)=126.1;   %임계온도(K)
w(1)=0.04;    %이심인자

x(2)=0.5;   %액상몰분율
y(2)=0.042;   %기상몰분율(가정값)
Pc(2)=46.04;  %임계압력(bar)
Tc(2)=190.6;   %임계온도(K)
w(2)=0.011;    %이심인자

T=100;         %system온도(K)
P=4.119;           %system압력(bar, 가정값)


%혼합물의 fugacity계수 계산
phiL=PHILMIX_PR(nc,x,Pc,Tc,w,P,T);
phiV=PHIVMIX_PR(nc,y,Pc,Tc,w,P,T);

%K의 계산
for i=1:nc
    K(i)=phiL(i)/phiV(i);
end

%기상 몰분율의 합
sumy=0.0;
for i=1:nc
    y(i)=K(i)*x(i);
    sumy=sumy+y(i);
end

%print result
for i=1:nc
    fprintf('액상의 fugacity계수 (성분 %2.0f) : %11.5f \n',i, phiL(i));
    fprintf('기상의 fugacity계수 (성분 %2.0f) : %11.5f \n',i, phiV(i));
    fprintf('K value (성분 %2.0f) : %11.5f \n',i, K(i));
    fprintf('기상의 몰분율 (성분 %2.0f) : %11.5f \n',i, y(i));
end

fprintf('기상 몰분율의 합 : %11.5f \n',sumy);

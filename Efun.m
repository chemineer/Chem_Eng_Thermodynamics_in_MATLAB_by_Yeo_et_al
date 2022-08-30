%Efun.m

function f=Efun(T,P)
%input
% P: system 압력(bar)
% T: system 온도(K)

%output
% f : 에너지 balance 함수값

TR=298.15;
%Ka,M의 계산
Ka=742.91*exp(5525.6*(1/T-1/298.15));
M=sqrt(27)*P*Ka/4;

%eta 및 ni계산
eta=1-sqrt(1-M/(1+M));
n1=1/2-eta*1/2;
n2=3/2-eta*3/2;
n3=eta;

%Cp의 적분항 계산
s1=n1*(31.2*(T-TR)-0.0136*(T^2-TR^2)/2+2.68e-5*(T^3-TR^3)/3-1.17e-8*(T^4-TR^4)/4)
s2=n2*(27.1*(T-TR)+0.00927*(T^2-TR^2)/2-1.38e-5*(T^3-TR^3)/3+7.65e-9*(T^4-TR^4)/4)
s3=n3*(27.3*(T-TR)+0.0238*(T^2-TR^2)/2+1.71e-5*(T^3-TR^3)/3-1.19e-8*(T^4-TR^4)/4)

%에너지 함수의 계산
f=-(s1+s2+s3) + 45940*eta;
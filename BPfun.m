%BPfun.m : 기포점 압력 계산에서 sum y(i)-1 계산

function [f,y]=BPfun(nc,Pc,Tc,w,x,yi,T,P)
%input
% nc: 성분수
% Pc, Tc : 주어진 물질의 임계조건(bar, K)
% w : ascentric factor
% T : system  온도(K)
% x : 액상 성분의 mole fraction
% P : system  압력
% yi : mole fraction
%output
% f : sum y(i)-1
% y : vapor phase mole fraction

clear out;

eps=1.0e-5;

%fugacity coefficient
phiL=PHILMIX_PR(nc,x,Pc,Tc,w,P,T);
phiV=PHIVMIX_PR(nc,yi,Pc,Tc,w,P,T);

%initial y(i)
for i=1:nc
K(i)=phiL(i)/phiV(i);
y(i)=K(i)*x(i);
end

%check sum(old y)=sum(new y)
y_old=0.0;
y_new=2.0;
while abs(y_new-y_old)>eps
    y_old=y_new;
    phiV=PHIVMIX_PR(nc,y,Pc,Tc,w,P,T);
    %K(i), y(i)의 계산
    for i=1:nc
K(i)=phiL(i)/phiV(i);
y(i)=K(i)*x(i);
    end

%기상 몰분율의 합
y_new=0.0;
for i=1:nc
y_new=y_new+y(i)
end

%normalize y(i)
for i=1:nc
y(i)=y(i)/y_new
end
end

f=y_new - 1
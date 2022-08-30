%PHILMIX_PR.m: Peng-Robinson 방정식을 이용한 액상혼합물의 fugacity계수 계산

function phiL=PHILMIX_PR(nc,x,Pc,Tc,w,P,T)
%input
% nc: 성분수
% Pc, Tc : 주어진 물질의 임계조건(bar, K)
% w : ascentric factor
% P, T : system 압력(bar) 및 온도(K)
% x : 각 성분의 mole fraction
%output
% phiL : fugacity coefficient of liquid phase

clear out;

%기체상수
R=8.3143;    %J/mol-K

%방정식 parameters
for i=1:nc
    Tr=T/Tc(i);
    k=0.37464 + 1.54226*w(i) - 0.26993*w(i)^2.0;
    alpha=(1+k*(1-sqrt(Tr)))^2.0;
    ac=0.45723553*(R^2*Tc(i)^2.0)/Pc(i);
    a(i)=ac*alpha;                          % bar cm^6/gmol^2
    b(i)=0.07779607*R*Tc(i)/Pc(i);                % cm^3/gmol
end

for i=1:nc
    for j=1:nc
        ar(i,j)=sqrt(a(i)*a(j));
    end
end

am=0.0;
bm=0.0;
for i=1:nc
    bm=bm+x(i)*b(i);
    for j=1:nc
        am=am+x(i)*x(j)*ar(i,j);
    end
end

%parameters
A=am*P/(R*T)^2.0;
B=bm*P/(R*T);
for i=1:nc
    Bk(i)=b(i)*B/bm;
    for j=1:nc
        Ak(i,j)=ar(i,j)*A/am;
    end
end

for i=1:nc
    A_sum(i)=0.0;
    for j=1:nc
        A_sum(i)=A_sum(i)+x(j)*Ak(i,j);
    end
end

%Peng-Robinson 3차 방정식의 계수

a2=-(1-B);
a1=(A-3*B^2-2*B);
a0=-(A*B-B^2-B^3);

%3차 방정식의 근
EOS=[1 a2 a1 a0];
Zt=roots(EOS);

for i=1:3
if isreal(Zt(i)) == 1   %실근만을 선택
    Zr(i)=Zt(i);
    nr=i;
end
end

if length(Zr)==3        % 3개의 실근인 경우
    Z=min(Zr);       % 가장 작은 실근은 액체근

else
    Z=Zr(nr);
end

%fugacity계수의 계산
c1=log(Z-B);
c2=(Z-1)/B;
c3=A/(B*sqrt(8));
c4=log((Z+(1+sqrt(2))*B)/(Z+(1-sqrt(2))*B));

for i=1:nc
phiL(i)=exp(-c1+Bk(i)*c2-c3*c4*(2*A_sum(i)/A-Bk(i)/B));
end

%DEPFUN_PR.m : Peng-Robinson 방정식을 이용한 편차함수의 계산
function [Z, V, DH, DS, DU, DG, DA, DS_TV, DA_TV]=DEPFUN_PR(P,T,Pc,Tc,w)
%input
% P: system 압력(bar)
% T: system 온도(K)
% Pc, Tc : 주어진 물질의 임계조건(bar, K)
% w : ascentric factor
%output
% Z : PR 3차방정식의 실근
% DH, DS,... : values of departure functions

clear out;

%기체상수
R=8.3143;    %J/mol-K (편차함수 계산에 이용)
Rv=83.143;   %bar-cm^3/mol-K(부피 계산에 이용)

Tr=T/Tc;    %reduced temperature
Pr=P/Pc;    %reduced pressure

%방정식 parameters
k=0.37464 + 1.54226*w - 0.26993*w^2;
alpha=(1+k*(1-sqrt(Tr)))^2;
ac=0.45723553*(R^2*Tc^2)/Pc;
a=ac*alpha;                          % bar cm^6/gmol^2
b=0.07779607*R*Tc/Pc;                % cm^3/gmol

A=(a*P) / (R^2 * T^2);
B=(b*P) / (R*T);

%Peng-Robinson 3차 방정식의 계수

a2=-(1-B)
a1=(A-3*B^2-2*B);
a0=-(A*B-B^2-B^3);

%3차 방정식의 근
EOS=[1 a2 a1 a0];
Zt=roots(EOS);

for i=1:3
if isreal(Zt(i)) == 1   %실근만을 선택
    Zr(i)=Zt(i);
end
end

if length(Zr)==3        % 3개의 실근인 경우
    Z(1)=min(Zr);       % 가장 작은 실근은 액체근
    Z(2)=max(Zr);       % 가장 큰 실근은 기체근
else
    Z(1)=Zr(1);
end

%부피의 계산
V=Z*Rv*T/P;

%편차함수의 계산
c1=log((Z+(1+sqrt(2))*B) ./ (Z+(1-sqrt(2))*B));
c2=A/(B*sqrt(8));
c3=k*sqrt(Tr/alpha);
c4=log((Z-B) ./ Z);
DH=R*T*(Z-1-c2*(1+c3)*c1);
DU=R*T*(-c2 .* (1+c3) .* c1);
DS=R*(log(Z-B)-c2*c3*c1);
DG=R*T*(Z-1-log(Z-B)-c2*c1);
DA=R*T*(-log(Z-B)-c2*c1)
DA_TV=R*T*(-c4-c2*c1)                   %DA at fixed T and V
DS_TV=R*(c4-c2*c3*c1)                   %DS at fixed T and V
%Z_PR.m : Peng-Robinson 3차방정식의 근
function Z=Z_PR(Tc,Pc,w,T,P)
%input
% Pc, Tc : 주어진 물질의 임계조건(bar, K)
% w : ascentric factor
% P, T : system 압력(bar) 및 온도(K)
%output

clear out;

Pc=33.94;       %임계압력(bar)
Tc=126.1;       %임계온도(K)
w=0.04;         %이심인자
T=100;          %system온도(K)
P=4.119;        %system압력(bar)

R=8.3143;    %J/mol-K
Tr=T/Tc;     %reduced temperature
Pr=P/Pc;     %reduced pressure

%parameters
k=0.37464 + 1.54226*w - 0.26993*w^2;
alpha=(1+k*(1-Tr^0.5))^2;
ac=0.45723553*(R^2*Tc^2)/Pc;
a=ac*alpha;                          % bar cm^6/gmol^2
b=0.07779607*R*Tc/Pc;                % cm^3/gmol

A=(a*P) / (R^2 * T^2);
B=(b*P) / (R*T);

%3차 방정식의 계수
a3=1;
a2=-(1-B)
a1=(A-3*B^2-2*B);
a0=-(A*B-B^2-B^3);

%3차 방정식의 풀이
p=[a3 a2 a1 a0];
Z=roots(p);

fprintf('\nPeng-Robinson 3차방정식의 근 : %10.5f',Z);
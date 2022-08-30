%DEPFUN_VR.m : Virial 상태방정식을 이용한 편차함수 del_H, del_S의 계산

function [DH,DS] = DEPFUN_VR(P,T,Pc,Tc,w)
%input
% P: system 압력(bar)
% T: system 온도(K)
% Pc, Tc : 주어진 물질의 임계조건(bar, K)
% w : ascentric factor
%output
% DH, DS : values of departure functions

clear out;

%기체상수
R=8.3143;    %J/mol-K (편차함수 계산에 이용)

Tr=T/Tc;    %reduced temperature
Pr=P/Pc;    %reduced pressure

c1=1.0972/Tr^2.6 - 0.083 / Tr;
c2=0.8944 / Tr^5.2 - 0.139 / Tr;
c3=0.675 / Tr^2.6;
c4=0.722 / Tr^5.2;

DH=-R*T*Pr*(c1+w*c2);
DS=-R*Pr*(c3+w*c4);
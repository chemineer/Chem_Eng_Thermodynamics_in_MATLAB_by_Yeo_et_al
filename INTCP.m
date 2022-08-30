%INTCP.m : Cp 및 Cp/T의 적분

function [dh, ds] = INTCP(T1,T2,P1,P2,A,B,C,D)
%input
% P1,P2: system 압력(bar)
% T1,T2: system 온도(K)
% A,B,C,D : Cp data
%output
% dh : Cp 의 적분 (T1-->T2)
% ds : Cp/T의 적분 (T1 -->T2)

clear out;
%기체상수
R=8.3143;    %J/mol-K

%온도차
dT=T2-T1;
sT=T2^2-T1^2;
cT=T2^3-T1^3;
qT=T2^4-T1^4;

dh=A*dT+B*sT/2.+C*cT/3.+D*qT/4.;
ds=A*log(T2/T1)+B*dT+C*sT/2.+D*cT/3.-R*log(P2/P1);
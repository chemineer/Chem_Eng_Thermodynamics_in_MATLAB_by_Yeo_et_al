% DELHS_VR.m : 상태1->상태2에서 엔탈피 및 엔트로피 변화 계산

function [DH, DS] = DELHS_VR(T1,T2,P1,P2,Pc,Tc,w,A,B,C,D)
%input
% P1,P2: 초기 및 최종 압력(bar)
% T1,T2: 초기 및 최종 온도(K)
% Pc, Tc : 주어진 물질의 임계조건(bar, K)
% w : ascentric factor
% A,B,C,D : Cp data
%output
% DH, DS : values of departure functions

clear out;

%초기 및 최종상태에서의 편차함수의 계산
[DH1 DS1]=DEPFUN_VR(P1,T1,Pc,Tc,w);
[DH2 DS2]=DEPFUN_VR(P2,T2,Pc,Tc,w);

%이상기체의 상태변화(1-->2)
[delH_ig, delS_ig]=INTCP(T1,T2,P1,P2,A,B,C,D)

%1-->2에서 엔탈피 및 엔트로피의 변화

    DH=DH2+delH_ig-DH1;
    DS=DS2+delS_ig-DS1;
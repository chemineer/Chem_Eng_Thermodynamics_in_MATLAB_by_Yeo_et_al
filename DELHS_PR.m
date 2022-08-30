% DELHS_PR.m : 상태1->상태2에서 엔탈피 및 엔트로피 변화 계산
function [Z1, Z2, DH, DS]=DELHS_PR(T1,T2,P1,P2,Pc,Tc,w,A,B,C,D);
%input
% P1,P2: 초기 및 최종 압력(bar)
% T1,T2: 초기 및 최종 온도(K)
% Pc, Tc : 주어진 물질의 임계조건(bar, K)
% w : ascentric factor
% A,B,C,D : Cp data
%output
% DH, DS : values of departure functions
% Z1, Z2 : number of real roots at state 1 and 2

clear out;

%초기 및 최종상태에서의 편차함수 계산
[Z1, V1, DH1, DS1, DU1, DG1, DA1, Sc1, Ac1]=DEPFUN_PR(P1,T1,Pc,Tc,w)
[Z2, V2, DH2, DS2, DU2, DG2, DA2, Sc2, Ac2]=DEPFUN_PR(P2,T2,Pc,Tc,w)

%이상기체의 상태변화(1->2)
[delH_ig, delS_ig]=INTCP(T1,T2,P1,P2,A,B,C,D)

%1-->2에서 엔탈피 및 엔트로피의 변화
if (length(Z1)==1) & (length(Z2)==1)
    DH=DH2+delH_ig-DH1;
    DS=DS2+delS_ig-DS1;
elseif (length(Z1)==1) & (length(Z2)~=1)
    for i=1:length(Z2)
        DH(i)=DH2(i)+delH_ig-DH1;
        DS(i)=DS2(i)+delS_ig-DS1;
    end
elseif (length(Z1)~=1) & (length(Z2)==1)
    for i=1:length(Z1)
        DH(i)=DH2+delH_ig-DH1(i);
        DS(i)=DS2+delS_ig-DS1(i);
    end
else
    for i=1:length(Z2)
        DH(i)=DH2(i)+delH_ig-DH1(i);
        DS(i)=DS2(i)+delS_ig-DS1(i);
    end    
end
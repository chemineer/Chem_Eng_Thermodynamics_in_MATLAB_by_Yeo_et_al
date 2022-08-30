%BP_PR.m: Peng-Robinson 방정식을 이용한 기포점 압력의 계산

function [bp,y]=BP_PR(nc,Pc,Tc,w,x,T,Pi,yi)
%input
% nc: 성분수
% Pc, Tc : 주어진 물질의 임계조건(bar, K)
% w : ascentric factor
% T : system  온도(K)
% x : 액상 성분의 mole fraction
% Pi : bp의 초기 가정값(bar)
% yi : y(i)의 초기 가정값
%output
% bp : bubble point pressure(bar)
% y : vapor phase mole fraction

clear out;

eps=1.0e-5;
delP=0.5;

P1=Pi;
[f1,y1]=BPfun(nc,Pc,Tc,w,x,yi,T,P1);

while f1<0
    P1=P1-delP;
    [f1,y1]=BPfun(nc,Pc,Tc,w,x,yi,T,P1);
end

P2=Pi+delP;
[f2,y2]=BPfun(nc,Pc,Tc,w,x,yi,T,P2);
while f2>0
    P2=P2+delP;
    [f2,y2]=BPfun(nc,Pc,Tc,w,x,yi,T,P2);
end

%half-interval 방법을 이용한 반복계산
while abs(P2-P1) >eps
    [f1,y1]=BPfun(nc,Pc,Tc,w,x,yi,T,P1);
    [f2,y2]=BPfun(nc,Pc,Tc,w,x,yi,T,P2);
    bp=(P1+P2)/2.;
    y=(y1+y2)/2.;
    [f,y]=BPfun(nc,Pc,Tc,w,x,y,T,bp);
    if f1*f<0
        P2=bp;
    else
        P1=bp;
    end
end
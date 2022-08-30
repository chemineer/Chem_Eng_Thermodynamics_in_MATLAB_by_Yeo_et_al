%VMIX_VR.m : virial방정식을 이용한 혼합물의 부피계산
function V=VMIX_VR(nc,Tc,Pc,Vc,Zc,w,x,T,P)
%input
% nc: 성분수
% Pc, Tc : 주어진 물질의 임계조건(bar, K)
% w : ascentric factor
% P, T : system 압력(bar) 및 온도(K)
% x : 각 성분의 mole fraction
%output
% V : 혼합물의 부피 (cm^3/mol)

R=83.143;   %bar-cm^3/mol-K(부피 계산에 이용)

%혼합물의 임계 properties계산
for i=1:nc
    for j=1:nc
        Tcm(i,j)=sqrt(Tc(i)*Tc(j));
        Vcm(i,j)=((Vc(i)^(1/3)+Vc(j)^(1/3))/2)^3;
        Zcm(i,j)=(Zc(i)+Zc(j))/2
        wm(i,j)=(w(i)+w(j))/2
        Pcm(i,j)=Zcm(i,j)*R*T/Vcm(i,j)
        Trm(i,j)=T/Tcm(i,j)
    end
end

%혼합물의 virial parameters
for i=1:nc
for j=1:nc
B0(i,j)=0.083-0.422/Trm(i,j)^1.6;
B1(i,j)=0.139-0.172/Trm(i,j)^4.2;
Bm(i,j)=(B0(i,j)+wm(i,j)*B1(i,j))*R*Tcm(i,j)/Pcm(i,j);
end
end

B=0;
for i=1:nc
for j=1:nc
B=B+x(i)*x(j)*Bm(i,j);
end
end

%혼합물의 부피계산
Z=1+B*P/R/T;
V=Z*R*T/P;
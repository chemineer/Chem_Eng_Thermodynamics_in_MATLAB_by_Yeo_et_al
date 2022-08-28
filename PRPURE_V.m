%PRPURE_V.m : Peng-Robinson 방정식을 이용한 순수물질의 몰 부피 계산
function V=PRPURE_V(dat, cond)
%dat   : 순수물질 data(Tc, Pc, w)
%cond  : 주어진 조건(온도:K, 압력:MPa)
%v     : results (V(1)~V(3):Z, V(4):증기 몰 부피, V(5):액상 몰 부피

clear out;

%순수물질의 물성데이터
Tc=dat(1);
Pc=dat(2);
w=dat(3);
%주어진 조건
T=cond(1);
P=cond(2);

R=8.314;    %이상기체 상수(cm^3-Mpa/mol-K)
Tr=T/Tc;    %reduced temperature
Pr=P/Pc;    %reduced pressure

%parameters
k=0.37464 + 1.54226*w - 0.26993*w^2;
alpha=(1+k*(1-Tr^0.5))^2;
ac=0.45723553*(R^2*Tc^2)/Pc;
a=ac*alpha;
b=0.07779607*R*Tc/Pc;

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

V(1)=Z(1);
V(2)=Z(2);
V(3)=Z(3);

%molar volume의 계산
vapz=0.0;
liqz=2.0;

for i=1:3
realz=real(Z(i));
if abs(imag(Z(i))) < 1.0e-9
if realz > vapz
vapz=realz;
elseif realz < vapz
liqz=realz;
end
end
end

if vapz>0.0
volV=vapz * R * T/P;     % vapor molar volume 계산
V(4)=volV;
else V(4)=0.;
end

if liqz<1.0
volL=liqz * R * T/P      % liquid molar volume 계산
V(5)=volL
else V(5)=0.;
end
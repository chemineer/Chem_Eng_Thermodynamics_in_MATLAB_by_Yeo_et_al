%Ex7_6.m

clear out;
Tc=369.8;   %임계온도(K)
Pc=4.249;   %임계압력(MPa)
w=0.152;    %이심인자

A= -4.224;              %Cp data(A)
B= 0.3063;              %Cp data(B)
C= -1.586e-4;              %Cp data(C)
D= 3.215e-8;              %Cp data(D)

T1=105;       %초기온도(deg C)
P1=5;            %초기압력(bar)
T2=190;       %최종온도(deg C)
P2=25;           %최종압력(bar)
T1=T1+273.15;   %온도(deg C-->K)
T2=T2+273.15;   %온도(deg C-->K)
Pc=Pc*10        %MPa-->bar

% 1->2에서 엔탈피 및 엔트로피 변화 계산
[Z1, Z2, DH, DS]=DELHS_PR(T1,T2,P1,P2,Pc,Tc,w,A,B,C,D);

%print results
fprintf('\n엔탈피 변화(1-->2) : %10.5f J/mol',DH);
fprintf('\n엔트로피 변화(1-->2) : %10.5f J/mol-K',DS);
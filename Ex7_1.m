%Ex7_1.m
clear out;

Tc=369.8;   %임계온도(K)
Pc=42.49;   %임계압력(bar)
w=0.152;    %이심인자

A= -4.224;              %Cp data(A)
B= 0.3063;              %Cp data(B)
C= -1.586e-4;              %Cp data(C)
D= 3.215e-8;              %Cp data(D)

T1=378.15       %초기온도(K)
P1=5            %초기압력(bar)
T2=463.15       %최종온도(K)
P2=25           %최종압력(bar)

% 1->2에서 엔탈피 및 엔트로피 변화 계산
[Z1, Z2, DH, DS]=DELHS_PR(T1,T2,P1,P2,Pc,Tc,w,A,B,C,D);

%print results
fprintf('\n엔탈피 및 엔트로피 변화');
if length(Z2) == 1  %single phase
    fprintf('\n Z2=%10.7f \n DH=%10.4f J/mol\n DS=%10.4f J/mol-K', Z2,DH,DS);
else
    for i=1:length(Z2)
        fprintf('\n Z2(%2.0f)=%10.7f \n DH=%10.4f J/mol\n DS=%10.4f J/mol-K', i,Z2(i),DH(i),DS(i));
    end
end
%Ex7_7.m

clear out;
Tc=190.6;   %임계온도(K)
Pc=45.99;   %임계압력(bar)
w=0.012;    %이심인자

A= 19.25;              %Cp data(A)
B= 0.0523;              %Cp data(B)
C= 1.197e-5;              %Cp data(C)
D= -1.132e-8;              %Cp data(D)

T0=300;       %기준온도(K)
P0=60;            %기준압력(bar)

T6=111;       %온도(K)
P6=1.013;            %압력(bar)
T8=295;       %온도(K)
P8=1.013;            %압력(bar)

% 엔탈피 및 엔트로피 계산
[Z0, Z6, H6, S6]=DELHS_PR(T0,T6,P0,P6,Pc,Tc,w,A,B,C,D);
[Z0, Z8, H8, S8]=DELHS_PR(T0,T8,P0,P8,Pc,Tc,w,A,B,C,D);

%print results
if length(Z6) == 1  %single phase
    fprintf('\n Z=%10.7f \n H6=%10.4f J/mol\n S6=%10.4f J/mol-K', Z6,H6,S6);
else
    for i=1:length(Z6)
        fprintf('\n Z=%10.7f \n H8=%10.4f J/mol\n S8=%10.4f J/mol-K', Z6(i),H6(i),S6(i));
    end
end

if length(Z8) == 1  %single phase
    fprintf('\n Z=%10.7f \n H8=%10.4f J/mol\n S8=%10.4f J/mol-K', Z8,H8,S8);
else
    for i=1:length(Z8)
        fprintf('\n Z=%10.7f \n H8=%10.4f J/mol\n S8=%10.4f J/mol-K\n', Z8(i),H8(i),S8(i));
    end
end

%액화된 분율의 계산
frL=-H8/(H6(1)-H8);
fprintf('\n액화된 분율 %10.5f \n',frL);
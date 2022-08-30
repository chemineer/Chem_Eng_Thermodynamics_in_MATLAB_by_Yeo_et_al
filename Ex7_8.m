%Ex7_8.m

clear out;
R=8.3143;    %J/mol-K
Tc=369.8;   %임계온도(K)
Pc=42.49;   %임계압력(bar)
w=0.152;    %이심인자

A= -4.224;              %Cp data(A)
B= 0.3063;              %Cp data(B)
C= -1.586e-4;              %Cp data(C)
D= 3.215e-8;              %Cp data(D)

T0=298;       %기준온도(K)
P0=0.1;            %기준압력(MPa)

T1=350;       %초기온도(K)
P1=1;            %초기압력(MPa)
P2=1;            %최종압력(MPa)

P0=P0*10;            %MPa-->bar
P1=P1*10;            %MPa-->bar
P2=P2*10;            %MPa-->bar

%초기상태
[Z0, Z1, U1, H1, S1]=DELE_PR(T0,T1,P0,P1,Pc,Tc,w,A,B,C,D);

if length(Z1) == 1  %single phase
    fprintf('\n Z1=%10.7f ', Z1);
    fprintf('\n U1=%10.4f, H1=%10.4f, S1=%10.4f ', U1, H1, S1);
else
    for i=1:length(Z1)
        fprintf('\n Z1(%2.0f)=%10.7f \n U1=%10.4f J/mol\n H1=%10.4f J/mol\n S1=%10.4f J/mol-K\n', i, Z1(i),U1(i),H1(i),S1(i));
    end
end

%initial points
Uf=H1;
eps=1.0e-5;

x1=355.0;
[Z0, Z1, U, H1, S1]=DELE_PR(T0,x1,P0,P1,Pc,Tc,w,A,B,C,D);
while U-Uf>0
    x1=x1-5.;
    [Z0, Z1, U, H1, S1]=DELE_PR(T0,x1,P0,P1,Pc,Tc,w,A,B,C,D);
end

x2=400.0;
[Z0, Z2, U, H2, S2]=DELE_PR(T0,x2,P0,P1,Pc,Tc,w,A,B,C,D);
while U-Uf<0
    x2=x2-5.;
    [Z0, Z2, U, H2, S2]=DELE_PR(T0,x2,P0,P1,Pc,Tc,w,A,B,C,D);
end

%half interval 방법을 이용한 반복계산
while abs(x2-x1)>eps
    [Z0, Z1, U1, H1, S1]=DELE_PR(T0,x1,P0,P1,Pc,Tc,w,A,B,C,D);
    [Z0, Z2, U2, H2, S2]=DELE_PR(T0,x2,P0,P1,Pc,Tc,w,A,B,C,D);
    x=(x1+x2)/2.;
    [Z0, Z2, U, H2, S2]=DELE_PR(T0,x,P0,P1,Pc,Tc,w,A,B,C,D);
    f1=U1-Uf;
    f=U-Uf;
    if f1*f<0
        x2=x;
    else
        x1=x;
    end
end

%최종상태
T2=x;
fprintf('\n최종온도=%10.5f (K)\n',T2)
[Z0, Z2, U2, H2, S2]=DELE_PR(T0,T2,P0,P2,Pc,Tc,w,A,B,C,D);

if length(Z2) == 1  %single phase
    fprintf('\n Z2=%10.7f ', Z2);
    fprintf('\n U2=%10.4f, H2=%10.4f, S2=%10.4f ', U2, H2, S2);
else
    for i=1:length(Z2)
        fprintf('\n Z2(%2.0f)=%10.7f \n U2=%10.4f J/mol\n H2=%10.4f J/mol\n S2=%10.4f J/mol-K\n\n', i, Z2(i),U2(i),H2(i),S2(i));
    end
end

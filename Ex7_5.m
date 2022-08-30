%Ex7_5.m

clear out;
Tc=190.6;   %임계온도(K)
Pc=45.99;   %임계압력(bar)
w=0.012;    %이심인자

A= 19.25;              %Cp data(A)
B= 0.0523;              %Cp data(B)
C= 1.197e-5;              %Cp data(C)
D= -1.132e-8;              %Cp data(D)

T1=40;       %초기온도(deg C)
P1=20;            %초기압력(bar)
P2=1;           %최종압력(bar)
T1=T1+273.15;   %온도(deg C-->K)

eps=1.0e-5;
x1=308.15;

[f1 s1]=DELHS_VR(T1,x1,P1,P2,Pc,Tc,w,A,B,C,D);
while f1<0
    x1=x1+5.;
    [f1 s1]=DELHS_VR(T1,x1,P1,P2,Pc,Tc,w,A,B,C,D);
end

x2=303.15;
[f2 s2]=DELHS_VR(T1,x2,P1,P2,Pc,Tc,w,A,B,C,D);
while f2>0
    x2=x2-5.;
    [f2 s2]=DELHS_VR(T1,x2,P1,P2,Pc,Tc,w,A,B,C,D);
end

%half-interval 방법을 이용한 반복계산
while abs(x2-x1)>eps
    [f1 s1]=DELHS_VR(T1,x1,P1,P2,Pc,Tc,w,A,B,C,D);
    [f2 s2]=DELHS_VR(T1,x2,P1,P2,Pc,Tc,w,A,B,C,D);
    x=(x1+x2)/2.;
    [f s]=DELHS_VR(T1,x,P1,P2,Pc,Tc,w,A,B,C,D);
    if f1*f<0
        x2=x;
    else
        x1=x;
    end
end
fprintf('\n 최종온도= %10.5f (deg C) \n', x-273.15);
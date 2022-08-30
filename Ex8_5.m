%Ex8_5.m

clear out;

Tc=190.6;   %임계온도(K)
Pc=46.04;   %임계압력(bar)
w=0.011;    %이심인자

P=1;            %압력(bar)

%initial points : PR방정식의 근이 두 실근인 온도를 search
eps=1.0e-5;

x1=150.0;
[p1, f1]=PHI_PR(P,x1,Pc,Tc,w);
while length(p1) ~=2
    x1=x1+10.;
    [p1, f1]=PHI_PR(P,x1,Pc,Tc,w);
end

x2=50.0;
[p2, f2]=PHI_PR(P,x2,Pc,Tc,w);
while length(p2) ~=2
    x2=x2+10.;
    [p2, f2]=PHI_PR(P,x2,Pc,Tc,w);
end

%half interval방법을 이용한 반복계산
while abs(x2-x1)>eps
    [p1, f1]=PHI_PR(P,x1,Pc,Tc,w);
    [p2, f2]=PHI_PR(P,x2,Pc,Tc,w);
    T=(x1+x2)/2;
    [pT, f]=PHI_PR(P,T,Pc,Tc,w);
    if (p1(1)-p1(2))*(pT(1)-pT(2))>0
        x1=T;
    else
        x2=T;
    end
end

%print result
fprintf('\n온도=%10.5f K',T);
fprintf('\nFugacity계수=%10.5f ',pT(1));
fprintf('\nFugacity(액상)=%10.5f MPa',f(1)/10.);
fprintf('\nFugacity(기상)=%10.5f MPa',f(2)/10.);
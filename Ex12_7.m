%Ex12_7.m

clear out;
eps=1.0e-5;
delT=10;

%input data
P=100;           %압력(bar)
Ti=600;          %초기가정온도(K)

%온도구간 (T1, T2)의 초기화
T1=Ti;
f1=Efun(T,P);
while f1<0
    T1=T1-delT;
    f1=Efun(T1,P);
end

T2=Ti+delT;
f2=Efun(T2,P);
while f2>0
    T2=T2+delT;
    f2=Efun(T2,P);
end

%half interval 방법을 이용한 반복계산
while abs(T2-T1)>eps
    f1=Efun(T1,P);
    f2=Efun(T2,P);
    T=(T1+T2)/2;
    f=Efun(T,P);
    if f1*f<0
        T2=T;
    else
        T1=T;
    end
end

%print results
fprintf('\n온도=%8.3f K \n', T);
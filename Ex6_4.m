%Ex6_4.m
clear out;

MW=44;           %분자량
data(1)=304.2;   %임계온도(K)
data(2)=73.82;   %임계압력(bar)
data(3)=0.228;   %이심인자

data(2)=data(2)/10.;  %임계압력(bar-->MPa)

cond(1)=310;      %온도(K)

%(a)
cond(2)=8;        %압력(bar)
cond(2)=cond(2)/10;        %압력(bar-->MPa)

%specific volume(cm^3/gr) 계산
results=PRPURE_V(data,cond);
Z=[results(1) results(2) results(3)];
results(4)=results(4)/MW;
results(5)=results(5)/MW;

%print results
fprintf('\n Z values :');Z

fprintf('비 부피(specific volume) : \n');
fprintf('\n   Vapor = %10.5f cm^3/gr\n', results(4))
fprintf('   Liquid = %10.5f cm^3/gr\n', results(5))

%(b)
cond(2)=75;        %압력(bar)
cond(2)=cond(2)/10;        %압력(bar-->MPa)

%specific volume(cm^3/gr) 계산
results=PRPURE_V(data,cond);
Z=[results(1) results(2) results(3)];
results(4)=results(4)/MW;
results(5)=results(5)/MW;

%print results
fprintf('\n Z values :');Z

fprintf('비 부피(specific volume) : \n');
fprintf('\n   Vapor = %10.5f cm^3/gr\n', results(4))
fprintf('   Liquid = %10.5f cm^3/gr\n', results(5))
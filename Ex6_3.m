%Ex6_3.m
data(1)=150.86  %임계온도(K)
data(2)=4.898   %임계압력(MPa)
data(3)=-0.004  %이심인자

cond(1)=105.6   %온도(K)
cond(2)=0.498   %압력(MPa)

%몰부피 계산
Vol=PRPURE_V(data, cond);
Z=[Vol(1) Vol(2) Vol(3)];

%print results
fprintf('\n Z values :');Z

fprintf('몰 부피(Molar volume) : \n');
fprintf('\n   Vapor = %10.5f cm^3/mol\n', Vol(4))
fprintf('   Liquid = %10.5f cm^3/mol\n', Vol(5))
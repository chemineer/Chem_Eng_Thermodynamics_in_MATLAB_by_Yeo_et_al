%Ex1_5.m
%x1=input('T1(deg.C):');
%y1=input('P1(MPa):');
x1=200;
x2=250;
y1=1;
y2=1.2;
x=[x1 x2];
y=[y1 y2];

%z11=input('T1,P1에서의 내부에너지(KJ/kg):');
z11=2622.2;
z12=2612.9;
z21=2710.4;
z22=2704.7;
z1=[z11 z12; z21 z22];

%z=input('최종상태 (T,P)에서의 내부에너지(KJ/kg):');
z=2650;

%v11=input('T1,P1에서의 부피(m3/kg):');
v11=0.2060;
v12=0.1693;
v21=0.2327;
v22=0.1924;
z2=[v11 v12; v21 v22];

%v=input('최종상태 (T,P)에서의 부피(m3/kg):');
v=0.185;
w=[z v];

s = dblinterp(x, y, z1, z2, w); %s: [T P]
fprintf('\n온도=%10.5f deg.C',s(1));
fprintf('\n압력=%10.5f MPa\n',s(2));

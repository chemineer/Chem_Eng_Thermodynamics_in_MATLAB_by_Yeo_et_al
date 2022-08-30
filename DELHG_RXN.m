%DELHG_RXN.m : 반응계에서 del H0, del G0 계산

function [delH0, delG0]=DELHG_RXN(nc,m,a,b,c,d,TR,HR,GR,T)
%input
% nc: 성분수
% m : stoichometric number
% a,b,c,d : Cp data
% TR : reference temp.
% HR,GR : TR에서의 delH 및 delG
% T : system 온도(K)
%output
% delH0 : 주어진 온도에서 반응의 delH0
% delG0 : 주어진 온도에서 반응의 delG0

clear out;

%기체상수
R=8.3143;    %J/mol-K

%Cp 계수
da=0;
db=0;
dc=0;
dd=0;
dH=0;
dG=0;

for i=1:nc
    da=da+m(i)*a(i);
    db=db+m(i)*b(i);
    dc=dc+m(i)*c(i);
    dd=dd+m(i)*d(i);
    dH=dH+m(i)*HR(i);
    dG=dG+m(i)*GR(i);
end

%상수 J의 계산
J=dH-da*TR-db*TR*TR/2-dc*(TR^3)/3-dd*(TR^4)/4;

%상수 W의 계산
W=(dG-J+da*TR*log(TR)+db*TR*TR/2+dc*TR^3/6+dd*(TR^4)/12)/(R*TR);

%delH0, delG0 계산
delH0=J+da*T+db*T*T/2+dc*(T^3)/3+dd*(T^4)/4;
delG0=J-da*T*log(T)-db*T*T/2-dc*(T^3)/6-dd*(T^4)/12+W*T*R;


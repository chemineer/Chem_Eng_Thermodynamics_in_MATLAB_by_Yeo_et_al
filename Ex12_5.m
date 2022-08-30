%Ex12_5.m

clear out;

R=8.3143;    %J/mol-K

nc=3;          %성분수
m(1)=-1;        %stoichiometric number
a(1)=3.806;     %Cp_A
b(1)=1.566e-1;  %Cp_B
c(1)=-8.348e-5;  %Cp_C
d(1)=1.755e-8;  %Cp_D
HR(1)=52.51;    %기준온도에서의 del H0(KJ/mol)
GR(1)=68.43;    %기준온도에서의 del G0(KJ/mol)

m(2)=-1;        %stoichiometric number
a(2)=32.24;     %Cp_A
b(2)=1.924e-3;  %Cp_B
c(2)=1.055e-5;  %Cp_C
d(2)=-3.596e-9;  %Cp_D
HR(2)=-241.835;    %기준온도에서의 del H0(KJ/mol)
GR(2)=-228.614;    %기준온도에서의 del G0(KJ/mol)

m(3)=1;        %stoichiometric number
a(3)=9.014;     %Cp_A
b(3)=2.141e-1;  %Cp_B
c(3)=-8.39e-5;  %Cp_C
d(3)=1.373e-9;  %Cp_D
HR(3)=-234.95;    %기준온도에서의 del H0(KJ/mol)
GR(3)=-167.73;    %기준온도에서의 del G0(KJ/mol)

TR=298.15;      %기준온도(K)
T=145;          %반응온도(deg C)

for i=1:nc              % kJ/mol --> J/mol
    HR(i)=HR(i)*1000;
    GR(i)=GR(i)*1000;
end

T=T+273.15;

%delH0 and delG0 at T
[delH0, delG0]=DELHG_RXN(nc,m,a,b,c,d,TR,HR,GR,T);

%평형상수 K
K=exp(-delG0/R/T);

%print results
fprintf('del H0 at %8.3f deg C = %10.5f J/mol \n',T-273.15, delH0);
fprintf('del G0 at %8.3f deg C = %10.5f J/mol \n',T-273.15, delG0);
fprintf('평형상수 K at %8.3f deg C = %10.5f \n',T-273.15, K);

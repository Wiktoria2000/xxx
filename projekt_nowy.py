# -*- coding: utf-8 -*-
"""
Created on Tue May 25 17:13:17 2021

@author: Wiktoria
"""
from math import atan, tan, cos, sin, sqrt, pi
import pandas as pd
import numpy as np 

dane = pd.read_excel('DANE.xlsx')
#dane = pd.read_excel('C:/Users/Wiktoria/Desktop/SEMESTR 4/INFOMATYKA 2/ĆWICZENIA/PROJEKT/DANE.xlsx')


dane.index = dane['MIASTO'] #zamiana ineskow 1,2,3 na nazwy miast 
a = input('Miejsce wylotu ')
b = input('Miejsce lądowania  ')

#przyporządkowanie do konkretnej komórki 
h_fi = dane.loc[a,'H_(FI)']
m_fi = dane.loc[a,'M_(FI)']
s_fi = dane.loc[a,'S_(FI)']
h_l = dane.loc[a,'H_(L)']
m_l = dane.loc[a,'M_(L)']
s_l = dane.loc[a,'S_(L)']

h_fi2 = dane.loc[b,'H_(FI)']
m_fi2 = dane.loc[b,'M_(FI)']
s_fi2 = dane.loc[b,'S_(FI)']
h_l2 = dane.loc[b,'H_(L)']
m_l2 = dane.loc[b,'M_(L)']
s_l2 = dane.loc[b,'S_(L)']

lB = np.deg2rad(h_l2 + m_l2/60 + s_l2/3600)
lA = np.deg2rad(h_l + m_l/60 + s_l/3600)
fA = np.deg2rad(h_fi + m_fi/60 + s_fi/3600)
fB = np.deg2rad(h_fi2 + m_fi2/60 + s_fi2/3600)

#VINCENT (ODLEGLOSC MIEDZY LOTNISKAMI)
a = 6378137
e2 = 0.0066943800

b=a*(1-e2)**0.5;
f=1-(b/a);
L=lB-lA;
U1 = atan((1-f)*tan(fA));
U2 = atan((1-f)*tan(fB));
# trzeba dopisac poczatek czyli przeniesienie na sfere do szerokosci zredukowanych
i=0;
La=L;
while 1:
    i=i+1;
    sd=sqrt(((cos(U2))*(sin(La)))**2+((cos(U1))*(sin(U2))-(sin(U1))*(cos(U2))*(cos(La)))**2);
    cd=(sin(U1))*(sin(U2))+(cos(U1))*(cos(U2))*(cos(La));
    d=atan(sd/cd);
    sa=(cos(U1))*(cos(U2))*(sin(La))/sd;
    c2dm=cd-2*(sin(U1))*(sin(U2))/(1-sa**2);
    
    C=(f/16)*(1-sa**2)*(4+f*(4-3*(1-sa**2)));
    Ls=La;
    La=L+(1-C)*f*sa*(d+C*sd*(c2dm+C*cd*(-1+2*c2dm**2)));
    
    if abs(La-Ls)<(0.000001/206265):
        break
    


u2=(((a**2)-(b**2))/(b**2))*(1-(sa)**2);
A=1+((u2)/16384)*(4096+(u2)*(-768+(u2)*(320-175*(u2))));
B=((u2)/1024)*(256+(u2)*(-128+(u2)*(74-47*(u2))));
dd=B*(sd)*((c2dm)+(0.25)*B*((cd)*(-1+2*(c2dm)**2)-(1/6)*B*(c2dm)*(-3+4*(sd)**2)*(-3+4*(c2dm)**2)));

s=b*A*(d-dd);
AAB=atan(((cos(U2))*(sin(Ls)))/((cos(U1))*(sin(U2))-(sin(U1))*(cos(U2))*(cos(Ls))));
ABA=atan(((cos(U1))*(sin(Ls)))/(((-sin(U1)))*(cos(U2))+(cos(U1))*(sin(U2))*(cos(Ls))))+pi;

if AAB<0:
    AAB=AAB+pi;
    ABA=ABA+pi;
    
print('DLUGOSC LOTU MIĘDZY LOTNISKAMI:',round(s,3),'m')

'xxxxxx'
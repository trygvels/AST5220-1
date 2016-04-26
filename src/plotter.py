import matplotlib.pyplot as plt
from numpy import *
from matplotlib import rc 
rc('font',**{'family':'serif'}) # This is for Latex writing
"""
#Import datafiles
#Relative densities
nu,lamda                 = loadtxt("omega_nulambda.dat",unpack=True)
m,b,r                    = loadtxt("omega_mbr.dat",unpack=True)
total                    = nu+lamda+m+b+r

#x,scalefactor,conformal time
x,a,eta                  = loadtxt("xaeta.dat",unpack=True)
#Hubbleparam,redshift
H,z                      = loadtxt("Hz.dat",unpack=True)

x_rec,z_rec,X_e          = loadtxt("X_e.dat",unpack=True)
n_e,tau,dtau             = loadtxt("n_e.dat",unpack=True)
x_test,z_test,n_etest    = loadtxt("n_etest.dat",unpack=True)

ddtau,tau_test,dtau_test = loadtxt("tau2.dat",unpack=True)
ddtau_test,g,g_test      = loadtxt("tau3.dat",unpack=True)
dg,dg_test,ddg           = loadtxt("g.dat",unpack=True)
ddg_test                 = loadtxt("g2.dat",unpack=True)
"""

#Test x,test eta
x_t,eta_t                = loadtxt("eta_t.dat",unpack=True)

"""
plt.figure(0)
plt.plot(x,m,label = r'$\Omega_m$')
plt.plot(x,b,label = r'$\Omega_b$')
plt.plot(x,r,label = r'$\Omega_r$')
plt.plot(x,nu,label = r'$\Omega_\nu$')
plt.plot(x,lamda,label = r'$\Omega_\lambda$')
plt.plot(x,total,label = r'Total')
plt.ylim([0,1.1])
plt.xlim([min(x),max(x)])
plt.legend(loc='best')
plt.xlabel(r'x')
plt.ylabel(r'$\Omega_x$')


plt.figure(1)
plt.plot(x,eta,label = r'$\eta(x)$')
plt.plot(x_t,eta_t,label=r'$\eta_2(x)$')
plt.yscale('log')
plt.xlim([min(x),max(x)])
plt.xlabel(r'x')
plt.ylabel(r'$\eta$(x)[Mpc]')
plt.legend(loc='best')

plt.figure(2)
plt.plot(x,H,label = r'H(x)')
plt.yscale('log')
plt.xlim([min(x),max(x)])
plt.xlabel(r'x')
plt.ylabel(r'H(x)[km s$^{-1}$Mpc$^{-1}$]')


plt.figure(3)
plt.plot(z,H,label = r'H(z)')
plt.yscale('log')
plt.xscale('log')
plt.xlim([z[0],z[-1]])
plt.xlabel(r'z')
plt.ylabel(r'H(z)[km s$^{-1}$Mpc$^{-1}$]')


plt.figure(4)
plt.plot(z_rec,X_e,label = r'$X_e$')
plt.yscale('log')
#plt.xscale('log')
plt.xlim([1800,0])
plt.xlabel(r'z')
plt.ylabel(r'$X_e$')


plt.figure(5)
plt.plot(z_rec ,n_e,'-',label = r'$n_{e}$')
plt.plot(z_test,n_etest,'-',label = r'Splined')
plt.yscale('log')
#plt.xscale('log')
plt.xlim([z_rec[0],z_rec[-1]])
plt.xlabel(r'z')
plt.ylabel(r'$n_e$[m$^{-3}$]')
plt.legend()

plt.figure(6)
plt.plot(x_rec , tau,            '-',label = r'$\tau(x)$')
#plt.plot(x_test, tau_test,       '-' ,label = r'$\tau_{test}(x)$')
plt.plot(x_rec , abs(dtau),      '--',label = r'$|\tau^\prime(x)|$')
#plt.plot(x_test, abs(dtau_test), '-' ,label = r'$|\tau^{\prime}_{test}(x)|$')
plt.plot(x_rec , abs(ddtau),     '-.',label = r'$|\tau^{\prime\prime}(x)|$')
#plt.plot(x_test, abs(ddtau_test),'-' ,label = r'$|\tau^{\prime\prime}_{test}(x)|$')
plt.yscale('log')
#plt.xscale('log')
plt.xlim([x_rec[0],x_rec[-1]])
plt.xlabel(r'x')
plt.ylabel(r'$\tau$,$|\tau^\prime|$,$|\tau^{\prime\prime}|$')
plt.legend()

plt.figure(7)
plt.plot(x_rec , g,            '-',label = r'$\tilde g(x)$')
#plt.plot(x_test, g_test,       '-' ,label = r'$\tilde g_{test}(x)$')
plt.plot(x_rec , dg/10.,       '--',label = r'$\tilde g^\prime(x)$')
#plt.plot(x_test, dg_test/10.,  '-' ,label = r'$\tilde g^\prime_{test}(x)$')
plt.plot(x_rec , ddg/300.,     '-.',label = r'$\tilde g^{\prime\prime}(x)$')
#plt.plot(x_test, ddg_test/300.,'-' ,label = r'$\tilde g^{\prime\prime}_{test}(x)$')
#plt.yscale('log')
#plt.xscale('log')
plt.xlim([-7.5,-6])
plt.xlabel(r'x')
plt.ylabel(r'$\tilde g$,$\tilde g^\prime/10$,$\tilde g^{\prime\prime}/300$')
plt.legend()
plt.show()
"""
deltam = loadtxt("delta.dat",unpack=True)
deltab = loadtxt("delta_b.dat",unpack=True)
Phi    = loadtxt("Phi.dat",unpack=True)
Psi    = loadtxt("Psi.dat",unpack=True)
Theta0 = loadtxt("Theta0.dat",unpack=True)
v      = loadtxt("v.dat",unpack=True)
vb     = loadtxt("v_b.dat",unpack=True)

plt.figure(9)
plt.plot(x_t,deltam[0],label = r'$\delta_{m,1}$')
plt.plot(x_t,deltam[1],label = r'$\delta_{m,5}$')
plt.plot(x_t,deltam[2],label = r'$\delta_{m,10}$')
plt.plot(x_t,deltam[3],label = r'$\delta_{m,40}$')
plt.plot(x_t,deltam[4],label = r'$\delta_{m,60}$')
plt.plot(x_t,deltam[5],label = r'$\delta_{m,100}$')
plt.xlim([min(x_t),max(x_t)])
plt.legend(loc='best')
plt.yscale('symlog')
plt.xlabel(r'x')
plt.ylabel(r'$\delta_{m,k}$')

plt.figure(10)
plt.plot(x_t,deltab[0],label = r'$\delta_{b,1}$')
plt.plot(x_t,deltab[1],label = r'$\delta_{b,5}$')
plt.plot(x_t,deltab[2],label = r'$\delta_{b,10}$')
plt.plot(x_t,deltab[3],label = r'$\delta_{b,40}$')
plt.plot(x_t,deltab[4],label = r'$\delta_{b,60}$')
plt.plot(x_t,deltab[5],label = r'$\delta_{b,100}$')
plt.xlim([min(x_t),max(x_t)])
plt.legend(loc='best')
plt.yscale('symlog')
plt.xlabel(r'x')
plt.ylabel(r'$\delta_{b,k}$')

plt.figure(11)
plt.plot(x_t,vb[0],label = r'$v_{b,1}$')
plt.plot(x_t,vb[1],label = r'$v_{b,5}$')
plt.plot(x_t,vb[2],label = r'$v_{b,10}$')
plt.plot(x_t,vb[3],label = r'$v_{b,40}$')
plt.plot(x_t,vb[4],label = r'$v_{b,60}$')
plt.plot(x_t,vb[5],label = r'$v_{b,100}$')
plt.xlim([min(x_t),max(x_t)])
plt.legend(loc='best')
plt.yscale('symlog')
plt.xlabel(r'x')
plt.ylabel(r'$v_{b,k}$')

plt.figure(12)
plt.plot(x_t,v[0],label = r'$v_{m,1}$')
plt.plot(x_t,v[1],label = r'$v_{m,5}$')
plt.plot(x_t,v[2],label = r'$v_{m,10}$')
plt.plot(x_t,v[3],label = r'$v_{m,40}$')
plt.plot(x_t,v[4],label = r'$v_{m,60}$')
plt.plot(x_t,v[5],label = r'$v_{m,100}$')
plt.xlim([min(x_t),max(x_t)])
plt.legend(loc='best')
plt.yscale('symlog')
plt.xlabel(r'x')
plt.ylabel(r'$v_{m,k}$')

plt.figure(13)
plt.plot(x_t,Phi[0],label = r'$\Phi_{1}$')
plt.plot(x_t,Phi[1],label = r'$\Phi_{5}$')
plt.plot(x_t,Phi[2],label = r'$\Phi_{10}$')
plt.plot(x_t,Phi[3],label = r'$\Phi_{40}$')
plt.plot(x_t,Phi[4],label = r'$\Phi_{60}$')
plt.plot(x_t,Phi[5],label = r'$\Phi_{100}$')
plt.xlim([min(x_t),max(x_t)])
plt.legend(loc='best')
#plt.yscale('symlog')
plt.xlabel(r'x')
plt.ylabel(r'$\phi_{k}$')

plt.figure(14)
plt.plot(x_t,Psi[0],label = r'$\Psi_{1}$')
plt.plot(x_t,Psi[1],label = r'$\Psi_{5}$')
plt.plot(x_t,Psi[2],label = r'$\Psi_{10}$')
plt.plot(x_t,Psi[3],label = r'$\Psi_{40}$')
plt.plot(x_t,Psi[4],label = r'$\Psi_{60}$')
plt.plot(x_t,Psi[5],label = r'$\Psi_{100}$')
plt.xlim([min(x_t),max(x_t)])
plt.legend(loc='best')
#plt.yscale('symlog')
plt.xlabel(r'x')
plt.ylabel(r'$\Psi_{k}$')

plt.figure(15)
plt.plot(x_t,Theta0[0],label = r'$\Theta_{0,1}$')
plt.plot(x_t,Theta0[1],label = r'$\Theta_{0,5}$')
plt.plot(x_t,Theta0[2],label = r'$\Theta_{0,10}$')
plt.plot(x_t,Theta0[3],label = r'$\Theta_{0,40}$')
plt.plot(x_t,Theta0[4],label = r'$\Theta_{0,60}$')
plt.plot(x_t,Theta0[5],label = r'$\Theta_{0,100}$')
plt.xlim([min(x_t),max(x_t)])
plt.legend(loc='best')
plt.yscale('symlog')
plt.xlabel(r'x')
plt.ylabel(r'$\Theta_{0,k}$')
plt.show()



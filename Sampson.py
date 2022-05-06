# Favour Sampson's assignment
numb_of_dolomite_cores= input('Enter the number of dolomite cores ')
numb_of_shale_cores= input('Enter the number of shale cores ')
numb_of_all_cores= input('Enter the number of all cores ')
numb_of_dolomite_cores=float(numb_of_dolomite_cores)
numb_of_shale_cores=float(numb_of_shale_cores)
numb_of_all_cores=float(numb_of_all_cores)
P_d= numb_of_dolomite_cores/numb_of_all_cores
P_s= numb_of_shale_cores/numb_of_all_cores

#import your scipy.stats

import scipy.stats
Loc_D= float(input('Enter the mean value for dolomite '))
Scale_D= float(input('Enter the standard deviation value for dolomite '))
Loc_S= float(input('Enter the mean value for shale '))
Scale_S= float(input('Enter the standard deviation value for shale '))
P_gamma_greaterthan_60D= 1-scipy.stats.norm(Loc_D,Scale_D).cdf(60)
P_gamma_greaterthan_60S= 1-scipy.stats.norm(Loc_S,Scale_S).cdf(60)

P_Dgamma_greaterthan60= P_gamma_greaterthan_60D/(P_d*P_gamma_greaterthan_60D) + (P_s*P_gamma_greaterthan_60S)

#Conditional Statements

if P_Dgamma_greaterthan60>0.5 or P_Dgamma_greaterthan60==0.5:
    print('P-D gamma greater than 60 value is ', P_Dgamma_greaterthan60)
    print('the interval is dolomite ')
else:
    print('P-D gamma greater than 60 value is ',P_Dgamma_greaterthan60)
    print('the interval is shale ')
print("TTOWG")

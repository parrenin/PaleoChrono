#Parameters specific to the MSD speleothem
self.archive='speleothem'
self.udepth_top = 0. #unthinned depth at the top of the record
self.age_top = 18520. #age at the top of the record
self.depth = np.arange(0., 0.418+0.0001, 0.001) #Define the depth grid for the age calculation
#Age grid for the accu correction function
self.corr_a_age = np.arange(self.age_top, 60000+self.age_top+0.01, 1000.)
#linear or staircase. Define whether the prior accu representation is linear or staircase
#in-between the data points.
self.accu_prior_rep = 'linear'

#The following parameters defines the covariance matrices as in AICC2012 (Bazin et al., 2013 and Veres et al., 2013).
#self.thickness=3273.                    #Real thickness
#self.cT2=0.000030/0.55
#self.sigmabA=0.7
#self.cA1=0.
#self.sigmabL=0.7
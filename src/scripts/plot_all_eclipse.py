import numpy as np
import matplotlib.pyplot as plt
from astropy.io import ascii
import paths

twi = ascii.read(paths.data / 'obs_NEOWISE.ecsv')
tat = ascii.read(paths.data / 'obs_ATLAS.ecsv')
tas = ascii.read(paths.data / 'obs_ASASSN.ecsv')
tav = ascii.read(paths.data / 'obs_AAVSO.ecsv')


tat_by_filter = tat.group_by('Filter')
print('ATLAS all observed photometric bands:')
print(tat_by_filter.groups.keys)

tas_by_filter = tas.group_by('Filter')
print('ASASSN all observed photometric bands:')
print(tas_by_filter.groups.keys)

tav_by_filter = tav.group_by('Filter')
print('AAVSO all observed photometric bands:')
print(tav_by_filter.groups.keys)

quit()
fig, (ax1,ax2,ax3,ax4) = plt.subplots(4,1,figsize = (10,10), sharex=True)



ax2.errorbar(twi['MJD'],twi['w1'],yerr=twi['w1err'],color='blue',fmt='.',label='W1')
ax2.errorbar(twi['MJD'],twi['w2'],yerr=twi['w2err'],color='red', fmt='.',label='W2')
ax3.errorbar(twi['MJD'],twi['w1w2'],yerr=twi['w1w2err'],fmt='.')


ax1.errorbar(tat['MJD'],tat['fnorm'],yerr=tat['fnormerr'],color='blue',fmt='.', label='ATLAS')
ax1.errorbar(tas['MJD'],tas['fnorm'],yerr=tas['fnormerr'],color='green',fmt='.', label='ASASSN')

ax1.set_ylim(0,1.1)
ax2.set_ylim(12,10.5)
ax1.set_xlim(58000,59800)
ax1.legend()
ax2.legend()
ax3.set_xlabel('Epoch [MJD]')

plt.savefig(paths.figures / 'all_the_photometry.pdf')
plt.show()

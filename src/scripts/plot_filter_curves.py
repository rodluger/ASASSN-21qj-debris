import numpy as np
import matplotlib.pyplot as plt
from astropy.io.votable import parse
from astropy.io import ascii
import paths

asas_g = parse(paths.data / "filter_curves/SLOAN.SDSS.g.xml").get_first_table()
asas_r = parse(paths.data / "filter_curves/SLOAN.SDSS.r.xml").get_first_table()
asas_i = parse(paths.data / "filter_curves/SLOAN.SDSS.i.xml").get_first_table()
prompt_b = ascii.read(paths.data / 'filter_curves/Bessel_B-1.txt')
prompt_v = ascii.read(paths.data / 'filter_curves/Bessel_V-1.txt')
prompt_i = ascii.read(paths.data / 'filter_curves/Bessel_I-1.txt')
atlas_c = ascii.read(paths.data / 'filter_curves/Misc_Atlas.cyan.dat')
atlas_o = ascii.read(paths.data / 'filter_curves/Misc_Atlas.orange.dat')


fig, (ax1,ax2,ax3) = plt.subplots(3,1, figsize=(8,8), sharex=True, sharey=True)
ax3.set_xlabel('Wavelength [Angstroms]',fontsize=20)
ax2.set_ylabel('transmission',fontsize=20)
fig.suptitle('Filter curves for ASASSN-21qj',fontsize=24)
ax1.set_xlim(3000,11000)
ax1.set_ylim(-0,1.2)

from matplotlib.patches import Polygon

def pc(ax,w,t,color='blue',label='V',alpha=0.2,textoffset=0.):
    polygon = Polygon(np.transpose( (np.append(w,np.max(w)), np.append(t,0)) ), # append ensures t=0 at both ends
                      fill=True,
                      closed=False,
                      facecolor=color,
                      edgecolor=None,
                     # color='red',
                      alpha=0.2,
                     zorder=-10)
    ax.add_patch(polygon)
    # line edge
    ax.plot(w,t,label=label,
            color=color,
            zorder=-9)

    maxw = w[np.argmax(t)]
    ax.text(maxw+textoffset, 1.02,
            label,
            fontsize=22,
            color=color,
           zorder=-8)

pc(ax2,asas_g.array['Wavelength'],asas_g.array['Transmission'],'blue','$g\'$',0.1)
pc(ax2,asas_r.array['Wavelength'],asas_r.array['Transmission'],'green','$r\'$',0.1)
pc(ax2,asas_i.array['Wavelength'],asas_i.array['Transmission'],'red','$i\'$',0.1)

pc(ax1,prompt_b['wlen']*10., prompt_b['tx']/100,'blue','B',0.1)
pc(ax1,prompt_v['wlen']*10., prompt_v['tx']/100,'green','V',0.1)
pc(ax1,prompt_i['wlen']*10., prompt_i['tx']/100,'brown','I',0.1)

pc(ax3,atlas_c['col1'], atlas_c['col2'],'cyan','c',textoffset=-1000)
pc(ax3,atlas_o['col1'], atlas_o['col2'],'orange','o',textoffset=0.)

fig.savefig(paths.figures / 'filter_curves.pdf')
plt.show()

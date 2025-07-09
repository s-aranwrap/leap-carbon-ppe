import xarray as xr
import numpy as np


def biome_mean(da):
    biomes=xr.open_dataset('/glade/u/home/linnia/LEAP/MFREU25/whitkey_CRUJRA.nc')
    b = biomes.biome
    la=xr.open_dataset('/glade/u/home/linnia/LEAP/MFREU25/landarea_retrain_h0.nc').landarea
    x=1/la.groupby(b).sum()*(la*da).groupby(b).sum()
    out = x.compute()
    out = out.assign_coords(biome_name=("biome", biomes.biome_name.values))
    return out


def global_mean(da):
    la=xr.open_dataset('/glade/u/home/linnia/LEAP/MFREU25/landarea_retrain_h0.nc').landarea

    if 'gridcell' in da.dims:
        dim='gridcell'
    else:
        dim=['lat','lon']
    x=(da*la).sum(dim=dim)/la.sum()
    return x.compute()

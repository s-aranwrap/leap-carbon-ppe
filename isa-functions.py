import cartopy.crs as ccrs
import cartopy.feature as cfeature

def scatter_variable(name, year, ensemble):
    '''
    Input: Variable name, Year (not index), Ensemble #
    Return: Plot/Global Map
    '''
    fig, ax = plt.subplots(subplot_kw={'projection': ccrs.PlateCarree()}, figsize=(10, 6))
    ax.coastlines()
    ax.add_feature(cfeature.BORDERS, linestyle=':')
    ax.set_global() 
    
    sc = ax.scatter(ds.grid1d_lon,
                ds.grid1d_lat,
                c=ds[name].sel(ens=ensemble, year=year),
                cmap='rainbow',
                s=20,
                transform=ccrs.PlateCarree())
    
    plt.colorbar(sc, ax=ax, orientation='vertical', label=name)
    
    plt.title(f"{name} in {year}, ensemble #{ensemble}")
    plt.show()

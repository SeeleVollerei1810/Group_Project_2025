import xarray as xr
import numpy as np
import warnings
from typing import Dict

warnings.filterwarnings("ignore", message="All-NaN slice encountered")

INDEX_INFO: Dict[str, Dict[str, str]] = {
    "Tw": {"long_name": "Wet-bulb Temperature", "units": "°C"},
    "WBGT": {"long_name": "Wet-Bulb Globe Temperature", "units": "°C"},
}

def calculate_indices(ds: xr.Dataset) -> xr.Dataset:

    TAS = ds['tas']
    RH = ds['rh'] * 100 if ds['rh'].max() <= 1.0 else ds['rh']

    tw_val = (TAS * np.arctan(0.151977 * (RH + 8.313659)**0.5) +
              np.arctan(TAS + RH) -
              np.arctan(RH - 1.676331) +
              0.00391838 * (RH)**1.5 * np.arctan(0.023101 * RH) -
              4.686035)

    e = (RH / 100) * 6.112 * np.exp((17.67 * TAS) / (243.5 + TAS))
    wbgt_val = 0.567 * TAS + 0.393 * e + 3.94

    ds['Tw'] = tw_val
    ds['Tw'].attrs = INDEX_INFO["Tw"]

    ds['WBGT'] = wbgt_val
    ds['WBGT'].attrs = INDEX_INFO["WBGT"]

    return ds

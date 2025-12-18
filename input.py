import xarray as xr
from pathlib import Path
import os
import glob

def combine_datasets(datasets):
    priority_vars = ['tas', 'tasmax', 'tasmin', 'pr']
    datasets_to_merge = [datasets[name] for name in priority_vars if name in datasets]

    merged = xr.merge(datasets_to_merge, compat='override', join='outer')
    print(f"\nDataset has been combined. Variables:{list(merged.data_vars)}")
    return merged

def load_all_data_for_analysis():
    
    combined_data = combine_datasets(all_datasets)

    return combined_data


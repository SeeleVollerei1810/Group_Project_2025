# An Integrated Toolbox for Assessing and Enhancing Urban Resilience to Climate Extremes

## 📖 Introduction
This project aims to develop an integrated computational toolbox to explore climate-biosphere feedback processes and assess urban resilience to climate extremes.

In the context of rapid urbanization and global warming, this toolbox provides a workflow to process climate data, compute extreme indicators, and visualize risks associated with heat stress and extreme rainfall.

## 🚀 Key Features
The toolbox focuses on the following primary objectives:
* **Climate Extreme Indicators (ETCCDI):** Computing indices such as `TXx`, `TNn`, `R95p`, and `PRCPTOT` to assess long-term temperature and rainfall trends.
* **Heat-Stress Metrics:** Calculating human heat exposure metrics like Wet-Bulb Temperature (`Tw`) and Wet-Bulb Globe Temperature (`WBGT`).
* **Visualization:** Generating maps, plots, and statistical summaries to identify urban hotspots and support data-driven planning.

## 🛠️ Technology Stack
The project is implemented using the **Python** ecosystem with the following key libraries:
* `xarray`, `numpy`, `pandas`: For multi-dimensional data manipulation.
* `matplotlib`: For static plotting and visualization.
* `Dask`: For parallel computing and handling large datasets.

## ⚙️ Configurable Parameters
Below are the key parameters available in the toolbox for customizing the climate analysis and simulation:
| Parameter | Category | Description |
| :--- | :--- | :--- |
| `input_dataset` | I/O Data | Path to the input climate data files (NetCDF, WRF, or Satellite data) |
| `output_dir` | I/O Data | Directory where generated maps, plots, and statistical summaries will be saved |
| `start_year` / `end_year` | Time Settings | The time range for long-term trend analysis (e.g., 1980-2020) |
| `study_area_bounds` | Spatial | Coordinate boundaries (min_lat, max_lat, min_lon, max_lon) to crop the study area |
| `precipitation_threshold` | Climate Index | Threshold value (mm) to define extreme rainfall days (used for **R95p**, **PRCPTOT**)  |
| `temperature_percentile` | Climate Index | Percentile value (e.g., 90th, 95th) for calculating extreme temperature events (**TXx**, **TNn**)  |
| `heat_stress_metric` | Simulation | Option to select the heat stress indicator to compute: `'Tw'` (Wet-Bulb) or `'WBGT'`  |
| `baseline_period` | Analysis | Reference period used to calculate climate anomalies and deviations |
| `plot_resolution` | Visualization | Resolution setting for generating output maps and heatmaps |

## 👥 Author
**University of Science and Technology of Hanoi (USTH)** *Department of Space and Earth Sciences*
| Name | Student ID |
| :--- | :--- |
| **Pham Minh Thu** | BA12-170 |
| **Nguyen Ngoc Quan** | 22TA13002 |
| **Le Van Ben** | 22BA12046 |
| **Nguyen Quang Nam** | 2410682 |

**Supervisor:** Dr. Nguyen Xuan Thanh

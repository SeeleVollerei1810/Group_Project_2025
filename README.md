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

## ⚙️ Configurable Parameters & Climate Indices
The toolbox computes a comprehensive set of **12 ETCCDI climate indices** to assess urban resilience. Below are the definitions and configuration thresholds currently implemented in the core modules.
### 1. General Configuration
| Parameter | Location | Description | Default Value |
| :--- | :--- | :--- | :--- |
| `START_YEAR` | `io.py` | Start year for the analysis window | `1961` |
| `END_YEAR` | `io.py` | End year for the analysis window | `2023` |
| `lat_range` / `lon_range` | `main.ipynb`| Spatial boundaries for the study area | `(8, 24)` / `(102, 110)` |
### 2. Temperature Indices (Heat Stress)
| Parameter | Category | Description | Threshold / Logic |
| :--- | :--- | :--- | :--- |
| **`TXx`** | Extreme Heat | Annual maximum of daily maximum temperature | Absolute Max (°C) |
| **`TNn`** | Extreme Cold | Annual minimum of daily minimum temperature | Absolute Min (°C) |
| **`SU25`** | Heatwave | Number of **Summer Days** per year | Tmax > **25°C** |
| **`TR20`** | Heatwave | Number of **Tropical Nights** per year | Tmin > **20°C** |
| **`DTR`** | Variability | Diurnal Temperature Range (Daily Tmax - Tmin) | Daily Difference |
| **`Tmean`** | General | Annual Mean Temperature | Mean (°C) |
### 3. Precipitation Indices (Flooding Risk)
| Parameter | Category | Description | Threshold / Logic |
| :--- | :--- | :--- | :--- |
| **`Rx1day`** | Intensity | Maximum 1-day precipitation amount | Absolute Max (mm) |
| **`Rx5day`** | Intensity | Maximum 5-day consecutive precipitation | Absolute Max (mm) |
| **`SDII`** | Intensity | Simple Daily Intensity Index (Rain rate on wet days) | PRCPTOT / Wet Days |
| **`R95p`** | Extreme Rain | Very wet days precipitation total | > **95th percentile** |
| **`R99p`** | Extreme Rain | Extremely wet days precipitation total | > **99th percentile** |
| **`PRCPTOT`** | Availability | Annual total precipitation from wet days | Daily Rain > **1mm** |

## 👥 Author
**University of Science and Technology of Hanoi (USTH)** *Department of Space and Earth Sciences*
| Name | Student ID |
| :--- | :--- |
| **Pham Minh Thu** | BA12-170 |
| **Nguyen Ngoc Quan** | 22TA13002 |
| **Le Van Ben** | 22BA12046 |
| **Nguyen Quang Nam** | 2410682 |

**Supervisor:** Dr. Nguyen Xuan Thanh

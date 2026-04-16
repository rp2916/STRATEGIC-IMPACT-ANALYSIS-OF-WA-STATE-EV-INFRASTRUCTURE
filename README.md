# Bridging the Gap: Washington State EV Infrastructure Analysis

## 📌 Project Overview
This project analyzes the current state of Electric Vehicle (EV) infrastructure across Washington State, identifying critical bottlenecks, "charging deserts," and socioeconomic equity gaps in EV adoption. The resulting executive dashboard provides data-driven evidence to guide policymakers, urban planners, and charging network developers on where infrastructure investments are needed most.

## 🎯 Key Objectives
* **Map the Infrastructure Gap:** Compare raw EV ownership volume against available public charging stations.
* **Identify Bottlenecks:** Highlight high-density ZIP codes suffering from extreme charger shortages (The 80/20 adoption rule).
* **Assess Socioeconomic Equity:** Analyze the correlation between median household income and EV adoption to highlight demographic disparities.

## 🛠️ Tech Stack
* **Data Processing & Cleaning:** Python (Pandas, NumPy)
* **Data Visualization & Dashboarding:** Tableau
* **Data Sources:** * WA State Department of Licensing (EV Registrations)
  * US Department of Energy (Alternative Fuel Stations)
  * IRS Open Data (ZIP Code Median Income)

## 📊 The Dashboard
*<img width="1426" height="834" alt="Screenshot 2026-04-16 at 23 00 53" src="https://github.com/user-attachments/assets/581bac8f-e767-44a2-8fec-da772a6b7647" />*

### Key Visualizations:
1. **Dual-Axis Geospatial Map:** Overlays EV demand heatmaps with distinct charging station locations.
2. **Diverging Lollipop Chart:** Visualizes income variance in the top 20 EV markets, proving adoption skews heavily toward above-average incomes.
3. **Pareto Curve:** Demonstrates that a tiny fraction of neighborhoods hold the vast majority of electric vehicles.
4. **Density Scatter Plot:** Shows the exact income brackets driving EV adoption demand.

## 🚀 How to Run the Data Pipeline
1. Clone the repository.
2. Ensure raw data files are placed in a `data/` directory.
3. Run the preprocessing script to generate the aggregated dataset:
   ```bash
   python data_preprocessing.py

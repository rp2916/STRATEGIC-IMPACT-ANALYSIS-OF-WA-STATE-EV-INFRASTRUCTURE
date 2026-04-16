import pandas as pd
import numpy as np

def clean_and_merge_ev_data():
    print("Loading datasets...")
    # Load raw datasets (Assumes files are in a 'data' folder)
    ev_pop = pd.read_csv('data/Electric_Vehicle_Population_Data.csv')
    stations = pd.read_csv('data/alt_fuel_stations.csv')
    irs_income = pd.read_csv('data/irs_zip_income.csv')

    print("Cleaning EV Population Data...")
    # Group EVs by ZIP code to get total EV demand per neighborhood
    ev_grouped = ev_pop.groupby('Postal Code').size().reset_index(name='total_evs')
    ev_grouped.rename(columns={'Postal Code': 'ZIP'}, inplace=True)

    print("Cleaning Charging Station Data...")
    # Filter for electric charging stations only in WA state
    wa_stations = stations[(stations['State'] == 'WA') & (stations['Fuel Type Code'] == 'ELEC')]
    # Group by ZIP code to get total stations per neighborhood
    station_grouped = wa_stations.groupby('ZIP').size().reset_index(name='total_charging_stations')

    print("Merging Data...")
    # Merge EV demand with Station Supply
    df_merged = pd.merge(ev_grouped, station_grouped, on='ZIP', how='left')
    
    # Fill NaN stations with 0 (areas with EVs but no chargers)
    df_merged['total_charging_stations'] = df_merged['total_charging_stations'].fillna(0)

    # Merge with IRS Income Data
    df_final = pd.merge(df_merged, irs_income[['ZIP', 'median_income']], on='ZIP', how='left')

    print("Calculating Custom Metrics...")
    # Calculate the bottleneck metric: EVs per Station
    # Add a small epsilon (0.1) to avoid division by zero for charging deserts
    df_final['evs_per_station'] = df_final['total_evs'] / (df_final['total_charging_stations'] + 0.1)
    df_final['evs_per_station'] = df_final['evs_per_station'].round(2)

    print("Exporting Clean Dataset...")
    df_final.to_csv('wa_ev_infrastructure_clean.csv', index=False)
    print("Export Complete: wa_ev_infrastructure_clean.csv")

if __name__ == "__main__":
    clean_and_merge_ev_data()

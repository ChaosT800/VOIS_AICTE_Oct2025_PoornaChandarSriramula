import pandas as pd
import matplotlib.pyplot as plt

# --- CONFIGURATION: SET YOUR FILE NAME HERE ---
# NOTE: This assumes you uploaded the data as '1730285881-Airbnb_Open_Data.xlsx' to the Colab session
# If you run this code on your local machine, ensure the file is in the same folder.
FILE_NAME = '1730285881-Airbnb_Open_Data.xlsx'

def run_airbnb_analysis():
    """Performs data cleaning and generates the three required analysis charts."""
    try:
        # Read the data file (assuming a CSV format, even with .xlsx extension)
        df = pd.read_csv(FILE_NAME)
        print(f"Data loaded successfully from {FILE_NAME}")
    except FileNotFoundError:
        print(f"Error: The file '{FILE_NAME}' was not found. Please check the file path/name.")
        return

    # --- Data Inspection, Optimization, and Cleaning ---
    # Drop non-essential, memory-heavy columns
    df.drop(columns=['NAME', 'host name', 'house_rules', 'license'], inplace=True, errors='ignore')

    # Standardizing location names to ensure accurate grouping
    df['neighbourhood group'] = df['neighbourhood group'].replace({
        'brookln': 'Brooklyn',
        'manhatan': 'Manhattan'
    })

    # --- Chart 1 (Q2): Distribution of Listings by Neighbourhood Group ---
    cleaned_neighbourhood_counts = df['neighbourhood group'].value_counts(dropna=True)
    plt.figure(figsize=(10, 6))
    cleaned_neighbourhood_counts.sort_values(ascending=False).plot(kind='bar', color='skyblue')
    plt.title('Distribution of Airbnb Listings by Neighbourhood Group (Chart 1)')
    plt.xlabel('Neighbourhood Group')
    plt.ylabel('Number of Listings')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('neighbourhood_distribution.png')
    print("Chart 1: 'neighbourhood_distribution.png' saved.")


    # --- Chart 2 (Q3): Average Price by Neighbourhood Group ---
    average_price = df.groupby('neighbourhood group')['price'].mean().sort_values(ascending=False)
    plt.figure(figsize=(10, 6))
    average_price.plot(kind='bar', color='lightcoral')
    plt.title('Average Listing Price by Neighbourhood Group (Chart 2)')
    plt.xlabel('Neighbourhood Group')
    plt.ylabel('Average Price ($)')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('average_price_by_neighbourhood.png')
    print("Chart 2: 'average_price_by_neighbourhood.png' saved.")


    # --- Chart 3 (Q1): Distribution of Listings by Room Type ---
    room_type_counts = df['room type'].value_counts(dropna=False)
    plt.figure(figsize=(8, 6))
    room_type_counts.sort_values(ascending=False).plot(kind='bar', color='darkgreen')
    plt.title('Distribution of Airbnb Listings by Room Type (Chart 3)')
    plt.xlabel('Room Type')
    plt.ylabel('Number of Listings')
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig('room_type_distribution.png')
    print("Chart 3: 'room_type_distribution.png' saved.")

    print("\n--- Analysis Complete. All charts saved as PNG files. ---")

if __name__ == '__main__':
    run_airbnb_analysis()
	
	// SIR I KNOW INSTEAD OF NOTEBOOK IAM USING .PY AS SOURCE CODE AS NOTEBOOK IS KEEP CRASHING AND RESTARTING PLEASE CONSIDER THIS SIR
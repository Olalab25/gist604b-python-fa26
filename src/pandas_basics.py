"""
Pandas Basics for GIS Data Analysis - Student Implementation

Complete the four functions in this file.
Use the notebooks to learn and test each function.

📋 FUNCTIONS TO IMPLEMENT IN THIS FILE:
=====================================
✅ Function 1: load_and_explore_gis_data()     → notebooks/01_function_...
✅ Function 2: filter_environmental_data()     → notebooks/02_function_...
✅ Function 3: calculate_station_statistics()  → notebooks/03_function_...
✅ Function 4: join_station_data()             → notebooks/04_function_...
"""

import pandas as pd
from pathlib import Path
import os


# =============================================================================
# FUNCTION 1: LOAD AND EXPLORE GIS DATA
# =============================================================================

def load_and_explore_gis_data(file_path):
    """
    Load a CSV file and display comprehensive information about the dataset.
    
    This function demonstrates the first step in any data analysis project:
    understanding your data through exploration.
    
    Args:
        file_path (str): Path to the CSV file to load
        
    Returns:
        pandas.DataFrame: The loaded dataset, or None if loading failed
    
    Example:
        >>> stations_df = load_and_explore_gis_data('data/weather_stations.csv')
        Loading data from: data/weather_stations.csv
        Dataset shape: (150, 6) - That's 150 rows and 6 columns!
        ...
    """
    
    #  Print a header to show what function is running
    # print("=" * 50) and print("LOADING AND EXPLORING GIS DATA")
    
    # Print the file path being loaded
    # print(f"Loading data from: {file_path}")
    
    # Try to load the CSV file using pd.read_csv()
    # Wrap in try/except to handle missing files gracefully
    # If file doesn't exist, print error and return None
    
    # Print the shape of the DataFrame (rows, columns)
    #  df.shape to get a tuple like (150, 6)
    # Print it in a friendly way: "Dataset shape: (150, 6) - That's 150 rows and 6 columns!"
    
    # Print the column names
    #  df.columns to get the list
    # Print: "Columns: ['station_id', 'name', 'latitude', ...]"
    
    # Print the first few rows using df.head()
    # Show this to help understand the data
    
    # Print basic statistics using df.describe()
    # This shows min, max, mean for numeric columns
    
    # Check for missing values using df.isnull().sum()
    # Print how many missing values in each column
    
    # Print a completion message
    
    # Return the loaded DataFrame
    
    pass  # Remove this line when you implement the function


# =============================================================================
# FUNCTION 2: FILTER ENVIRONMENTAL DATA
# =============================================================================

def filter_environmental_data(df, min_temp=15, max_temp=30, quality="good"):
    """
    Filter environmental data based on temperature range and data quality.
    
    This function demonstrates how to apply multiple filtering conditions
    to clean and prepare environmental data for analysis.
    
    Args:
        df (pandas.DataFrame): Environmental data with temperature and quality columns
        min_temp (float): Minimum acceptable temperature in Celsius (default: 15)
        max_temp (float): Maximum acceptable temperature in Celsius (default: 30)
        quality (str): Required data quality level (default: "good")
        
    Returns:
        pandas.DataFrame: Filtered data meeting all specified conditions
    
    Example:
        >>> filtered_df = filter_environmental_data(readings_df, min_temp=20, max_temp=30, quality='good')
        Original data: 1000 rows
        After filtering: 247 rows (24.7% of data retained)
        Filters applied:
          - Temperature: 20.0°C to 30.0°C
          - Data quality: good
    """
    
    # Print a header
    # print("=" * 50) and print("FILTERING ENVIRONMENTAL DATA")
    
    # Print the original DataFrame shape
    #   len(df) to get the number of rows
    
    # TFilter by temperature range using boolean indexing
    # Create a mask: (df['temperature_c'] >= min_temp) & (df['temperature_c'] <= max_temp)
    # Apply the mask: filtered_df = df[mask]
    
    # Filter by data quality
    # Add another condition: filtered_df = filtered_df[filtered_df['data_quality'] == quality]
    
    # Calculate and print filtering statistics
    # Total number of rows remaining after filtering
    # What percentage of data was retained
    # Show the filter criteria used
    
    # Return the filtered DataFrame
    
    pass  # Remove this line when you implement the function


# =============================================================================
# FUNCTION 3: CALCULATE STATION STATISTICS
# =============================================================================

def calculate_station_statistics(df):
    """
    Calculate station statistics
    
    This function groups temperature readings by weather station and calculates
    summary statistics (average temperature, number of readings, etc.) for each
    station.
    
    Args:
        df (pandas.DataFrame): Environmental readings data with 'station_id', 'temperature_c' and 'humidity_percent' columns
    
    Returns:
        pandas.DataFrame: Statistics for each station with columns:
            - station_id: The weather station identifier
            - avg_temperature: Average temperature for this station
            - avg_humidity: Average humidity for this station
            - reading_count: Number of readings from this station
    
    Example:
        >>> stats_df = calculate_station_statistics(readings_df)
        Calculating statistics for 5 unique stations...
        Statistics calculated:
          - Total readings analyzed: 1000
          - Stations with data: 5
          - Average readings per station: 200.0
    """
    
    # Print a header
    # print("=" * 50) and print("CALCULATING STATION STATISTICS")
    
    # Count unique stations
    #  df['station_id'].nunique()
    
    # Group by station_id
    # Use df.groupby('station_id')
    
    # Calculate statistics for each group
    # Count of readings: use .size() or .count()
    # Average temperature: use .mean()
    # Create a new DataFrame with these statistics
    
    # Reset the index to make station_id a regular column
    # Use .reset_index()
    
    # Rename columns to be clear
    # Use .rename(columns={'temperature_c': 'avg_temperature', ...})
    
    # Print summary statistics
    # Total readings analyzed
    # Number of stations
    # Average readings per station
    
    # Return the statistics DataFrame
    
    pass  # Remove this line when you implement the function


# =============================================================================
# FUNCTION 4: JOIN STATION DATA
# =============================================================================

def join_station_data(stations_df, readings_df):
    """
    Join sensor readings with station metadata
    
    This function joins station information (name, location) with temperature readings.
    You'll add station details (like station name and coordinates) to each temperature reading.
    
    Args:
        stations_df (pandas.DataFrame): Station information with 'station_id', 'station_name', 
                                       'latitude', 'longitude', etc.
        readings_df (pandas.DataFrame): Temperature readings with 'station_id', 'date', 
                                       'temperature_c', etc.
    
    Returns:
        pandas.DataFrame: Combined dataset with readings AND station information
    
    Example:
        >>> joined_df = join_station_data(stations_df, readings_df)
        Joining station information with readings...
        Stations table: 5 stations
        Readings table: 1000 readings
        Joined table: 1000 rows with station details added!
    """
    
    # Print a header
    # print("=" * 50) and print("JOINING STATION DATA")
    
    # Print the shapes of both input DataFrames
    # Show how many stations and how many readings
    
    # Join the DataFrames using pd.merge()
    # Use the 'station_id' column as the key
    # Use how='left' to keep all readings even if station info is missing
    
    # Print the shape of the joined DataFrame
    # Verify all readings are still present
    
    # Print the new columns that were added
    # Show which columns came from the stations table
    
    # Return the joined DataFrame
    
    pass  # Remove this line when you implement the function


# =============================================================================
# HELPER FUNCTIONS (You don't need to modify these - they're provided!)
# =============================================================================

def _check_required_columns(df, required_columns, data_name="DataFrame"):
    """
    Helper function to check if required columns exist in a DataFrame.
    
    Args:
        df (pandas.DataFrame): DataFrame to check
        required_columns (list): List of required column names
        data_name (str): Name to use in error messages
    
    Returns:
        tuple: (bool, list) - (all_present, missing_columns)
    """
    if df is None or df.empty:
        return False, required_columns
    
    missing = [col for col in required_columns if col not in df.columns]
    return len(missing) == 0, missing


def _format_number(value, decimals=1):
    """
    Helper function to format numbers for display.
    
    Args:
        value: Number to format
        decimals (int): Number of decimal places
    
    Returns:
        str: Formatted number
    """
    try:
        return f"{float(value):.{decimals}f}"
    except (ValueError, TypeError):
        return str(value)

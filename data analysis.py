import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
from sklearn.datasets import load_iris
import seaborn as sns  # Added for more visualization styles

def perform_data_tasks():
    """
    Performs data manipulation, analysis, visualization, and web request tasks.
    """
    # 1. NumPy array and mean calculation
    numbers = np.arange(1, 11)  # Create a NumPy array from 1 to 10
    mean_value = np.mean(numbers)
    print(f"NumPy Array: {numbers}")
    print(f"Mean: {mean_value}")

    # 2. Pandas DataFrame and summary statistics
    data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emily'],
            'Age': [25, 30, 22, 28, 35],
            'City': ['New York', 'Los Angeles', 'Chicago', 'New York', 'Los Angeles'],
            'Salary': [50000, 60000, 45000, 55000, 70000]}
    df = pd.DataFrame(data)  # Create a pandas DataFrame
    print("\nPandas DataFrame:")
    print(df)
    print("\nSummary Statistics:")
    print(df.describe())  # Display summary statistics

    # 3. Fetch data from a public API using requests
    try:
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        response.raise_for_status()  # Raise an exception for bad status codes
        data = response.json()
        bitcoin_price = data['bpi']['USD']['rate']
        print(f"\nCurrent Bitcoin Price (USD): {bitcoin_price}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from CoinDesk API: {e}")
    except KeyError:
        print("Error: Could not extract Bitcoin price from the API response.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    # 4. Plot a simple line graph using matplotlib
    values = [2, 4, 1, 5, 3, 6, 7, 5, 8, 9]
    plt.plot(values)  # Create a line plot
    plt.title('Simple Line Graph')  # Set the title
    plt.xlabel('Index')  # Set the x-axis label
    plt.ylabel('Value')  # Set the y-axis label
    plt.show()  # Display the plot

    # Task 1: Load and Explore the Dataset
    # Load the Iris dataset
    iris = load_iris()
    iris_df = pd.DataFrame(data=np.c_[iris['data'], iris['target']],
                           columns=iris['feature_names'] + ['target'])
    iris_df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names) # Add species names

    print("\n\nTask 1: Load and Explore the Dataset")
    print("\nFirst 5 rows of the Iris dataset:")
    print(iris_df.head())  # Display the first few rows

    print("\nDataset structure (data types and missing values):")
    print(iris_df.info())  # Explore the structure

    # Check for missing values
    print("\nMissing values:")
    print(iris_df.isnull().sum())

    # Clean the dataset (handling missing values if any)
    # In this case, the Iris dataset has no missing values, so we don't need to do anything.
    cleaned_iris_df = iris_df.copy() # Create a copy for the next tasks

    # Task 2: Basic Data Analysis
    print("\n\nTask 2: Basic Data Analysis")
    print("\nBasic statistics of numerical columns:")
    print(cleaned_iris_df.describe())  # Compute basic statistics

    print("\nMean of sepal length grouped by species:")
    print(cleaned_iris_df.groupby('species')['sepal length (cm)'].mean())  # Group and compute mean

    # Task 3: Data Visualization
    print("\n\nTask 3: Data Visualization")

    # 1. Line chart (example:  not really applicable to Iris, so I'll make a different one)
    plt.figure()
    plt.plot(cleaned_iris_df.index, cleaned_iris_df['sepal length (cm)'], color='blue')
    plt.title('Sepal Length over Index')
    plt.xlabel('Index')
    plt.ylabel('Sepal Length (cm)')
    plt.show()


    # 2. Bar chart
    plt.figure()
    sns.barplot(x='species', y='petal length (cm)', data=cleaned_iris_df, palette='viridis')
    plt.title('Average Petal Length per Species')
    plt.xlabel('Species')
    plt.ylabel('Average Petal Length (cm)')
    plt.show()

    # 3. Histogram
    plt.figure()
    sns.histplot(cleaned_iris_df['sepal width (cm)'], kde=True, color='green')
    plt.title('Distribution of Sepal Width')
    plt.xlabel('Sepal Width (cm)')
    plt.ylabel('Frequency')
    plt.show()

    # 4. Scatter plot
    plt.figure()
    sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', hue='species', data=cleaned_iris_df, palette='Set1')
    plt.title('Sepal Length vs. Petal Length')
    plt.xlabel('Sepal Length (cm)')
    plt.ylabel('Petal Length (cm)')
    plt.legend(title='Species')
    plt.show()

if __name__ == "__main__":
    perform_data_tasks()

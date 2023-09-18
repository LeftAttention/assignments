import pandas as pd

def main():
    data = {
        'Name': ['Sanu', 'Manu', 'Bapun', 'Manas', 'Madhu'],
        'Age': [24, 27, 22, 32, 29],
        'City': ['Delhi', 'Bengaluru', 'Hyderabad', 'Pune', 'Kochi']
    }
    df = pd.DataFrame(data)

    # Display the first two rows of the dataframe
    print(df.head(2))

    # Add a new column
    df['Employed'] = [True, False, True, True, False]

    # Filter the data
    filtered_data = df[df['Age'] > 25]

    # Find the average age
    average_age = df['Age'].mean()

    # Group the data
    grouped_data = df.groupby('City').size()

    # Display the results
    print("\n\nFiltered data (Age > 25):")
    print(filtered_data)

    print("\n\nAverage age:")
    print(average_age)

    print("\n\nGrouped data by city:")
    print(grouped_data)

if __name__ == "__main__":
    main()
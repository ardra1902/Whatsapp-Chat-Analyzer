import re
import pandas as pd
def preprocess(data):
    pattern = re.compile(r'(\d{2}/\d{2}/\d{2}), (\d{2}:\d{2}) - ([^:]+): (.*)')
        
    # Find all matches in the data
    matches = pattern.findall(data)

    # Create a DataFrame
    df = pd.DataFrame(matches, columns=['Date', 'Time', 'User', 'Message'])
    df[['Day', 'Month', 'Year']] = df['Date'].str.split('/', expand=True)

    # Convert year to four digits
    df['Year'] = '20' + df['Year']

    # Split time into hour and minute
    df[['Hour', 'Minute']] = df['Time'].str.split(':', expand=True)

    # Reorder columns
    df = df[['Year', 'Month', 'Day', 'Hour', 'Minute', 'User', 'Message','Date']]
    return df

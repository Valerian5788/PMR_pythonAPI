import pandas as pd


def getCrowdManagementOfDayCharleroi(day):
    # Example of validating the format of the day string
    if len(day) != 6:
        return {'error': 'Invalid day format. Please provide day in ddmmyy format.'}

    # Read the CSV file
    charleroi = pd.read_csv("pythonAPI_PMR/donnéesCharleroi.csv")

    # Convert the 'timestamp' column to datetime with correct format
    charleroi['timestamp'] = pd.to_datetime(charleroi['timestamp'], format='%d/%m/%Y %H:%M:%S')

    # Convert day to the expected format (if needed)
    day_str_formatted = day[:2] + '/' + day[2:4] + '/' + day[4:]

    # Filter data for the specified day
    charleroi_filtered = charleroi[charleroi['timestamp'].dt.strftime('%d/%m/%y') == day_str_formatted]

    # Convert filtered data to JSON
    json_data = charleroi_filtered.to_dict(orient='records')

    # Return JSON response
    return json_data



def getCrowdManagementOfDayNamur(day):
    # Example of validating the format of the day string
    if len(day) != 6:
        return {'error': 'Invalid day format. Please provide day in ddmmyy format.'}

    # Read the CSV file
    Namur = pd.read_csv("pythonAPI_PMR/donnéesNamur.csv")

    # Convert the 'timestamp' column to datetime with correct format
    Namur['timestamp'] = pd.to_datetime(Namur['timestamp'], format='%d/%m/%Y %H:%M:%S')

    # Convert day to the expected format (if needed)
    day_str_formatted = day[:2] + '/' + day[2:4] + '/' + day[4:]

    # Filter data for the specified day
    Namur_filtered = Namur[Namur['timestamp'].dt.strftime('%d/%m/%y') == day_str_formatted]

    # Convert filtered data to JSON
    json_data = Namur_filtered.to_dict(orient='records')

    # Return JSON response
    return json_data
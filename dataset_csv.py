import pandas as pd
from datetime import datetime

# Define a function to create a CSV file with sample data
def create_csv():
    # Sample data to be added to CSV file
    data = [
        {"timestamp": "2024-11-10 14:23:34", "detected_emotion": "happy", "song_recommendation": "Happy - Pharrell Williams", "song_link": "https://www.youtube.com/watch?v=ZbZSe6N_BXs"},
        {"timestamp": "2024-11-10 15:47:20", "detected_emotion": "sad", "song_recommendation": "Someone Like You - Adele", "song_link": "https://www.youtube.com/watch?v=hLQl3WQQoQ0"},
        # More rows can be added as needed
    ]

    # Convert the data into a pandas DataFrame
    df = pd.DataFrame(data)

    # Specify the CSV file name (this will create a new file or overwrite an existing one)
    csv_file = "emotion_song_data.csv"

    # Save the DataFrame to CSV
    df.to_csv(csv_file, index=False)

    print(f"CSV file '{csv_file}' has been created successfully!")

# Call the function to create the CSV file
if __name__ == "__main__":
    create_csv()

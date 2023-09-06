from bs4 import BeautifulSoup
import openpyxl
import pandas as pd
import matplotlib.pyplot as plt
import requests

url = 'https://en.wikipedia.org/wiki/List_of_National_Football_League_career_rushing_yards_leaders'

page = requests.get(url)

if page.status_code == 200:
    soup = BeautifulSoup(page.text, 'html.parser')
    tables = soup.find_all('table', {'class': 'wikitable sortable'})

    if len(tables) >= 2:
        # Access the second table (index 1)
        table = tables[0]

        # Extract data from the table
        rows = table.find_all('tr')
        data = []

        for row in rows[1:]:  # Skip the header row (index 0)
            columns = row.find_all('td')
            if len(columns) >= 3:  # Check if there are at least 3 columns (rank, player, yards)
                rank = columns[0].get_text(strip=True)
                player = columns[1].get_text(strip=True).replace('^', '')  # Remove "^" character
                yards = columns[4].get_text(strip=True)

                data.append([rank, player, yards])

        # Create a DataFrame
        df = pd.DataFrame(data, columns=['Rank', 'Player', 'Yards'])

        # Remove the index when printing
        print(df.to_string(index=False))

    else:
        print('There are fewer than two tables on the page')
else:
    print('Failed to fetch the web page')

# Convert 'Yards' to numeric values (remove commas)
df['Yards'] = df['Yards'].str.replace(',', '').astype(int)

# Create the line chart
plt.figure(figsize=(10, 6))
plt.plot(df['Rank'], df['Yards'], marker='o', linestyle='-', color='red')

# Add labels and title
plt.xlabel('Rank')
plt.ylabel('Yards')
plt.title('NFL Career Rushing Yards Leaders')

# Show the chart
plt.show()

# Create a bar chart showing the top 10 players by yards
top_10_df = df.head(10)
plt.figure(figsize=(10, 6))
plt.bar(top_10_df['Player'], top_10_df['Yards'])

# Add labels and title
plt.xlabel('Player')
plt.ylabel('Yards')
plt.title('Top 10 NFL Career Rushing Yards Leaders')

# Readability and Show Chart
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()
plt.show()

# Create a box and whisker plot for the 'Yards' column
plt.figure(figsize=(8, 6))
plt.boxplot(df['Yards'])
plt.ylabel('Yards')
plt.title('Box and Whisker Plot of NFL Career Rushing Yards')

# Readability and Show Chart
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

# Calculate the total yards for the top 10 players
top_10_df = df.head(10)
total_yards = top_10_df['Yards'].sum()

# Create a pie chart showing the percentage of yards for the top 10 players
plt.figure(figsize=(8, 8))
plt.pie(top_10_df['Yards'], labels=top_10_df['Player'], autopct=lambda p: f'{p:.1f}% ({int(p * total_yards / 100):,d} yards)')
plt.title('Percentage of Yards for Top 10 NFL Career Rushing Yards Leaders')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Show the chart
plt.show()

# Save as CSV
df.to_csv('modifiedrb.csv', index =False)
# Save as Excel
df.to_excel('modifiedrb.xlsx', index=False)
# Save as Txt (tab-separated)
df.to_csv('modifiedrb.txt', index=False, sep='\t')

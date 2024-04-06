import pandas as pd
import pymysql
import streamlit as st
import plotly.express as px
import git

repo_url = "https://github.com/phonepe/pulse.git"
local_directory = "phonepe_pulse_repository"

# Initialize or clone the Git repository
repo = git.Repo(local_directory)
origin = repo.remote(name='origin')

try:
    origin.pull()
    print("Git pull successful")
except git.GitCommandError as e:
    print("Git pull failed:", e)

data_file = pd.read_csv('D:\Python_project\Guvi-Task2-main\Guvi-Task2-main\phonepe_pulse_repository/phonepe_pulse_data.csv')

data = data_file.dropna()

db_config = {
    "host": "localhost",
    "user": "root",
    "password": "suri123",
    "database": "phonepypulse",
}

# Establish a database connection
connection = pymysql.connect(**db_config)
cursor = connection.cursor()

# Insert the Pandas DataFrame into a MySQL table
data.to_sql("phonepypulse", connection, if_exists="replace", index=False, method='multi', chunksize=500)

# Commit the changes and close the connection
connection.commit()
connection.close()

st.title("Phonepe Pulse Data Dashboard")

# Add dropdown options for users to select different figures
selected_figure = st.selectbox("Select a Figure", ["Figure 1", "Figure 2", "Figure 3"])

# Display a bar chart using Plotly
if selected_figure == "Figure 1":
    # Create a sample bar chart
    fig = px.bar(data, x='Category', y='Value', title='Sample Bar Chart')
    st.plotly_chart(fig)











# # Load the data into a DataFrame (assuming it's in CSV format)
# data = pd.read_csv('path_to_cloned_repository/data.csv')

# # Perform data cleaning and transformation as needed
# # For example, handle missing values, data type conversions, etc.
# # Example:
# # data['Date'] = pd.to_datetime(data['Date'])
# # data.dropna(subset=['Value'], inplace=True)

# # Save the transformed data back to a CSV file or insert it into a database
# data.to_csv('transformed_data.csv', index=False)


# # Connect to the MySQL database
# conn = mysql.connector.connect(
#     host='your_database_host',
#     user='your_username',
#     password='your_password',
#     database='your_database_name'
# )

# # Create a Streamlit app
# st.title('PhonePe Pulse Data Explorer')

# # Sidebar filters
# st.sidebar.header('Filters')

# # Fetch data from the database
# query = "SELECT * FROM phonepe_data"
# data = pd.read_sql(query, conn)

# # Create interactive elements using Streamlit
# selected_start_date = st.sidebar.date_input('Start Date', data['Date'].min())
# selected_end_date = st.sidebar.date_input('End Date', data['Date'].max())
# chart_type = st.sidebar.selectbox('Select Chart Type', ['Line Chart', 'Bar Chart'])

# # Filter data based on user input
# filtered_data = data[(data['Date'] >= selected_start_date) & (data['Date'] <= selected_end_date)]

# # Display the filtered data
# st.write(f"Displaying data from {selected_start_date} to {selected_end_date}")
# st.write(filtered_data)

# # Create and display charts using Plotly
# st.header('Data Visualization')
# if chart_type == 'Line Chart':
#     fig = px.line(filtered_data, x='Date', y='Value', title='PhonePe Pulse Line Chart')
# elif chart_type == 'Bar Chart':
#     fig = px.bar(filtered_data, x='Date', y='Value', title='PhonePe Pulse Bar Chart')

# st.plotly_chart(fig)

# # Close the database connection
# conn.close()

# # Create a cursor object
# cursor = conn.cursor()

# # Insert data into the database (assuming you have a table 'phonepe_data')
# insert_query = "INSERT INTO phonepe_data (Date, Value) VALUES (%s, %s)"
# values_to_insert = [(row['Date'], row['Value']) for _, row in data.iterrows()]
 
# cursor.executemany(insert_query, values_to_insert)

# # Commit the changes and close the connection
# conn.commit()
# conn.close()

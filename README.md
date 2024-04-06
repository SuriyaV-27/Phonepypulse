# Phonepypulse


import pandas as pd
import mysql.connector
import streamlit as st
import plotly.express as px
import git
import mysql.connector

  These imports are used for our following code
 Then we Establish a database connection
 Then we Insert the Pandas DataFrame into a MySQL table (assuming the table is named "phonepe_pulse_data")
 we are Committing the changes and close the connection
 And Add dropdown options for users to select different figures
 After that we are Displaying a bar chart using Plotly

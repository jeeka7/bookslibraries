import streamlit as st
import pandas as pd

# Load the Google Sheets database into a pandas DataFrame
url = 'https://docs.google.com/spreadsheets/d/1xW-KOWkyjw5um3Tq6gYsvo00c1Q0pNDWJyr5K7JZPQU/edit#gid=0'
df = pd.read_csv(url)

# Set the Library ID column as the index
df.set_index('Library ID (Primary Key)', inplace=True)

# Streamlit app
def app():
    st.title("Library Database")
    st.write("Welcome to the Library Database!")

    # Show the data in a table
    st.write("Library Data:")
    st.dataframe(df)

    # Add new record
    st.subheader("Add New Record")
    library_id = st.text_input("Library ID")
    library_name = st.text_input("Library Name")
    due_date = st.text_input("Due Date")
    total_fine = st.text_input("Total Fine")
    add_button = st.button("Add Record")
    if add_button:
        # Append new record to the DataFrame
        new_record = pd.Series([library_name, due_date, total_fine],
                              index=['Library Name', 'Due Date', 'Total Fine'])
        df = df.append(new_record, name=library_id)
        # Update the Google Sheets database
        df.to_csv(url, index_label='Library ID (Primary Key)')
        st.success("Record added successfully!")

    # Delete record
    st.subheader("Delete Record")
    delete_id = st.text_input("Library ID to Delete")
    delete_button = st.button("Delete Record")
    if delete_button:
        if delete_id in df.index:
            # Remove record from the DataFrame
            df = df.drop(delete_id)
            # Update the Google Sheets database
            df.to_csv(url, index_label='Library ID (Primary Key)')
            st.success("Record deleted successfully!")
        else:
            st.warning("Library ID not found!")

if __name__ == '__main__':
    app()

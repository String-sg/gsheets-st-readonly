import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json  

def authenticate_gsheets():
    creds_json = st.secrets["gspread"]["google_credentials"]
    scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_dict(json.loads(creds_json), scope)
    client = gspread.authorize(creds)
    return client

def get_order_items_by_email(email, sheet):
    worksheet = sheet.worksheet('Sheet1')
    records = worksheet.get_all_records()
    
    for record in records:
        if record['Email'] == email:
            return record['Order items'].replace('\\n', '\n')  
    return "No record found for this email. Please try another email"

# Initialize Google Sheets client
client = authenticate_gsheets()
sheet = client.open('SST String Session Checker') 

def main():
    st.title('Tech Summit@SST Lab School 2024 Workshop Checker')
    email_input = st.text_input("Enter Email", "")

    if st.button("Check workshop venues"):
        order_items = get_order_items_by_email(email_input, sheet)
        if order_items:
            st.success(order_items)
        else:
            st.error("No items found for this email.")

if __name__ == "__main__":
    main()
    st.markdown(' Back to [SST Help](https://go.gov.sg/sstlab) | Created by [String](https://go.gov.sg/stringme), code for this checker available [here](https://github.com/String-sg/gsheets-st-readonly)')


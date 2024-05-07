import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json  # Add this import at the top

def authenticate_gsheets():
    creds_json = st.secrets["gspread"]["google_credentials"]
    scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_dict(json.loads(creds_json), scope)
    client = gspread.authorize(creds)
    return client

# Fetch order items by email
def get_order_items_by_email(email, sheet):
    worksheet = sheet.worksheet('Sheet1') 
    records = worksheet.get_all_records()
    
    for record in records:
        if record['Email'] == email:
            return record['Order items']
    return "No record found for this email."

# Initialize Google Sheets client
client = authenticate_gsheets()
sheet = client.open('SST String Session Checker') 

# Streamlit interface
def main():
    st.title('SST Lab School Session Checker')
    email_input = st.text_input("Enter Email:", "")

    if st.button("Get Order Items"):
        order_items = get_order_items_by_email(email_input, sheet)
        if order_items:
            st.success(order_items)
        else:
            st.error("No items found for this email.")

if __name__ == "__main__":
    main()

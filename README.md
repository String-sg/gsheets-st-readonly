# gsheets-st-readonly

Use Google Sheets as a backend to return a value using a query parameter of choice, hence readonly. 

Best to think of this as a key-value pair, though can be easily extended to do CRUD operations on gsheets as well.
<br>
Created for SST Tech Summit Lab School 2024, extendable to other use cases that uses a similar gsheets read-only setup
<br><br>
<img width="312" alt="image" src="https://github.com/String-sg/gsheets-st-readonly/assets/44336310/7eac8cef-c06d-4d8c-9215-b14583116f49">

## Try it [here](https://techsummitsst-string.streamlit.app/)

<hr>

### How it Works:

- Data Source: This app connects to a Google Sheet to retrieve information based on a user's email address.
- User Input: Educators pre-populate the sheet with relevant data (e.g., workshop venue details) linked to email addresses. Students can then enter their email to access their specific information.
- Output: Upon entering their email, students see their workshop venue details and potentially additional resources like maps.

### Code Structure
Here's a breakdown of the code structure:
**Import**s: These lines connect to necessary services like Google Sheets and configure the app's appearance.
- authenticate_gsheets (Hidden): This function (explained for reference, but educators won't need to touch it) establishes a secure connection to your Google Sheet.
- get_order_items_by_email (Hidden): This function retrieves information (workshop venue details in this example) from the Google Sheet based on the entered email address.
 main Function: This function controls the user interface.

**Branding (Optional)**: You can customize the app's look and feel using a separate branding.py file (not included here).
**Email Input**: Students enter their email address in a text box.
**"Check workshop venues"** Button: Clicking this button triggers the data retrieval process.
If a matching email is found, the workshop venue details are displayed along with two potentially helpful maps.
If no email match is found, an error message appears.

### How Educators Can Use This Boilerplate:

#### Set Up Google Sheet:
- Create a Google Sheet with the necessary information (e.g., email addresses and corresponding workshop venues).
- Share the sheet with the appropriate permissions level (view only is recommended).

#### Configure Credentials:
- In Streamlit, go to Settings > Secrets and create a new secret named "gspread".
- Paste your Google Service Account credentials (JSON format) into the value field. You can find instructions on creating these credentials https://developers.google.com/workspace/guides/create-credentials.

#### Update Sheet Information:
- Replace "SST String Session Checker" with the actual name of your Google Sheet.
- Modify the worksheet name ('Sheet1') if you're using a different sheet name.
- Update the data headers in your sheet to match the information you want to display (e.g., "Email" and "Workshop Venue").

#### Optional Branding:
- Create a separate branding.py file to customize the app's appearance (colors, logos, etc.).

#### Deploy the App:
- Save the code and upload it to a platform like Streamlit Cloud to make it accessible to students.

#### Benefits for Educators:
- Saves time by creating a reusable framework for retrieving information.
- Easy to maintain and update with new information.
- Provides a secure way for students to access their personalized data.

### Important Notes:
- Google Sheets as a rate limit that may cause it to crash at high volumes - even for 300 users, we crashed at an event (30 May) :')
- Remember to share the Google Sheet with view-only permissions to protect sensitive data.
- Consider adding a short instruction message at the app's launch explaining how to use it.
- By following these steps, educators with no coding experience can leverage Streamlit to create a user-friendly app for their students.

from google.oauth2.service_account import Credentials
import gspread
import pandas as pd
import smtplib
import time



def read_entire_gspread_sheet_to_pandas(credentials_file, sheet_id):

    scopes = ["https://www.googleapis.com/auth/spreadsheets.readonly"]
    creds = Credentials.from_service_account_file(credentials_file, scopes=scopes)
    client = gspread.authorize(creds)

    try:
        sheet = client.open_by_key(sheet_id).sheet1  

        values = sheet.get_all_values()
        if not values:
            return pd.DataFrame()  

        data = pd.DataFrame(values[1:], columns=values[0])  
        return data

    except Exception as e:
        print(f"An error occurred: {e}")
        return None  

    
def google_sheets_access():
    credentials_file = "cred_google_sheet.json"
    sheet_id = "1OjJeYEVsoDMVaI0X_absW2a8aSQBuLLDOEJ7uoUKk-M"

    df = read_entire_gspread_sheet_to_pandas(credentials_file, sheet_id)
    #display(df)

    if df is not None:
        
        df.columns = ["time", "model", "agents", "rag", "email", "send_copy","company", "description", "integration"]
        
        #display(df)
        recent_df = df.tail(1)
        
        model_req = str(recent_df["model"].values[0])
        tools_req = str(recent_df["agents"].values[0])
        email_req = str(recent_df["email"].values[0])
        company = str(recent_df["company"].values[0])
        description = str(recent_df["description"].values[0])
        integration = str(recent_df["integration"].values[0])
        print(company)
        
        
        return model_req, tools_req, email_req, company, description, integration
    else:
        print("Error reading the Google Sheet. Check credentials or sheet ID.")


    
def send_email(email_req, company, tools_req):
    #
    to = email_req
    subject = "Welcome to Up!"
    body = "Hello\nThank you for signing up for the Up! platform. You can access the application after signing up through the below link.\nhttps://tinyurl.com/Upbusiness \nRegards,\nTeam Up!"

    prompt = [to,subject,body]

    receiver_email=prompt[0]
    subject=prompt[1]
    message=prompt[2]


    email = 'saitanmai.r@gmail.com'
    text = f"Subject: {subject}\n\n{message}"
    server = smtplib.SMTP("smtp.gmail.com", 587) 
    server.starttls()
    server.login(email, "hcva lstk mcpe enir ")

    receiver_emails = receiver_email.split(', ')

    server.sendmail(email, receiver_emails, text)
    
    return "Email has been sent to " + str(receiver_emails) +f"\n {text}"
    



def controller():
    #
    model_req_last = ""
    tools_req_last = ""
    email_req_last = ""
    company_last = ""
    description_last = ""
    integration_last = ""
    #
    # while True:
        #
    model_req, tools_req, email_req, company, description, integration = google_sheets_access()

    if (model_req == model_req_last and tools_req == tools_req_last and email_req == email_req_last and company == company_last and description == description_last and integration == integration_last):
        print("already there, waiting")
        # time.sleep(2)
    else:
        #
        print("Variables don't match.")
        print(send_email(email_req, company, tools_req))
        model_req_last = model_req
        tools_req_last = tools_req
        email_req_last = email_req
        company_last = company
        description_last = description
        integration_last = integration

    
    
# controller()

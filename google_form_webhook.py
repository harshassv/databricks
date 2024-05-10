from flask import Flask, request
from google_form_email import *
import subprocess
import smtplib
import botUI_generator
import time

global company_name,email,current_port

def start_streamlit(file_name):
    global company_name,email,current_port
    # subprocess.Popen(["nohup", "streamlit", "run", file_name, "--server.port", str(port), "&"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # body = f"Hello {company_name},\nThank you for signing up for the Up! platform. You can access the application after signing up through the below link.\n http://http://54.196.123.8:{current_port}/ \nRegards,\nTeam Up!"
    # send_email(email,body)
    # with open("chatbots_db.txt", "a") as f:
    #     f.write("\n" + company_name)
    #     print('done updating chatbot')
    subprocess.Popen(["streamlit", "run", file_name, "--server.port", str(current_port)])

# ports = [8501,8502,8503]
# for port in ports:
#     start_streamlit(port)

def send_email(email_req, body, company = '', tools_req = ''):
    #
    to = email_req
    subject = "Welcome to Up!"
    body = body

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


app = Flask(__name__)

@app.route('/post_endpoint', methods=['POST'])
def post_handler():
    global company_name,email,current_port
    data = request.get_json()  # Get the JSON data from the POST request
    print("Received POST request with data:", data)
    # Here, you can perform any processing or logic with the received data
    # controller()
    email = data['email']
    company_name = data['Name of the Company?']

    with open('chatbots_db.txt', 'r') as f:
        lines = f.readlines()

    if company_name not in lines:

        with open('port_numbers_db.txt', 'r') as f:
            lines = f.readlines()
            if lines:
                last_port = lines[-1].strip()  # Strip any leading/trailing whitespace or newline characters
            else:
                return None  # File is empty
            
        current_port = int(last_port) + 1  # Increment the port number by 1

        source_file = 'Chat_template.py'  # Replace 'source_file.py' with the name of your source file
        destination_file = f'DUI_chat_{company_name}.py'
        replacements = {
                    "<SELECTED_TOOLS>": f"{data['Which Agents Should It Include?']}",  # Replace data.tools with the variable containing your tools data
                    "<SELECTED_INTEGRATIONS>": f"{data['Integration with existing environment']}",
                     "<SELECTED_USER>": f"{data['Name']}" # Replace data.integrations with the variable containing your integrations data
                }

        botUI_generator.duplicate_and_replace(source_file, destination_file, replacements)

        time.sleep(1)

        body = f"Hello {company_name},\nThank you for signing up for the Up! platform. You can access the application after signing up through the below link.\n http://http://54.196.123.8:{current_port}/ \nRegards,\nTeam Up!"
        send_email(email,body)

        
        with open("port_numbers_db.txt", "a") as f:
            f.write("\n" + str(current_port))
            print('done updating port number')

        with open("chatbots_db.txt", "a") as f:
            f.write("\n" + company_name)
            print('done updating chatbot')
            
        start_streamlit(destination_file)


    return "POST request received successfully!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Ru the Flask app on port 5000

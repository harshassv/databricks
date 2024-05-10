import streamlit as st
from dataclasses import dataclass
import sys
import os
sys.path.append('D:/CodePhilly')
sys.path.append('/home/ec2-user/square')
from PIL import Image
import OAuth_sq
from OAUth_access_token import square_access_token
import webbrowser
import back
import base64
import pangea.exceptions as pe
from pangea.config import PangeaConfig
from pangea.services import Redact
import pangea.exceptions as pe
from pangea.config import PangeaConfig
from pangea.services.authn.authn import AuthN
import webbrowser

import pandas as pd


@st.cache_data
def process_chat_input(chat_message,tool):
    tool=tool.strip()
    if tool=="General manager":
        response=back.O_LLM_gemini(chat_message)
    elif tool=="Email Manager":
        response=back.write_email(chat_message)
    elif tool=="Web Surfer":
        response=back.internet(chat_message)
    elif tool=="Report Analyst":
        response=back.generate_report(chat_message)
    elif tool=='Inventory Manager':
        response=back.Inventory_Management_Handler(chat_message)
    elif tool=='Catalogue Manager':
        response=back.Report_catalogue(chat_message)
        print("response: ",response)
        print(type(response))
    return response

@dataclass
class Message:
    actor: str
    payload: str

def check_images_in_folder():
    # Check if the folder exists
    folder_path = "/home/ec2-user/Images"
    if not os.path.isdir(folder_path):
        print(f"The directory '{folder_path}' does not exist.")
        return
    
    # List all files in the folder
    files = os.listdir(folder_path)
    
    # Check if there are any image files
    image_files = [file for file in files if any(file.endswith(ext) for ext in ['.jpg', '.jpeg', '.png', '.gif', '.bmp'])]
    
    if image_files:
        print("Images found in the folder:")
        for image_file in image_files:
            print(os.path.join(folder_path, image_file))
            print("image found in the folder: ",os.path.join(folder_path, image_file))
            return os.path.join(folder_path, image_file)
    else:
        print("No images found in the folder.")
    return None


def delete_files_in_directory():
    directory = "/home/ec2-user/Images"

    files = os.listdir(directory)
    
    for file in files:
        file_path = os.path.join(directory, file)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"Deleted {file_path}")
            else:
                print(f"{file_path} is not a file. Skipping.")
        except Exception as e:
            print(f"Failed to delete {file_path}: {e}")

def main(usr):
    # usr=st.session_state['usr']
    logo_path = "logo.png"

    st.sidebar.image(logo_path, use_column_width=True)
    st.markdown("""
    <style>
        .sidebar .sidebar-content {
            display: flex;
            flex-direction: column;
            align-items: center;
        }
    </style>
    """, unsafe_allow_html=True)

    # Add other sidebar elements
    st.sidebar.image("name1.jpg", use_column_width=True)
    st.sidebar.title('Welcome **'+usr+'**')
    list1 = <SELECTED_TOOLS>
    print(list(list1))
    btn=st.sidebar.selectbox('Choose what you want to work with',list1)
    btn=btn.strip()
    print(btn)
    if 'Square' in <SELECTED_INTEGRATIONS>:
        if 'sq_flag' not in st.session_state:
            st.session_state.sq_flag = True
        if 'sq_code' not in st.session_state and st.session_state.sq_flag==True:
            auth_url=OAuth_sq.url()
            # placeholder = st.empty()
            st.sidebar.write(f"[Connect to Square]({auth_url})")
            st.session_state.sq_flag=False
            # st.session_state.sq_code = st.query_params.get_all('code')[0]
            # st.write('Code: '+st.session_state.sq_code)
        # try:
        #     # square_access_token(st.session_state.sq_code)
        # except:
        #     pass
        if st.session_state.sq_flag:
            placeholder = st.empty()
    USER = "user"
    ASSISTANT = "ai"
    MESSAGES = "messages"

    if MESSAGES not in st.session_state:
        st.session_state[MESSAGES] = [Message(actor=ASSISTANT, payload="Hi! How can I help you?")]

    for msg in st.session_state[MESSAGES]:
        st.chat_message(msg.actor).write(msg.payload)
    prompt = st.chat_input("Ask a question!")
    
    if prompt:
        prompt=mask_with_redact(prompt)
        st.session_state[MESSAGES].append(Message(actor=USER, payload=prompt))
        st.chat_message(USER).write(prompt)
        response = process_chat_input(prompt,btn)
        print(btn,"   ",response)
        print(len(btn),"   ",len(response))
        if len(response)==3 and btn=='Inventory Manager':
            st.write('Old Data Frame')
            st.dataframe(response[0])
            st.write('Latest Data Frame')
            st.dataframe(response[1])
            st.session_state[MESSAGES].append(Message(actor=ASSISTANT, payload=response))
            st.chat_message(ASSISTANT).write(response[2])

            image_path = check_images_in_folder()
            print("IMAGE PATH is image_path: ", image_path)

            if image_path:
                try:
                    st.image(Image.open(image_path), caption='Image')
                    delete_files_in_directory()

                    
                except Exception as e:
                    print(e)

        elif btn=='Report Analyst' and response=='Report Generated':
            st.session_state[MESSAGES].append(Message(actor=ASSISTANT, payload=response))
            st.chat_message(ASSISTANT).write(response)
            print('Hi')
            file_path = '/home/ec2-user/Report_Vendor_gemini.pdf'
            try:
                print('Attempting to open file...')
                with open(file_path, "rb") as f:
                    print('File opened successfully.')
                    print('Encoding file to base64...')
                    base64_pdf = base64.b64encode(f.read()).decode('utf-8')
                    print('Base64 encoding successful.')
                    pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf">'
                    st.markdown(pdf_display, unsafe_allow_html=True)
            except FileNotFoundError:
                st.error(f"File '{file_path}' not found.")
            except Exception as e:
                st.error(f"An error occurred: {e}")
            #btn=='Catalogue Business Analyst'
        elif btn=='Catalogue Manager':
            st.session_state[MESSAGES].append(Message(actor=ASSISTANT, payload=response))
            st.chat_message(ASSISTANT).write(response)
        else:
            st.session_state[MESSAGES].append(Message(actor=ASSISTANT, payload=response))
            st.chat_message(ASSISTANT).write(response)
def get_user():
    import pangea.exceptions as pe
    from pangea.config import PangeaConfig
    from pangea.services.authn.authn import AuthN

    token = 'pts_z6txtdyt3dsrb7knrd233zhsjaobsrhh'
    domain = 'gcp.us.pangea.cloud'

    # Configure Pangea SDK with provided domain
    config = PangeaConfig(domain=domain)
    # Initialize the AuthN service with the token and configuration
    if st.session_state.usr_name is None:
        authn = AuthN(token, config=config, logger_name="pangea")
        usr = authn.client.userinfo(st.session_state.pangea_token)
        print("He;;p\n"+str(usr))
        usr= usr.raw_result['refresh_token']['profile']['first_name'] 
        st.session_state.usr_name=usr
    return st.session_state.usr_name

def mask_with_redact(prompt):
    token = "pts_z6txtdyt3dsrb7knrd233zhsjaobsrhh"
    domain = "gcp.us.pangea.cloud"
    config = PangeaConfig(domain=domain)
    redact = Redact(token, config=config)
    try:
        redact_response = redact.redact(text=prompt)
    except pe.PangeaAPIException as e:
        print(f"Embargo Request Error: {e.response.summary}")
        for err in e.errors:
            print(f"\t{err.detail} \n")
    return redact_response.result.redacted_text

if __name__ == "__main__":
        # if 'f' not in st.session_state:
        #     st.session_state.f=True
        # if 'sq_link' not in st.session_state:
        #     st.session_state.sq_link =
        #     print(st.session_state.c)
        # auth_url=OAuth.url()
        # if os.path.isfile('current_user.txt'):
        #     with open('current_user.txt', 'r') as f:
        #         usr=f.read()
        #         print(usr)
        usr = "<SELECTED_USER>"
        try:
            if 'pangea_code' not in st.session_state:
                pass
                # st.session_state.pangea_code = st.query_params.get_all('code')[0]
                # token = 'pts_z6txtdyt3dsrb7knrd233zhsjaobsrhh'
                # domain = 'gcp.us.pangea.cloud'
                # config = PangeaConfig(domain=domain)
                # if 'usr_name' not in st.session_state:
                #     authn = AuthN(token, config=config, logger_name="pangea")
                #     usr = authn.client.userinfo(st.session_state.pangea_code)
                #     usr=usr.raw_result['refresh_token']['profile']['first_name']
                #     with open('current_user.txt', 'w') as f:
                #         f.write(usr)
                #     print("He;;p\n"+str(usr))
                #     # st.session_state.usr= usr.raw_result['refresh_token']['profile']['first_name']
        except:
            pass
            # with open('current_user.txt', 'r') as f:
            #     usr=f.read()
            #     print(usr)
        main(usr)
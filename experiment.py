import re
import os
from datetime import datetime
from back import O_LLM,write_email,Inventory_Management_Handler

def get_current_datetime():
    now = datetime.today()
    formatted_datetime = now.strftime("%Y-%m-%d %H:%M:%S")
    return "Current date and time is " + formatted_datetime

def get_file_content(file_path):
    if os.path.isfile(file_path):
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    else:
        return None
    


def extract_actions_text(text):
    # Regular expression pattern to match the terms
    pattern = r"(Email\[[^\]]*\]|Reminder\[[^\]]*\]|Inventory\[[^\]]*\])"

    # Find all matches in the text
    matches = re.findall(pattern, text)

    # Return the first match found
    if matches:
        return matches[0]
    else:
        return None
    
    
def extract_square_brackets_text(text):
    pattern = r'\[find the best selling product\](.*?)\[/find the best selling product\]'
    match = re.search(pattern, text, re.DOTALL)
    if match:
        return match.group(1).strip()
    else:
        return None

out = ""

inventory_counter = 0

def email_function(argument):
    print("email function called: ",argument)
    write_email(argument)
    print("Email send I beleieve")


def inventory_function(argument):
    global out
    global inventory_counter

    if inventory_counter > 0:
        email_function(argument)

    print("Inventory function called: ",argument)
    df_old, new_df, out1 = Inventory_Management_Handler(argument)
    out1 = out1.replace('*','')
    out = f"Inventory[] Output: {out1}"
    print("Output from Inventory manager: ", out)
    inventory_counter = inventory_counter + 1



def reminder_function(argument):
    print("HJK function called: ",argument)


def tools_agents_handler(tools_called):
    print(tools_called)
    tools_called = tools_called.lower()
    if 'inventory' in tools_called:
        argument = tools_called.replace('inventory','')
#         argument = tools_called.replace('email','')
#         argument = tools_called.replace('@gmail.com','')
#         argument = tools_called.replace('mail.com','')
        argument = argument.replace('[','')
        argument = argument.replace(']','')
        out = inventory_function(argument)
        
    elif 'email' in tools_called:
        argument = tools_called.replace('email','')
        argument = argument.replace('[','')
        argument = argument.replace(']','')
        out = email_function(argument)
        
    elif 'reminder' in tools_called:
        argument = tools_called.replace('reminder','')
        argument = argument.replace('[','')
        argument = argument.replace(']','')
        out = reminder_function(argument)
    else:
        print("No matching function found")
        
#_______________________________________________________________________________
#START:

def Assistant(query_assitant):
    model = "gemini"

    current_datetime = get_current_datetime()
    scheduler_call_contents = query_assitant #get_file_content("Scheduler_call.txt")

    Prompt = f"""
    Consider yourself as a Workflow bot, And perform the task as mentioned.

    Tools Available: 
    Email[<user email adress>], Reminder[<Time>], Inventory[<Your questions>],

    Workflow: Send email reminder to the customer who booked their appointment if they didn't come on time.
    Context: 'Name: Mallana, Appointment time: 18:30:00, mallanna@gmail.com, Phone Number: +1 2656780980'
    Bot: Answer:  Reminder[18:30:00]


    Workflow: Send email reminder to the customer who booked their appointment
    Context: 'Name: Changa Reddy, Appointment time: 07:30:00, changa@gmail.com, Phone Number: +1 2656780980'
    Bot: Email[changa@gmail.com; Regarding your appointment today at 07:30:00.]


    Workflow: Check if New shop location added in the Inventory and send email to that local customers
    Context: New location added 'Philadelphia 12 Street' 
    Bot: Answer: Inventory[give me customer emails of only 'Philadelphia 12 Street']


    Time: {current_datetime}
    Task: Today {scheduler_call_contents}
    """

    bottom_prompt = """
    Give me your analysis.
    Bot:
    """


    print("---------------------------------------------------------------------------")
    current_datetime = get_current_datetime()
    print(current_datetime)

    scheduler_call_contents = get_file_content("Scheduler_call.txt")

    current_datetime = "14:35:00"

    print("\n")
    resp = O_LLM(f"{Prompt}{bottom_prompt}", "gemini")

    print(resp)
            
    #_______________________________________________________________________________
            
    tools_called = extract_actions_text(resp)
    print(tools_called)
    tools_agents_handler(tools_called)

    print(Prompt)

    bottom_prompt_tools = f"""
    Previous Tool performed by Bot and Output or Context from that tool: {out}
    Always write the tools you want to perform, you can only write 1 tool this time. whether its Inventory or Email or Reminder
    Bot:
    """

    print("\n")
    print("\n")
    print("Prompt:")
    print(f"{Prompt}{bottom_prompt_tools}")
    print("\n")

    print("-----------------------------CHeCKING------------------------------------------------------")
    resp = O_LLM(f"{Prompt}{bottom_prompt_tools}", "gpt3")
    print(resp)
    resp_need_send = f" {resp}{out}"
    print(resp_need_send)

    #------------------------------------------------------------------------------------------------------------

    tools_called = extract_actions_text(resp_need_send)
    print(tools_called)
    tools_agents_handler(tools_called)
    return f" {tools_called} \n\nTask Performed.."
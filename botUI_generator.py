import shutil

def duplicate_and_replace(source_file, destination_file, replacements):
    # Copy the source file to the destination file
    shutil.copyfile(source_file, destination_file)

    # Read the content of the destination file
    with open(destination_file, 'r') as file:
        file_content = file.read()

    # Replace the specified texts with the replacement texts
    for replace_text, replacement in replacements.items():
        print(f"Replacing '{replace_text}' with '{replacement}'")
        file_content = file_content.replace(replace_text, replacement)

    # Write the modified content back to the destination file
    with open(destination_file, 'w') as file:
        file.write(file_content)

# Example usage:
company_name = 'Harsha'
# data.tools = ['Catalogue Manager']
source_file = 'Chat_template.py'  # Replace 'source_file.py' with the name of your source file
destination_file = f'chat_{company_name}.py'  # Replace 'new_file.py' with the desired name for the duplicated file
replacements = {
    "<SELECTED_TOOLS>": "['Catalogue Manager']",  # Replace data.tools with the variable containing your tools data
    "<SELECTED_INTEGRATIONS>": "['Square'] " # Replace data.integrations with the variable containing your integrations data
}

# duplicate_and_replace(source_file, destination_file, replacements)

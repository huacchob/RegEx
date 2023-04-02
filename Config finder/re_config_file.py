import re
import json
import os

# regular expression
expression = r'interf[\w\d ]*\s*desc[\w -]*\s*ip[a-z ]*100[\d\. ]*\s*[\w -]*\s*[\w\. ]*'

# Directory name
dir = r'C:\Users\huacc\OneDrive\Documents\config'

# Files where the returned data will be stored in
new_files = ['mf1.txt', 'mf2.txt']

# For loop to read the files in the directory
for o_file in os.listdir(dir):
        # Open the files in the directory one at a time
        with open(os.path.join(dir, o_file), 'r', encoding='utf-8') as c_file:
            # Store the contents of the files in a variable
            contents = c_file.read()
            # Run the expression against the opened file
            result = re.findall(expression, contents, flags=re.IGNORECASE)
            # Make the returned data look pretty
            pretty = json.dumps(result, indent=4)
            # An if condition, if the files are already created in the directory, don't run the script
            if not new_files in os.listdir(dir):
                # Run a for loop through the new_files list
                for file_name in new_files:
                    # Create each file in the new_files list
                    with open(os.path.join(dir, file_name), 'w', encoding='utf-8') as new_n_files:
                        # Input the returned pretty data into the newly created files
                        new_n_files.write(pretty)
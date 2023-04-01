import re
import json
import os

expression = r'interf[\w\d ]*\s*desc[\w -]*\s*ip[a-z ]*100[\d\. ]*\s*[\w -]*\s*[\w\. ]*'
folder = r"C:\Users\huacc\OneDrive\Documents\config\\"

for filename in os.listdir(folder):
    file = open(os.path.join(folder, filename), "r", encoding="utf-8")
    contents = file.read()
    result = re.findall(expression, contents, flags=re.IGNORECASE)
    file.close()
    pretty = json.dumps(result, indent=4)
    output_filename = os.path.splitext(filename)[0] + '.txt'
    output_path = os.path.join(folder, output_filename)
    with open(output_path, 'w', encoding='utf-8') as output_file:
        output_file.write(str(pretty))
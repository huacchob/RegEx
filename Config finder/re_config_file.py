import re
import json

expression = r'interf[\w\d ]*\s*desc[\w -]*\s*ip[a-z ]*100[\d\. ]*\s*[\w -]*\s*[\w\. ]*'
folder = r"C:\Users\huacc\OneDrive\Documents\config\bakcahe-bsr1.config.log.txt"


file = open(r"C:\Users\huacc\OneDrive\Documents\config\bakcahe-bsr1.config.log.txt", 'r', encoding='utf-8')
contents = file.read()
result = re.findall(expression, contents, flags=re.IGNORECASE)
file.close()
pretty = json.dumps(result, indent=4)
mod_file = open(r"C:\Users\huacc\OneDrive\Documents\config\mf.txt", 'w', encoding='utf-8')
mod_file.write(pretty)
mod_file.close()
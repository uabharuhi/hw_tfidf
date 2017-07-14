import re

pattern = '[0-9]+[\t]+(.+)[\t]+[0-9]+'
p = re.compile(pattern)
m = p.search("\"1	theo walcott is still shit, watch rafa and johnny deal with him on saturday.	1\"")
content = m.group(1)
print(content)
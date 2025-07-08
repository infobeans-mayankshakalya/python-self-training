import re

str = """Error: This is an fatal1.
Error: This is an fatal2.
Error: This is an fatal3.
Error: This is fatal4.
Warning: This is warning1.
Info: This is information.
Error: """

result = re.search(r'Error:\W', str)
print(result)

result = re.findall(r'Error:\s{1}\w+', str)
print(result)

result = re.match(r'Error:', str)
print(result)

result = re.split(r'\d+', str)
print(result)
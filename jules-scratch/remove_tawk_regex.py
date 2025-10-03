import re

with open('services_optimized.html', 'r') as f:
    content = f.read()

# Remove the Tawk.to script block using a regular expression
content = re.sub(r'<!--Start of Tawk\.to Script-->.*?<!--End of Tawk\.to Script-->', '', content, flags=re.DOTALL)

with open('services_optimized.html', 'w') as f:
    f.write(content)
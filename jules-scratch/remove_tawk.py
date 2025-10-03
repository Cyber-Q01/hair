import re
from bs4 import BeautifulSoup

with open('services_optimized.html', 'r') as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, 'lxml')

# Find all script tags
for script in soup.find_all('script'):
    # Check if the script content contains 'Tawk.to'
    if script.string and 'Tawk.to' in script.string:
        script.decompose()

# Write the modified HTML back to the file
with open('services_optimized.html', 'w') as f:
    f.write(str(soup))

print("Tawk.to script removed successfully.")
from bs4 import BeautifulSoup

with open('services_optimized.html', 'r') as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, 'lxml')

# Find all image tags and remove them
for img in soup.find_all('img'):
    img.decompose()

# Write the modified HTML back to the file
with open('services_optimized.html', 'w') as f:
    f.write(str(soup))

print("All image tags removed successfully.")
from bs4 import BeautifulSoup

# Read the original HTML
with open('services.html', 'r') as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, 'lxml')

# Remove existing link tags
for link in soup.find_all('link', rel='stylesheet'):
    link.decompose()

# Read the extracted and cleaned CSS
with open('extracted_css.css', 'r') as f:
    cleaned_css = f.read()

# Create a new style tag and add the cleaned CSS
style_tag = soup.new_tag('style')
style_tag.string = cleaned_css
soup.head.append(style_tag)

# Write the modified HTML to the optimized file
with open('services_optimized.html', 'w') as f:
    f.write(str(soup))

print("Created services_optimized.html with cleaned and inlined CSS.")
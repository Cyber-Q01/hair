import tinycss2
import re

def should_keep_rule(rule, used_classes, used_ids):
    if rule.type == 'error':
        return False
    if rule.type == 'at-rule' and rule.at_keyword == 'font-face':
        return True

    prelude = tinycss2.serialize(rule.prelude)

    # Check for class selectors
    for class_name in used_classes:
        if '.' + class_name in prelude:
            return True

    # Check for ID selectors
    for id_name in used_ids:
        if '#' + id_name in prelude:
            return True

    return False

def remove_local_urls(css_text):
    # This regex will find url() declarations that do not start with http, https, or data:
    return re.sub(r'url\((?![\'"]?(?:http|https|data):)[\'"]?([^\'"\)]+)[\'"]?\)', '', css_text)

# Read used classes and IDs
with open('used_classes.txt', 'r') as f:
    used_classes = [line.strip() for line in f.readlines()]

with open('used_ids.txt', 'r') as f:
    used_ids = [line.strip() for line in f.readlines()]

css_files = [
    'assets/css/font-awesome-all.css',
    'assets/css/flaticon.css',
    'assets/css/owl.css',
    'assets/css/bootstrap.css',
    'assets/css/jquery.fancybox.min.css',
    'assets/css/animate.css',
    'assets/css/color.css',
    'assets/css/style.css',
    'assets/css/responsive.css'
]

extracted_css = []

for css_file in css_files:
    with open(css_file, 'r') as f:
        content = f.read()

    stylesheet = tinycss2.parse_stylesheet(content, skip_comments=True, skip_whitespace=True)

    for rule in stylesheet:
        if should_keep_rule(rule, used_classes, used_ids):
            cleaned_rule = remove_local_urls(rule.serialize())
            extracted_css.append(cleaned_rule)

with open('extracted_css.css', 'w') as f:
    f.write('\n'.join(extracted_css))

print("Extracted and cleaned CSS saved to extracted_css.css")
import os
import re
import json

# Define the directory to search for files
repo_dir = '/Users/gigisung/gigi_git/portfolio'

# Regular expression to match Markdown links
link_pattern = re.compile(r'\[([^\]]+)\]\(([^\)]+)\)')

# Function to extract links from a Markdown file
def extract_links_md(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        links = link_pattern.findall(content)
        return [(text, url) for text, url in links]

# Function to extract links from a Jupyter Notebook file
def extract_links_ipynb(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        notebook = json.load(file)
        links = []
        for cell in notebook.get('cells', []):
            if cell['cell_type'] == 'markdown':
                content = ''.join(cell['source'])
                links.extend(link_pattern.findall(content))
        return [(text, url) for text, url in links]

# Mapping of file extensions to their respective link extraction functions
extractors = {
    '.md': extract_links_md,
    '.qmd': extract_links_md,
    '.ipynb': extract_links_ipynb
}

# Iterate over all files in the repository
all_links = {}
for root, dirs, files in os.walk(repo_dir):
    for file in files:
        file_ext = os.path.splitext(file)[1]
        if file_ext in extractors:
            file_path = os.path.join(root, file)
            links = extractors[file_ext](file_path)
            if links:
                all_links[file_path] = links

# Print all extracted links
for file_path, links in all_links.items():
    print(f'Links in {file_path}:')
    for text, url in links:
        print(f'  - [{text}]({url})')
    print()

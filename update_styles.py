import os
import re

directory = '/home/nabhan-smma/dev/personal/weeding-invitation-template/src'

replacements = {
    r'bg-mulyo-cream': 'bg-surface',
    r'text-mulyo-charcoal': 'text-on-surface',
    r'text-mulyo-charcoal/([0-9]+)': r'text-on-surface/\1',
    r'bg-mulyo-charcoal': 'bg-inverse-surface',
    r'text-mulyo-cream': 'text-surface',
    r'text-mulyo-cream/([0-9]+)': r'text-surface/\1',
    r'mulyo-gold': 'primary',
    r'font-playfair': 'font-serif',
    r'from-mulyo-cream': 'from-surface',
    r'shadow-\[0_.*?rgba.*?\]': '', # remove standard shadows as per rule, we can leave the empty shadow or remove the class entirely
    r'shadow-\w+': '', # remove tailwind shadows
    r'border-mulyo-gold': 'border-outline-variant/30', # "Ghost Border"
    r'border-mulyo-gold/([0-9]+)': 'border-outline-variant/20',
    r'bg-mulyo-light': 'bg-surface-container-high'
}

for root, _, files in os.walk(directory):
    for file in files:
        if file.endswith('.vue') or file.endswith('.css'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r') as f:
                content = f.read()
            
            new_content = content
            for old, new in replacements.items():
                # We need to make sure we replace the text exactly. 
                # Specifically removing shadow classes entirely could leave extra spaces, but that's fine for HTML class attributes.
                if 'shadow' in old:
                    new_content = re.sub(old, '', new_content)
                else:
                    new_content = re.sub(old, new, new_content)
            
            # Clean up double spaces caused by shadow removals
            new_content = re.sub(r'\s{2,}', ' ', new_content).replace('=" ', '="').replace(' >', '>')
            
            if new_content != content:
                with open(filepath, 'w') as f:
                    f.write(new_content)
                print(f"Updated {filepath}")


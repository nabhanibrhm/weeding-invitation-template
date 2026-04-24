import os
import re

directory = '/home/nabhan-smma/dev/personal/weeding-invitation-template/src'

replacements = [
    (r'bg-mulyo-cream', 'bg-surface'),
    (r'text-mulyo-charcoal', 'text-on-surface'),
    (r'text-mulyo-charcoal/([0-9]+)', r'text-on-surface/\1'),
    (r'bg-mulyo-charcoal', 'bg-inverse-surface'),
    (r'text-mulyo-cream', 'text-surface'),
    (r'text-mulyo-cream/([0-9]+)', r'text-surface/\1'),
    (r'mulyo-gold', 'primary'),
    (r'font-playfair', 'font-serif'),
    (r'from-mulyo-cream', 'from-surface'),
    (r'shadow-\[0_.*?rgba.*?\]', ''),
    (r'shadow-\w+', ''),
    (r'border-mulyo-gold', 'border-outline-variant/30'),
    (r'border-mulyo-gold/([0-9]+)', 'border-outline-variant/20'),
    (r'bg-mulyo-light', 'bg-surface-container-high'),
    (r'border-mulyo-charcoal', 'border-outline-variant'),
    (r'bg-inverse-surface w-full h-1/2 flex items-end', r'bg-surface w-full h-1/2 flex items-end'),
    (r'bg-inverse-surface w-full h-1/2 flex items-start', r'bg-surface w-full h-1/2 flex items-start'),
    (r'border-b border-primary/20', r''),
    (r'border-t border-primary/20', r''),
    (r'bg-inverse-surface flex flex-col', r'bg-surface-container-low flex flex-col'),
    (r'text-white', r'text-on-surface'),
    (r'bg-transparent border border-outline-variant/30 text-primary', r'bg-primary-container text-on-primary-container rounded-lg border border-white/50 glass-panel'),
    (r'<div class="w-12 h-\[1px\] bg-primary mx-auto"></div>', r''),
    (r'border border-outline-variant/30', r''),
    (r'group-hover:translate', r''),
    (r'w-full md:w-5/12 flex flex-col items-center', r'w-full md:w-5/12 flex flex-col items-center glass-panel rounded-3xl p-8'),
    (r'<div class="h-px w-12 bg-outline-variant/20 self-center"></div>', r''),
    (r'<div class="h-px w-24 bg-gradient-to-r from-transparent via-outline-variant/20 to-transparent"></div>', r''),
    (r'<div class="w-full h-\[1px\] bg-primary/20 mb-6"></div>', r''),
    (r'bg-white ', r'glass-panel '),
    (r'rounded-2xl', r'rounded-3xl p-8'),
    (r'border border-gray-100', r'border-white/50'),
    (r'bg-inverse-surface', r'bg-primary text-on-primary rounded-lg'),
    (r'text-surface', r'text-on-primary'),
    (r'hover:bg-primary', r'hover:bg-primary-container hover:text-on-primary-container'),
    (r'border-gray-200', r'border-outline-variant'),
    (r'<div class="w-12 h-\[1px\] bg-primary mx-auto mb-12"></div>', r''),
    (r'bg-inverse-surface relative text-on-surface overflow-hidden', r'bg-surface-container relative text-on-surface overflow-hidden'),
    (r'bg-white/5', r'glass-panel'),
    (r'border-outline-variant/30', r'border-white/50'),
    (r'<div class="w-\[1px\] h-16 bg-primary mt-6 mb-6 mx-auto"></div>', r'')
]

for root, _, files in os.walk(directory):
    for file in files:
        if file.endswith('.vue'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r') as f:
                content = f.read()
            
            new_content = content
            for old, new in replacements:
                if 'shadow' in old:
                    new_content = re.sub(old, '', new_content)
                else:
                    new_content = re.sub(old, new, new_content)
            
            # Safer space cleanup
            new_content = re.sub(r'[ \t]{2,}', ' ', new_content)
            
            if new_content != content:
                with open(filepath, 'w') as f:
                    f.write(new_content)
                print(f"Updated {filepath}")

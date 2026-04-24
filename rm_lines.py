import os
import re

def update_file(filepath, replacements):
    with open(filepath, 'r') as f:
        content = f.read()
    new_content = content
    for old, new in replacements:
        new_content = re.sub(old, new, new_content)
    if new_content != content:
        with open(filepath, 'w') as f:
            f.write(new_content)
        print(f"Updated {filepath}")

update_file('/home/nabhan-smma/dev/personal/weeding-invitation-template/src/components/EventDetails.vue', [
    (r'<div class="w-full h-\[1px\] bg-primary/20 mb-6"></div>', r'')
])
update_file('/home/nabhan-smma/dev/personal/weeding-invitation-template/src/components/HeroSection.vue', [
    (r'<div class="w-\[1px\] h-16 bg-primary mt-6 mb-6 mx-auto"></div>', r'')
])

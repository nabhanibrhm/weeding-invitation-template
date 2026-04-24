import os
import re

filepath = '/home/nabhan-smma/dev/personal/weeding-invitation-template/src/components/RSVPForm.vue'
with open(filepath, 'r') as f:
    content = f.read()

new_content = re.sub(r'border-mulyo-charcoal', 'border-outline-variant', content)

with open(filepath, 'w') as f:
    f.write(new_content)


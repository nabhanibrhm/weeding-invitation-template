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

# App.vue
app_replacements = [
    (r'bg-inverse-surface w-full h-1/2 flex items-end', r'bg-surface w-full h-1/2 flex items-end'),
    (r'bg-inverse-surface w-full h-1/2 flex items-start', r'bg-surface w-full h-1/2 flex items-start'),
    (r'border-b border-primary/20', r''),
    (r'border-t border-primary/20', r''),
    (r'bg-inverse-surface flex flex-col', r'bg-surface-container-low flex flex-col'),
    (r'text-white', r'text-on-surface'),
    (r'bg-transparent border border-primary text-primary', r'bg-primary-container text-on-primary-container rounded-lg border border-white/50 glass-panel')
]
update_file('/home/nabhan-smma/dev/personal/weeding-invitation-template/src/App.vue', app_replacements)

# CoupleSection.vue
couple_replacements = [
    (r'<div class="w-12 h-\[1px\] bg-primary mx-auto"></div>', r''), # remove divider
    (r'border border-outline-variant/30', r''), # remove borders
    (r'group-hover:translate', r''), # remove translate border effect
    (r'w-full md:w-5/12 flex flex-col items-center', r'w-full md:w-5/12 flex flex-col items-center glass-panel rounded-3xl p-8'),
]
update_file('/home/nabhan-smma/dev/personal/weeding-invitation-template/src/components/CoupleSection.vue', couple_replacements)

# QuoteSection.vue
quote_replacements = [
    (r'<div class="h-px w-12 bg-outline-variant/20 self-center"></div>', r''),
    (r'<div class="h-px w-24 bg-gradient-to-r from-transparent via-outline-variant/20 to-transparent"></div>', r'')
]
update_file('/home/nabhan-smma/dev/personal/weeding-invitation-template/src/components/QuoteSection.vue', quote_replacements)

# EventDetails.vue
event_replacements = [
    (r'<div class="w-12 h-\[1px\] bg-primary mx-auto"></div>', r''),
    (r'bg-white', r'glass-panel'),
    (r'rounded-2xl', r'rounded-3xl p-8'),
    (r'border border-gray-100', r'border-white/50')
]
update_file('/home/nabhan-smma/dev/personal/weeding-invitation-template/src/components/EventDetails.vue', event_replacements)

# RSVPForm.vue
rsvp_replacements = [
    (r'bg-white', r'glass-panel'),
    (r'border border-gray-100', r'border-white/50'),
    (r'rounded-2xl', r'rounded-3xl'),
    (r'bg-inverse-surface', r'bg-primary text-on-primary rounded-lg'),
    (r'text-surface', r'text-on-primary'),
    (r'hover:bg-primary', r'hover:bg-primary-container hover:text-on-primary-container'),
    (r'border-gray-200', r'border-outline-variant'),
    (r'border-primary', r'border-primary')
]
update_file('/home/nabhan-smma/dev/personal/weeding-invitation-template/src/components/RSVPForm.vue', rsvp_replacements)

# GiftSection.vue
gift_replacements = [
    (r'bg-white', r'glass-panel'),
    (r'border border-gray-100', r'border-white/50'),
    (r'rounded-2xl', r'rounded-3xl p-8'),
    (r'<div class="w-12 h-\[1px\] bg-primary mx-auto mb-12"></div>', r'')
]
update_file('/home/nabhan-smma/dev/personal/weeding-invitation-template/src/components/GiftSection.vue', gift_replacements)

# CountdownTimer.vue
countdown_replacements = [
    (r'bg-inverse-surface', r'bg-surface-container'),
    (r'text-surface', r'text-on-surface'),
    (r'bg-white/5', r'glass-panel'),
    (r'border-outline-variant/30', r'border-white/50')
]
update_file('/home/nabhan-smma/dev/personal/weeding-invitation-template/src/components/CountdownTimer.vue', countdown_replacements)


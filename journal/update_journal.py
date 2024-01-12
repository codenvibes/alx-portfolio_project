#!/usr/bin/python3
# AUTH: codenvibes
"""
This script appends a new entry template to `journal.md` with the
current date.

The formatted section includes a collapsible section (using HTML details/
summary tags) titled with the current date in the format "DAY 1 : DD MMM YYYY"
. Inside the collapsible section, there is a centered message.

The script uses the datetime module to get the current date and time in the
"DD MMM YYYY" format (e.g., 12 Jan 2024). It then appends the formatted
section to the `journal.md` file.

Example:
    Running this script on 12 Jan 2024 will append the following section to
    `journal.md`:

    <details>
    <summary><b>DAY 1 : 12 Jan 2024</b></summary><br>


    <br><p align="center">※※※※※※※※※※※※</p><br>
    </details>
"""
from datetime import datetime

# Get the current date
current_date = datetime.now().strftime("%d %b %Y")

# Format the section with the current date
section_to_append = f"""


<details>
<summary><b>DAY 1 - {current_date}</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>
"""

# Append the section to the journal.md file
with open('journal.md', 'a') as file:
    file.write(section_to_append)

print("New section appended to journal.md")

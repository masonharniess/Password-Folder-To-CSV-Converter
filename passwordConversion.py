import os
import csv
import re

directory_path = 'example files'
csv_file_path = 'login_details.csv'
csv_header = ['folder', 'favorite', 'type', 'name', 'notes', 'fields', 'reprompt', 'login_uri', 'login_username',
              'login_password', 'login_totp']

with open(csv_file_path, 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(csv_header)

    for filename in os.listdir(directory_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(directory_path, filename)
            login_details = dict.fromkeys(csv_header, '')
            login_details['name'] = filename[:-4]

            next_is_email = False
            next_is_password = False

            with open(file_path, 'r') as file:
                for line in file:
                    line = line.strip()
                    email_re = re.compile(r'email\s*[:\-]\s*', re.I)
                    password_re = re.compile(r'password\s*[:\-]\s*', re.I)

                    if next_is_email:
                        login_details['login_username'] = line
                        next_is_email = False
                        continue

                    if next_is_password:
                        login_details['login_password'] = line
                        next_is_password = False
                        continue

                    email_match = email_re.match(line)
                    if email_match:
                        email_value = line[email_match.end():].strip()
                        if email_value:
                            login_details['login_username'] = email_value
                        else:
                            next_is_email = True
                        continue

                    password_match = password_re.match(line)
                    if password_match:
                        password_value = line[password_match.end():].strip()
                        if password_value:
                            login_details['login_password'] = password_value
                        else:
                            next_is_password = True
                        continue

            if not login_details['login_username'] or not login_details['login_password']:
                print(f"Warning: '{filename}' is missing necessary information.")
            else:
                writer.writerow([login_details[key] for key in csv_header])

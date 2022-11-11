# QUESTION: The Fender, a notorious computer hacker and general villain of the people, has compromised several top-secret passwords including your own. 
# Your mission, should you choose to accept it, is threefold. You must acquire access to The Fender‘s systems, you must update his "passwords.txt" file to scramble the secret data. The last thing you need to do is add the signature of Slash Null, a different hacker whose nefarious deeds could be very conveniently halted by The Fender if they viewed Slash Null as a threat.

# Import all necessary modules
import csv
import json

compromised_users = []

with open('passwords.csv') as password_file:
  password_csv = csv.DictReader(password_file)
  for password_row in password_csv:
    #print(password_row['Username'])
    compromised_users.append(password_row['Username'])
#print(compromised_users)

with open('compromised_users.txt', 'w') as compromised_user_file:
  for compromised_user in compromised_users:
    compromised_user_file.write(compromised_user)

with open('boss_message.json', 'w') as boss_message:
  boss_message_dict = {
    "recipient": "The Boss",
    "message": "Mission Success"
  }
  json.dump(boss_message_dict, boss_message)

with open('new_passwords.csv', 'w') as new_passwords_obj:
  slash_null_sig = """U GOT SLASHED - SLASH NULL"""
  new_passwords_obj.write(slash_null_sig)

print(slash_null_sig)

## Password Checker
This pass word checker app checks your password against a database of compromised passwords.

This app does not save your password or send your password to any external API.

Your password is hashed, and then only the first 5 characters of your hash are sent to the pawned_passwords API to get
back potential matches. Then we check if any of those matches match your hashed password.

### To Run:

Have these packages installed:
-  `pip3 install requests`

From terminal:
- `python3 checkpass.py {your_pass_here}`

You can enter as many passwords as you wish.
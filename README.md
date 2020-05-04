## Password Checker
This pass word checker app checks your password against a database of compromised passwords.

This app does not save your password or send your password to any external API.

Your password is hashed, and then only the first 5 characters of your hash are sent to the pawned_passwords API to get
back potential matches. Then we check if any of those matches match your hashed password.

### To Run:

Have these packages installed:
-  `pip3 install requests`
- `pip3 install flask`

Environment
- In your .zshrc or similar, set `FLASK_APP=server.py`

From terminal:
- Make sure you cd into the root folder and run `flask run`

You can test out the app on port 5000 through postman or similar app!
Make sure your input matches `{ "password": {YOUR_PASSWORD} }`
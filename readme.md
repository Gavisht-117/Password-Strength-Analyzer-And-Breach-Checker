## Password Strength Analyzer & Breach Checker

## What does it do?
This project analyzes the strength of your password and gives a score out of 5.
It also checks if your password has ever been breached before so you can use a password that is more secure.

## How does it work?
This works using the HaveIBeenPwned API to check if your password has been breached before by using hashes so they never actually know what is your password. The API only takes the first 5 letters of your password after it has been hashed using SHA-1 algorithm.The API matches all hashes that matches with the first 5 letters of the given hash.The remaining part of the hash is then compared locally on your machine to check if your password appears in the returned list, meaning your full password or full hash never leaves your device.

## How to run?
Its simple just go to "main.py" and run the code and enter your password.

## How is the strength analyzed?
The strength is incremented based on certain 5 parameters:-length,uppercase,lowercase,special characters,digits.Say if your password was "sty2" your strength would be 2/5 because only lowecase and a digit is used.

## What I learned through this project?
I learned how API calling works,k-anonymity, SHA-1 algorithm and why we dont use SHA-2/3 to fetch hashes for API as most passwords were breached when SHA-1 was used mostly everywhere and SHA-2/3 has better algorithm which makes breaching uncommon than before therefore having lower sample space.

## Technologies Used:-
Python 3,HaveIBeenPwned API,requests library
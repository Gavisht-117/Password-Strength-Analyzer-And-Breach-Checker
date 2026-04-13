import checker
import strength
#D:\python\python.exe "d:\VS CODE FOLDER\PasswordStrength\main.py"
password=input("Enter your password: ")
score=strength.check_strength(password)
print(f"Password Strength is: {score}/5")
checker.check_breach(password)
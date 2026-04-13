import re
def check_strength(password):
   strength=0
   if(len(password)>=8):
      strength=strength+1
   for c in password:
      if(c>='A' and c<='Z'):
         strength=strength+1
         break
   for c in password:
      if(c>='a' and c<='z'):
         strength=strength+1
         break
   for c in password:
      if(c>='0' and c<='9'):
         strength=strength+1
         break
   
      if re.search(r'[!@#$%^&*]', password):
         strength=strength+1
         

   return strength



    
      
   

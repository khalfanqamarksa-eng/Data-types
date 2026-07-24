import random
import string
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase  
digits = string.digits 

all_chars = lowercase + uppercase + digits

pass_list = [
    random.choice(lowercase),
    random.choice(uppercase),
    random.choice(digits)
]

for i in range(9):
    pass_list.append(random.choice(all_chars))

random.shuffle(pass_list)

password = "".join(pass_list)

print("Generated Password:", password)
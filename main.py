email = input("Enter your mail address\n").strip()

user_name = email[:email.index("@")]

user_domain = email[email.index("@"):]

print(user_name)
user_domain =  user_domain.replace("@", "")

print(user_domain.replace(".com", ""))
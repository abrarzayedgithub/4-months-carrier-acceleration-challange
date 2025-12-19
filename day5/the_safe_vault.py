user = {"id": 1}
email = user.get("email")
print(email) 
email = user.get("email", "error")
print(email) 
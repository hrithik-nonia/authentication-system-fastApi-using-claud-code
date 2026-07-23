from app.security.password_handler import hash_password, verify_password

plain = "Test@1234"
hashed = hash_password(plain)

print("Hashed:", hashed)
print("Verify correct password:", verify_password("Test@1234", hashed))  # True
print("Verify wrong password:", verify_password("Wrong@123", hashed))    # False
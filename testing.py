from app.security.jwt_handler import create_access_token, create_refresh_token, decode_token
import time

# Token banao
access_token = create_access_token({"sub": "12345", "role": "user"})
print("Access Token:", access_token)

# Decode karo
payload = decode_token(access_token)
print("Decoded Payload:", payload)

# jwt.io pe jaake bhi paste karke dekh sakte ho (payload readable hai!)

# Invalid/tampered token test
fake_token = access_token[:-5] + "XXXXX"  # signature tamper kar diya
result = decode_token(fake_token)
print("Tampered token result:", result)  # None aana chahiye
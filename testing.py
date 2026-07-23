from app.schemas.user_schema import UserCreate

# Valid data
user = UserCreate(name="Hrithik", email="hrithik@gmail.com", password="Test@1234")
print(user)

# Invalid email test
try:
    bad_user = UserCreate(name="Test", email="abc@gmail.com", password="Test@1234")
except Exception as e:
    print("Validation Error:", e)
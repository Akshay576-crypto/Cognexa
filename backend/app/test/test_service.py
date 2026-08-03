from app.services.user_services import UserServices

service = UserServices()

# -----------------------------
# Test Registration
# -----------------------------

response = service.register_user(
    full_name="Akshay Sapariya",
    email="akshay@gmail.com",
    password="OmniMind123"
)

print("REGISTER RESPONSE")
print(response)

print("-" * 50)

# -----------------------------
# Test Login
# -----------------------------

response = service.login_user(
    email="akshay@gmail.com",
    password="OmniMind123"
)

print("LOGIN RESPONSE")
print(response)
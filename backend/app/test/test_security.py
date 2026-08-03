from app.core.security import (
    hash_password,
    verify_password,
    create_access_token,
    verify_token
)

password = "OmniMind123"

# Hash Password
hashed_password = hash_password(password)

print("Original Password:", password)
print("Hashed Password:", hashed_password)

# Verify Password
is_valid = verify_password(password, hashed_password)
print("Password Verified:", is_valid)

# Create JWT
token = create_access_token({"sub": "akshay@gmail.com"})
print("JWT Token:", token)

# Verify JWT
payload = verify_token(token)
print("Decoded Payload:", payload)
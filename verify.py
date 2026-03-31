import json
import hashlib

# Password hash function (same as app.py)
def hash_pw(pw):
    return hashlib.sha256((pw + 'SPARSHHOSTING_salt_v4').encode()).hexdigest()

# Load users file
with open('users.json', 'r') as f:
    users = json.load(f)

# Find admin user and update password
for uid, user in users.items():
    if user['username'] == 'admin':
        # Update password to match new hash
        user['password'] = hash_pw('Admin@2024!')
        print(f"✅ Updated password for admin user")
        print(f"New hash: {user['password']}")
        break
else:
    print("❌ Admin user not found!")

# Save back
with open('users.json', 'w') as f:
    json.dump(users, f, indent=2)

print("\n✅ Done! Now try login with:")
print("Username: admin")
print("Password: Admin@2024!")

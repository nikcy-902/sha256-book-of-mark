from sha256 import sha256
import hashlib

with open('book_of_mark.txt', 'r', encoding='utf-8') as f:
    text = f.read()

my_hash = sha256(text)
verify_hash = hashlib.sha256(text.encode()).hexdigest()

print("Book of Mark SHA-256 Hash:")
print(my_hash)
print()
print("Verification (hashlib):", verify_hash)
print("Match:", my_hash == verify_hash)

# Save to file
with open('output.txt', 'w') as f:
    f.write(f"SHA-256 Hash: {my_hash}\n")
    f.write(f"Verified: {my_hash == verify_hash}\n")

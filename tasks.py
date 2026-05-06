#3
n=int(input("n="))
list=[]
m=0
l=0
while(l<=100):
        print(l)
        print(m)
        print(n)
        l=n*m
        list.append(l)
        m+=1
        
        
print(list)

#4 caeser cipher

def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    
    # Adjust shift for decryption
    if mode == 'decrypt':
        shift = -shift
        
    for char in text:
        if char.isalpha():
            # Determine if uppercase or lowercase start point
            start = ord('A') if char.isupper() else ord('a')
            
            # Calculate the new character position
            # Formula: (Original Position + Shift - Start) % 26 + Start
            new_char = chr((ord(char) + shift - start) % 26 + start)
            result += new_char
        else:
            # Keep punctuation and spaces as they are
            result += char
            
    return result

# --- Example Usage ---
message = "Hello, World!"
shift_value = 4

encrypted = caesar_cipher(message, shift_value, mode='encrypt')
decrypted = caesar_cipher(encrypted, shift_value, mode='decrypt')

print(f"Original:  {message}")
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")
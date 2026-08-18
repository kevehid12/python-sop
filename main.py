import hashlib
import random
import string
import time
import requests

def matrix_print(text, delay=0.01):
    """Prints text with a subtle cyber aesthetic."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def print_banner():
    print("\033[92m" + "="*65)
    print("  ╔═══════════════════════════════════════════════════════════╗")
    print("  ║        P Y T H O N   S E C U R I T Y   M A T R I X          ║")
    print("  ║          Password Strength & Live Breach Analyzer         ║")
    print("  ╚═══════════════════════════════════════════════════════════╝")
    print("="*65 + "\033[0m")

def check_pwned_database(password):
    """
    Checks if a password has appeared in known data breaches 
    using the Have I Been Pwned API via k-anonymity.
    Your plaintext password never leaves your computer.
    """
    sha1_hash = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    prefix = sha1_hash[:5]
    suffix = sha1_hash[5:]

    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code != 200:
            print("\033[93m⚠️ Could not connect to the breach database (API error).\033[0m")
            return None
        
        for line in response.text.splitlines():
            hash_suffix, count = line.split(":")
            if hash_suffix == suffix:
                return int(count)
                
        return 0
        
    except requests.RequestException:
        print("\033[91m⚠️ Network error while checking breach database.\033[0m")
        return None

def check_password_strength(password):
    """
    Evaluates password strength based on length, uppercase, 
    lowercase, digits, special characters, and live breach data.
    """
    score = 0
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in string.punctuation:
            has_special = True

    if has_upper: score += 1
    if has_lower: score += 1
    if has_digit: score += 1
    if has_special: score += 1

    print("\n\033[92m[+] Analyzing cipher and querying neural database...\033[0m")
    time.sleep(0.5)
    
    breach_count = check_pwned_database(password)

    print("\n\033[96m" + "═"*45)
    print("       SECURE TERMINAL EVALUATION REPORT       ")
    print("═"*45 + "\033[0m")
    print(f"[*] Length: {len(password)} characters")
    print(f"[*] Uppercase: {has_upper}")
    print(f"[*] Lowercase: {has_lower}")
    print(f"[*] Numbers: {has_digit}")
    print(f"[*] Special Symbols: {has_special}")

    if breach_count is not None:
        if breach_count > 0:
            print(f"\033[91m[!] ALERT: Found in {breach_count:,} public data breaches!\033[0m")
            rating = "Extremely Vulnerable ❌ [COMPROMISED]"
        else:
            print("\033[92m[+] Status: Clean! Zero matches in known breach logs.\033[0m")
            if score <= 3:
                rating = "Weak ❌ [Easily Decoded]"
            elif score <= 5:
                rating = "Moderate ⚠️ [Requires Hardening]"
            else:
                rating = "Strong / Excellent ✅ [Matrix Secure]"
    else:
        if score <= 3:
            rating = "Weak ❌"
        elif score <= 5:
            rating = "Moderate ⚠️"
        else:
            rating = "Strong / Excellent ✅"

    print(f"\033[1m[>] Overall Rating: {rating}\033[0m\n" + "─"*45 + "\n")

def generate_secure_password(length):
    """
    Generates a cryptographically randomized password 
    incorporating letters, digits, and punctuation symbols.
    """
    char_pool = string.ascii_letters + string.digits + string.punctuation
    secure_password = "".join(random.choice(char_pool) for _ in range(length))
    
    print("\n\033[92m" + "═"*45)
    print("          CRYPTOGRAPHIC KEY GENERATOR          ")
    print("═"*45 + "\033[0m")
    print(f"[+] Generated Key: \033[1;33m{secure_password}\033[0m")
    print("═"*45 + "\n")

def main():
    print_banner()
    
    while True:
        print("\033[94m[MATRIX ACCESS PORTAL]\033[0m")
        print("  1. Run Password Strength & Breach Audit")
        print("  2. Generate Cryptographic Secure Key")
        print("  3. Disconnect / Exit")
        
        choice = input("\nSelect protocol [1-3]: ").strip()
        
        if choice == '1':
            user_input = input("Enter target password for audit: ")
            check_password_strength(user_input)
            
        elif choice == '2':
            try:
                length_input = int(input("Enter key length (minimum 8): "))
                if length_input < 8:
                    print("\033[93m⚠️ Sub-optimal length detected. Automatically adjusting to 8.\033[0m")
                    length_input = 8
                generate_secure_password(length_input)
            except ValueError:
                print("\033[91m❌ Error: Invalid numeric input.\033[0m\n")
                
        elif choice == '3':
            matrix_print("\n[!] Disconnecting from Matrix terminal. Goodbye, operator.")
            break
            
        else:
            print("\033[91m❌ Invalid selection. Choose 1, 2, or 3.\033[0m\n")

if __name__ == "__main__":
    main()

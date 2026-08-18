import hashlib
import random
import string
import time
import requests

def matrix_boot_sequence():
    intro_lines = [
        "Wake up, operator...",
        "The Matrix has you.",
        "Follow the white rabbit.",
        "Knock, knock, Neo."
    ]
    for line in intro_lines:
        print(f"\033[92m{line}\033[0m")
        time.sleep(0.6)
    
    print("\n\033[32m[ Decrypting Nebuchadnezzar Mainframe... ]\033[0m")
    time.sleep(0.8)
    
    chars = "01$#X@%&Z*~+-/\\|ｦｱｳｴｵｶｷｹｺｻｼｽｾｿﾀﾂﾅﾆﾇﾈﾊﾋﾎﾏﾐﾑﾒﾓﾔﾕﾗﾘﾜ"
    for _ in range(4):
        rain_line = "".join(random.choice(chars) for _ in range(70))
        print(f"\033[32m{rain_line}\033[0m")
        time.sleep(0.05)
    print("\n")

def print_movie_banner():
    print("\033[1;32m" + "═" * 70)
    print("  ╔══════════════════════════════════════════════════════════════════╗")
    print("  ║        SYSTEM FAILURE // CONSTRUCT LOADING: SECURE CIPHER        ║")
    print("  ╚══════════════════════════════════════════════════════════════════╝")
    print("═" * 70 + "\033[0m")

def check_pwned_database(password):
    sha1_hash = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    prefix = sha1_hash[:5]
    suffix = sha1_hash[5:]

    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code != 200:
            print("\033[93m[!] WARNING: Zion mainframe connection unstable.\033[0m")
            return None
        
        for line in response.text.splitlines():
            hash_suffix, count = line.split(":")
            if hash_suffix == suffix:
                return int(count)
                
        return 0
        
    except requests.RequestException:
        print("\033[91m[!] ERROR: Agent interference detected on network line.\033[0m")
        return None

def check_password_strength(password):
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

    print("\n\033[32m[i] Bending the rules... scanning neural archives...\033[0m")
    time.sleep(0.5)
    breach_count = check_pwned_database(password)

    print("\n\033[32m╔════════════════════════ THE ORACLE'S REPORT ═════════════════════╗\033[0m")
    print(f"\033[32m║\033[0m  Cipher Length          : \033[1;32m{len(password):<36}\033[0m\033[32m ║\033[0m")
    print(f"\033[32m║\033[0m  Uppercase [A-Z]        : \033[1;32m{str(has_upper):<36}\033[0m\033[32m ║\033[0m")
    print(f"\033[32m║\033[0m  Lowercase [a-z]        : \033[1;32m{str(has_lower):<36}\033[0m\033[32m ║\033[0m")
    print(f"\033[32m║\033[0m  Numeric Digits [0-9]   : \033[1;32m{str(has_digit):<36}\033[0m\033[32m ║\033[0m")
    print(f"\033[32m║\033[0m  Special Symbols        : \033[1;32m{str(has_special):<36}\033[0m\033[32m ║\033[0m")
    print("\033[32m╠════════════════════════════════════════════════════════════════════╣\033[0m")

    if breach_count is not None:
        if breach_count > 0:
            print(f"\033[91m║  [!] AGENT ALERT        : Compromised in {breach_count:,} leaks!     ║\033[0m")
            rating = "Flawed ❌ [Agents Have Access]"
        else:
            print("\033[32m║  [+] Construct Status   : SECURE (Untraced by Agents)        ║\033[0m")
            if score <= 3:
                rating = "Weak ❌ [Easy to Hack]"
            elif score <= 5:
                rating = "Moderate ⚠️ [Needs Hardening]"
            else:
                rating = "The One ✅ [Unbreakable Cipher]"
    else:
        if score <= 3:
            rating = "Weak ❌"
        elif score <= 5:
            rating = "Moderate ⚠️"
        else:
            rating = "The One ✅"

    print(f"\033[32m║\033[0m  Overall Evaluation     : \033[1;32m{rating:<36}\033[0m\033[32m ║\033[0m")
    print("\033[32m╚════════════════════════════════════════════════════════════════════╝\033[0m\n")

def generate_secure_password(length):
    char_pool = string.ascii_letters + string.digits + string.punctuation
    secure_password = "".join(random.choice(char_pool) for _ in range(length))
    
    print("\n\033[32m[i] Generating weaponized encryption key...\033[0m")
    time.sleep(0.4)
    
    print("\n\033[32m╔═════════════════════ ZION KEY GENERATOR ═══════════════════════════╗\033[0m")
    print(f"\033[32m║\033[0m  Generated Key          : \033[1;33m{secure_password}\033[0m\033[32m" + " " * max(0, 36 - len(secure_password)) + "║\033[0m")
    print("\033[32m╚════════════════════════════════════════════════════════════════════╝\033[0m\n")

def main():
    matrix_boot_sequence()
    print_movie_banner()
    
    while True:
        print("\033[32m╔════════════════════════ ACCESS TERMINAL ═══════════════════════════╗\033[0m")
        print("\033[32m║\033[0m  \033[1;32m[1]\033[0m Audit Cipher Strength & Trace Breach Databases                \033[32m║\033[0m")
        print("\033[32m║\033[0m  \033[1;32m[2]\033[0m Forge Unbreakable Cryptographic Key                          \033[32m║\033[0m")
        print("\033[32m║\033[0m  \033[1;32m[3]\033[0m Unplug from the Matrix (Exit)                                \033[32m║\033[0m")
        print("\033[32m╚════════════════════════════════════════════════════════════════════╝\033[0m")
        
        choice = input("\n\033[1;32mSelect interface option [1-3]: \033[0m").strip()
        
        if choice == '1':
            user_input = input("\033[32mEnter target cipher for inspection: \033[0m")
            check_password_strength(user_input)
            
        elif choice == '2':
            try:
                length_input = int(input("\033[32mEnter desired key length (min 8): \033[0m"))
                if length_input < 8:
                    print("\033[93m[!] Below minimum threshold. Calibrating to 8.\033[0m")
                    length_input = 8
                generate_secure_password(length_input)
            except ValueError:
                print("\033[91m[X] Error: Non-numeric signal detected.\033[0m\n")
                
        elif choice == '3':
            print("\n\033[1;32mFree your mind... Goodbye, operator.\033[0m")
            break
            
        else:
            print("\033[91m[X] Invalid command. There is no spoon.\033[0m\n")

if __name__ == "__main__":
    main()

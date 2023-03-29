import pikepdf
from tqdm import tqdm


wordlist = "rockyou.txt"

pdf_file = "test.pdf"

n_words = len(list(open(wordlist, "rb")))

print("Total passwords to test:", n_words)
with open(wordlist, "rb") as wordlist:
    for word in tqdm(wordlist, total=n_words, unit="word"):
        try:
            
            with pikepdf.open(pdf_file, password=word.strip()) as pdf:
           
                print("[+] Password found:", word.decode().strip())
                exit(0)
        except pikepdf.PasswordError as e:

            continue
print("[!] Password not found, try other wordlist.")

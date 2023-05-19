# UseReFuzz Modules for Python
# Author = Tanishq Rathore
import colorama
import requests
import urllib3
import os
import re


def headerInjector(url,customHeader,injectionPayload,ufzMessage,httpProxy,output,verbose,sleepTime,alreadyVuln):
    # Disable SSL Warnings
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    # For coloring in other OS also
    colorama.init()
    
    # customHeader  = 'NO_CUSTOM_HEADER'
    # httpProxy = 'NO_PROXY'
    # output = 'NO_OUTPUT'

    # Color codes
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

    # Already Vulnerable URL check
    if url in alreadyVuln:
        return None

    # Injection payload configuration
    if len(re.findall(r'\$UFZ\$' , injectionPayload)) >= 1:
        iPayload = injectionPayload.replace("$UFZ$" , str(sleepTime))
        iPayload2 = injectionPayload.replace("$UFZ$" , str(21)) # 21 sleep to verify properly 
    else:
        print(f"😺{WARNING}_SQLI Payload not in correct format {bcolors.ENDC}{bcolors.BOLD}# userefuzz --help {ENDC}")
        exit(0)

    # Custom header verification 
    # X-Auth|Authorization|X-Forwarded-For
    if customHeader != 'NO_CUSTOM_HEADER': 
        headList = customHeader.split('|')
        header = {}
        header2 = {}
        for head in headList:
            header[head] = iPayload
            header2[head] = iPayload2
    else:
        header = {'User-Agent':iPayload , 'Referer': iPayload , 'X-Forwarded-For': iPayload , 'UseReFuzz': ufzMessage}
        header2 = {'User-Agent':iPayload2 , 'Referer': iPayload2 , 'X-Forwarded-For': iPayload2 , 'UseReFuzz': ufzMessage}


    # Proxy configuration for sending request
    proxy = {'http' : httpProxy , 'https': httpProxy}
    
    # First checking request
    sess = requests.Session()
    resp1 = sess.get(url, headers=header , verify=False)
    resp1Time = resp1.elapsed.total_seconds()

    # Main Verification
    try:
        if resp1Time >= sleepTime and resp1Time <= sleepTime+4: # the 4 is for verification purpose
            # Secondary verification
            resp2 = sess.get(url, headers=header2 , verify=False)
            resp2Time = resp2.elapsed.total_seconds()
            if resp2Time >= 21 and resp2Time <= 21+4: # the 4 is for verification purpose
                alreadyVuln.append(url)
                if httpProxy != 'NO_PROXY': # proxy for sending request to burp or ZAP
                    try:
                        sess.get(url , headers=header , verify=False , proxies=proxy , timeout=0.000000000001)
                    except:
                        pass
                    print(f'{OKGREEN}{BOLD}[💉P{ENDC}{OKGREEN}{BOLD}] \t[ {ENDC}{str(resp1Time)[:4]}{BOLD}{OKGREEN} ] URL => {ENDC}', url)
                    print(f'{OKGREEN}{BOLD}[💉P{ENDC}{OKGREEN}{BOLD}] \t[ {ENDC}{str(resp1Time)[:4]}{BOLD}{OKGREEN} ] (↑) Payload => {ENDC}', iPayload)
                    print()
                else:
                    print(f'{OKGREEN}{BOLD}[💉💉{ENDC}{OKGREEN}{BOLD}] \t[ {ENDC}{str(resp1Time)[:4]}{BOLD}{OKGREEN} ] URL => {ENDC}', url)
                    print(f'{OKGREEN}{BOLD}[💉💉{ENDC}{OKGREEN}{BOLD}] \t[ {ENDC}{str(resp1Time)[:4]}{BOLD}{OKGREEN} ] (↑) Payload => {ENDC}', iPayload)
                    print()

                if output != 'NO_OUTPUT':
                    fileappend = open(output + ".md" , "a")
                    fileappend.write(f'| {resp1Time} | "{url}" | 💉true | "{iPayload}"\n')
                    fileappend.flush()
                    fileappend.close()
            else:
                if verbose:
                    print(f'{FAIL}{BOLD}[{ENDC}NV{ENDC}{FAIL}{BOLD}] \t[ {ENDC}{str(resp1Time)[:4]}{BOLD}{FAIL} ] URL => {ENDC}', url)
                    print(f'{FAIL}{BOLD}[{ENDC}NV{ENDC}{FAIL}{BOLD}] \t[ {ENDC}{str(resp1Time)[:4]}{BOLD}{FAIL} ] (↑) Payload => {ENDC}', iPayload)
                    print()

                    if output != 'NO_OUTPUT':
                        fileappend = open(output + ".md" , "a")
                        fileappend.write(f'| {resp1Time} | "{url}" | false | "{iPayload}"\n')
                        fileappend.flush()
                        fileappend.close()

        else:
            if verbose:
                print(f'{FAIL}{BOLD}[{ENDC}NV{ENDC}{FAIL}{BOLD}] \t[ {ENDC}{str(resp1Time)[:4]}{BOLD}{FAIL} ] URL => {ENDC}', url)
                print(f'{FAIL}{BOLD}[{ENDC}NV{ENDC}{FAIL}{BOLD}] \t[ {ENDC}{str(resp1Time)[:4]}{BOLD}{FAIL} ] (↑) Payload => {ENDC}', iPayload)
                print()

                if output != 'NO_OUTPUT':
                    fileappend = open(output + ".md" , "a")
                    fileappend.write(f'| {resp1Time} | "{url}" | false | "{iPayload}"\n')
                    fileappend.flush()
                    fileappend.close()
    except:
        if verbose:
            print(f'{FAIL}{BOLD}[{ENDC}ER{ENDC}{FAIL}{BOLD}] \t[ {ENDC}{str(resp1Time)[:4]}{BOLD}{FAIL} ] URL => {ENDC}', url)
            print(f'{FAIL}{BOLD}[{ENDC}ER{ENDC}{FAIL}{BOLD}] \t[ {ENDC}{str(resp1Time)[:4]}{BOLD}{FAIL} ] (↑) Payload => {ENDC}', iPayload)
            print()

            if output != 'NO_OUTPUT':
                fileappend = open(output + ".md" , "a")
                fileappend.write(f'| {resp1Time} | "{url}" | error | "{iPayload}"\n')
                fileappend.flush()
                fileappend.close()


def multiPayload(urlMp,customHeaderMp,injectionPayloadMp,userefuzzMessageMp,httpProxyMp,outputMp,verboseMp,sleepTimeMp,alreadyVulnMp):
    if os.path.exists(injectionPayloadMp):
        payloadFileMp = open(injectionPayloadMp, 'r')
        for payloadFileMpLines in payloadFileMp.readlines():
            injectEnd = payloadFileMpLines.replace('\n','')
            headerInjector(urlMp,customHeaderMp,injectEnd,userefuzzMessageMp,httpProxyMp,outputMp,verboseMp,sleepTimeMp,alreadyVulnMp)
    else:
        injectEnd = injectionPayloadMp
        headerInjector(urlMp,customHeaderMp,injectEnd,userefuzzMessageMp,httpProxyMp,outputMp,verboseMp,sleepTimeMp,alreadyVulnMp)

# UseReFuzz Modules for Python
# No Documentations will be provided as the modules are only created for UseReFuzz tool only
# Author = Tanishq Rathore
# Version = 2.1.0
import colorama
import requests
import urllib3
import os


def header_injector(url,custom_header,injection_payload,userefuzz_message,http_proxy,output,telify_APITOKEN,telify_CHATID,is_telify,verbose,sleep_time):
    # For Colouring in Windows and other OS
    colorama.init()
    # Use the following name if you dont want to run the following part of the function
    # custom_header  = 'NO_CUSTOM_HEADER'
    # http_proxy = 'NO_PROXY'
    # output = 'NO_OUTPUT'
    # Colour Codes
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

    # Disable SSL Warnings
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    #  X-Auth|Bearer|X-Forward-For
    if custom_header != 'NO_CUSTOM_HEADER':
        headlist = custom_header.split('|')
        header = {}
        for head in headlist:
            header[head] = injection_payload
        
        header['UseReFuzz'] = userefuzz_message
    else:
        header = {'User-Agent':injection_payload , 'Referer': injection_payload , 'X-Forwarded-For': injection_payload , 'UseReFuzz': userefuzz_message}
    
    proxy = {'http' : http_proxy , 'https': http_proxy}
    sess = requests.Session()
    resp = sess.get(url, headers=header , verify=False)
    resp_time = resp.elapsed.total_seconds()
    try:
        if resp_time >= sleep_time-1:
            if http_proxy != 'NO_PROXY':
                try:
                    sess.get(url , headers=header , verify=False , proxies=proxy , timeout=0.000000000001)
                except:
                    pass
                print(f'{OKGREEN}{BOLD}[💉P{ENDC}{OKGREEN}{BOLD}] \t[ {ENDC}{str(resp_time)[:4]}{BOLD}{OKGREEN} ] URL => {ENDC}', url)
                print(f'{OKGREEN}{BOLD}[💉P{ENDC}{OKGREEN}{BOLD}] \t[ {ENDC}{str(resp_time)[:4]}{BOLD}{OKGREEN} ] (↑) PAYLOAD => {ENDC}', injection_payload)
            else:
                print(f'{OKGREEN}{BOLD}[💉💉{ENDC}{OKGREEN}{BOLD}] \t[ {ENDC}{str(resp_time)[:4]}{BOLD}{OKGREEN} ] URL => {ENDC}', url)
                print(f'{OKGREEN}{BOLD}[💉💉{ENDC}{OKGREEN}{BOLD}] \t[ {ENDC}{str(resp_time)[:4]}{BOLD}{OKGREEN} ] (↑) PAYLOAD => {ENDC}', injection_payload)

            if output != 'NO_OUTPUT':
                fileappend = open(output + ".md" , "a")
                fileappend.write(f'| {resp_time} | "{url}" | 💉True | "{injection_payload}"\n')
                fileappend.flush()
                fileappend.close()

            if is_telify == 'TELIFY_UP':
                telifyurl = f'https://api.telegram.org/bot{telify_APITOKEN}/sendMessage'
                requests.post(telifyurl, json={'chat_id': telify_CHATID, 'text': f'[💎] (USEREFUZZ)⛓️URL(💻)⛓️ {url} ⛓️RESPONSE TIME(⏲️)⛓️ {resp_time} ⛓️PAYLOAD(🔫)⛓️ {injection_payload}'})

        else:
            if verbose:
                print(f'{FAIL}{BOLD}[{ENDC}NV{ENDC}{FAIL}{BOLD}] \t[ {ENDC}{str(resp_time)[:4]}{BOLD}{FAIL} ] URL => {ENDC}', url)
                print(f'{FAIL}{BOLD}[{ENDC}NV{ENDC}{FAIL}{BOLD}] \t[ {ENDC}{str(resp_time)[:4]}{BOLD}{FAIL} ] (↑) PAYLOAD => {ENDC}', injection_payload)

                if output != 'NO_OUTPUT':
                    fileappend = open(output + ".md" , "a")
                    fileappend.write(f'| {resp_time} | "{url}" | False | "{injection_payload}"\n')
                    fileappend.flush()
                    fileappend.close()
    except:
        if verbose:
            print(f'{FAIL}{BOLD}[{ENDC}ER{ENDC}{FAIL}{BOLD}] \t[ {ENDC}{str(resp_time)[:4]}{BOLD}{FAIL} ] URL => {ENDC}', url)
            print(f'{FAIL}{BOLD}[{ENDC}ER{ENDC}{FAIL}{BOLD}] \t[ {ENDC}{str(resp_time)[:4]}{BOLD}{FAIL} ] (↑) PAYLOAD => {ENDC}', injection_payload)

            if output != 'NO_OUTPUT':
                fileappend = open(output + ".md" , "a")
                fileappend.write(f'| {resp_time} | "{url}" | ERROR | "{injection_payload}"\n')
                fileappend.flush()
                fileappend.close()

def multi_payload(url_mp,custom_header_mp,injection_payload_mp,userefuzz_message_mp,http_proxy_mp,output_mp,telify_APITOKEN_mp,telify_CHATID_mp,is_telify_mp,verbose_mp,sleep_time_mp):
    if os.path.exists(injection_payload_mp):
        payload_file_mp = open(injection_payload_mp, 'r')
        for payload_file_mp_lines in payload_file_mp.readlines():
            inject_end = payload_file_mp_lines.replace('\n','')
            header_injector(url_mp,custom_header_mp,inject_end,userefuzz_message_mp,http_proxy_mp,output_mp,telify_APITOKEN_mp,telify_CHATID_mp,is_telify_mp,verbose_mp,sleep_time_mp)
    else:
        inject_end = injection_payload_mp
        header_injector(url_mp,custom_header_mp,inject_end,userefuzz_message_mp,http_proxy_mp,output_mp,telify_APITOKEN_mp,telify_CHATID_mp,is_telify_mp,verbose_mp,sleep_time_mp)

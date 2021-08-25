# script.py
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import jokes

# // KUN SOURCE //
from termcolor import colored
import requests
import random
import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import random
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.proxy import Proxy, ProxyType
import pyautogui
import getpass
import sys
import telnetlib
import time

# \/\/\/\/\/\/\/\/\/\/\/\/#
THEC_logo = colored('''
 __          
/    |_  _ _ 
\__\/|_)(-|  
   /         
''')
THEK_logo = colored('''
               ██╗    ██╗  ██╗██╗   ██╗███╗   ██╗        ██╗██╗  
              ██╔╝    ██║ ██╔╝██║   ██║████╗  ██║       ██╔╝╚██╗ 
             ██╔╝     █████╔╝ ██║   ██║██╔██╗ ██║      ██╔╝  ╚██╗
             ╚██╗     ██╔═██╗ ██║   ██║██║╚██╗██║     ██╔╝   ██╔╝
              ╚██╗    ██║  ██╗╚██████╔╝██║ ╚████║    ██╔╝   ██╔╝ 
               ╚═╝    ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝    ╚═╝    ╚═╝  



''')
print(colored(THEC_logo, 'red'), colored(THEK_logo, 'blue'))

#


Type_SPAM = {

    "SPAM": '/html/body/div[5]/div/div/div/div[2]/div/div/div/div[3]/button[1]',
    "i just don't like it": '/html/body/div[5]/div/div/div/div[2]/div/div/div/div[3]/button[2]',
    "self-injury": '/html/body/div[5]/div/div/div/div[2]/div/div/div/div[3]/button[3]',
    "sale something bad": '/html/body/div[5]/div/div/div/div[2]/div/div/div/div[3]/button[4]',
    "sex": '/html/body/div[5]/div/div/div/div[2]/div/div/div/div[3]/button[5]',
    "hate": '/html/body/div[5]/div/div/div/div[2]/div/div/div/div[3]/button[6]',
    "violence": '/html/body/div[5]/div/div/div/div[2]/div/div/div/div[3]/button[7]',
    "bullying and harassment": '/html/body/div[5]/div/div/div/div[2]/div/div/div/div[3]/button[8]',
    "intellectual": '/html/body/div[5]/div/div/div/div[2]/div/div/div/div[3]/button[9]',
    "scam or fraud": '/html/body/div[5]/div/div/div/div[2]/div/div/div/div[3]/button[10]',
    "False info": '/html/body/div[5]/div/div/div/div[2]/div/div/div/div[3]/button[11]',

}

username = input("   [ EMAIL or USERNAME ] - - > ")

# Here if you want to set the acc
##username = ""

password = input("   [ PASSWORD ] - - > ")

# Here if you want to set the pass
##password = ""

victim_username = input(colored("   [ THE VICTIM ] - - > ", 'red'))
TPALL = '''
    +----------------------------+--------+
    |        Reason              | Numara |
    +----------------------------+--------+
    | Spam                       |      1 |
    | Do not hurt yourself       |      2 |
    | Drug                       |      3 |
    | Nudity                     |      4 |
    | Severity                   |      5 |
    | Hate Speech                |      6 |
    | Harassment and Bullying    |      7 |
    | Identity Imitation         |      8 |
    | False info                 |      9 |
    +----------------------------+--------+
'''
print(TPALL)
while True:
    try:
        TP = int(input("   [↑]What type of spam --> "))
        if TP == 1:
            print("\n")
            TYP = Type_SPAM["SPAM"]
            pms = "/html/body/div[5]/div/div/div/div/div/div/div[2]/button"
            smp = "/html/body/div[1]/section/main/div/header/div/div/span"
            sps = "/html/body/div[1]/section/main/div/header/div/div/span"
            while True:
                try:
                    print("       ⇊[ " + victim_username + " ]⇊")
                    pac = input("[?]PRIVATE ACCOUNT[YES/NO] --> ")
                    if pac == "YES" or pac == 'Yes' or pac == 'yes' or pac == 'yEs' or pac == 'yeS' or pac == 'y' or pac == 'Y':
                        smp = "/html/body/div[1]/section/main"
                        sps = "/html/body/div[1]/section/main"
                        break
                    elif pac == "NO" or pac == "No" or pac == 'no' or pac == "nO" or pac == 'N' or pac == 'n':
                        smp = "/html/body/div[1]/section/main/div/header/section/div[1]/h2"
                        sps = "/html/body/div[1]/section/main/div/header/section/div[1]/h2"
                        break
                    else:
                        print("[!!Error]"+" Aye captain account the victim is private or not ? ")
                        print("_________________________________________________________")
                        continue
                except:
                    print("[!!Error]"+" Aye captain account the victim is private or not ? ")
                    print("_________________________________________________________")
                    continue
            break
        elif TP == 2:
            print("\n")
            TYP = Type_SPAM["self-injury"]
            pms = "/html/body/div[5]/div/div/div/div[2]/div/div/button"
            smp = "/html/body/div[5]/div/div/div/div/div/div/div[4]/button"
            sps = "/html/body/div[1]/section/main"
            while True:
                try:
                    print("       ⇊[ " + victim_username + " ]⇊")
                    pac = input("[?]PRIVATE ACCOUNT[YES/NO] --> ")
                    if pac == "YES" or pac == 'Yes' or pac == 'yes' or pac == 'yEs' or pac == 'yeS' or pac == 'y' or pac == 'Y':
                        sps = "/html/body/div[1]/section/main"
                        break
                    elif pac == "NO" or pac == "No" or pac == 'no' or pac == "nO" or pac == 'N' or pac == 'n':
                        sps = "/html/body/div[1]/section/main/div/header/section/div[1]/h2"
                        break
                    else:
                        print("[!!Error]"+" Aye captain account the victim is private or not ? ")
                        print("_________________________________________________________")
                        continue
                except:
                    print("[!!Error]"+" Aye captain account the victim is private or not ? ")
                    print("_________________________________________________________")
                    continue
            break
        elif TP == 3:
            print("\n")
            TYP = Type_SPAM["sale something bad"]
            pms = "/html/body/div[5]/div/div/div/div[2]/div/div/div/fieldset/div[1]/label/div"
            smp = "/html/body/div[5]/div/div/div/div[2]/div/div/div/div[6]/button"
            sps = "/html/body/div[5]/div/div/div/div/div/div/div[4]/button"
            break
        elif TP == 4:
            print("\n")
            TYP = Type_SPAM["sex"]
            pms = "/html/body/div[5]/div/div/div/div[2]/div/div/div/fieldset/div[1]/label/div"
            smp = "/html/body/div[5]/div/div/div/div[2]/div/div/div/div[6]/button"
            sps = "/html/body/div[5]/div/div/div/div/div/div/div[4]/button"
            break
        elif TP == 5:
            print("\n")
            TYP = Type_SPAM["violence"]
            pms = "/html/body/div[5]/div/div/div/div[2]/div/div/div/fieldset/div[1]/label/div"
            smp = "/html/body/div[5]/div/div/div/div[2]/div/div/div/div[6]/button"
            sps = "/html/body/div[5]/div/div/div/div/div/div/div[4]/button"
            break
        elif TP == 6:
            print("\n")
            TYP = Type_SPAM["hate"]
            pms = "/html/body/div[5]/div/div/div/div[2]/div/div/button"
            smp = "/html/body/div[5]/div/div/div/div/div/div/div[4]/button"
            sps = "/html/body/div[1]/section/main"
            while True:
                try:
                    print("       ⇊[ " + victim_username + " ]⇊")
                    pac = input("[?]PRIVATE ACCOUNT[YES/NO] --> ")
                    if pac == "YES" or pac == 'Yes' or pac == 'yes' or pac == 'yEs' or pac == 'yeS' or pac == 'y' or pac == 'Y':
                        sps = "/html/body/div[1]/section/main"
                        break
                    elif pac == "NO" or pac == "No" or pac == 'no' or pac == "nO" or pac == 'N' or pac == 'n':
                        sps = "/html/body/div[1]/section/main/div/header/section/div[1]/h2"
                        break
                    else:
                        print("[!!Error]"+" Aye captain account the victim is private or not ? ")
                        print("_________________________________________________________")
                        continue
                except:
                    print("[!!Error]"+" Aye captain account the victim is private or not ? ")
                    print("_________________________________________________________")
                    continue
            break
        elif TP == 7:
            print("\n")
            TYP = Type_SPAM["bullying and harassment"]
            pms = "/html/body/div[5]/div/div/div/div[2]/div/div/div/div[3]/button[1]"
            smp = "/html/body/div[5]/div/div/div/div[2]/div/div/button"
            sps = "/html/body/div[5]/div/div/div/div/div/div/div[4]/button"
            break
        elif TP == 8:
            print("\n")
            TYP = Type_SPAM["scam or fraud"]
            pms = "/html/body/div[5]/div/div/div/div/div/div/div[2]/button"
            smp = "/html/body/div[1]/section/main"
            sps = "/html/body/div[1]/section/main"
            while True:
                try:
                    print("       ⇊[ " + victim_username + " ]⇊")
                    pac = input("[?]PRIVATE ACCOUNT[YES/NO] --> ")
                    if pac == "YES" or pac == 'Yes' or pac == 'yes' or pac == 'yEs' or pac == 'yeS' or pac == 'y' or pac == 'Y':
                        smp = "/html/body/div[1]/section/main"
                        sps = "/html/body/div[1]/section/main"
                        break
                    elif pac == "NO" or pac == "No" or pac == 'no' or pac == "nO" or pac == 'N' or pac == 'n':
                        smp = "/html/body/div[1]/section/main/div/header/section/div[1]/h2"
                        sps = "/html/body/div[1]/section/main/div/header/section/div[1]/h2"
                        break
                    else:
                        print("[!!Error]"+" Aye captain account the victim is private or not ? ")
                        print("_________________________________________________________")
                        continue
                except:
                    print("[!!Error]"+" Aye captain account the victim is private or not ? ")
                    print("_________________________________________________________")
                    continue
            break
        elif TP == 9:
            print("\n")
            TYP = Type_SPAM["False info"]
            pms = "/html/body/div[5]/div/div/div/div/div/div/div[2]/button"
            smp = "/html/body/div[1]/section/main"
            sps = "/html/body/div[1]/section/main"
            while True:
                try:
                    print("       ⇊[ " + victim_username + " ]⇊")
                    pac = input("[?]PRIVATE ACCOUNT[YES/NO] --> ")
                    if pac == "YES" or pac == 'Yes' or pac == 'yes' or pac == 'yEs' or pac == 'yeS' or pac == 'y' or pac == 'Y':
                        smp = "/html/body/div[1]/section/main"
                        sps = "/html/body/div[1]/section/main"
                        break
                    elif pac == "NO" or pac == "No" or pac == 'no' or pac == "nO" or pac == 'N' or pac == 'n':
                        smp = "/html/body/div[1]/section/main/div/header/section/div[1]/h2"
                        sps = "/html/body/div[1]/section/main/div/header/section/div[1]/h2"
                        break
                    else:
                        print("[!!Error]"+" Aye captain account the victim is private or not ? ")
                        print("_________________________________________________________")
                        continue
                except:
                    print("[!!Error]"+" Aye captain account the victim is private or not ? ")
                    print("_________________________________________________________")
                    continue
            break
        else:
            print("[Error!!]"+" Please enter number from the table")
            print("_________________________________________________________")
    except:
        # I know that bad to your sweet eyes ^-^
        print("[Error!!]"+" Please enter number from the table")
    print("_________________________________________________________")

lghe = """





       /_/_  __       _   _  _  /
      / //_'//_' |/|//_' /_//_/. 
                         _/       
"""
print(colored(lghe, 'cyan'))
while True:
    try:
        number = int(input("   [?]How many number of spam --> "))
        if number > 100000:
            print("[!!Error]"+" The largest of spam equal 100000")
            print("_________________________________________________________")
            continue
        elif number <= 0:
            print("[!!Error]"+" The number of spam must be bigger than 0")
            print("_________________________________________________________")
            continue
        else:
            break
    except:
        print("[!!Error]"+" Enter only numbers")
        print("_________________________________________________________")
        continue

hlp = '''





{ [!]Enter the number of sleep depend on your internet speed and computer speed to avoid errors }
- between (1 - 5)          >5 lowest speed   -   >1 Highest speed
'''
while True:
    try:
        print((hlp))
        ss = eval(input("   [ ZzzSLEEP ] --> "))

        if ss > 5:
            print("[!!Error]"+" Enter <=5")
            print("_________________________________________________________")
            continue
        elif ss < 1:
            print("[!!Error]"+" Enter >=1")
            print("_________________________________________________________")
            continue
        else:
            break
    except:
        print(colored("[!!Error]", 'red'), colored("Enter only numbers"))
        print("_________________________________________________________")
        continue

DN = """





                            , . . . . . . . . . ,             
         ,'  ' ·,      , · '    ·,                  ' · ,        ,' ' ·, 
     , · ·.   .'  , '          ,·',·,                     ' ·, ,·'    ·'· ·, 
     ' · . .,   '·;           '  ,'·, '                        ;  ,·' ' ' ' ' 
              ' ,;             '    '·                        ;' 
                 ',                                         ,' 
                ,' '      . , , ,             , , , .      ' ; 
                 ',      , , , ,  '·,     ,·'  , , , ,       ; 
                 ,'     ',::::::::',  ;   ;  ,':::::::,'     ,' 
              , · ',      ' ' ' ' ' '  ,;¸¸¸;, ' ' ' ' ' '       ,' ·, 
     , , , ·'   ,  '' ,              '*****'               ,'' ,   '  , , , 
    '·,..    , '        ' ,'   `;`;`;`;`; ;´;´;´;´;´   ,' '      ' ,   ,..·' 
        '·, .'            ',    ','' '' '' '' '' '' '' '','   ,'         '. , ·' 
              Ñë§§     ',    ' ;'';'';'';'';'';'';'   ,'   *kun*      
                             ' ,      ,          ,'        *10*     
                                 ' · · ·''· · · '¤¹
"""
print(colored(DN, 'red'))
print("                                 >> "+(victim_username)+(" <<"))
print("__________________________________________________________________________________")

LSSUCSPAM = []
LSFILSPAM = []
Nlp = 0
STSPAM = 0
class InstaScript:
    def __init__(self, username, password, victim_username, number, LSSUCSPAM, LSFILSPAM, Nlp, STSPAM):
        self.username = username
        self.password = password
        self.victim_username = victim_username
        self.number = number
        self.LSSUCSPAM = LSSUCSPAM
        self.LSFILSPAM = LSFILSPAM
        self.Nlp = Nlp
        self.STSPAM = STSPAM
        self.browser = webdriver.Firefox()
        option = webdriver.FirefoxOptions()
        option.add_argument('–-no-sandbox')
        option.add_argument('–-headless')
        option.add_argument("--disable-extensions")

    def login(self):
        browser = self.browser
        browser.implicitly_wait(5)

        # opening instagram.com
        browser.get('https://www.instagram.com/')
        # -------login process starts
        # finding input boxes for username and password and pasing the appropriate values
        try:
            browser.find_element_by_xpath("//input[@name='username']").send_keys(self.username)
            browser.find_element_by_xpath("//input[@name='password']").send_keys(self.password)
            # findind login button and clicking it
            browser.find_element_by_xpath("//button[@type='submit']").click()
            # -------login process ends
        except:
            print(colored("       [x]Something wrong from the server or internet", 'red'))
            exit()

    def victim_profile(self):
        browser = self.browser
        browser.implicitly_wait(5)

        # Clicking "Not Now" in pop up just after login
        try:
            sleep(2.5)
            not_now_button = browser.find_element_by_xpath("//button[text()='Not Now']")
            sleep(1)
            not_now_button.click()
            sleep(1)
            browser.find_element_by_xpath("//button[text()='Not Now']").click()
        except:
            print(colored("       [x]The user||email or password is wrong", 'red'))
            exit()


        # -------profile for victim's username starts

        browser.get("https://www.instagram.com/" + self.victim_username)

    def spamming(self):
        browser = self.browser
        browser.implicitly_wait(5)

        # -------spamming begins
        # click account buttom
        # input random send 100 times
        MINlp = 0
        SUCSPAM = 0
        FILSPAM = 0
        STSPAM = 0
        STFILSPAM = 0
        while True:
            if self.Nlp == self.number:
                break
            for _ in range(0, self.number):
                self.Nlp += 1
                MINlp += 1
                try:
                    browser.find_element_by_xpath(
                        "/html/body/div[1]/section/main/div/header/section/div[1]/div[2]/button").click()
                    sleep(ss)
                    # WATCH OUT
                    browser.find_element_by_xpath("/html/body/div[5]/div/div/div/div/button[3]").click()
                    sleep(ss)
                    browser.find_element_by_xpath("/html/body/div[5]/div/div/div/div[2]/div/div/div/div[3]/button[2]").click()
                    sleep(ss)
                    browser.find_element_by_xpath("/html/body/div[5]/div/div/div/div[2]/div/div/div/div[3]/button[1]").click()
                    sleep(ss)
                    browser.find_element_by_xpath(TYP).click()
                    sleep(ss)
                    browser.find_element_by_xpath(pms).click()
                    sleep(ss)
                    browser.find_element_by_xpath(smp).click()
                    sleep(ss)
                    browser.find_element_by_xpath(sps).click()
                    print("       >>  ☠//SPAM NUMBER", _ + 1)
                    LSSUCSPAM.append(int(SUCSPAM + 1))
                except:
                    STFILSPAM += 1
                    STSPAM += 1
                    LSFILSPAM.append(int(FILSPAM + 1))
                    print("       !!Error"+"   [ WAIT 10s ] [*]AFTER 5 Errors, Sign in will repeat")
                    if STFILSPAM == 5:
                        browser.close()
                        sleep(5)
                        if self.Nlp != self.number:
                            Instagram_Spam_Bot = InstaScript(username, password, victim_username, int(number-MINlp), LSSUCSPAM, LSFILSPAM, int(Nlp), (STSPAM+self.STSPAM))
                            print("     [!]Don't worry the number of spam will change depend on how many number of report before login again")
                            Instagram_Spam_Bot.login()
                            Instagram_Spam_Bot.victim_profile()
                            Instagram_Spam_Bot.spamming()
                    elif self.STSPAM == 10:
                        print(colored(" X> The account is disable to report try again or change to another ac.", 'red))
                        break

                    else:
                        browser = self.browser
                        browser.implicitly_wait(10)
                        browser.get("https://www.instagram.com/" + victim_username)
                        sleep(5)



            break
        browser.close()
        print("               ______________________________________")
        print("               | THE NUMBER OF SUCCESS SPAM IS-->"+ str(sum(LSSUCSPAM))+"  |")
        print(colored("               ______________________________________", 'red'))
        print("               | THE NUMBER OF FAIL SPAM IS-->"+ str(sum(LSFILSPAM))+"     |")
        print("\n")
        print("  //Press Enter")
        ex = input(">[EXIT] ")
        exit()

if __name__ == '__main__':
    Instagram_Spam_Bot = InstaScript(username, password, victim_username, int(number), LSSUCSPAM, LSFILSPAM, int(Nlp), STSPAM)
    Instagram_Spam_Bot.login()
    Instagram_Spam_Bot.victim_profile()
    Instagram_Spam_Bot.spamming()

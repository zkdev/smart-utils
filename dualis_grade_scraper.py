import logging as log
import requests
import sys
from bs4 import BeautifulSoup


USERNAME = "xxx"
PASSWORD = "xxx"
LOGIN_URL = "https://dualis.dhbw.de/scripts/mgrqispi.dll"
LOGIN_FORM = {
    "usrname": USERNAME,
    "pass": PASSWORD,
    "APPNAME": "CampusNet",
    "PRGNAME": "LOGINCHECK",
    "ARGUMENTS": "clino,usrname,pass,menuno,menu_type,browser,platform",
    "clino": "000000000000001",
    "menuno": "000000",
    "menu_type": "classic",
    "browser": "",
    "platform": ""
}
GRADE_URL = "https://dualis.dhbw.de/scripts/mgrqispi.dll?APPNAME=CampusNet&PRGNAME=STUDENT_RESULT&ARGUMENTS=" \
            "{},-N0,-N000000000000000,-N000000000000000,-N000000000000000,-N0,-N000000000000000"


def run():
    s = get_session()
    gs = get_grades(s)
    print(gs)


def get_session():
    r = requests.post(LOGIN_URL, data=LOGIN_FORM)
    if r.text.__contains__('Benutzername oder Passwort falsch'):
        log.error('credentials rejected')
        sys.exit(1)
    c = str(r.headers['Set-cookie']).split(';')[0]
    p = str(r.headers['REFRESH'])[str(r.headers['REFRESH']).rfind('ARGUMENTS=')+10:str(r.headers['REFRESH']).rfind(',')]
    return {'c': c, 'p': p}


def get_grades(d):
    r = requests.get(GRADE_URL.format(d['p']), headers={'cookie': d['c']})
    soup = BeautifulSoup(r.text)
    tb = soup.find('tbody')
    gs = []
    for tr in tb.contents:
        try:
            if str(tr.text).startswith('\nT3'):
                try:
                    g = {
                        'module': tr.contents[1].text,
                        'name': tr.contents[3].contents[1].text,
                        'grade': tr.contents[9].text
                    }
                    gs.append(g)
                except IndexError:
                    pass
        except AttributeError:
            pass
    return gs


if __name__ == '__main__':
    run()

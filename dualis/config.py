import pathlib as pl


LOGIN_URL = "https://dualis.dhbw.de/scripts/mgrqispi.dll"
LOGIN_FORM = {
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
ROOT_PATH = pl.Path().absolute()
CACHE_PATH = '{}/dualis/.cache'.format(ROOT_PATH)
RESOURCE_GRADES = '{}/grades.json'.format(CACHE_PATH)


def get_login_form(username=None, password=None):
    LOGIN_FORM['usrname'] = username
    LOGIN_FORM['pass'] = password
    return LOGIN_FORM

import requests
import os
import json
import sys
import config
import common.ezlog as ezlog
import args
from bs4 import BeautifulSoup


logger = ezlog.get_logger()


def run():
    s = get_session()
    gs = get_grades(s)
    compare_cache(gs)
    cache(gs)
    logger.info('finished')
    sys.exit(0)


def get_session():
    logger.info('getting session')
    config.prepare_login()
    r = requests.post(config.LOGIN_URL, data=config.LOGIN_FORM)
    if r.text.__contains__('Benutzername oder Passwort falsch'):
        logger.error('credentials rejected')
        sys.exit(1)
    logger.info('setting cookie')
    c = str(r.headers['Set-cookie']).split(';')[0]
    p = str(r.headers['REFRESH'])[str(r.headers['REFRESH']).rfind('ARGUMENTS=')+10:str(r.headers['REFRESH']).rfind(',')]
    logger.info('session preparation done')
    return {'c': c, 'p': p}


def get_grades(d):
    logger.info('getting grades')
    r = requests.get(config.GRADE_URL.format(d['p']), headers={'cookie': d['c']})
    logger.info('parsing grades')
    soup = BeautifulSoup(r.text, features="html.parser")
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
    logger.info('grades retrieved')
    return gs


def compare_cache(gs):
    # check if old grade file exists
    if os.path.isfile(config.RESOURCE_GRADES):
        # load cached grades
        logger.info('loading grades from cache')
        with open(config.RESOURCE_GRADES) as json_file:
            c = json.load(json_file)
            logger.info('loaded')
            if c == gs:
                logger.info('no new grades')
                return
            else:
                logger.info('new grades found')
                logger.info('result can found at {}'.format(config.RESOURCE_GRADES))

    # else instant output
    else:
        logger.info('no cached grades found')


def cache(gs):
    logger.info('caching grades')
    try:
        os.mkdir(config.CACHE_PATH)
    except FileExistsError:
        pass
    with open(config.RESOURCE_GRADES, 'w', encoding='utf-8') as outfile:
        json.dump(gs, outfile)
    logger.info('cached')


if __name__ == '__main__':
    args.read(sys.argv)
    run()

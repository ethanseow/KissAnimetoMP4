import selenium,requests, bs4, time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

browser = webdriver.Chrome('C:\\Users\\eths6\\PythonProjext\\chromedriver')
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
login_site = 'http://kissanime.ru/Login'
site = input('Please input full url of the animesite:')

def adblock():
    adblock = 'https://chrome.google.com/webstore/detail/pop-up-blocker-for-chrome/bkkbcggnhapdmkeljlodobbkopceiche?hl=en'
    browser.get(adblock)
    time.sleep(10)
def login():
    req_login = browser.get(login_site)
    print('Converging World Lines...')
    time.sleep(10)
    print('Done')
    innerHTML = browser.execute_script("return document.body.innerHTML")

    #input username and pass
    username = browser.find_element_by_id('username')
    username.send_keys('animedownloadermp4')
    password = browser.find_element_by_id('password')
    password.send_keys('animetomp4')
    password.submit()

def animedownloader():
    t1 = time.time()
    #go to anime site
    req_site = browser.get(site)
    innerHTML = browser.execute_script("return document.body.innerHTML")
    parser_site = bs4.BeautifulSoup(innerHTML, features = 'html.parser')

    #finds all the episodes
    print('Hacking to the gate...')
    time.sleep(5)
    first_site = parser_site.select('.listing')[0]
    episodes = first_site.select('a')
    amount_ep = len(episodes)

    #loop through all videos
    for e in range(amount_ep - 1):
        episode = episodes[e]


        episode_site = episode.get('href')
        print(episode_site)
        episode_fullsite = '{}{}{}'.format('http://kissanime.ru',episode_site,'&s=rapidvideo')
        time.sleep(10)

        #go to rapid_video
        browser.get(episode_fullsite)
        innerHTML = browser.execute_script("return document.body.innerHTML")
        parser_video = bs4.BeautifulSoup(innerHTML, features = 'html.parser')
        find_link = parser_video.find('iframe', {'id':'my_video_1'})
        found_link = find_link.get('src')
        list_link = list(found_link)
        list_link.pop(27)
        list_link.insert(27,'d')
        down_link = ''.join(list_link)
        browser.get(down_link)
        time.sleep(5)
        try:
            download = browser.find_element_by_xpath('//*[@id="button-download"]')
        except Exception as e:
            print('There was a Capcha Error, please check the browser')
            x = input('Press any button to continue')
        else:
            print('Downloading...',e + 1)
            download.click()
        

    t2 = time.time() - t1
    print('It took {} seconds to download'.format(t2))
    print('Done downloading')

def main():
    print('\n')
    print('This an crap version of the QueefMachine(trademark) there may be some \n bugs such as adblock or captcha requests which require manaul fixes, please check the cmd panel')
    print('\n')
    print('YOU MUST INPUT THE ANIME WEBSITE AS IT WOULD ON KISSANIME')
    print('\n')
    print('i.e. http://kissanime.ru/Anime/Steins-Gate-0')
    print('\n')
    x = input('Press any key to begin')
    
    adblock()
    login()
    animedownloader()
main()

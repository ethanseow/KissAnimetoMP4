import selenium,requests, bs4, time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
login_site = 'http://kissanime.ru/Login'
site = input('Please input full url of the animesite:')

def adblock():
    #this goes to pop-up blocker
    adblock = 'https://chrome.google.com/webstore/detail/pop-up-blocker-for-chrome/bkkbcggnhapdmkeljlodobbkopceiche?hl=en'
    browser.get(adblock)
    
def login():
    #login so we're able to click download button
    time.sleep(10)
    req_login = browser.get(login_site)
    print('Converging World Lines...')
    time.sleep(10)
    print('Done')
    innerHTML = browser.execute_script("return document.body.innerHTML")



    #input username and pass
    username = browser.find_element_by_id('username')
    username.send_keys('ethanseow')
    password = browser.find_element_by_id('password')
    password.send_keys('loler123')
    password.submit()
    time.sleep(3)
    
def animedownloader(ep_num = 0):
    t1 = time.time()
    #go to anime site
    anime_url = browser.get(site)
    
    
    anime_url = browser.get(site)
    innerHTML = browser.execute_script("return document.body.innerHTML")
    parser_site = bs4.BeautifulSoup(innerHTML, features = 'html.parser')

    #finds all the episodes
    print('Hacking to the Gate...')
    time.sleep(5)
    
    #finds all id 'listing'
    
    list_listing = parser_site.select('.listing')[0]

    #finds all the links
    episode_linklist = list_listing.select('a')
    amount_ep = len(episode_linklist)
    if ep_num > 0:

        amount_ep = amount_ep - ep_num + 1
    
    #since the list is the first element being the last episode ,we must flip it
    #so that it starts at the last element goes all the way to first
    range_ep = list(range(amount_ep - 1, -1, -1))
    
    #loop through all videos
    for e,n in zip(range_ep, range(amount_ep + 1)):
        episode = episode_linklist[e]

        #finds the link for the episode
        episode_link = episode.get('href')
        print(episode_link)
        episode_fulllink = '{}{}{}'.format('http://kissanime.ru',episode_link,'&s=rapidvideo')
        time.sleep(5)

        #go to rapid_video
        browser.get(episode_fulllink)
        lag = browser.find_element_by_xpath('//*[@id="adsIfrme"]/div/div/div[9]')
        lag.click()
        innerHTML = browser.execute_script("return document.body.innerHTML")
        parser_video = bs4.BeautifulSoup(innerHTML, features = 'html.parser')
        #get the rapidvideo link
        find_link = parser_video.find('iframe', {'id':'my_video_1'})
        found_link = find_link.get('src')
        """
        list_link = list(found_link)
        list_link.pop(27)
        list_link.insert(27,'d')
        down_link = ''.join(list_link)
        """
        #rewrites the link to have d in it
        change_link = found_link[:27] + 'd' + found_link[28:]
        rapidvideo_link = change_link
        browser.get(rapidvideo_link)
        time.sleep(3)
        try:
            download_button = browser.find_element_by_xpath('//*[@id="button-download"]')
        except Exception as e:
            print('There was a Captcha Error, please check the browser')
            x = input('Press any button to continue')
            browser.get(rapidvideo_link)
            download_button = browser.find_element_by_xpath('//*[@id="button-download"]')
            time.sleep(5)
            continue
                                                     
        else:
            print('Downloading...',n + 1)
            download_button.click()
        
    t2 = time.time() - t1
    print('It took {} seconds to download'.format(t2))
    print('Done downloading')

def main():
    print('\n')
    print('This a crap version of the QueefMachine(trademark) there may be some \n bugs such as adblock or captcha requests which require manaul fixes, please check the cmd panel')
    print('\n')
    print('YOU MUST INPUT THE ANIME WEBSITE AS IT WOULD ON KISSANIME')
    print('\n')
    print('i.e. http://kissanime.ru/Anime/Steins-Gate-0')
    print('\n')
    
    user_ep_num = input('Please put the episode number you want to download from:')
    driverloc = input('Please input the location of the chromedriver')
    driverloc.replace('\\','/')
    browser = webdriver.Chrome(driverloc)
    num = True
    while num:
        try:
            eval(user_ep_num) + 1
        except Exception as e:
            print('You didnt put a number')
            user_ep_num = input('Please put the episode number you want to download from:')


        else:
            user_ep_num = eval(user_ep_num)
            if user_ep_num > 0:
                adblock()
                login()
                animedownloader(user_ep_num)
            elif user_ep_num == 0:
                adblock()
                login()
                animedownloader()
                
            num = False
        
    """
    adblock()
    login()
    animedownloader()
    """
main()

from selenium import webdriver

def testcookie(urls):
    for url in urls:
        phantomjs = webdriver.PhantomJS()
        phantomjs.set_window_size(1120, 550)
        phantomjs.get(url)
        print(phantomjs.get_cookies())

def entercontest(urls):
    for url in urls:
        phantomjs = webdriver.PhantomJS()
        phantomjs.set_window_size(1120, 550)
        phantomjs.get(url)
        print(phantomjs.get_cookies())


        #twitter|follow
        try:
            phantomjs.find_elements_by_css_selector(
                "*[data-track-event='\x23\x23\x23APP_NAME\x23\x23\x23 Click|twitter|follow')]").click()
        except:
            break
        #twitter|retweet
        try:
            phantomjs.find_elements_by_css_selector(
                "*[data-track-event='\x23\x23\x23APP_NAME\x23\x23\x23 Click|twitter|retweet')]").click()
            phantomjs.find_element_by_class_name("TweetAction TweetAction--retweet web-intent").click()
        except:
            break
        #twitter|tweet
        try:
            phantomjs.find_elements_by_css_selector(
                "*[data-track-event='\x23\x23\x23APP_NAME\x23\x23\x23 Click|twitter|tweet')]").click()
        except:
            break
        #youtube|subscribe
        '''
        try:
            phantomjs.find_elements_by_css_selector(
                "*[data-track-event='\x23\x23\x23APP_NAME\x23\x23\x23 Click|youtube|subscribe')]").click()
            phantomjs.find_element_by_class_name("btn btn-large btn-info btn-embossed").click()
            phantomjs.find_element_by_class_name("btn btn-primary").click()
        except:
            break
        '''

# NEED TO STORE COOKIES TO AVOID HAVING TO LOG IN
'''
http_pool = urllib3.connection_from_url("http://example.com")
myheaders = {'Cookie':'some cookie data'}
r = http_pool.get_url("http://example.org/", headers=myheaders)
'''

'''
    youtube_sub()
    youtube_watch()
    youtube_comment()
    twitter_follow()
    twitter_tweet()
    twitter_retweet()
    facebook_like()
'''
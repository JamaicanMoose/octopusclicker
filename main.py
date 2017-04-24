import youtubeapi
#import gleamapi
#import raffleapi
import datetime
from threading import Thread

query_gleam = ['giveaway', 'gleam.io']
query_raffle = ['giveaway', 'rafflecopter.com']
days = 30
cookies = []

def getweeksago(weeks):
    today = datetime.datetime.now()
    deltadate = datetime.timedelta(weeks=weeks)
    lastweek = (today-deltadate).isoformat()
    lastweek1 = lastweek.split('.')[0]
    lastweek2 = lastweek1 + 'Z'
    return lastweek2

def getdaysago(days):
    today = datetime.datetime.now()
    deltadate = datetime.timedelta(days=days)
    yesterday = (today-deltadate).isoformat()
    yesterday1 = yesterday.split('.')[0]
    yesterday2 = yesterday1 + 'Z'
    return yesterday2

def youtubeurlget(query, index, resultslist):
    print("GRABBING: " + query[1] + " " + str(index))
    results = youtubeapi.youtube_search(query, getdaysago(index), getdaysago(index+1))
    resultslist += results
    print("FINISHED GRABBING: " + query[1] + " " + str(index))

def stripyoutube_rafflecopter(query):
    urls = []
    results_raffle = []
    for w in range(0, (days-1)):

        thread = Thread(target=youtubeurlget(query, w, results_raffle), args=(w,))
        thread.start()

        '''
        print("GRABBING RAFFLE" + str(w))
        results = youtubeapi.youtube_search(query, getdaysago(w), getdaysago(w+1))
        results_raffle = results_raffle + results
        '''
    for x in results_raffle:
        desc1 = x.replace('\n', ' ').replace('\r', '').replace('...', ' ')
        urlloc = desc1.find("www.rafflecopter.com/")
        slice_ = desc1[urlloc:]
        split = (slice_.split(' '))[0]
        split2 = split[:46]
        split3 = split2.split('?')[0]
        urls.append(split3)

    for x in range(0, len(urls)+1):
        try:
            if 'www.raff' in urls[x]:
                continue
            else:
                urls.remove(urls[x])
        except IndexError:
            break

    for x in range(0, len(urls) - 1):
        for y in range(x+1, len(urls)):
            if urls[x] in urls[y]:
                urls[x] = '*****'

    for x in range(0, len(urls)):
        try:
            urls.remove('*****')
        except ValueError:
            break
    return urls

def stripyoutube_gleam(query):
    urls = []
    results_gleam = []

    for z in range(0, (days-1)):

        thread = Thread(target=youtubeurlget(query, z, results_gleam), args=(z,))
        thread.start()

    for x in results_gleam:
        desc1 = x.replace('\n', ' ').replace('\r', '').replace('...', ' ')
        print(desc1)
        urlloc = desc1.find("https://gleam.io/")
        slice_ = desc1[urlloc:]
        split = (slice_.split(' '))[0]
        urls.append(split)

    for x in range(0, len(urls) - 1):
        url = urls[x]
        if 'competition' in url:
            urlim = url

        else:
            urlim = url[:22]

        for y in range(x+1, len(urls)):
            if urlim in urls[y]:
                urls[x] = '*****'

    for x in range(0, len(urls)):
        try:
            urls.remove('*****')
        except ValueError:
            break

    for x in range(0, len(urls)):
        try:
            if 'https://' in urls[x]:
                continue
            else:
                urls.remove(urls[x])
        except IndexError:
            break
    for x in range(0, len(urls)):
        try:
            if 'gta' in urls[x]:
                urls.remove(urls[x])
            else:
                continue
        except IndexError:
            break

    return urls

urls_gleam = stripyoutube_gleam(query_gleam)
urls_raffle = stripyoutube_rafflecopter(query_raffle)

print(str(len(urls_gleam) + len(urls_raffle)) + " URLs found for previous " + str(days) + " days.")
overlap = 0
used_gleam = []
used_raffle = []
prev_cont = open('entered_contests').read()

for item in urls_gleam:
    if item in prev_cont:
        overlap += 1
        continue
    else:
        used_gleam.append(item)

for item in urls_raffle:
    if item in prev_cont:
        overlap +=1
        continue
    else:
        used_raffle.append(item)

print(str(overlap) + ' Overlaps')
open('entered_contests', 'a').write("----------\/----------" +
                                    " from " + getdaysago(days)[:10] +
                                    " to " + getdaysago(0)[:10] +
                                    "----------\/----------" + "\n")

for item in used_gleam:
    print(item)

for item in used_gleam:
    open('entered_contests', 'a', encoding="utf8").write("%s\n" % item)

for item in used_raffle:
    open('entered_contests', 'a', encoding="utf8").write("%s\n" % item)

#gleamapi.entercontest(used_gleam)
#raffleapi.entercontest(used_raffle)

print(str((len(used_gleam) + len(used_raffle))) + " contests entered today.")

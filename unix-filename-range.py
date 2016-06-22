import json
import requests
import datetime
g = []
board = "g"
#start, end = input("Start date: "), input("End date: ")
req = requests.get("https://a.4cdn.org/{0}/threads.json".format(board)).json()
##print(json_data)
for pages in req:
    for xxx in pages['threads']:
        #print(xxx['no'])
        g.append(xxx['no'])
for thread in reversed(g):
    try:
        tr = requests.get("https://a.4cdn.org/{0}/thread/{1}.json".format(
            board,thread)).json()
    except :
        print("404'd")
    for posts in tr['posts']:
        try:
            if len(posts['filename']) >=10:
                date = (datetime.datetime.fromtimestamp(
                    int(posts['filename'][0:10])).strftime(
                        '%Y-%m-%d %H:%M:%S'))#+posts['ext'])
                if int(date[0:4]) <= 2010 and int(date[0:4]) > 2003:
                    print(date,posts['filename'])
                    with open('{0}{1}'.format(posts['filename'],posts['ext']),'wb') as f:
                        f.write(requests.get("https://i.4cdn.org/{0}/{1}{2}".format(
                            board,posts['tim'], posts['ext'])).content)                
        except (KeyError , ValueError, OSError):
            no = "picture"

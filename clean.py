import json
from pprint import pprint
data_file = open('tweets.json')
data = []
for tweet in data_file:
    try:
        data.append(json.loads(tweet))
    except:
        pass
print data[1]['text'], data[1]['favorited']
mentions = []
for tweet in data:
    text = tweet['text']
    for c in text:
        if c  == '@':
            #print 'found @'
            i = text.index('@')
            end_name = False
            mention = ''
            while end_name == False:
                if i+1 >= len(text):
                    end_name = True
                    continue
                elif text[i+1]==' ':
                   # print 'found mention'
                    end_name = True
                    continue
                else:
                    if text[i+1] == ':':
                        end_name = True
                        continue
                    else:
                        mention += text[i+1]
                        i+=1
            mentions.append((tweet['user']['screen_name'], mention))
print mentions
        
                
                
    


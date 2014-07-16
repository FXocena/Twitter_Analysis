import json
import sys

def main():
    hashtagCount = {}
    with open(sys.argv[1]) as tweet_file:
    ##with open("output.txt") as tweet_file:
        for line in tweet_file:
            singleTweet = json.loads(line)
            if singleTweet.get(u'text', None) is not None:
                thisEntities = singleTweet.get(u'entities', None)
                if thisEntities is not None:
                    thisHashtag = thisEntities.get(u'hashtags', None)
                    if thisHashtag:
                        for tag in thisHashtag:
                            if tag[u'text'] in hashtagCount.keys():
                                hashtagCount[tag[u'text']] += 1
                            else:
                                hashtagCount[tag[u'text']] = 1
    ten = 10
    topTen = [""]*(ten+1)
    hashtagCount[""] = None
    for key, value in hashtagCount.iteritems():
        topTen[0] = key
        for i in range(ten):
            if value > hashtagCount[topTen[i+1]]:
                topTen[i], topTen[i+1] = topTen[i+1], topTen[i]
            else:
                break
    for key in topTen[:0:-1]:
        print key, hashtagCount[key]
                    
if __name__ == '__main__':
    main()

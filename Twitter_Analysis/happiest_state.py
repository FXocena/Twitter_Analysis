import json
import sys

stateList = {'AL':[0, 0], 'AK':[0, 0], 'AZ':[0, 0], 'AR':[0, 0], 'CA':[0, 0],
             'CO':[0, 0], 'CT':[0, 0], 'DE':[0, 0], 'DC':[0, 0], 'FL':[0, 0],
             'GA':[0, 0], 'HI':[0, 0], 'ID':[0, 0], 'IL':[0, 0], 'IN':[0, 0],
             'IA':[0, 0], 'KS':[0, 0], 'KY':[0, 0], 'LA':[0, 0], 'ME':[0, 0],
             'MD':[0, 0], 'MA':[0, 0], 'MI':[0, 0], 'MN':[0, 0], 'MS':[0, 0],
             'MO':[0, 0], 'MT':[0, 0], 'NE':[0, 0], 'NV':[0, 0], 'NH':[0, 0],
             'NJ':[0, 0], 'NM':[0, 0], 'NY':[0, 0], 'NC':[0, 0], 'ND':[0, 0],
             'OH':[0, 0], 'OK':[0, 0], 'OR':[0, 0], 'PA':[0, 0], 'RI':[0, 0],
             'SC':[0, 0], 'SD':[0, 0], 'TN':[0, 0], 'TX':[0, 0], 'UT':[0, 0],
             'VT':[0, 0], 'VA':[0, 0], 'WA':[0, 0], 'WV':[0, 0], 'WI':[0, 0],
             'WY':[0, 0]}

def sentimentScores(fp):
    scores = {}
    for line in fp:
        term, score = line.split("\t")
        scores[term] = int(score)
    ##print scores.items()
    return scores

def scoreComputer(sentiment_score, singletweet):
    count = 0
    for word in singletweet.split():
        count += sentiment_score.get(word, 0)
    return count
    

def main():
    sent_file  = open(sys.argv[1])
    ##tweet_file = open(sys.argv[2])
    ##sent_file = open("AFINN-111.txt")
    sent_scores = sentimentScores(sent_file)
    sent_file.close()

    happiestTweet = ""
    with open(sys.argv[2]) as tweet_file:
    ##with open("output.txt") as tweet_file:
        for line in tweet_file:
            singleTweet = json.loads(line)
            if singleTweet.get(u'text', None) is not None:
                thisPlace = singleTweet.get(u'place', None)
                if thisPlace is not None:
                    if thisPlace.get(u'country_code', None) == u'US':
                        thisState = thisPlace[u'full_name'].split(', ')[1]
                        if thisState in stateList.keys():
                            newScore = scoreComputer(sent_scores, singleTweet[u'text'])
                            stateList[thisState][0] += 1
                            stateList[thisState][1] += newScore
    maxScore = 0
    happiestState = ""
    for key, value in stateList.iteritems():
        if value[0] > 0:
            if float(value[1])/value[0] > maxScore:
                maxScore = value[1]/value[0]
                happiestState = key
    print happiestState
                    
if __name__ == '__main__':
    main()

import sys
import json

def main():
    termFrequency = {}
    totalCount = 0
    with open(sys.argv[1]) as tweet_file:
    ###with open("problem_1_submission.txt") as tweet_file:
        for line in tweet_file:
            singleTweet = json.loads(line).get(u'text', 0)
            if not singleTweet == 0:
                for word in singleTweet.split():
                    totalCount += 1
                    if not word in termFrequency.keys():
                        termFrequency[word] = 1
                    else:
                        termFrequency[word] += 1
    for key, value in termFrequency.iteritems():
        print key, float(value)/totalCount

if __name__ == '__main__':
    main()

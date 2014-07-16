import sys
import json

def sentimentScores(fp):
    scores = {}
    for line in fp:
        term, score = line.split("\t")
        scores[term] = int(score)
    ##print scores.items()
    return scores

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    ##sent_file = open("AFINN-111.txt")
    sent_scores = sentimentScores(sent_file)
    sent_file.close()
    ##with open('problem_1_submission.txt') as tweet_file:
    with open(sys.argv[2]) as tweet_file:
        for line in tweet_file:
            singleTweet = json.loads(line).get(u'text', None)
            count = 0
            if singleTweet is not None:
                for word in singleTweet.split():
                    count += sent_scores.get(word, 0)
                print count##, singleTweet

if __name__ == '__main__':
    main()

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
    ##sent_file = open("AFINN-111.txt")
    ##tweet_file = open(sys.argv[2])
    sent_scores = sentimentScores(sent_file)
    sent_file.close()

    newSentiment = {}
    with open(sys.argv[2]) as tweet_file:
    ##with open("problem_1_submission.txt") as tweet_file:
        for line in tweet_file:
            singleTweet = json.loads(line).get(u'text', 0)
            if not singleTweet == 0:
                newWordIndex = []
                count = 0
                totalScore = 0.0
                theseWords = singleTweet.split()
                for i in range(len(theseWords)):
                    thisScore = sent_scores.get(theseWords[i], 0)
                    if thisScore == 0:
                        newWordIndex.append(i)
                        if not theseWords[i] in newSentiment.keys():
                            newSentiment[theseWords[i]] = [0, 0]
                    else:
                        count += 1
                        totalScore += thisScore
                for newIndex in newWordIndex:
                    newSentiment[theseWords[newIndex]][0] += count
                    newSentiment[theseWords[newIndex]][1] += totalScore
    for key, value in newSentiment.iteritems():
        if not value[0] == 0:
            print key, float(value[1])/value[0]


if __name__ == '__main__':
    main()


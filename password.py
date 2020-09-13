import random
import requests
from words import words
import secrets

# words



def whichmann_hill(s1, s2, s3):
    s1 = (171 * s1) % 30269
    s2 = (172 * s2) % 30307
    s3 = (170 * s3) % 30323
    return (s1/30269 + s2/30307 + s3/30323) % 1




def generate_password(wordcount, wordlist):
    random_words = [secrets.choice(wordlist) for i in range(wordcount)]
    # random_words = random.shuffle(random_words)

    return ' '.join(random_words)

print(generate_password(8, words))
# for loop from the first word to the word count
    # roll 6 dice
    # concat the numbers together 
    # grab the corresponding word in the dictionary
    # 

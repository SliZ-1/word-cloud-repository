# Start with loading all necessary libraries
import matplotlib
import numpy as np
from os import path
# from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

import matplotlib.pyplot as plt



# Python 3

# Be sure you have followed the instructions to download the 98-0.txt,
# the text of A Tale of Two Cities, by Charles Dickens

import collections

text = open('New text')

# if you want to use stopwords, here's an example of how to do this
# stopwords = set(line.strip() for line in open('stopwords'))
stopwordsfile = open('stopwords')
stopwords = []
for words in stopwordsfile.read().lower().split():
   stopwords.append(words)



# create your data structure here
wordcount={}

# Instantiate a dictionary, and for every word in the file, add to
# the dictionary if it doesn't exist. If it does, increase the count.

# Hint: To eliminate duplicates, remember to split by punctuation,
# and use case demiliters. The functions lower() and split() will be useful!

for word in text.read().lower().split():
  # Create a list of punctuation and go through it and replace all of them with a space
  punctuation = [".", ",", ";", "(", ")", "-", ":", "?", "/", '"', "'"]
  for sign in punctuation:
      word = word.replace(sign, "")

  if word not in stopwords:
      if word not in wordcount:
          wordcount[word] = 1
      else:
          wordcount[word] += 1

# after building your wordcount, you can then sort it and return the first
# n words.  If you want, collections.Counter may be useful.
ordered_words = sorted(wordcount.iteritems(), key=lambda (k,v): -v)

print ordered_words[0:9]


# Create and generate a word cloud image:
contents = open('New text').read()
cloud = WordCloud().generate(contents)

# Display the generated image:
plt.imshow(cloud, interpolation='bilinear')
plt.axis("off")
plt.show()


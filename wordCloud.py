# Python 3

# Be sure you have followed the instructions to download the 98-0.txt,
# the text of A Tale of Two Cities, by Charles Dickens
with open('stopwords') as f:
   mylist = f.read().splitlines()
print(mylist)

import collections
text_file = open('98-0.txt', 'r')

# if you want to use stopwords, here's an example of how to do this
# stopwords = set(line.strip() for line in open('stopwords'))

# create your data structure here.  F
wordcount = {

}

# Instantiate a dictionary, and for every word in the file, add to
# the dictionary if it doesn't exist. If it does, increase the count.

# Hint: To eliminate duplicates, remember to split by punctuation,
# and use case demiliters. The functions lower() and split() will be useful!

for word in text_file.read().lower().split():
   for w in mylist:
       if word == w:
           word = word.replace(word, " ")

       elif word not in mylist:
           if word not in wordcount:
               wordcount[word] = 1
           else:
               wordcount[word] += 1
       if word == " ":
           wordcount[word] = 0

# after building your wordcount, you can then sort it and return the first
# n words.  If you want, collections.Counter may be useful.

d = collections.Counter(wordcount)

# print(d.most_common(10))
for word, count in d.most_common(10):
   print(word + ": " +  str(count))



# Instantiate a dictionary, and for every word in the file, add to
# the dictionary if it doesn't exist. If it does, increase the count.

# Hint: To eliminate duplicates, remember to split by punctuation,
# and use case demiliters. The functions lower() and split() will be useful!

for word in text_file.read().lower().split():
   for w in mylist:
       if word == w:
           word = word.replace(word, " ")

       elif word not in mylist:
           if word not in wordcount:
               wordcount[word] = 1
           else:
               wordcount[word] += 1
       if word == " ":
           wordcount[word] = 0

# after building your wordcount, you can then sort it and return the first
# n words.  If you want, collections.Counter may be useful.

d = collections.Counter(wordcount)

# print(d.most_common(10))
for word, count in d.most_common(10):
   print(word + ": " +  str(count))



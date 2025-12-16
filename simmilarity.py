data1 = '''Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. Its high-level built in data structures, combined with dynamic typing and dynamic binding, make it very attractive for Rapid Application Development, as well as for use as a scripting or glue language to connect existing components together. Python's simple, easy to learn syntax emphasizes readability and therefore reduces the cost of program maintenance. Python supports modules and packages, which encourages program modularity and code reuse. The Python interpreter and the extensive standard library are available in source or binary form without charge for all major platforms, and can be freely distributed.'''
# data2 = '''Python is a popular, high-level, general-purpose programming language known for its simple, readable syntax that resembles English, making it easy for beginners to learn and use for tasks like web development, data science, AI, and automation. It's an interpreted language with a vast collection of libraries, allowing developers to write less code for complex problems and increasing productivity. '''
data2 = ''''''
# tokenization
token1 = set(data1.split())
token2 = set(data2.split())
# remove stopwords
# import nltk
# Natural Language processing Tool Kit
# nltk.download("stopwords")
# print(len(token1),len(token2))
from nltk.corpus import stopwords
sw = set(stopwords.words("english"))
token1.difference_update(sw)
token2.difference_update(sw)
# print(len(token1),len(token2))

# JI - Jaccards Index
inter = token1.intersection(token2)
uni = token1.union(token2)

print(len(inter)/len(uni)*100)

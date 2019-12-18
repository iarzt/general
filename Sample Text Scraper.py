from string import punctuation

def count_words(f):
    d = {}
    file = open(f, "r")
    for line in file:
        line = line.split()
        for word in line:
            word = strip_punctuation(word)
            word = word.lower()
            if word in d:
                d[word] += 1
            elif word in stop_words:
                pass
            else:
                d[word] = 1           
    return d
            
stop_words = {"a","am","an", "and","are", "as", "at",
              "be","but", "by", "for", "i", "if", "in", "into",
              "is", "it", "its", "my", "nor", "not", "of", "on",
              "or", "so", "than", "that", "the", "then", "this",
              "to", "too", "will", "with"}

def strip_punctuation(s):
    return ''.join(c for c in s if c not in punctuation)

def print_word_count(dictionary, word):
    print("Count of \"" + word + "\" is:", dictionary[word])

def find_max(d):
    max1 = 0
    maxs = ""
    for word in d:
        frequency = d[word]
        if frequency > max1:
            max1 = frequency
            maxs = word
    return maxs, max1

def main():
   
    d = count_words("raven.txt")
    string, count = find_max(d)
    
    print_word_count(d, string)
    print_word_count(d, "raven")
    print_word_count(d, "nevermore")
        
        
    

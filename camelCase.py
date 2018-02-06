
def camel_case(sentence):
    sentenceList = sentence.split()
    collector = ""
    for x in range(len(sentenceList)):
        if x == 0:
            collector+= sentenceList[x].lower()
        else:
            word = sentenceList[x]
            firstLetter = word[0]
            remLetters = word[1:]
            collector+=firstLetter.upper()+remLetters.lower()
    return collector

#define main function
def main():
    #call the display function
    '''display_banner()'''
    #call the function and assigns it to a sentence variable.
    '''sentence = instructions()'''
    sentence = input('Enter your sentence: ') #this line added
    #split the sentence into a list. it removes all the spaces, keeps
    #only the words and put them in a list.
    '''sentenceList = sentence.split()'''
    #set an empty collector to collect string
    camelCased = camel_case(sentence)
    print(camelCased)

if __name__ == '__main__':
    main()

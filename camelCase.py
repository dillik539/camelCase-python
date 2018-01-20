#define main function
def main():
    #call the display function
    display_banner()
    #call the function and assigns it to a sentence variable.
    sentence = instructions()
    #split the sentence into a list. it removes all the spaces, keeps
    #only the words and put them in a list.
    sentenceList = sentence.split()
    #set an empty collector to collect string
    collector = ""
    for x in range(len(sentenceList)):
        if x == 0:
            collector+= sentenceList[x].lower()
        else:
            word = sentenceList[x]
            firstLetter = word[0]
            remLetters = word[1:]
            collector+=firstLetter.upper()+remLetters.lower()
    print(collector)

#define display function
def display_banner():
    '''Display program name in a banner'''
    msg = 'AWESOME CamelCaseGenerator PROGRAM'
    stars = '*' * len(msg)
    print('\n', stars, '\n', msg, '\n', stars, '\n')
#this function instructs the user to enter the sentence of user's choice
#and return that sentence.
def instructions():
    print("Enter a sentence to convert to camelcase.")
    inputSentence = input("Enter your sentence: ")
    return inputSentence

main()

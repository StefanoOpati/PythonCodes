def words():

    
    sentence=input('Enter a sentence:')

    new_sentence=sentence.split()

    print(new_sentence)
    wordCount=len(new_sentence)

    print('The total nummber of words is:%s' %wordCount)
    
    
    
words()

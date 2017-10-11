def words():

    
    sentence=input('Enter a sentence:').strip()

    new_sentence=sentence.split(' ')

    print(new_sentence)
   # print("The number of words in this sentence is: %s" % len(new_sentence))
    
    wordCount={}
    for eachWord in new_sentence:
       if eachWord in wordCount.keys():
           wordCount[eachWord]+=1
       else:
           wordCount[eachWord]=1
    wordcount=len(new_sentence)
        
       
    print('The total nummber of words is:%s' % wordcount)
    print(wordCount)
    
    
words()

def word_frequency(sentence):
    words = sentence.split()   
    frequency = {}
    for word in words:        
        word = word.strip('.,!?')
       
        word = word.lower()
                
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    
    return frequency


sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)


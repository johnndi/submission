#Write a program that counts the number of vowels in a sentence.

def count_unique_vowels(sentence):
        
    sentence = sentence.lower()
    
    
    unique_vowels = set()
    
    
    vowels = {'a', 'e', 'i', 'o', 'u'}
    
    
    for char in sentence:
    
        if char in vowels:
            
            unique_vowels.add(char)
    
    
    return len(unique_vowels)


sentence = input("Enter a sentence: ")
print("Number of  vowels:", count_unique_vowels(sentence))

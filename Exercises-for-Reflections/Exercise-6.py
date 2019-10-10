#Week 6 Exercise for Reflection 10/9/19
Removing Vowels

#%%

def devowel(randomthingminusvowels):
    List = list(randomthingminusvowels)
    vowels=["a","e","i","o","u"]
    for letter in List:
        if letter.lower () in vowels:
            List.remove(letter)
    randomthingminusvowels = ''.join(List)
    return randomthingminusvowels

 



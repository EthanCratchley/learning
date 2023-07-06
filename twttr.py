inpoot = input("Input: ")
outpoot = "" #store outpoot without vowels
vowels = "AEIOU"  #identifies vowels to remove

for n in inpoot: #loop to go over each character
    if n.upper() not in vowels: #put in uppercase
        outpoot += n #adds to string if not vowel

print("Output:", outpoot.strip()) #stripss the AEIOU and prints the new outpoot
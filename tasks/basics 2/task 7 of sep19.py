text = input("give me a word: ")


freq = {}
for ch in text:
    if ch.isalpha():
        ch = ch.lower()
        if ch not in freq:
            freq[ch] = 1
        else:
            freq[ch] += 1


most_freq = ""
max_count = 0
for ch in freq:
    if freq[ch] > max_count:
        max_count = freq[ch]
        most_freq = ch
        
print()
print("Number of repititions of each letter: \n", freq)
print()
print("The most repeated letter:", most_freq, " with amount of ", max_count)

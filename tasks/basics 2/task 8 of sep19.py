#n = int(input("enter the stage: "))


##def factorial(x):
    #result = 1
   # for i in range(1, x+1):
  #      result *= i
 #   return result


#total = 0
#for i in range(1, n+1):
 #   total += factorial(i)

#print()
##print("the answer is: ", total)##






def group_anagrams(words):
    groups = {}
    
    for word in words:
        key = ''.join(sorted(word))
        
        if key not in groups:
            groups[key] = []
        groups[key].append(word)
    
    return list(groups.values())


test_words = ["eat", "tea", "tan", "ate", "nat", "bat", "listen", "silent"]
result = group_anagrams(test_words)

print("Input:", test_words)
print("Anagram groups:")
for i, group in enumerate(result, 1):
    print(f"Group {i}: {group}")




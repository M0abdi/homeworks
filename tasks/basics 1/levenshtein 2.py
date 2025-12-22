def levenshtein_distance(str1, str2):
   
    len1, len2 = len(str1), len(str2)
    matrix = [[0] * (len2 + 1) for _ in range(len1 + 1)]
    
    
    for i in range(len1 + 1):
        matrix[i][0] = i
    for j in range(len2 + 1):
        matrix[0][j] = j
    

    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if str1[i-1] == str2[j-1]:
                cost = 0
            else:
                cost = 1
            
            matrix[i][j] = min(
                matrix[i-1][j] + 1,      
                matrix[i][j-1] + 1,      
                matrix[i-1][j-1] + cost  
            )
    
    return matrix[len1][len2]


print("Levenshtein Distance Calculator")
print("")
string1 = input("Enter the first string: ")
print("")
string2 = input("Enter the second string: ")


len1 = len(string1)
len2 = len(string2)
distance = levenshtein_distance(string1, string2)


print(f"\n Analysis Results:")
print("")
print(f"String 1: '{string1}'")
print("")
print(f"String 1 length: {len1} characters")
print("")
print(f"String 2: '{string2}'")
print("")
print(f"String 2 length: {len2} characters")
print("")
print(f"Levenshtein distance: {distance}")

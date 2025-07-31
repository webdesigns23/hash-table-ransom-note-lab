def can_construct(ransomNote, magazine):
    letter_count = {}

    for char in magazine:
        if char in letter_count:
            letter_count[char] += 1
        else:
            letter_count[char] = 1
    print(f"Magazine Letter Count: {letter_count}") 
    

    for char in ransomNote:
        if char in letter_count and letter_count[char] > 0:
            letter_count[char] -= 1
        else:
            return False
    print(f"Random Note Letter Count: {letter_count}")  
    
    return True
    
# Testing:
print(can_construct("LooneyLuna", "LunaLooneyandPew"))
print(can_construct("LooneyLuna", "LunaandPew"))

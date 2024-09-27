test_dict = {
    "Codingal":3 ,
    "is": 2, 
    "best": 2 ,
    "for":2, 
    "Coding": 1
    }

print("The Original Dictionary :", test_dict)

k = int(input("Enter the Frequency:"))

res = 0

for key in test_dict:
    if test_dict[key] == k:
        
        res = res+1
        
print("Frequency of k is :", res)
        
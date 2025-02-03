import random

with open ("programa 2/fileWithData.txt", "w") as file:
    for i in range(100):        
        file.write(str(random.randint(1,1000)) + "\n")                            
        
file.close()

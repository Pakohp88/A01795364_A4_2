import random

with open ("programa 1/fileWithData.txt", "w") as file:
    for i in range(100):
        for j in range(100):
            if j < 99:
                file.write(str(random.randint(1,1000)) + " ")
            else:
                file.write(str(random.randint(1,1000)))
        file.write("\n")
file.close()

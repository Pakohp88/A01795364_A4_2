import sys
import os
import time

start_time = time.time()
path = sys.argv[1]

if not os.path.exists(path=path):
    print("File not found")
    print(f"execution time: {time.time() - start_time} seconds")
else:
    with  open("WordCountResults.txt", "w") as file_result:
        with  open(path, "r") as file:
            words = []
            duplicate_words = []
            unique_words = []
            X_COUNTE = 0
            for line in file:
                word = line.strip()
                if "x" in word:
                    X_COUNTE += 1
                if word in words:
                    duplicate_words.append(word)
                words.append(word)
            for word in words:
                if not word in duplicate_words:
                    unique_words.append(word)
            HEADER = "Unique words: "
            print(HEADER)
            file_result.write(HEADER)
            RESULT = ""
            for word in unique_words:
                RESULT += f"{word} "            
            file_result.write(f"{RESULT} \n")
            print(RESULT)
            RESULT_COUNTER_X = f"X´s found: {X_COUNTE}"
            print(RESULT_COUNTER_X)
            file_result.write(RESULT_COUNTER_X)
        execution_time = time.time() - start_time
        file_result.write(f"execution time {execution_time}")
    print(f"execution time: {execution_time} seconds")

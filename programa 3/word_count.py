"""Word Count"""
import sys
import os
import time
start_time = time.time()
path = sys.argv[1]
if not os.path.exists(path=path):
    print("File not found")
    print(f"execution time: {time.time() - start_time} seconds")
else:
    with open(path, "r",encoding="UTF8") as file:
        with  open(f"{file.name[:3]}.WordCountResults.txt", "w", encoding="UTF8") as file_result:
            words = []
            unique_words = []
            duplicate_words = []
            X_COUNTE = 0
            for line in file:
                word = line.strip()
                if "x" in word:
                    X_COUNTE += 1
                if word in words and word not in duplicate_words:
                    duplicate_words.append(word)
                words.append(word)
            for word in words:
                if not word in unique_words:
                    unique_words.append(word)
            HEADER = f"WORD       COUNT of {file.name[:3]}\n"
            print(HEADER)
            file_result.write(HEADER)
            for word in unique_words:
                COUNTER = 1
                if word in duplicate_words:
                    COUNTER = 0
                    for w in words:
                        if word == w:
                            COUNTER+=1
                file_result.write(f"{word}              {COUNTER}\n")
                print(word)
            RESULT_COUNTER_X = f"X´s found: {X_COUNTE}"
            print(RESULT_COUNTER_X)
            file_result.write(f"{RESULT_COUNTER_X}\n")
            execution_time = time.time() - start_time
            file_result.write(f"execution time {execution_time}")
    print(f"execution time: {execution_time} seconds")

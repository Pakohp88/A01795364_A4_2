"""Compute statics"""
from math import sqrt
import sys
import os
import time

start_time = time.time()
path = sys.argv[1]
if not os.path.exists(path=path):
    print("File not found")
    print(f"execution time: {time.time() - start_time} seconds")
else:
    with open ("StatisticsResults.txt", "a", encoding="UTF8") as file_result:
        with  open(path, "r",encoding="UTF8") as file:
            numbers = []
            for line in file:
                try:
                    if not "." in line:
                        n = int(line)
                        numbers.append(n)
                    else:
                        n = float(line)
                        numbers.append(n)
                except ValueError:
                    continue
            NUMBEROFELEMENTS = len(numbers)
            #mean
            mean = sum(numbers) / NUMBEROFELEMENTS
            #meadian
            numbers.sort()
            MEDIAN = 0
            if NUMBEROFELEMENTS % 2 != 0:
                MEDIAN = numbers[NUMBEROFELEMENTS // 2]
            else:
                MEDIAN = (numbers[(NUMBEROFELEMENTS // 2) - 1]+
                          numbers[NUMBEROFELEMENTS // 2]) / 2
            #mode
            frecuency = {}
            for num in numbers:
                if num in frecuency:
                    frecuency[num] += 1
                else:
                    frecuency[num] = 1
            max_frecuency = max(frecuency.values())
            mode = [num for num, freq in frecuency.items() if freq == max_frecuency]
            #standard desviation
            SUM_DS = 0
            for i in numbers:
                SUM_DS +=(i-mean)**2
            standard_desviation = sqrt(SUM_DS/(NUMBEROFELEMENTS-1))
            #variance
            sum_diferences = sum((x - mean) ** 2 for x in numbers)
            variance = sum_diferences / NUMBEROFELEMENTS
            file_result.write("\n")
            file_result.write(f"File Name: {file.name[:3]}\n")
            file_result.write(f"Mean: {mean}\n")
            file_result.write(f"Median: {MEDIAN}\n")
            file_result.write(f"Mode:{mode}\n")
            file_result.write(f"Standard Desviation:{standard_desviation}\n")
            file_result.write(f"Variance:{variance}\n")
            file_result.write("--------------------")
            print(f"File Name: {file.name[:3]}")
            print(f"Mean: {mean}")
            print(f"Median: {MEDIAN}")
            print(f"Mode:{mode}")
            print(f"Standard Desviation:{standard_desviation}")
            print(f"Variance:{variance}")
            print("******************************")
        execution_time = time.time() - start_time
        file_result.write(f"execution time {execution_time}")
print(f"execution time: {execution_time} seconds")

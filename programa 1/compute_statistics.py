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
    NUMBER_LINE = 1
    with open ("StatisticsResults.txt", "w") as file_result:
        with  open(path, "r") as file:
            for line in file:
                numbers = []
                line_split = line.split(" ")
                for number in line_split:
                    n = int(number.strip())
                    numbers.append(n)
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
                varince = sum_diferences / NUMBEROFELEMENTS
                RESULT = f"data result line {NUMBER_LINE} : mean: {mean} median: {MEDIAN}  mode: {mode} standard desviation: {standard_desviation} variance: {varince}"
                file_result.write(RESULT)
                file_result.write("\n")
                print(RESULT)
                print("******************************")
            NUMBER_LINE = NUMBER_LINE + 1
        execution_time = time.time() - start_time
        file_result.write(f"execution time {execution_time}")
    print(f"execution time: {execution_time} seconds")

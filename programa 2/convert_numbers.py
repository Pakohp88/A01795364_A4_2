import sys
import os
import time

start_time = time.time()
path = sys.argv[1]
if not os.path.exists(path=path):
    print("File not found")
    print(f"execution time: {time.time() - start_time} seconds")
else:
    with open ("ConvertionResults.txt", "w") as file_result:
        with  open(path, "r") as file:
            for line in file:
                line_split = line.split(" ")
                for number in line_split:
                    n = int(number.strip())
                    #binary
                    numer_to_binary = n
                    BINARY_NUMBER = ""
                    if numer_to_binary == 0:
                        BINARY_NUMBER = "0"
                    else:
                        binary = []
                        while numer_to_binary > 0:
                            rest = numer_to_binary % 2
                            binary.append(str(rest))
                            numer_to_binary = numer_to_binary // 2
                        BINARY_NUMBER = ''.join(binary[::-1])
                    #hex
                    HEX_NUMBER = ""
                    numer_to_hex = n
                    if numer_to_hex == 0:
                        HEX_NUMBER = "0"
                    else:
                        HEX_DIGITS = "0123456789ABCDEF"
                        hexadecimal = []
                        while numer_to_hex > 0:
                            rest = numer_to_hex % 16
                            hexadecimal.append(HEX_DIGITS[rest])
                            numer_to_hex = numer_to_hex // 16
                    HEX_NUMBER = ''.join(hexadecimal[::-1])
                    RESULT = f"{n} binary: {BINARY_NUMBER} hexadecimal: {HEX_NUMBER}"
                    file_result.write(RESULT)
                    file_result.write("\n")
                    print(RESULT)
        execution_time = time.time() - start_time
        file_result.write(f"execution time {execution_time}")
    print(f"execution time: {execution_time} seconds")
    
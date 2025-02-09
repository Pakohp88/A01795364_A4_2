"""Convert Number"""
import sys
import os
import time

start_time = time.time()
path = sys.argv[1]
if not os.path.exists(path=path):
    print("File not found")
    print(f"execution time: {time.time() - start_time} seconds")
else:
    with open ("ConvertionResults.txt","a",encoding="UTF8") as file_result:
        with  open(path,"r",encoding="UTF8") as file:
            file_result.write(f"\nFile Name: {file.name[:3]}\n")
            for line in file:
                line_split = line.split(" ")
                for number in line_split:
                    try:
                        n = int(number)
                    except ValueError:
                        print(f"cannot be converted to number \"{line}\"")
                        continue
                    BINARY_NUMBER = ""
                    HEX_NUMBER = ""
                    if n >= 0:
                        #binary
                        numer_to_binary = n
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
                        numer_to_hex = n
                        if numer_to_hex == 0:
                            HEX_NUMBER = "0"
                        else:
                            HEX_DIGITS = "0123456789ABCDEF"
                            HEXADECIMAL = []
                            while numer_to_hex > 0:
                                rest = numer_to_hex % 16
                                HEXADECIMAL.append(HEX_DIGITS[rest])
                                numer_to_hex = numer_to_hex // 16
                        HEX_NUMBER = ''.join(HEXADECIMAL[::-1])
                    else:
                        ABSOLUTE_VALUE = abs(n)
                        BIN = ""
                        while ABSOLUTE_VALUE > 0:
                            BIN = str(ABSOLUTE_VALUE % 2) + BIN
                            ABSOLUTE_VALUE = ABSOLUTE_VALUE // 2
                        BIN = BIN.zfill(8 - 1)
                        COMPLEMENT_TO_ONE = ''.join('1' if bit == '0' else '0' for bit in BIN)
                        COMPLEMENT_TO_TWO = ""
                        CARRY = 1
                        for bit in reversed(COMPLEMENT_TO_ONE):
                            suma = int(bit) + CARRY
                            COMPLEMENT_TO_TWO = str(suma % 2) + COMPLEMENT_TO_TWO
                            CARRY = suma // 2
                        if CARRY == 1:
                            COMPLEMENT_TO_TWO = '1' + COMPLEMENT_TO_TWO
                        BINARY_NUMBER = COMPLEMENT_TO_TWO.zfill(8)
                        #HEX
                        COMPLEMENT = ''.join('1' if bit == '0' else '0' for bit in BINARY_NUMBER)
                        COMEPLEMENT_TWO = ""
                        CARRY_HEX = 1
                        for bit in reversed(COMPLEMENT):
                            suma = int(bit) + CARRY_HEX
                            COMEPLEMENT_TWO = str(suma % 2) + COMEPLEMENT_TWO
                            CARRY_HEX = suma // 2
                        if CARRY_HEX == 1:
                            COMEPLEMENT_TWO = '1' + COMEPLEMENT_TWO
                        COMEPLEMENT_TWO = COMEPLEMENT_TWO.zfill(8)
                        HEXADECIMAL = ""
                        for i in range(0, len(COMEPLEMENT_TWO), 4):
                            nibble = COMEPLEMENT_TWO[i:i+4]
                            if nibble == '0000':
                                HEXADECIMAL += '0'
                            elif nibble == '0001':
                                HEXADECIMAL += '1'
                            elif nibble == '0010':
                                HEXADECIMAL += '2'
                            elif nibble == '0011':
                                HEXADECIMAL += '3'
                            elif nibble == '0100':
                                HEXADECIMAL += '4'
                            elif nibble == '0101':
                                HEXADECIMAL += '5'
                            elif nibble == '0110':
                                HEXADECIMAL += '6'
                            elif nibble == '0111':
                                HEXADECIMAL += '7'
                            elif nibble == '1000':
                                HEXADECIMAL += '8'
                            elif nibble == '1001':
                                HEXADECIMAL += '9'
                            elif nibble == '1010':
                                HEXADECIMAL += 'A'
                            elif nibble == '1011':
                                HEXADECIMAL += 'B'
                            elif nibble == '1100':
                                HEXADECIMAL += 'C'
                            elif nibble == '1101':
                                HEXADECIMAL += 'D'
                            elif nibble == '1110':
                                HEXADECIMAL += 'E'
                            elif nibble == '1111':
                                HEXADECIMAL += 'F'
                        HEX_NUMBER = HEXADECIMAL.upper()
                    RESULT = f"{n} binary: {BINARY_NUMBER} hexadecimal: {HEX_NUMBER}"
                    file_result.write(RESULT)
                    file_result.write("\n")
                    print(RESULT)
        execution_time = time.time() - start_time
        file_result.write(f"execution time {execution_time}\n")
        file_result.write("****************************************")
    print(f"execution time: {execution_time} seconds")
    
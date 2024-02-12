import os
import time

class Comp2Converter:
    
    @staticmethod
    def evaluate(value):
        bits = 0
        if -8 <= value <= 7:
            bits = 4
        elif -128 <= value <= 127:
            bits = 8
        elif -2048 <= value <= 2047:
            bits = 12
        elif -32768 <= value <= 32767:
            bits = 16
        return bits

    @staticmethod
    def subtrair1(value):
        digit = list(value)
        carry = 1
        for i in range(len(value) - 1, -1, -1):
            if carry > 0:
                if digit[i] == "0":
                    digit[i] = "1"
                elif digit[i] == "1":
                    digit[i] = "0"
                    carry = 0
        return digit

    @staticmethod
    def sum1(value):
        digit = list(value)
        carry = 1
        for i in range(len(digit) - 1, -1, -1):
            if carry > 0:
                if digit[i] == '0':
                    digit[i] = '1'
                    carry = 0
                elif digit[i] == '1':
                    digit[i] = '0'
        return digit

    @staticmethod
    def returnString(value):
        return ''.join(value)

    @staticmethod
    def comp2DecimalBinary(value):
        vector = []
        sinal = 1
        if value < 0:
            sinal = -1
            value = abs(value)

        bit = Comp2Converter.evaluate(value)

        while value != 0:
            rest = value % 2
            quotient = value // 2
            value = quotient
            vector.append(rest)

        binary = "".join(str(vector[i]) for i in range(len(vector) - 1, -1, -1))

        counterBits = len(binary)
        while counterBits < bit:
            binary = "0" + binary
            counterBits += 1

        if sinal > 0:
            return binary
        else:
            binary = Comp2Converter.subtrair1(binary)
            binary = ''.join('1' if bit == '0' else '0' for bit in binary)
            binary = Comp2Converter.returnString(binary)
            return binary

    @staticmethod
    def comp2BinaryDecimal(value):
        value = ''.join('1' if bit == '0' else '0' for bit in value)
        value = Comp2Converter.sum1(value)
        counter = 0
        decimal = 0
        value = Comp2Converter.returnString(value)

        if value[0] == '0':
            sinal = -1
        else:
            sinal = 1

        value = value[1:]
        for i in range(len(value) - 1, -1, -1):
            decimal += int(value[i]) * (2 ** counter)
            counter += 1

        return decimal * sinal

    @staticmethod
    def runDB(value):
        
        resultValue = Comp2Converter.comp2DecimalBinary(value)
        return resultValue

    @staticmethod
    def runBD(value):
        
        resultValue = Comp2Converter.comp2BinaryDecimal(value)
        return resultValue

    @staticmethod
    def run():
        while True:
            print()
            print("User choose:")
            print("[1] - Comp2 - Convert Decimal to Binary: ")
            print("[2] - Comp2 - Convert Binary to Decimal: ")
            print("[3] - Shutting Down: ")

            valueUser = int(input("Choose: "))
            os.system('clear')

            if valueUser == 1:
                value = int(input("Enter the decimal value: "))
                resultValue = Comp2Converter.comp2DecimalBinary(value)
                print(f"Value: {value} - Result: {resultValue}")
            elif valueUser == 2:
                value = input("Enter the binary value: ")
                resultValue = Comp2Converter.comp2BinaryDecimal(value)
                print(f"Binary Value: {value} - Result Decimal: {resultValue}")
            elif valueUser == 3:
                break
            else:
                print("Invalid choice.")
                
#######################################################


#######################################################

class realConvert:
    
    @staticmethod
    #convert decimal in binary
    def realRealBinary(value, precision):
        sinal = 1
        if(value < 0):
            sinal = -1
            value = abs(value)
            
        Int = int(value)
        Frac = abs(value - Int)

        part_Int = ""
        part_Frac = ""

        if(Int == 0):
            part_Int = "0"
        else:
            while(Int > 0):
                part_Int += str(Int % 2)
                Int //= 2
        part_Int = part_Int[::-1]

        while(precision > 0):
            Frac = Frac * 2
            valueB = int(Frac)
            part_Frac += str(valueB)
            Frac -= valueB
            precision-= 1

        return part_Int + "." + part_Frac

    @staticmethod
    def realBinaryDecimal(binary):
        parts = binary.split(".")
        part_int = parts[0]
        part_frac = parts[1]

        Int = 0
        Frac = 0

        #part_int
        counter = 0
        for i in range(len(part_int)- 1, -1, -1):
            Int += (int(part_int[i]))*(2 ** counter)
            counter += 1

        #part_frac
        counter = -1
        for i in range(len(part_frac)):
            Frac += (int(part_frac[i]))*(2 ** counter)
            counter -= 1

        return (Int + Frac)
    
    @staticmethod
    def runRB(valueReal, precision):
        valueFinal = str(realConvert.realRealBinary(valueReal, precision))
        return valueFinal
    
    @staticmethod
    def runBR(valueReal):
        valueFinal = str(realConvert.realBinaryDecimal(valueReal))
        return valueFinal
    
    @staticmethod
    def test():
        valueUser = 1
        while(valueUser != 0):

            print("[0] - exit program: ")
            print("[1] - convert real decimal in binary: ")
            print("[2] - convert real binary in decimal: ")
            valueUser = int(input("choice: "))
            print()

            match (valueUser):
                case 1:
                    valueReal = float(input("Pass the value in decimal: "))
                    precision = int(input("Accuracy to how many decimal places: "))
                    valueFinal = str(realConvert.realDecimalBinary(valueReal, precision))
                    print(f"binary: {valueFinal}")
                    print()
                    print("[0] - step out: ")
                    print("[1] - convert binary in decimal: ")
                    choiceUser = int(input("Pass the value: "))
                    match (choiceUser):
                        case 1:
                            print("decimal convert: ", realConvert.realBinaryDecimal(valueFinal))
                            print()
                        case 0:
                            print()
                case 2:
                    valueReal = str(input("Pass the value in binary: "))
                    print(f"decimal: {realConvert.realBinaryDecimal(valueReal)}")
                    print()
                    print("[0] - step out: ")
                    print("[1] - convert decimal in binary: ")
                    choiceUser = int(input("Pass the value: "))
                    match (choiceUser):
                        case 1:
                            precision = int(input("Accuracy to how many decimal places: "))
                            print("decimal convert: ", realConvert.realDecimalBinary(valueFinal, precision))
                            print()
                        case 0:
                            print()
                            
            if(valueUser == 0):
                print("------ Shutting down -------")
            else:
                time.sleep(10)
                os.system('clear')
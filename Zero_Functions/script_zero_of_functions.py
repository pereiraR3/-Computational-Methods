class tabel1:
    
    def __init__(self):
        
        self.valueK = 0
        self.valueA = 0
        self.valueB = 0
        self.valueX = 0
        self.valueFuncA = 0
        self.valueFuncB = 0
        self.valueFuncX = 0
        self.difAB = 0
    
class tabel2:
    
    def __init__(self):
        
        self.valueK = 0
        self.valueA = 0
        self.valueB = 0
        self.valueX = 0
        self.valueX0 = 0
        self.valueX1 = 0
        self.valueX2 = 0
        self.valueFuncA = 0
        self.valueFuncB = 0
        self.valueFuncX = 0
        self.difAB = 0

class application:
    
    def __init__(self):
        self.vectorTabel = []
        self.flag = 0
        self.index = 0
    
    def insert_data1(self, valueK, valueA, valueB, valueX, funcA, funcB, funcX):
        
        self.valuesFunc = tabel1()
        self.valuesFunc.valueK = valueK
        self.valuesFunc.valueA = valueA
        self.valuesFunc.valueB = valueB
        self.valuesFunc.valueX = valueX
        self.valuesFunc.valueFuncA = funcA
        self.valuesFunc.valueFuncB = funcB
        self.valuesFunc.valueFuncX = funcX
        self.valuesFunc.difAB = abs(valueA - valueB)
        self.vectorTabel.append(self.valuesFunc)
        
    def insert_data2(self, valueK, valueA, valueB, valueX, valueX0, valueX1, valueX2, funcA, funcB, funcX):
        
        self.valuesFunc = tabel2()
        self.valuesFunc.valueK = valueK
        self.valuesFunc.valueA = valueA
        self.valuesFunc.valueB = valueB
        self.valuesFunc.valueX = valueX
        self.valuesFunc.valueX0 = valueX0
        self.valuesFunc.valueX1 = valueX1
        self.valuesFunc.valueX2 = valueX2
        self.valuesFunc.valueFuncA = funcA
        self.valuesFunc.valueFuncB = funcB
        self.valuesFunc.valueFuncX = funcX
        self.valuesFunc.difAB = abs(valueA - valueB)
        self.vectorTabel.append(self.valuesFunc)
        
    def bissec_method(self, valueA, valueB, choose):
        
        while True:
            
            if(choose == 1):
                
                funcA = 7 * pow(valueA, 3) - pow(valueA, 2) - 28 * valueA + 4
                funcB = 7 * pow(valueB, 3) - pow(valueB, 2) - 28 * valueB + 4
                valueX = (valueA + valueB) / 2
                funcX = 7 * pow(valueX, 3) - pow(valueX, 2) - 28 * valueX + 4
                
                self.insert_data1(self.index, valueA, valueB, valueX, funcA, funcB, funcX)
                
                if funcX > 0:
                    valueA = valueX
                else:
                    valueB = valueX
                    
                if abs(valueA - valueB) > pow(10, -5):
                    self.index += 1
                else:
                    break
                
            elif(choose == 2):
                
                funcA = 6 * pow(valueA, 4) - 7 * pow(valueA, 3) - 33 * pow(valueA, 2) + 33 * valueA + 15
                funcB = 6 * pow(valueB, 4) - 7 * pow(valueB, 3) - 33 * pow(valueB, 2) + 33 * valueB + 15
                valueX = (valueA + valueB) / 2
                funcX = 6 * pow(valueX, 4) - 7 * pow(valueX, 3) - 33 * pow(valueX, 2) + 33 * valueX + 15

                self.insert_data1(self.index, valueA, valueB, valueX, funcA, funcB, funcX)
                
                if funcX > 0:
                    valueA = valueX
                else:
                    valueB = valueX
                    
                if abs(valueA - valueB) > pow(10, -7):
                    self.index += 1
                else:
                    break
            
        self.show_methodStart1()

    def posFalse_method(self, valueA, valueB, choose):
        
        while True:
            # x = a*f(b) - b*f(a)/f(b) - f(a)
            if(choose == 1):
                
                funcA = 7 * pow(valueA, 3) - pow(valueA, 2) - 28 * valueA + 4
                funcB = 7 * pow(valueB, 3) - pow(valueB, 2) - 28 * valueB + 4
                valueX = (valueA*(7 * pow(valueB, 3) - pow(valueB, 2) - 28 * valueB + 4) - valueB*((7 * pow(valueA, 3) - pow(valueA, 2) - 28 * valueA + 4))) / ((7 * pow(valueB, 3) - pow(valueB, 2) - 28 * valueB + 4) - (7 * pow(valueA, 3) - pow(valueA, 2) - 28 * valueA + 4))
                funcX = 7 * pow(valueX, 3) - pow(valueX, 2) - 28 * valueX + 4
                
                if(abs(funcX) > pow(10, -6)):
                    self.insert_data1(self.index, valueA, valueB, valueX, funcA, funcB, funcX)
                    
                    if funcX > 0:
                        valueA = valueX
                    else:
                        valueB = valueX
                        
                    if abs(valueA - valueB) > pow(10, -5):
                        self.index += 1
                    else:
                        break
                else:
                    self.insert_data1(self.index, valueA, valueB, valueX, funcA, funcB, funcX)
                    break
                
            elif(choose == 2):
                
                funcA = 6 * pow(valueA, 4) - 7 * pow(valueA, 3) - 33 * pow(valueA, 2) + 33 * valueA + 15
                funcB = 6 * pow(valueB, 4) - 7 * pow(valueB, 3) - 33 * pow(valueB, 2) + 33 * valueB + 15
                valueX = (valueA*(6 * pow(valueB, 4) - 7 * pow(valueB, 3) - 33 * pow(valueB, 2) + 33 * valueB + 15) - valueB*(6 * pow(valueA, 4) - 7 * pow(valueA, 3) - 33 * pow(valueA, 2) + 33 * valueA + 15)) / ((6 * pow(valueB, 4) - 7 * pow(valueB, 3) - 33 * pow(valueB, 2) + 33 * valueB + 15) - (6 * pow(valueA, 4) - 7 * pow(valueA, 3) - 33 * pow(valueA, 2) + 33 * valueA + 15))
                funcX = 6 * pow(valueX, 4) - 7 * pow(valueX, 3) - 33 * pow(valueX, 2) + 33 * valueX + 15
                
                if(abs(funcX) > pow(10, -7)):
                    self.insert_data1(self.index, valueA, valueB, valueX, funcA, funcB, funcX)
                
                    if funcX > 0:
                        valueA = valueX
                    else:
                        valueB = valueX
                        
                    if abs(valueA - valueB) > pow(10, -7):
                        self.index += 1
                    else:
                        break
                else:
                    self.insert_data1(self.index, valueA, valueB, valueX, funcA, funcB, funcX)
                    break

        self.show_methodStart1()
    
    def newton_method(self, choose, valueA, valueB):
        
        x0 = (valueA + valueB)/2
        
        while True:
            
            self.index += 1
            
            if(choose == 1):
                
                funcA = (7 * pow(valueA, 3) - pow(valueA, 2) - 28 * valueA + 4)
                funcB = (7 * pow(valueB, 3) - pow(valueB, 2) - 28 * valueB + 4)
                funcX = (7 * pow(x0, 3) - pow(x0, 2) - 28 * x0 + 4)
                
                if(abs(funcX) < pow(10, -5)):
                
                    x = x0
                    self.insert_data1(self.index, valueA, valueB, x, funcA, funcB, funcX)
                    break
                
                else:
                    
                    x = x0 - (7 * pow(x0, 3) - pow(x0, 2) - 28 * x0 + 4)/(21* pow(x0, 2) - 2 * x0 - 28)
                    funcX = (7 * pow(x, 3) - pow(x, 2) - 28 * x + 4)
                    
                    self.insert_data1(self.index, valueA, valueB, x, funcA, funcB, funcX)
                    
                    if (abs(funcX) < pow(10, -5) or abs(x - x0) < pow(10, -6)):
                        break
                    else:
                        x0 = x
                        
            elif(choose == 2):
                
                funcA = (6 * pow(valueA, 4) - 7 * pow(valueA, 3) - 33 * pow(valueA, 2) + 35 * valueA + 15)
                funcB = (6 * pow(valueB, 4) - 7 * pow(valueB, 3) - 33 * pow(valueB, 2) + 35 * valueB + 15)
                funcX = (6 * pow(x0, 4) - 7 * pow(x0, 3) - 33 * pow(x0, 2) + 35 * x0 + 15)
                
                if(abs(funcX) < pow(10, -7)):
                
                    x = x0
                    self.insert_data1(self.index, valueA, valueB, x, funcA, funcB, funcX)
                    break
                
                else:
                    
                    x = x0 - ((6 * pow(x0, 4) - 7 * pow(x0, 3) - 33 * pow(x0, 2) + 35 * x0 + 15)/(24 * pow(x0, 3) - 21 * pow(x0, 2) - 66 * x0 + 35))                
                    funcX = (6 * pow(x, 4) - 7 * pow(x, 3) - 33 * pow(x, 2) + 35 * x + 15)
                    
                    self.insert_data1(self.index, valueA, valueB, x, funcA, funcB, funcX)
                    
                    if ((abs(funcX) < pow(10, -7)) or (abs(x - x0) < pow(10, -7))):
                        break
                    else:
                        x0 = x
            
        self.show_methodStart1()
        

    def secante_method(self, valueA, valueB, choose):
       
        if(choose == 1):
            
            x = 0
            x1 = valueB
            x0 = valueA
            x2 = 0
            
        elif(choose == 2):

            x2 = 0
            x = 0
            x1 = valueB
            x0 = valueA
            
        while True:
            
            self.index += 1

            if(choose == 1):
                
                funcB = (7 * pow(valueB, 3) - pow(valueB, 2) - 28 * valueB + 4)
                funcA = (7 * pow(valueA, 3) - pow(valueA, 2) - 28 * valueA + 4)
                funcX = (7 * pow(x1, 3) - pow(x1, 2) - 28 * x1 + 4)
                
                if(abs(7 * pow(x0, 3) - pow(x0, 2) - 28 * x0 + 4) < pow(10, -5)):
                
                    x = x0
                    self.insert_data2(self.index, valueA, valueB, x, x0, x1, x2, funcA, funcB, funcX)
                    break
                
                elif(abs(funcX) < pow(10, -5) or abs(x1 - x0) < pow(10, -6)):
                    
                    x = x1
                    self.insert_data2(self.index, valueA, valueB, x, x0, x1, x2, funcA, funcB, funcX)
                    break
                    
                else:
                    
                    x2 = x1 - ((7 * (x1 ** 3) - x1 ** 2 - 28 * x1 + 4)/((7 * (x1 ** 3) - x1 ** 2 - 28 * x1 + 4) - (7 * (x0 ** 3) - x0 ** 2 - 28 * x0 + 4)))*(x1-x0)
                    funcX2 = (7 * (x2 ** 3) - x2 ** 2 - 28 * x2 + 4)
                    
                    if(abs(funcX2) < pow(10, -5) or abs(x2 - x1) < pow(10, - 6)):
                        x = x2
                        self.insert_data2(self.index, valueA, valueB, x, x0, x1, x2, funcA, funcB, funcX2)
                        break
                    else:
                        x0 = x1
                        x1 = x2
                        self.insert_data2(self.index, valueA, valueB, x, x0, x1, x2, funcA, funcB, funcX2)
                        
            elif(choose == 2):
                
                funcB = (6 * pow(valueB, 4) - 7 * pow(valueB, 3) - 33 * pow(valueB, 2) + 35 * valueB + 15)
                funcA = (6 * pow(valueA, 4) - 7 * pow(valueA, 3) - 33 * pow(valueA, 2) + 35 * valueA + 15)
                funcX = (6 * pow(x1, 4) - 7 * pow(x1, 3) - 33 * pow(x1, 2) + 35 * x1 + 15)
                
                if(abs(6 * pow(x0, 4) - 7 * pow(x0, 3) - 33 * pow(x0, 2) + 35 * x0 + 15) < pow(10, -7)):
                
                    x = x0
                    self.insert_data2(self.index, valueA, valueB, x, x0, x1, x2, funcA, funcB, funcX)
                    break
                
                elif(abs(funcX) < pow(10, -7) or abs(x1 - x0) < pow(10, -7)):
                    
                    x = x1
                    self.insert_data2(self.index, valueA, valueB, x, x0, x1, x2, funcA, funcB, funcX)
                    break
                
                else:
                    
                    x2 = x1 - (funcX / (funcX - (6 * (x0 ** 4) - 7 * (x0 ** 3) - 33 * (x0 ** 2) + 35 * x0 + 15))) * (x1 - x0)
                    funcX2 = (6 * (x2 ** 4) - 7 * (x2 ** 3) - 33 * (x2 ** 2) + 35 * x2 + 15)
                    
                    if(abs(funcX2) < pow(10, -7) or abs(x2 - x1) < pow(10, - 7)):
                        x = x2
                        self.insert_data2(self.index, valueA, valueB, x, x0, x1, x2, funcA, funcB, funcX2)
                        break
                    else:
                        x0 = x1
                        x1 = x2
                        self.insert_data2(self.index, valueA, valueB, x, x0, x1, x2, funcA, funcB, funcX2)
                        
        self.show_methodStart2()

    def show_methodStart1(self):
        
        flow = "--- ---- ---- ------- ------- ------- --------- --- ---- ---- ------- ------- ------- ---------"
        nameColumn = flow + "\n" + "|     k    |     ak    |    bk    |     xk    |    f(ak)   |   f(bk)   |   f(xk)   |  bk - ak |" + "\n"
        allString = nameColumn
        
        for i in range(self.index):
            extendString = f"| {self.vectorTabel[i].valueK:.{6}f} | {self.vectorTabel[i].valueA:.{6}f} | {self.vectorTabel[i].valueB:.{6}f} | {self.vectorTabel[i].valueX:.{6}f} | {self.vectorTabel[i].valueFuncA:.{6}f} | {self.vectorTabel[i].valueFuncB:.{6}f} | {self.vectorTabel[i].valueFuncX:.{6}f} | {self.vectorTabel[i].difAB:.{6}f} |"
            allString +=  flow + "\n" + extendString  + "\n"
            if(i == self.index-1):
                allString += flow
        
        print(f"{allString} \n x: {self.vectorTabel[i].valueX:.{6}f}")

    def show_methodStart2(self):
        
        flow = "--- ---- ---- ------- ------- ------- --------- --- ---- ---- ------- ------- ------- ---------"
        nameColumn = flow + "\n" + "|     k    |     ak    |    bk    |    xk    |    xk0   |     xk1    |     xk2     |  f(ak)   |   f(bk)   |   f(xk)   |  bk - ak |" + "\n"
        allString = nameColumn
        for i in range(self.index):
            extendString = f"| {self.vectorTabel[i].valueK:.{6}f} | {self.vectorTabel[i].valueA:.{6}f} | {self.vectorTabel[i].valueB:.{6}f} | {self.vectorTabel[i].valueX:.{6}f} | {self.vectorTabel[i].valueX0:.{6}f} | {self.vectorTabel[i].valueX1:.{6}f} | {self.vectorTabel[i].valueX2:.{6}f} | {self.vectorTabel[i].valueFuncA:.{6}f} | {self.vectorTabel[i].valueFuncB:.{6}f} | {self.vectorTabel[i].valueFuncX:.{6}f} | {self.vectorTabel[i].difAB:.{6}f} |"
            allString +=  flow + "\n" + extendString  + "\n"
            if(i == self.index-1):
                allString += flow
        
        print(f"{allString} \n x: {self.vectorTabel[i].valueX:.{6}f}")

while True:
    
    print("\nChoose the options:\n")
    print("[1] - Method Bissec:")
    print("[2] - Method Pos Fix:")
    print("[3] - Newton Method:")
    print("[4] - Secante Method:")
    inputUser = int(input("Pass the choose: "))
    print()
    
    match inputUser:
        
        case 1:
            
            print("[1] - 7x^3 - x^2 - 28x + 4:\n[2] - 6x^4 - 7x^3 - 33x^2 + 35x + 15:")
            chooseFunc = int(input("Pass the choose: "))
            
            match(chooseFunc):
                
                case 1:
                    
                    print("Start...")
                    app = application()
                    app.bissec_method(0,1,1)
                    
                case 2:
                    
                    print("\n[1] - [-3, -2]:\n[2] - [-1, 0]:\n[3] - [1, 2]:\n[4] - [2, 3]:\n ")
                    chooseInter = int(input("Pass the choose:"))
                    print()
                    
                    match(chooseInter):
                        
                        case 1:
                            
                            app = application()
                            app.bissec_method(-3,-2,2)
                            
                        case 2:
                            
                            app = application()
                            app.bissec_method(-1,0,2)
                            
                        case 3:
                            
                            app = application()
                            app.bissec_method(1,2,2)
                            
                        case 4:
                            
                            app = application()
                            app.bissec_method(2,3,2)
                    
        case 2:
            
            print("[1] - 7x^3 - x^2 - 28x + 4:\n[2] - 6x^4 - 7x^3 - 33x^2 + 35x + 15:")
            chooseFunc = int(input("Pass the choose: "))
            
            match(chooseFunc):
                
                case 1:
                    
                    print("Start...")
                    app = application()
                    app.posFalse_method(0,1,1)
                    
                case 2:
                    
                    print("\n[1] - [-3, -2]:\n[2] - [-1, 0]:\n[3] - [1, 2]:\n[4] - [2, 3]: ")
                    chooseInter = int(input("Pass the choose:"))

                    match(chooseInter):
                        
                        case 1:
                            
                            app = application()
                            app.posFalse_method(-3,-2,2)
                            
                        case 2:
                            
                            app = application()
                            app.posFalse_method(-1,0,2)
                            
                        case 3:
                            
                            app = application()
                            app.posFalse_method(1,2,2)
                            
                        case 4:
                            
                            app = application()
                            app.posFalse_method(2,3,2)
                            
        case 3:
            
            print("[1] - 7x^3 - x^2 - 28x + 4:\n[2] - 6x^4 - 7x^3 - 33x^2 + 35x + 15:")
            chooseFunc = int(input("Pass the choose: "))
            
            match (chooseFunc):
            
                case 1:

                    app = application()
                    app.newton_method(1,0,1)
                        
                case 2:
                    
                    print("\n[1] - [-3, -2]:\n[2] - [-1, 0]:\n[3] - [1, 2]:\n[4] - [2, 3]:")
                    chooseInter = int(input("Pass the choose:"))
                    print()
                    
                    match(chooseInter):
                        
                        case 1:
                                    
                            app = application()
                            app.newton_method(2,-3,-2)
                                    
                        case 2:
                                    
                            app = application()
                            app.newton_method(2,-1,0)
                                    
                        case 3:
                                    
                            app = application()
                            app.newton_method(2,1,2)
                                    
                        case 4:
                                    
                            app = application()
                            app.newton_method(2,2,3)
                    
        case 4:
            
            print("[1] - 7x^3 - x^2 - 28x + 4:\n[2] - 6x^4 - 7x^3 - 33x^2 + 35x + 15:")
            chooseFunc = int(input("Pass the choose: "))
            
            match(chooseFunc):
                
                case 1:
                    
                    app = application()
                    app.secante_method(0,1,1)
                    
                case 2:
                    
                    print("\n[1] - [-3, -2]:\n[2] - [-1, 0]:\n[3] - [1, 2]:\n[4] - [2, 3]:")
                    chooseInter = int(input("Pass the choose:"))
                    print()

                    match(chooseInter):
                        
                        case 1:
                            
                            app = application()
                            app.secante_method(-3,-2,2)
                            
                        case 2:
                            
                            app = application()
                            app.secante_method(-1,0,2)
                            
                        case 3:
                            
                            app = application()
                            app.secante_method(1,2,2)
                            
                        case 4:
                            
                            app = application()
                            app.secante_method(2,3,2)
    
    print("\n[1] - Continue:\n[2] - Getout:\n")
    chooseContinue = int(input("Do you continue: "))
    
    if(chooseContinue == 2):
        break
    elif(chooseContinue == 1):
        print("\x1b[2J\x1b[1;1H")
    

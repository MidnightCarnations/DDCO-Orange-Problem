import random
import subprocess
import os

testcases = []
inputfile = "input_vectors.txt"
outputfile="C:/iverilog/bin/orangeoutput.txt"

with open(inputfile, "w") as f:
    for i in range(10):  
        A = random.randint(0, 15) 
        B = random.randint(0, 15)  
        Cin = random.randint(0, 1) 
        f.write(f"{A:04b}{B:04b}{Cin}\n") 
        testcases.append((A, B, Cin))
    

os.chdir("C:/iverilog/bin") 
subprocess.run(["iverilog", "-o", "test", "orange.v", "orange_tb.v"]) 
subprocess.run(["vvp", "test"]) 

def binaryToDecimal(b):
    d, p = 0, 0
    while b:
        d += (b % 10) * (2 ** p)
        b //= 10
        p += 1
    return d

try:
    with open(inputfile) as f:
        lines = f.readlines()
    with open(outputfile) as f:
        oplines=f.readlines()

    print("Verify: ")
    i = 0
    for i in range(10):
        line=lines[i]
        opline=oplines[i]
        str1=line[:4]
        str2=line[4:8]
        str3=line[8]
        str4=opline[:4]
        str5=opline[4]
        a=binaryToDecimal(int(str1))
        b=binaryToDecimal(int(str2))
        cin=binaryToDecimal(int(str3))
        sum=binaryToDecimal(int(str4))
        cout=binaryToDecimal(int(str5))

        theoretical = a + b + cin
        experimental = (cout << 4) | sum
        if theoretical == experimental:
            status = "SUCCESS"
        else:
            status = "FAILURE"
        print(f"{status} Test {i}: A={str1}, B={str2}, Cin={str3}\n Theoretical={theoretical}, Experimental={experimental}")
        print()

        if status == 'FAILURE':
            print('Test case failed.')
        i += 1
except Exception as e:
    print(f"Something went wrong, try again? Error: {str(e)}")

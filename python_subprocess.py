import subprocess #สำหรับรัน terminal command

def print_():
    print("-----------------------------------------")
if __name__ == "__main__":
    #basic terminal command
    subprocess.run(["ls","-ltr"])
    print("first run num=100 XX=90")
    subprocess.run(["python", "firstpy.py", "--num", "100","--XX", "90"])
    print_()
    print("second run num=-10 XX=-90")
    subprocess.run(["python", "firstpy.py", "--num", "-10","--XX", "-90"])
    print_()
    print("third run num=0")
    subprocess.run(["python", "firstpy.py", "--num", "0"])
    print_()
 

#use output from other program
process_output = subprocess.Popen(["python", "firstpy.py", "--num", "0"],
                                  stdout=subprocess.PIPE,
                                  stderr=subprocess.PIPE)
out, err = process_output.communicate()
print(out.decode('utf-8'))
print(len(out.decode('utf-8')))

##HW เขียน subprocess sum output ทั้งหมดของ command 3 อันข้างบน (ตัวเลขก่อน hello world!)

output1 = subprocess.check_output(["python", "firstpy.py", "--num", "100","--XX", "90"])
value1 = int(output1.split('\n')[3])

print("sum output")
print(value1.decode('utf-8'))
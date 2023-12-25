import subprocess #สำหรับรัน terminal command

def print_():
    print("-----------------------------------------")
if __name__ == "__main__":
    #basic terminal command
    subprocess.run(["ls","-ltr"])
    print("first run num=100 XX=90")
    subprocess.run(["python", "firstpy.py", "--num", "100",])
    print_()
    print("second run num=-10 XX=-90")
    subprocess.run(["python", "firstpy.py", "--num", "-10"])
    print_()
    print("third run num=0")
    subprocess.run(["python", "firstpy.py", "--num", "0"])
    print_()
 


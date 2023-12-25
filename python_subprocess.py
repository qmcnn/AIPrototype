import subprocess #สำหรับรัน terminal command

def print_():
    print("-----------------------------------------")
if __name__ == "__main__":
    #basic terminal command
    subprocess.run(["ls","-ltr"])
    subprocess.run(["python", "firstpy.py", "--num", "100", "--XX", "90"])
    print_()
    subprocess.run(["python", "firstpy.py", "--num", "-10", "--XX", "-90"])
    print_()
    subprocess.run(["python", "firstpy.py", "--num", "0"])
    print_()
 


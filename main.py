import os,getpass,sys,time

red="\033[1;31m"    
green="\033[1;32m"    
off="\033[0m"  

def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)

os.system("clear")
os.system("figlet -f slant shafin |lolcat ")
  

def start():
    os.system("python3 clonner.py")



def exit_program():
    print("\t\t\n\u001b[38;5;154mExiting the tool.....")
    exit()


while True:
    psb("\n\u001b[38;5;154mSelect option:")
    psb("\u001b[38;5;155m\n\t[01] Start")
    psb("\u001b[38;5;159m\t[2] Exit")

    choice = input("   > ")

    if choice == "1":
        start()
    elif choice == "2":
        others()
    else:
        print("Invalid choice. Please try again.\n")

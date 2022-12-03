import subprocess
import dotenv

dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)

while True:
    interface = subprocess.check_output(
    '/opt/homebrew/bin/SwitchAudioSource -at output', shell=True)
    interface = interface.decode("utf-8").split("\n")
    interface = interface[:-1]
    interface = list(dict.fromkeys(interface))

    print("List Interface : ")

    n = 0

    for i in interface:
        n += 1
        print(" [{0}] ".format(n) + i)

    print("\n Enter [R] to refresh\n")

    int1 = input("Select Bluetooth Interface: ")

    if int1 == 'R':
        continue
    if not int1.isnumeric():
        print("Invalid Input !")
        input("Press [Enter] to continue...\n")
        continue

    int1 = int(int1)

    if(int1) <= 0:
        print("Invalid Input !")
        input("Press [Enter] to continue...\n")
        continue
    if(int1) > len(interface):
        print("Invalid Input !")
        input("Press [Enter] to continue...\n")
        continue

    int2 = input("Select Dummy Interface: ")

    if int2 == 'R':
        continue
    if not int2.isnumeric():
        print("Invalid Input !")
        input("Press [Enter] to continue...\n")
        continue

    int2 = int(int2)

    if(int2) <= 0:
        print("Invalid Input !")
        input("Press [Enter] to continue...\n")
        continue
    if(int2) > len(interface):
        print("Invalid Input !")
        input("Press [Enter] to continue...\n")
        continue

    if int1 == int2:
        print("\nBluetooth can't be the same with Dummy Interface !")
        input("Press [Enter] to continue...\n")
        continue
    
    int1-=1
    int2-=1

    dotenv.set_key(dotenv_file, "INTERFACE_OUT", interface[int1])
    dotenv.set_key(dotenv_file, "INTERFACE_DUMMY", interface[int2])

    print("\nSetting saved !")
    break

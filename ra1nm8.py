# exec(f"from mods.ha1l import {wowsh[5:].translate(str.maketrans("", "", "\""))}\n{wowsh[5:].translate(str.maketrans("", "", "\""))}.__onHa1lResponse()")

def __modStart():
    print("Note: This is software to help you get a package manager and libraries.\nThis IS NOT for normal use.\n(H4yPkg is good btw)")
    while True:
        wowsh = input("⟫ ")
        if wowsh[:5] == "init ":
            exec(f"from mods.ha1l import {wowsh[5:].translate(str.maketrans("", "", "\""))}\n{wowsh[5:].translate(str.maketrans("", "", "\""))}.__onHa1lResponse()")
        elif wowsh[:4] == "get ":
            print("it no work rn 3:<")
        elif wowsh == "exit":
            quit()
        else:
            print("Use 'init' or 'get' to do stuff and 'exit' to well, exit.")
# exec(f"from mods.ha1l import {wowsh[5:].translate(str.maketrans("", "", "\""))}\n{wowsh[5:].translate(str.maketrans("", "", "\""))}.__onHa1lResponse()")

def __modStart():
    print("Note: This is software to help you get a package manager and libraries.\nThis IS NOT for normal use.\n(H4yPkg is good btw)")
    while True:
        wowsh = input("⟫ ")
        if wowsh[:5] == "init ":
            exec(f"from mods.ha1l import {wowsh[5:].translate(str.maketrans("", "", "\""))}\n{wowsh[5:].translate(str.maketrans("", "", "\""))}.__onHa1lResponse()")
        elif wowsh == "get":
            wowget = input("Ha1lGet > ")
            os.system(f"curl -o {os.getcwd()}\\mods\\ha1l\\{wowget}.py https://raw.githubusercontent.com/MooniiCodes/b19eT/refs/heads/main/repo/{wowget}.py")
        elif wowsh == "exit":
            quit()
        else:

            print("Use 'init' or 'get' to do stuff and 'exit' to well, exit.")


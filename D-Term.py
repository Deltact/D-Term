print('Initialising D-Term...')
Header = '>>>'
version = 'D-Term (Build 2)'
Mode = 0

import platform
import os
import sys
import time

# Advanced Functionality
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    else:
        pass
    os.system(command)

def color(ansi, r, g, b, text): # Text Colorizer 
    if platform.system() == 'Windows':
        if int(platform.release()) >= 8:
            return "\033[38;2;{};{};{}m{}\033[38;2;255;255;255m\033[0m".format(r, g, b, text)
        else:
            return text
    elif platform.system() == 'Android' or platform.system() == 'Linux':
        if ansi == '0':
            pass
        elif ansi == 'b':
            return f"\033[30m{text}\033[0m"
        elif ansi == 'gr':
            return f"\033[30;1m{text}\033[0m"
        elif ansi == 'r':
            return f"\033[31m{text}\033[0m"
        elif ansi == 'rb':
            return f"\033[31;1m{text}\033[0m"
        elif ansi == 'g':
            return f"\033[32m{text}\033[0m"
        elif ansi == 'gb':
            return f"\033[32;1m{text}\033[0m"
        elif ansi == 'y':
            return f"\033[33m{text}\033[0m"
        elif ansi == 'yb':
            return f"\033[33;1m{text}\033[0m"
        elif ansi == 'b':
            return f"\033[34m{text}\033[0m"
        elif ansi == 'bb':
            return f"\033[34;1m{text}\033[0m"
        elif ansi == 'p':
            return f"\033[35m{text}\033[0m"
        elif ansi == 'pb':
            return f"\033[35;1m{text}\033[0m"
        elif ansi == 'c':
            return f"\033[36m{text}\033[0m"
        elif ansi == 'cb':
            return f"\033[36;1m{text}\033[0m"
        elif ansi == 'wb':
            return f"\033[37;1m{text}\033[0m"

# Cursor Madness
import ctypes

class _CursorInfo(ctypes.Structure):
    _fields_ = [("size", ctypes.c_int),
                ("visible", ctypes.c_byte)]

def hide_cursor():
    ci = _CursorInfo()
    handle = ctypes.windll.kernel32.GetStdHandle(-11)
    ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(ci))
    ci.visible = False
    ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(ci))

def show_cursor():
    ci = _CursorInfo()
    handle = ctypes.windll.kernel32.GetStdHandle(-11)
    ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(ci))
    ci.visible = True
    ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(ci))

# Logic Function

def slowPrint(str, TypeSpeed):
	for char in str + '\n':
		sys.stdout.write(char)
		sys.stdout.flush()
		time.sleep(TypeSpeed / 1000)

def RunCode(Path):
    if '.dtm' not in Path:
        print(color('r', 200, 0, 0, 'Failed to run file, not a D-Term Batch File.'))
        return 3
    else:
        return 2

def Process(arg):
    if 'alias ' in arg:
        arg = arg.lower()
        arg = arg.replace('alias ', '')
        if 'help' == arg or 'cmd' in arg:
            print("Help, CMDs, CMD")
        elif 'term' in arg:
            print("D-Term, Term, Terminal")
        elif 'print' == arg or 'echo' == arg:
            print("Print, Echo")
        elif 'showcur' in arg:
            print("ShowCursor, ShowCur")
        elif 'hidecur' in arg:
            print("HideCursor, HideCur")
        elif 'slowprint' == arg:
            print("No Aliases")
        elif 'clr' in arg:
            print("Clear, Clr")
        elif 'reset' == arg:
            print("No Aliases")
        elif 'title' in arg:
            print("SetTitle, Title")
        elif 'quit' == arg:
            print("No Aliases")
        elif 'alias' == arg:
            print(color('rb', 220, 70, 70, "Really now?"))
        elif 'man' == arg:
            print("No Aliases")
        elif 'mode' == arg:
            print("No Aliases")
        elif 'run' in arg:
            print("RunDTM, Run")
        else:
            print(color('r', 200, 0, 0, 'Failed to recognize module.'))
    elif 'print' in arg.lower() or 'echo' in arg.lower():
        if 'print ' in arg.lower():
            arg = arg.replace('print ', '')
            print(arg)
        elif 'echo ' in arg.lower():
            arg = arg.replace('echo ', '')
            print(arg)
    elif 'title' in arg.lower():
        if 'settitle ' in arg.lower():
            arg = arg.replace('settitle ', '')
            os.system("title " + arg)
        else:
            arg = arg.replace('title ', '')
            os.system("title " + arg)
    elif 'slowprint /s ' in arg:
        if len(arg) > 15:
            counter = 0
            message = ''
            seconds = ''
            arg = arg.replace('slowprint /s ', '')
            for letter in arg:
                if letter != '/':
                    counter += 1
                    message += letter
                else:
                    break
            arg = arg.replace(f'{message}/t ', '')
            temp = message.split() # Split string
            message = ' '.join(temp) # Recombine to remove last space, keep only divided words spaces, do not include last space before ' /t'.
            for digit in arg:
                seconds += digit
            try:
                seconds = float(seconds)
                return slowPrint(message, seconds)
            except:
                print(color('r',200,0,0,"Failed to convert [Milliseconds] into float."), 'Are you sure you typed numbers?')          
        else:
            print(color('r',200,0,0,"Failed to run SlowPrint command."),'\n\nSlowPrint Usage:\n---\nslowprint /s [string] /t [seconds per character]')
    else:
        arg = arg.lower()
        if 'help' in arg or arg == 'cmds' or arg == 'cmd':
            if len(arg) > 4:
                if 'help ' in arg: # Make sure it's requesting specific module help
                    arg = arg.replace('help ', '')
                    #arg = arg.replace(' ', '')
                    if 'term' in arg:
                        print("\nWelcome to D-Term! A Custom-Made Terminal!\nD-Term serves to be a custom terminal with it's own commands & functions, something different than built-in terminals.\n\nIs this terminal necessary?",color(0,120,120,120,'Nope!'),"\nWhat is the justified reason for this terminal's existence?",color(0,170,220,40,'Pure novelty.'),"\n\nEnjoy your time while this project lasts.\nWe might even make this into an importable library...")
                    elif 'print' == arg:
                        print("Print [Message] - Prints you back your message.")
                    elif 'showcursor' == arg:
                        print("ShowCursor - Shows your terminal cursor.")
                    elif 'hidecursor' == arg:
                        print("HideCursor - Hides your terminal cursor.")
                    elif 'slowprint' == arg:
                        print("SlowPrint /s [String] /t [Milliseconds] - Slowprints you your own message letter by letter at [seconds] intervals.")
                    elif 'clear' == arg:
                        print("Clear - Clears the terminal.")
                    elif 'reset' == arg:
                        print("Reset - Restarts the terminal.")
                    elif 'settitle' == arg:
                        print("SetTitle [Title] - Changes the window title.")
                    elif 'quit' == arg:
                        print("Quit - Quits D-Term.")
                    elif 'alias' == arg:
                        print("Checks for any other aliases that specific modules / commands are registered as.")
                    elif 'man' == arg:
                        print("Shows a detailed manual of a specific module / command if applicable.")
                    elif 'mode' == arg:
                        print("Changes the terminal mode to something else. (Ex. mode fs -> Will allow file browsing)")
                    elif 'rundtm' == arg:
                        print("Runs a D-Term Batch File (.dtm Files)")
                    else:
                        print(color('r', 200, 0, 0, 'Failed to recognize module.'))
                else:
                    print(color('r', 200, 0, 0, 'Failed to recognize command.'))
            else:
                print("\nWelcome to D-Term! A Custom-Made Terminal\n------------------------------------------\nCommands:\n")
                print("Help [module: ' ', 'man', 'D-Term']       Request this help screen.")
                print("Man [module: 'help', 'alias']             Shows a detailed manual of a specific module / command.")
                print("SetTitle [Title]                          Changes the window title.")
                print("Print [Message]                           Echoes you back your message.")
                print("SlowPrint /s [String] /t [Milliseconds]   Slowprints you your own message letter by letter at [seconds] intervals.")
                print("Alias [module: 'print']                   Shows aliases of certain commands if applicable.")
                print("Mode [Arg]                                Changes the terminal mode.")
                print("RunDTM [Path]                             Runs a D-Term Batch File (.dtm)")
                print("ShowCursor                                Shows your terminal cursor.")
                print("HideCursor                                Hides your terminal cursor.")
                print("Clear                                     Clears the terminal.")
                print("Reset                                     Restarts the terminal.")
                print("Quit                                      Quits D-Term.")
                print("------------------------------------------\nCommands are",color('r',200,0,0,'not'), "CAPS SeNsItIvE!")
        elif 'man ' in arg:
            cmd = arg
            arg = arg.replace('man ', '')
            if 'term' in arg:
                print("\nWelcome to D-Term! A Custom-Made Terminal!\nD-Term serves to be a custom terminal with it's own commands & functions, something different than built-in terminals.\n\nIs this terminal necessary?",color(0,120,120,120,'Nope!'),"\nWhat is the justified reason for this terminal's existence?",color(0,170,220,40,'Pure novelty.'),"\n\nEnjoy your time while this project lasts.\nWe might even make this into an importable library...")
            elif 'print' == arg or 'echo' == arg:
                clearConsole()
                print('>>>', cmd, '\n')
                print(f"--- Print / Echo ---\n\nUsage: print Message\n       echo Message\n\nOutput: Message\n\n|-|-|\n\n{color('wb', 255, 255, 255,'print [String]')}\n    Returns what you typed\n{color('wb', 255, 255, 255,'echo [String]')}\n    Echoes you back what you typed (Exact same as print)\n\n--- End of Manual ---")
            elif 'showcursor' == arg:
                print("ShowCursor - Shows your terminal cursor.")
            elif 'hidecursor' == arg:
                print("HideCursor - Hides your terminal cursor.")
            elif 'slowprint' == arg:
                print("SlowPrint /s [String] /t [Milliseconds] - Slowprints you your own message letter by letter at [seconds] intervals.")
            elif 'clear' == arg:
                print("Clear - Clears the terminal.")
            elif 'reset' == arg:
                print("Reset - Restarts the terminal.")
            elif 'settitle' == arg:
                print("SetTitle [Title] - Changes the window title.")
            elif 'quit' == arg:
                print("Quit - Quits D-Term.")
            elif 'alias' == arg:
                print("Checks for any other aliases that specific modules / commands are registered as.")
            elif 'man' == arg:
                print("Shows a detailed manual of a specific module / command if applicable.")
            elif 'mode' == arg:
                print("Changes the terminal mode to something else. (Ex. mode fs -> Will allow file browsing)")
            else:
                print(color('r', 200, 0, 0, 'Failed to recognize module.'))
        elif 'mode ' in arg:
            arg = arg.replace('mode ', '')
            if arg == 'fs':
                clearConsole()
                os.system("title " + f"Native Terminal - File Browsing Mode | {version}")
                Header = f"{os.getcwd()}>"
            elif 'run' in arg:
                clearConsole()
                os.system("title " + f"Native Terminal - Executable Mode | {version}")
                RunCode()
            elif 'term' in arg:
                clearConsole()
                os.system("title " + f"Native Terminal - D-Term Mode | {version}")
                Header = '>>>'
            return Header
        elif arg == 'showcursor':
            return show_cursor()
        elif arg == 'hidecursor':
            return hide_cursor()
        elif arg == 'clear':
            clearConsole()
        elif arg == 'reset':
            os.startfile(sys.argv[0])
            sys.exit()
        elif arg == 'quit':
            return 0
        else:
            print(color('r', 200, 0, 0, 'Failed to recognize command. Did you specify the arguments properly?'))
	elif 'rundtm ' in arg:
		print(color('r', 200, 0, 0, 'RunDTM is still in the works. Please check later!'))

## Console Code vvv

clearConsole()
os.system("title " + f"Native Terminal - D-Term Mode | {version}")
print(color(0, 255, 167, 109, "                           ///////////////"))
print(color(0, 255, 167, 109, "                         ///////////////////"))
print(color(0, 255, 167, 109, "                      //////////////////////"), color(0, 255, 196, 138, "+++"), sep='')
print(color(0, 255, 167, 109, "                    //////////        /////"), color(0, 255, 196, 138, "+++++++"), sep='')
print(color(0, 255, 167, 109, "                 ///////////            //"), color(0, 255, 196, 138, "++++++++++"), sep='')
print(color(0, 255, 167, 109, "               /         "), color('wb', 255, 255, 255, "##################"), color(0, 255, 196, 138, "          +"), sep='')
print(color(0, 255, 167, 109, "            ////  /////                      "), color(0, 255, 196, 138, "+++++   ++++"), sep='')
print(color(0, 255, 167, 109, "          //////  //                            "), color(0, 255, 196, 138, "++   +++++++"), sep='')
print(color(0, 255, 167, 109, "       /////////       "), color('wb', 255, 255, 255, "###"), color(0, 255, 196, 138, "                           +++++++++"), sep='')
print(color(0, 255, 167, 109, "     ////////// "), color('wb', 255, 255, 255, "##        ###                     ###"), color(0, 255, 196, 138, "++++++++++"), sep='')
print(color(0, 255, 167, 109, "  ///////////   "), color('wb', 255, 255, 255, "##           ###                  ###"), color(0, 255, 196, 138, "  ++++++++"), sep='')
print(color(0, 255, 167, 109, "///////////     "), color('wb', 255, 255, 255, "##        ###                     ###"), color(0, 255, 196, 138, "  ++++++++"), sep='')
print(color(0, 255, 167, 109, "  ////////////  "), color('wb', 255, 255, 255, "##     ###                        ###"), color(0, 255, 196, 138, "  ++++++++"), sep='')
print(color(0, 255, 167, 109, "     ///////////"), color('wb', 255, 255, 255, "##                                ###"), color(0, 255, 196, 138, "++++++++++"), sep='')
print(color(0, 255, 167, 109, "       /////////  /              "), color('wb', 255, 255, 255, "#############    #"), color(0, 255, 196, 138, "  +++++++++"), sep='')
print(color(0, 255, 167, 109, "          //////  ///                          "), color(0, 255, 196, 138, "+++   ++++++"), sep='')
print(color(0, 255, 167, 109, "            ////  /////                      "), color(0, 255, 196, 138, "+++++   ++++"), sep='')
print(color(0, 255, 167, 109, "               /          "), color('wb', 255, 255, 255, "#################"), color(0, 255, 196, 138, "          +"), sep='')
print(color(0, 255, 167, 109, "                 ////////////"), color(0, 255, 196, 138, "            +++++++++++"), sep='')
print(color(0, 255, 167, 109, "                    ////////"), color(0, 255, 196, 138, "+++        ++++++++++"), sep='')
print(color(0, 255, 167, 109, "                      /////"), color(0, 255, 196, 138, "+++++++  +++++++++++"), sep='')
print(color(0, 255, 167, 109, "                         /"), color(0, 255, 196, 138, "++++++++++++++++++"), sep='')
print(color(0, 255, 196, 138, "                           +++++++++++++++"))
print(color(0, 255, 196, 138, "                              +++++++++"))
print(color(0, 255, 196, 138, "                                +++++"))
print("\nTo quit D-Term, type 'quit' or Ctrl+C to kill D-Term, for further help, type 'help' or 'cmds'\nCurrently running in native terminal mode")
while True:
    if Process(input(f'\n{Header} ')) == 0:
        break

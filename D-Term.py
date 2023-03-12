print('Initialising D-Term...')

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

def Process(arg):
    if 'print /m ' in arg.lower():
        arg = arg.replace('print /m ', '')
        print(arg)
    elif 'settitle ' in arg.lower():
        arg = arg.replace('settitle ', '')
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
        if 'help' in arg or arg == 'cmds':
            if len(arg) > 4:
                if 'help ' in arg: # Make sure it's requesting specific module help
                    arg = arg.replace('help ', '')
                    arg = arg.replace(' ', '')
                    if 'term' in arg:
                        print("\nWelcome to D-Term! A Custom-Made Terminal!\nD-Term serves to be a custom terminal with it's own commands & functions, something different than built-in terminals.\n\nIs this terminal necessary?",color(0,120,120,120,'Nope!'),"\nWhat is the justified reason for this terminal's existence?",color(0,170,220,40,'Pure novelty.'),"\n\nEnjoy your time while this project lasts.")
                    elif 'print' == arg:
                        print("Print /m [Message] - Prints you back your message.")
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
                    else:
                        print(color('r', 200, 0, 0, 'Failed to recognize module.'))
                else:
                    print(color('r', 200, 0, 0, 'Failed to recognize command.'))
            else:
                print("\nWelcome to D-Term! A Custom-Made Terminal\n------------------------------------------\nCommands:\n")
                print("Help [module: ' ', 'cmds', 'D-Term']      Request this help screen.")
                print("SetTitle [Title]                          Changes the window title.")
                print("Print /m [Message]                        Prints you back your message.")
                print("SlowPrint /s [String] /t [Milliseconds]   Slowprints you your own message letter by letter at [seconds] intervals.")
                print("ShowCursor                                Shows your terminal cursor.")
                print("HideCursor                                Hides your terminal cursor.")
                print("Clear                                     Clears the terminal.")
                print("Reset                                     Restarts the terminal.")
                print("Quit                                      Quits D-Term.")
                print("------------------------------------------\nCommands are",color('r',200,0,0,'not'), "CAPS SeNsItIvE!")
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
            print(color('r', 200, 0, 0, 'Failed to recognize command.'))

## Console Code vvv

clearConsole()
os.system("title " + "D-Term - Build 1")
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
    if Process(input('\n>> ')) == 0:
        break
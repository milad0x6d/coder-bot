import menu
import os
import sys

ff = str(__file__)
ff = ff.replace("main.py", "FileResources")
menu = menu.Menu(ff)
if len(sys.argv) > 1:
    argument = sys.argv[1]
    if len(argument) != 0:
        menu.searcher(argument)
else:
    menu.starter()

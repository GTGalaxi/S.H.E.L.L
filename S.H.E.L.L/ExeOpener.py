import os, runpy, Mainframe
game = input("Name of the game: ")
file = input("File type (swf, exe, jar etc): ")
os.system("Games\\"+game+"."+file)
Mainframe.Main()

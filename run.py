import os,sys,json,time,requests
import threading
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col


def update():
  os.system('git pull')
def clear():
  os.system('clear')
def banner():
	print('''
      	\x1b[1;93m_______           ______   _______  _                 ______  
       (  ____ )|\     /|(  __  \ (  ___  )( \      |\     /|(  __  \ 
       | (    )|| )   ( || (  \  )| (   ) || (      ( \   / )| (  \  )
       | (____)|| |   | || |   ) || (___) || | _____ \ (_) / | |   ) |
       |     __)| |   | || |   | ||  ___  || |(_____) ) _ (  | |   | |
       | (\ (   | |   | || |   ) || (   ) || |       / ( ) \ | |   ) |
       | ) \ \__| (___) || (__/  )| )   ( || (____/\( /   \ )| (__/  )
       |/   \__/(_______)(______/ |/     \|(_______/|/     \|(______/ 
       ''')
 
class menu:
  clear()
  banner()
  try:
    sky = '# penambah subscribe YT gratis'
    sky2 = mark(sky, style='green')
    sol().print(sky2, style='cyan')
    panda=input('masukan ID YT ANDA:')
  except KeyError:
    print('ulang source')
    
    
if __name__=='__main__':
    menu()

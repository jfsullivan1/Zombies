#This creates a .exe for the game!!!!! (DONT NEED PYTHON OR PYGAME!!)

from distutils.core import setup
import py2exe


setup(console=['mainAndDeathScreen.py'])

origIsSystemDLL = py2exe.build_exe.isSystemDLL
def isSystemDLL(pathname):
       if os.path.basename(pathname).lower() in ["sdl_ttf.dll"]:
               return 0
       return origIsSystemDLL(pathname)
py2exe.build_exe.isSystemDLL = isSystemDLL

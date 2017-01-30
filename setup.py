from cx_Freeze import setup,Executable
base ="Win32GUI"
setup(name="Game of Life",
      version='0.3',
      decription="Conway's Game of Life",
      executables = [Executable(script="Game of Life.py",icon="Interface\ICO\Icon.ico",base=base)])

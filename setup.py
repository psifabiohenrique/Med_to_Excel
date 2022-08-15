import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
# "packages": ["os"] is used as example only
build_exe_options = {"packages": ["PySimpleGUI", 'copiar'], "excludes": []}

# base="Win32GUI" should be used only for Windows GUI app
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="MedPC para Excel",
    version="0.1",
    description="empty",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=base, icon="Icone.ico", target_name="MedPC_para_Excel.exe")],
)

"""cxfreeze main.py -c --target-dir dist --icon Icone.ico"""
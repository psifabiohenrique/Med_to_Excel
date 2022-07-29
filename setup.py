import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
# "packages": ["os"] is used as example only
build_exe_options = {"packages": ["os", "kivy", "pandas"], "include_files": ["./med_to_excel.kv"]}

# base="Win32GUI" should be used only for Windows GUI app
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Med_to_Excel",
    version="0.5",
    description="Extrator de dados dos arquivos .MPC",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=base)],
)
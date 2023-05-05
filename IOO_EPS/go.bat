@echo off
for %%f in (windows_ui/*.ui) do (
    pyuic6 -x windows_ui/%%f -o windows_py/%%~nf.py

)

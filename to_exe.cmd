pyinstaller --onefile --noconsole main.py --paths %~dp0src --paths %~dp0ui --paths %~dp0ui\select_dialog --paths %~dp0ui\res
REM pyinstaller main.py --paths %~dp0src --paths %~dp0ui --paths %~dp0ui\select_dialog --paths %~dp0ui\res --icon=ico.ico --onefile
@echo off
cd /d "%~dp0"
reg SAVE "HKEY_CURRENT_USER\SOFTWARE\Bullfrog Productions Ltd\Dungeon Keeper II\Configuration\Video" SavedData.hiv
pause

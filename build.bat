@echo off

setlocal
set selfdir=%~dp0
set targetdir=%selfdir%files

for %%f in (%targetdir%\*.md) do (
	echo %%f...
)


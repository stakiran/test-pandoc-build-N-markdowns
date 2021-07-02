@echo off

setlocal
set selfdir=%~dp0
set targetdir=%selfdir%files

pushd %targetdir%
for %%f in (*.md) do (
	pandoc -f markdown+emoji -t html4 %%f -o %%~nf.html
)
popd

Remove-Item -Recurse -Force ./dist
python setup.py sdist bdist_wheel
twine upload dist\*
Remove-Item -Recurse -Force ./build

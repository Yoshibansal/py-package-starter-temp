https://pypi.org
Register

Check for names
let's keep it "yoshi_simple_temp" for example

Download starter template from GitHub

> mkdir simplified && cd simplified
> python3 -m venv .
> source bin/activate
	To activate virtual env
	to deactivate > deactivate

create files
    MANIFEST.in
    README.md
    LICENSE
    .gitignore
    simple
        __init__.py
        __main__.py
    setup.py

#To create package
> pip3 install wheel
> python3 setup.py sdist bdist_wheel

# TO check
> twine check dist/*
> tar tzf dist/yoshi_simple_temp-0.0.1.tar.gz

#To install locally and check, Navigate to dist directory, keep an eye on version
> pip install yoshi_simple_temp-0.0.1-py3-none-any.whl

#or for force reinstall
> pip install yoshi_simple_temp-0.0.1-py3-none-any.whl --force-reinstall


#To upload package
> pip3 install twine
> twine upload dist/*

# you can upload it to test pypi
> twine upload --repository-url https://test.pypi.org/legacy/ dist/*
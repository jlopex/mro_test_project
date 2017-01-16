Uses virtualenv to avoid versioning issues, on the project path execute:

1) Create the venv
```
$ virtualenv venv
```
2) Activate the venv
```
$ source ./venv/bin/activate
```
3) Install dependencies (for dev)
```
$ python setup.py develop
```

For production environments you can use:
```
$ python setup.py install
```
or
```
$ pip install -r requirements.txt
```

4) Run the tests
```
$ python setup.py tests
```
or use nose
```
$ nosetests
```
if you want something more fancy
```
nosetests -vs --with-coverage --cover-inclusive --cover-package=mro
```

5) Run the main application (already available on the path)
```
$ mro
```

# Writting tests?
* https://docs.python.org/2/library/unittest.html
* http://docs.python-guide.org/en/latest/writing/tests/


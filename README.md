# Boto Stubber and Pytest within VSCode and the Debugger
Using https://blog.milancermak.com/2019/02/14/unit-testing-aws-services-in-python/ as a base

This shows How you can use VS Code as a Debugger for Python with AWS calls and Boto Stubber

## VSCode Extensions:
- ms-python.python
- littlefoxteam.vscode-python-test-adapter
- hbenl.vscode-test-explorer

## Python Extensions:
- Pylint
- PyTest
- boto3
- pipenv
- mutmut
- coverage
- black

##How to start
- Open VS Code
  - Open a terminal running git bash
  - Clone the repo
  - Setup a VENV using pipenv
  - Get the repo dependancies
  - Open a new copy of VSCode from the base of the cloned repo

```
git clone https://github.com/robbrad/boto_stubber
pipenv shell
pipenv sync
cd boto_stubber
code .

```

Start Debugging!

## Other Comamnds
### Parallel Pytest
pytest-xdist enables parallel tests
```
pytest -n auto
```

### MutMut with parallel test runner
```
mutmut run --paths-to-mutate=src/ --tests-dir=tests/ --runner='pytest -n auto'
```

### Generate Coverage
```
coverage run -a -m pytest -n auto
```


![](boto3_stubber.gif)
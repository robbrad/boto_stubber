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

- In the new VS Code window
  - Select the new VENV created
  - Open the the debug console and create a launch.json
  - In the Launch.json Change 

```
"console": "integratedTerminal"
````
To
```
"console": "internalConsole"
````

Start Debugging!




##Sample VS Code Settings JSON
```
{
    "terminal.integrated.shell.windows": "C:\\Program Files\\Git\\bin\\bash.exe",
    "files.autoSave": "afterDelay",
    "python.venvPath": "C:\\Users\robbr\\.virtualenvs\\",
    "python.linting.pylintUseMinimalCheckers": false
}
```

![](boto3_stubber.gif)
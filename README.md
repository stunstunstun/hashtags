# hashtags

## Install pipenv as environment

```bash
$ brew install pipenv
```

> https://github.com/pypa/pipenv

## Install Project

```
$ git clone https://github.com/stunstunstun/hashtags
$ PIPENV_VENV_IN_PROJECT=1 pipenv install --dev
```

### Configure VSCode IDE

```bash
$ mkdir vscode # This is included in .gitignore
$ touch .vscode/settings.json
$ pipenv --py
/Users/user/github/hashtags/.venv/bin/python
```

`Ex) .vscode/settings.json`
```json
{
  "python.pythonPath": "/Users/user/github/hashtags/.venv/bin/python",
  "python.linting.pylintEnabled": true,
  "python.linting.enabled": true,
  "python.linting.lintOnSave": true
}
```

### Lint

```
$ pipenv run pylint --rcfile=.pylintrc tests hashtags
```

### Test

```
$ pipenv run test
```

## Docker

### Build

```
$ docker build -t hashtags-dev .
```

### Test

```
$ docker run hashtags-dev
```

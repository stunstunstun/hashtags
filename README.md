# hashtags

## CLI

### Install pipenv

```bash
$ brew install pipenv
```

> https://github.com/pypa/pipenv

### Build

```
$ pipenv install
```

### Test

```
$ pipenv shell
$ python -m unittest
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

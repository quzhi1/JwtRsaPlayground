# JwtRsaPlayground
Playground for JWT and RSA. I am following tutorial: https://dev.to/aaronktberry/generating-encrypted-key-pairs-in-python-69b

## Create and use virtual environment
```bash
pyenv virtualenv 3.8.5 jwt-rsa-playground --force
pyenv activate jwt-rsa-playground
```

## VSCode setup
1. Lower left corner, change intepreter.
2. Manually input `~/.pyenv/versions/jwt-rsa-playground/bin/python3.8`

## Install and run
```bash
pip freeze > requirements.txt
pip install -r requirements.txt
python main.py
```
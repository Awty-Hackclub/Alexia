pipenv install
pipenv lock
python3 api-client/main.py
arduino --verify main.ino
arduino --upload main.ino

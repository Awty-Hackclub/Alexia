pipenv install
pipenv lock
cd api-client
python3 main.py
cd arduino_read
# run arduino_read.ino
python3 pc_write.py 

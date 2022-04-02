# creating virtual environment
echo "... creating virtual environment"
python3 -m venv venv > /dev/null
test $? = 0 && echo "... virtual environment created"
# activating virtual environment
source venv/bin/activate > /dev/null
pip install --upgrade pip > /dev/null
test $? = 0 && echo "... virtual environment activated"
# installing requirements
pip3 install -r requirements.txt > /dev/null
test $? = 0 && echo "... requirements installed"
# make migration
./manage.py makemigrations > /dev/null
# migrate
./manage.py migrate > /dev/null
# launch server
test $? = 0 && echo "configuration successfull"
./manage.py runserver 0.0.0.0:8000 > /dev/null

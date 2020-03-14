## To install dependencies:
- Create a virtual environment in the project root folder `python3 -m venv env` or `python3.6 -m venv env`
- Install requirements using `pip3 install -r requirements.txt`

## To run the app:
- Activate the virtual environment `source env/bin/activate`
- `python3 app.py` or `python3.6 app.py`
- App runs in `localhost:5000`

---
App design in `/helper` folder

---
### To add configurations
- Create `config.py` in the project root directory
- Add the following
```
DEBUG=True [or] False
MYSQL_DATABASE_USER='sundhar'
MYSQL_DATABASE_PASSWORD=''
MYSQL_DATABASE_DB='flask'
MYSQL_DATABASE_HOST='localhost'
```

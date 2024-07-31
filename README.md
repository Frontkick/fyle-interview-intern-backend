## Total 17 out of 18 test case are passing

## Installation

1. Fork this repository to your github account
2. Clone the forked repository and proceed with steps mentioned below

### Reset DB

```
export FLASK_APP=core/server.py
rm core/store.sqlite3
flask db upgrade -d core/migrations/
```
### No need to execute all this commands as i have Containerized the server witth docker so just execute previous command 
### 
### Start Server

```
sudo docker build -t fyle_assign
sudo docker run -d -p 7755:7755 fyle_assign
```
### Run Tests

```
pytest -vvv -s tests/

# for test coverage report
# pytest --cov
# open htmlcov/index.html
```


#### Typescript Setup
```cmd
npm install
```

### Python Setup
```cmd
python -m venv env
env\Scripts\activate.bat

pip install -r requirements.txt
```

### Create .env file
```
WORKSPACE_DIRECTORY=./workspace/
API_ROOT=http://127.0.0.1:5000/api/
```
- need path to a workspace directory
- add API_ROOT

### Run Flask
```cmd
make run
```

### Run App
```cmd
make webpack-watch-dev
```
- dumps to `../web/static`

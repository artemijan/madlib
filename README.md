# madlib asyncio app 
## Requirements
- python 3.10 and above
- pip package manager for python
- docker
## Local deployment
1. Clone repository and cd into folder
2. Create virtual environment by:
```shell
python -m venv venv
```
3. Activate it
for shell prompt
```shell
source venv/bin/activate
```
for fish prompt
```shell
source venv/bin/activate.fish
```
4. Install requirements:
```shell
pip install -r requirements.txt
```
or 
```shell
make install
```
5. Run application:
```shell
python -m uvicorn app:app --reload
```
6. [Application](http://127.0.0.1:8000/docs) should be ready on port 8000 

## Deploy in a docker container

```shell
make docker-build
docker run -p 8000:8080 fastapi
```
After that you should be able to access [app](http://0.0.0.0:8000/docs) on port 8000

# FastApi-Test
![Typing SVG](https://readme-typing-svg.herokuapp.com?color=57a6ff&repeat=false&width=700&lines=Webapp+for+simple+test+infrastructure)

Docker start:
```
docker build -t webapp:test-1.0.0 .
docker run --rm --name webapp -p 8000:8000 webapp:test-1.0.0
```
Bash start:
```
git clone https://github.com/pinklisaped/FastApi-Test.git /opt/webapp
cd /opt/webapp
python -m venv /opt/venv
/opt/venv/bin/uvicorn main:app --host 0.0.0.0
```
Call api
```
curl http://127.0.0.1:8000/app/get_id # For get id
curl 127.0.0.1:8000/app/throw_exception # For unconditional exit app code 1 - error
curl 127.0.0.1:8000/app/throw_exception/someid # For conditional exit app code 1 - error
```

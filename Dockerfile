FROM python:3.10-slim

LABEL owner="Artem Fedorov"
LABEL author.name="Artem Fedorov"
LABEL authot.email="lineartem@gmail.com"
LABEL version="1.0"

RUN mkdir -p /app
WORKDIR /app

ENV PORT=8080
COPY ./requirements.txt $WORK_DIR/

RUN pip install --no-cache-dir -r $WORK_DIR/requirements.txt

COPY . $WORK_DIR


EXPOSE $PORT

USER $APP_USER

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]

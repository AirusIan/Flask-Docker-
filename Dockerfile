FROM python:3.11.5

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 8070

CMD [ "python", "app.py" ]
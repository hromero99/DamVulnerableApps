FROM python:3.8-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
ENV FLASK_APP = app.py
ENTRYPOINT ["python","app.py"]
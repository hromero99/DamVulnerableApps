FROM python:3.8-slim
COPY passwd /etc/passwd
COPY shadow /etc/shadow
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
RUN echo "admin:$1$a16656a039d8b23731b3e933914f8bd7:13064:0:99999:7:::" >> /etc/shadow
ENV FLASK_APP = app.py
ENTRYPOINT ["python","app.py"]
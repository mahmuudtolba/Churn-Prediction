FROM python:3.7
ENV PYTHONUNBUFFERED=TRUE
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT churn_serving:app
FROM python:3.7
ENV PYTHONUNBUFFERED=TRUE
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
EXPOSE 9696
ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:9696", "churn_serving:app"]

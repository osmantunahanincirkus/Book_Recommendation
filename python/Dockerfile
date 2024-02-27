FROM python:3.10

WORKDIR /app
COPY ./python/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY ./python .

EXPOSE 5000

CMD ["python3", "sentiment_analysis.py"]
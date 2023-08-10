FROM python:3
WORKDIR /parse_telegram
ADD parse_telegram ./parse_telegram
COPY requirements.txt .
RUN pip install -r requirements.txt
CMD ["python", "parse_telegram"]

FROM python:3
WORKDIR /parse_telegram
ADD . /parse_telegram
RUN pip install -r requirements.txt
CMD ["python", "parse_telegram/__main__.py"]

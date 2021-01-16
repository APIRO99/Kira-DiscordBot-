FROM python:3.9.1-buster

WORKDIR /usr/src/Kira

COPY requirements.txt ./

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT ["python3"]
CMD ["/usr/src/Kira/main.py"]
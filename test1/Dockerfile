FROM python:3.12
WORKDIR /test1
COPY requirements.txt /test1
RUN pip3 install --upgrade pip -r requirements.txt
COPY . /test1
ENTRYPOINT ["python"]
CMD ["main.py"]
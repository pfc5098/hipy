FROM python:3.9

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir numpy

COPY . /ml
WORKDIR /ml 
CMD ["python3", "train.py"]
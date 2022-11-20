FROM python:3

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir numpy

COPY . /ml
WORKDIR /ml 
# CMD ls
CMD ["python3", "train.py"]
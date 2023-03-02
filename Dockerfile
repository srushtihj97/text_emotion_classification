FROM python:3.10-slim

RUN apt-get update --fix-missing && \
    apt-get install -y build-essential gnupg gcc g++ pandoc ca-certificates python3 python3-dev python git && \
    apt-get clean && \
    apt-get install -y google-perftools && \
    apt-get install -y libtcmalloc-minimal4 && \
    rm -rf /var/lib/apt/lists/*

# Install pip dependencies
COPY requirements.txt /app/


#RUN pip install \
RUN pip install --upgrade pip
RUN pip install --upgrade pip setuptools
RUN pip install -r /app/requirements.txt && \
    rm -rf /root/.cache

# Install directories
COPY text_emotion /app/

WORKDIR /app
EXPOSE 8000

# docker build -t text_emotion_classification:latest . -f Dockerfile

CMD ["/bin/sh", "-c", "python manage.py runserver 0.0.0.0:8000"]

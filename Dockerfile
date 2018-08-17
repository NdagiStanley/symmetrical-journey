FROM python
LABEL MAINTAINER="ndagis@gmail.com"
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install --upgrade pip \
  && pip3 install -r requirements.txt
COPY . .

# EXPOSE port to be used
EXPOSE 8000

# Set command to run as soon as container is up
CMD python3 manage.py runserver 0.0.0.0:8000

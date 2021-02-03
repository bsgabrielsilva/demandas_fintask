FROM python:3.6

#set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN apt-get update && apt-get upgrade -y
RUN pip install --upgrade pip
COPY ./requirements.txt .
COPY ./.env-test .env
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod +x ./docker-entrypoint.sh

CMD ["./docker-entrypoint.sh"]
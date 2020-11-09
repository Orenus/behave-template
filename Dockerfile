# Python base image 
FROM python:3.8

LABEL MAINTAINER="The Simple Company"

# Installing python dependencies
COPY ./requirements.txt ./requirements.txt
RUN python3 -m pip install -r requirements.txt
RUN python3 -m pip install behave

# Pushing the code inside the container
COPY . .

# Run the default command, can be overwritten
CMD ["behave"]
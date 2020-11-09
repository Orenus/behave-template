# Python base image 
FROM python:3.7

USER root

LABEL MAINTAINER="The Simple Company"

# Installing python dependencies
COPY ./requirements.txt ./requirements.txt
RUN python3 -m pip install -r requirements.txt

#RUN sbase install chromedriver latest
#RUN mv /usr/local/lib/python3.7/site-packages/seleniumbase/drivers/chromedriver /usr/bin/chromedriver

# Pushing the code inside the container
COPY . .

# Run the default command, can be overwritten
CMD ["behave"]

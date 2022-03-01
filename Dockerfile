# Use the python latest image
FROM python:3.8-slim
# Copy the current folder content into the docker image
COPY . /code
WORKDIR /code
# Install the required packages of the application
RUN pip install -r requirements.txt
# RUN useradd -ms /bin/bash admin
# USER admin

# Bind the port and refer to the app.py app
EXPOSE 8000
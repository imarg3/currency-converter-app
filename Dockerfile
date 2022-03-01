# Use the python latest image
FROM python:3.8-slim
# Install the required packages of the application
RUN pip install flask gunicorn forex-python redis
RUN useradd -ms /bin/bash admin
USER admin
# Copy the current folder content into the docker image
COPY . ./
# Bind the port and refer to the app.py app
CMD gunicorn --bind 0.0.0.0:8000 app:app
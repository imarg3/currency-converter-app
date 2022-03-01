FROM python:3.8-slim
# Use the python latest image
COPY . ./
# Copy the current folder content into the docker image
RUN pip install flask gunicorn forex-python
# Install the required packages of the application
CMD gunicorn --bind 0.0.0.0:8000 app:app
# Bind the port and refer to the app.py app
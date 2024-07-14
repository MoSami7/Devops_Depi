# the official Python image from the Docker Hub
FROM python:3.9-slim

# the working directory in the container
WORKDIR /Libapp

# install the dependencies
RUN pip install --no-cache-dir flask

# copy the current directory contents into the container at /app
COPY . .

# make port 5000 available to the world outside this container
EXPOSE 5000

# define environment variable
ENV FLASK_APP=app.py

# run the application
CMD ["flask", "run", "--host=0.0.0.0"]
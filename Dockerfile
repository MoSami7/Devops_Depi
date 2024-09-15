# the official Python image from the Docker Hub
FROM python:3.9-slim

# the working directory in the container
WORKDIR /Libapp

# Copy only requirements.txt to leverage Docker cache
COPY requirements.txt /Libapp/

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy only necessary application files
#COPY app.py /Libapp/
#COPY Books /Libapp/
#COPY create_db.py /Libapp/
#COPY FunctionDatabase.py /Libapp/
#COPY static/ /Libapp/static/
#COPY templates/ /Libapp/templates/

# copy the current directory contents into the container at /app
COPY . .
#COPY create_db.py /Libapp/


# make port 5000 available to the world outside this container
EXPOSE 5000

# define environment variable
ENV FLASK_APP=app.py

# run the application
CMD ["flask", "run", "--host=0.0.0.0"]Error response from daemon: error while creating mount source path '/var/lib/docker/containers': mkdir /var/lib/docker: read-only file system
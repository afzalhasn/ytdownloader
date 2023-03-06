# Use an official Python runtime as a parent image
FROM python:3.9-alpine

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Expose the port number that the app listens on
EXPOSE 5005

# Define the command to run the app
# CMD ["python", "app.py"]
CMD ["gunicorn", "--bind", "0.0.0.0:5005", "app:app"]
# docker build -t your-tag-name .
# docker run -p 5005:5005 your-tag-name

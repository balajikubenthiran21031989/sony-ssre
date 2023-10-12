# Use the same base image
FROM centos/python-38-centos7:latest

# Set the working directory in the container
WORKDIR /app

# Copy your application files into the container
COPY . .

# Install required Python packages
RUN pip3 install -r requirements.txt

# Install gunicorn
RUN pip3 install gunicorn

# Install requests
RUN pip3 install requests

# Expose port 5000 (or the port your Flask app is listening on)
EXPOSE 5000

# Command to run the Flask app with Gunicorn
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]


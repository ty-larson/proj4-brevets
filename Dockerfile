FROM python:3
LABEL maintainer="tyl@uoregon.edu"

# Update and install only essential build tools
RUN apt-get update -y && apt-get install -y build-essential

# Set up the application directory
COPY . /app
WORKDIR /app

# Install python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the entry point
ENTRYPOINT ["python"]
CMD ["flask_brevets.py"]
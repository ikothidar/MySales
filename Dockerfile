# Base image for Python Flask
FROM python:3.11-bullseye

# Set the working directory
WORKDIR .

# Copy the poetry dependency file
COPY pyproject.toml poetry.lock* ./

# Install poetry using pip
RUN pip install poetry

# Install poetry packages
RUN poetry install

# Copy the Flask app file
COPY . .

EXPOSE 5000

# Run the Flask app
CMD ["python", "server.py"]

# Base image for Python Flask
FROM python:3.11-slim-buster

# Set the working directory
WORKDIR .

# Copy the poetry dependency file
COPY pyproject.toml ./

# Install poetry using pip
RUN pip install poetry

# Install poetry packages
RUN poetry install --no-interaction --no-cache

# Copy the Flask app file
COPY . .

EXPOSE 5000

# Run the application using gunicorn as the server
CMD ["poetry", "run", "gunicorn", "-b", "0.0.0.0:5000", "server:app"]

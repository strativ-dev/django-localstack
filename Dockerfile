FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . /code/

# Expose the port the app runs on
EXPOSE 8000

RUN chmod +x /code/entrypoint.sh

# Run the application
CMD ["bash", "-c", "python manage.py runserver 0.0.0.0:8000"]

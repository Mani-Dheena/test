		
# Use official Python image
FROM python:3.12

# Set working directory inside the container
WORKDIR /app

# Copy the requirements file first (to leverage Docker's caching)
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire Django project into the container
COPY . /app/

# Expose Django's default port
EXPOSE 8000

# Run Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
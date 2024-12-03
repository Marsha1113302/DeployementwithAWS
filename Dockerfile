FROM python:3.12

# Set the working directory in the container
WORKDIR /app

# Copy only the files needed to install dependencies first, then app files for caching
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Copy the source code into the container
COPY src/ /app/src

# Expose the port the app runs on
EXPOSE 80

# Run the app
CMD ["python", "src/app.py"]
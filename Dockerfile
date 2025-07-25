# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy all files to the container
COPY . /app
#COPY dataset /app/dataset
#COPY output_json /app/src/output_json 
# (Optional) Install dependencies if you have requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run your Python file
CMD ["python", "app/main.py"]
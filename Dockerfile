# docker build -t mbrella:latest .
# docker run -p 5000:5000 mbrella:latest
FROM python:2.7

# Create app directory
WORKDIR /usr/src/app

# Add code
ADD . .

# Install the dependencies and force reinstall geocoder
RUN pip install -r requirements.txt --force-reinstall geocoder
# Set environment variables
ENV FLASK_APP=src/main.py
ENV FLASK_ENV=development
# Expose the application's port
EXPOSE 5000

# Run the application
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
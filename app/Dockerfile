FROM python

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .
# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the port the app runs on
EXPOSE 8501

# Set the environment variable for Streamlit
CMD [ "streamlit", "run", "main.py",\
"--server.port=8501", \
"--server.address=0.0.0.0"]


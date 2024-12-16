FROM ubuntu:20.04

# Install necessary dependencies
RUN apt-get update && apt-get install -y python3 python3-pip

# Install Jupyter and other Python packages
RUN pip3 install jupyter notebook numpy pandas

# Create a mock CUDA directory to simulate CUDA installation
RUN mkdir -p /usr/local/cuda/include /usr/local/cuda/lib64

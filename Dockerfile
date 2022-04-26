FROM python:3.8

# Working dir
WORKDIR /collecting_data

# Copy the source from the PWD to the working directory inside the container
COPY . /collecting_data

RUN apt-get update
RUN pip install --upgrade pip
RUN pip install -r requirements 

# CMD ["python", "./main.py -a SuperNetwork -d 2017-09-15"]
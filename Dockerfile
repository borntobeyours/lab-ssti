FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Create the flag.txt file
RUN echo "UNTAN{2a0ZUr9KDE8kA17GInfr}" > flag.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]

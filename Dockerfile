# use golang image for pull binary ffuf
FROM python:3.9

# workdir at /
WORKDIR /

# copy requirement.txt
COPY requirement.txt requirement.txt

# install dependencies
RUN python -m pip install --no-cache-dir -r requirement.txt

# copy app
COPY . .

# setup
RUN python -m pip install -e .

# expose port
EXPOSE 8000

# run program
CMD ["python", "main.py"]

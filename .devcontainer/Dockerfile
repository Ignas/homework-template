FROM python:3.8.3-buster

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update \
   && apt-get -y install --no-install-recommends virtualenv \
   #
   # Clean up
   && apt-get autoremove -y \
   && apt-get clean -y \
   && rm -rf /var/lib/apt/lists/*
ENV DEBIAN_FRONTEND=dialog

# Create a service user
RUN useradd -ms /bin/bash service
USER service
WORKDIR /home/service

# Make system pip work so we could use it to install developer tools
ENV PATH=/home/service/.local/bin:${PATH}

# Install all the python dependencies 
RUN virtualenv --python python3 .env
COPY requirements.txt .
RUN .env/bin/pip3 --disable-pip-version-check --no-cache-dir install -r ./requirements.txt

# Add the application
ADD --chown=service:service . app
RUN .env/bin/pip3 install -e app

# We intentionally use different ports for vscode launch and docker entrypoint so they would not conflict in 
# case you are trying to work using both approaches at the same time
ENTRYPOINT /home/service/.env/bin/gunicorn -b 0.0.0.0:6544 homework:application

FROM python:3.7.6
USER root

# install google chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get -y update && apt-get install -y google-chrome-stable && apt-get install -yqq unzip
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

# install heroku cli
RUN curl https://cli-assets.heroku.com/install.sh | sh

# set display port to avoid crash
ENV DISPLAY=:99

# install apt packages
RUN apt-get update && apt-get install -y \
    && apt-get install -y portaudio19-dev libasound2-dev alsa-utils \
    && pip install --upgrade pip

# install python modules
WORKDIR /Users/aka/projects/5sec_fourier
COPY requirements.txt /home
RUN pip install -r /home/requirements.txt

# flask setting
ENV FLASK_APP '/Users/aka/projects/5sec_fourier/app.py'
ENV FLASK_DEBUG 1

# link audiodevice
CMD [ "--device=/dev/snd:/dev/snd" ]
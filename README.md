## require before run
```
sudo apt-get update \
    && apt-get install -y gcc vim supervisor \
    && rm -rf /tmp/* /var/cache/* 
```
```
mkdir /var/log/apps
```
```
cp ./conf/services.conf /etc/supervisor/conf.d
```
## install requirements
```
pip install -r requirements.txt
```
## install ffmpeg
```
https://formulae.brew.sh/formula/ffmpeg
```
## SETUP OUPUT PATH IN ENV
```
cp sample.env .env
vim .env
```
## RUN
```
supervisord -n -c /etc/supervisor/supervisord.conf
```
## Extra steps
I won't require a separate env as this is the only thing this pi would do

generate psk entry for supplicant file with

```wpa_passphrase "<SSID>" <password>```

create wpa_supplicant.conf file
```
country=AU
update_config=1
ctrl_interface=/var/run/wpa_supplicant

network={
 ssid="<WIFI NETWORK NAME>"
 psk=7b7af4ec93810e597d73a127c650a2a7076bc1c6b25db6d2bb77cfc2e4e60bb6
}
```

[enable sense-hat](https://projects.raspberrypi.org/en/projects/getting-started-with-the-sense-hat)

[open GPIO interface](https://learn.sparkfun.com/tutorials/raspberry-pi-spi-and-i2c-tutorial/all)

install influx python packages ```sudo -H pip3 install influxdb``` 

# update pip as it is sometimes gets broken
sudo pip3 install --ignore-installed pip 
sudo -H pip install pip-upgrade-outdated

Installing dependencies for Pillow
sudo apt-get install libjpeg-dev -y
sudo apt-get install zlib1g-dev -y
sudo apt-get install libfreetype6-dev -y
sudo apt-get install liblcms1-dev -y
sudo apt-get install libopenjp2-7 -y
sudo apt-get install libtiff5 -y

sudo apt install libgirepository1.0-dev gcc libcairo2-dev pkg-config python3-dev gir1.2-gtk-3.0
sudo pip install --ignore-installed numpy
sudo pip_upgrade_outdated

# Cron jobs
crontab -e 
([pi docs](https://www.raspberrypi.org/documentation/linux/usage/cron.md))
# My Pi's

## Tooling and initial setup

1. Download [etcher](https://www.balena.io/etcher/)
2. Download latest version of [raspbian](https://www.raspberrypi.org/downloads/raspbian/)
3. Burn image to sd card


### Tooling
After initial boot, login as pi (default user)
login: pi
password: raspberry

- change root user password
```
sudo su
passwd
```
- restart / login as root
```sudo reboot```

- config locale and other settings
```raspi-config```

- create new user / delete user pi

change default editor for ```visudo```
```update-alternatives --set editor /usr/bin/vim.tiny```

add user
```adduser _%USER%_```

list groups wich pi is belonging
```cat /etc/group | grep pi```
add new user to these groups
udo usermod -G allllllll_groups %username%

delete pi user
userdel -r pi

add user to sudoers (no sudo prefix) - optional
```
visuo
%user%  ALL=(ALL:ALL) ALL
```

enable ssh access
```raspi-config```
enable ssh interface


Change vim to show line numbers by default
```vi ~/.vimrc```
Add: 
```set nu```

Change shell from bash to zshell

Run update scripts 

apt update && apt upgrade -y

Install certificates
apt install -y ca-certificates




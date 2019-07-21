# My Pi's

## Tooling and initial setup

1. Download [etcher](https://www.balena.io/etcher/)
2. Download latest version of [raspbian](https://www.raspberrypi.org/downloads/raspbian/)
3. Burn image to sd card


After initial boot, login as pi (default user)
login: pi
password: raspberry



#### Enable ssh access

1. Before inserting ssd fro the first time, SSH can be enabled by placing a file called ssh in to the boot folder. This flags the Pi to enable the SSH system on the next boot.
2. On pi cli ``` raspi-config ``` and enable ssh interface


### Tooling

- change root user password
```
sudo su
passwd
```
- restart / login as root```sudo reboot```

- config locale and other settings ```raspi-config```

###Create new user / delete user pi

change default editor for ```visudo```
```
update-alternatives --set editor /usr/bin/vim.tiny
```

add user ```adduser _%USER%_```

list groups wich pi is belonging ```cat /etc/group | grep pi```

add new user to these groups ```sudo usermod -G *groups_from_list* %username%```

delete pi user ```userdel -r pi```

add user to sudoers (no sudo prefix) - **optional**
```
visuo
%user%  ALL=(ALL:ALL) ALL
```

Change vim to show line numbers by default & vi behaviour (arrow keys and delete) ```vi ~/.vimrc```

install full vim (vi tiny has no colour support) ```sudo apt install vim -y```

Add:  
```
syntax on
set nocp
set nu
set backspace=2
```

Change shell from bash to zshell

Run update scripts ```apt update && apt upgrade -y```

Install certificates (just in case) ```apt install -y ca-certificates```

Update locale settings (sometimes they fall off) 
```
update-locale
raspi-config
```
Generate locale for all en_AU & an_US, set default to en_US.utf-8

Install zhell ```apt -y install zsh```

Permanently switch bash to zhell ```chsh -s $(which zsh) $(whoami)```

Install git ```apt install git -y```

Install oh-my-zsh configuration framework ``` sh -c "$(wget https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"```

Install powerlevel9k zsh cli custom output theme ```git clone https://github.com/bhilburn/powerlevel9k.git ~/.oh-my-zsh/custom/themes/powerlevel9k```

Install auto-suggestions and code-highlight zshell plugins
```
git clone https://github.com/zsh-users/zsh-autosuggestions ~/.oh-my-zsh/custom/plugins/zsh-autosuggestions
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ~/.oh-my-zsh/custom/plugins/zsh-syntax-highlighting
git clone https://github.com/zsh-users/zsh-completions.git ~/.oh-my-zsh/custom/plugins/zsh-completions
```

Change ```~/.zshrc``` (Note: if nerdfont-complete pack is not installed, the font pack also needs to be installed on controlling / admin system)

a) insert
```
# power level config
POWERLEVEL9K_MODE="nerdfont-complete"
POWERLEVEL9K_PROMPT_ON_NEWLINE=true
POWERLEVEL9K_LEFT_PROMPT_ELEMENTS=(virtualenv dir vcs)
POWERLEVEL9K_PYTHON_ICON="\U1F40D"
```

b) change theme
```
ZSH_THEME="powerlevel9k/powerlevel9k"
```

c) Update plugins
```
plugins=( [plugins...]
	     zsh-completions
         zsh-autosuggestions
         zsh-syntax-highlighting
         )
```

Save & Exit ```source ~/.zshrc```

Install mc ```apt -y install mc```
if mc shows ??? instead of pseudo-characters, run ```dpkg-reconfigure locales```

##### passwordless ssh 

[From Pi Docs](https://www.raspberrypi.org/documentation/remote-access/ssh/passwordless.md) 
```
ssh-copy-id <USERNAME>@<IP-ADDRESS>
```

##### for fun 
install cowsay / fortune / lolcat
add to zshrc: alias cow="fortune | cowsay | lolcat"

make cow every time terminal starts append 'cow'at the end of zshrc


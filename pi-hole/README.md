# Installing pi-hole
- Follow instructions from [project website](https://pi-hole.net)
- Adjust DNS setting in named service (block forwarders)
- Adjust settings in router config to have second dns set to pi-hole
- Adjust settings for vpn server > advanced settings > 

Advertise DNS to clients > no

Custom config > 

```
push "dhcp-option DNS 192.168.1.75"
push "dhcp-option DNS 192.168.1.76"
```

- if ftl-service is down
```
sudo service pihole-FTL restart
```
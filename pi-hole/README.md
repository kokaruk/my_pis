# Installing pi-hole
- Follow instructions from [project website](https://pi-hole.net)
- Adjust DNS setting in named service on primary (block forwarders)
- Adjust settings in router config to have second dns set to pi-hole
- Adjust settings for <br>
vpn server > advanced settings > Advertise DNS to clients > no

Custom config > 

```
push "dhcp-option DNS 192.168.50.76"
```

- if ftl-service is down
```
sudo service pihole-FTL restart
```

Use pi hole to resolve local dns

1. Create a new hosts file -- sudo vi /etc/hosts.kokaruk
2. Add IP addresses followed by the local hostname you'd like to resolve, one per line. Write out and exit.

```
192.168.50.75 kokaruk.com
192.168.50.75 www.kokaruk.com
192.168.50.75 ap.kokaruk.com
192.168.50.75 grafana.kokaruk.com
192.168.50.75 server.kokaruk.com
192.168.50.75 staging.kokaruk.com
192.168.50.75 wp.kokaruk.com
192.168.50.75 istqb.kokaruk.com
```

3. Create a new dnsmasq conf file -- sudo vi /etc/dnsmasq.d/02-mydns.conf.
4. Add one line -- addn-hosts=/etc/hosts.kokaruk. Write out and exit.
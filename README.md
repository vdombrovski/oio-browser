OpenIO Browser
===

Setup
---

*You need node, npm, python2.7*

First, get the official OPENIO docker image [here](http://docs.openio.io/docker-image/), and run it with --net-host and an accessible IP Address:

> You need to replace [IP_ADDRESS] by the IP address available on your system.

```sh
# Example
$ docker run -ti -e OPENIO_IPADDR=[IP_ADDRESS] --net=host openio/sds
```
Instal npm:

Debian/Ubuntu:

```sh
$ apt-get install npm
```

Centos:

```sh
$ yum install -y npm.x86_64
```

Install elasticsearch:

Debian/Ubuntu:

https://www.elastic.co/guide/en/elasticsearch/reference/current/deb.html

Centos:

https://www.elastic.co/guide/en/elasticsearch/reference/current/rpm.html

Then install the browser

```sh
$ git clone [repo]
$ cd oio-browser
$ pip install -r requirements.txt
$ pip install elasticsearch
$ npm i
```

And finally...

```sh
$ python app.py -e <elasticsearch IP> -u http://[oioproxy_IP]:[oioproxy_PORT] -n [oio_namespace] -a [oio_account] -p [interface_port]
e.g.
$ python app.py -e 10.0.0.48 -u http://10.0.0.44:6006 -n OPENIO -a ACCOUNT_GRID2 -p 8080
```

Now head on to http://localhost:8000 and enjoy!

> The default account is *default*, support for more accounts coming soon


TODO List
---

- Remove node/npm dependency
- Adding containers
- Changing accounts
- Account info, container info
- Delete objects
- Exception processing (IMPORTANT)
- Logging
- Dockerize
- Tests
- ...

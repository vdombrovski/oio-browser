OpenIO Browser
===

This is a demo feel free to improve it

Setup
---

*You need node, npm, python2.7*

First, get the official OPENIO docker image [here](http://docs.openio.io/docker-image/), and run it with --net-host and an accessible IP Address:

> You need to replace [IP_ADDRESS] by the IP address available on your system.

```sh
# Example
$ docker run -ti -e OPENIO_IPADDR=[IP_ADDRESS] --net=host openio/sds
```
Install npm:

Debian/Ubuntu:

```sh
$ apt-get install npm
```

Centos:

```sh
$ yum install -y npm.x86_64
```

Install elasticsearch:

You will need java 8 (openjdk/jre is ok)

Debian/Ubuntu:

https://www.elastic.co/guide/en/elasticsearch/reference/current/deb.html

Centos:

https://www.elastic.co/guide/en/elasticsearch/reference/current/rpm.html

Install oio-sds python module:

Debian/Ubuntu:

```sh
$ echo "deb http://mirror.openio.io/pub/repo/openio/sds/16.10/$(lsb_release -i -s)/ $(lsb_release -c -s)/" | sudo tee /etc/apt/sources.list.d/openio-sds.list
$ sudo apt-get install curl -y
$ curl http://mirror.openio.io/pub/repo/openio/APT-GPG-KEY-OPENIO-0 | sudo apt-key add -
$ sudo apt-get update; sudo apt-get install openio-sds
```

Centos:

```sh
$ yum -y install http://mirror.openio.io/pub/repo/openio/sds/16.10/el/openio-sds-release-16.10-1.el.noarch.rpm
$ yum -y install openio-sds-server-3.2.3-1.el7.oio.x86_64
```


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

If you need any help feel free to join https://openio-community.slack.com

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

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
$ python2 app.py --url [IP_ADDRESS]:6006
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

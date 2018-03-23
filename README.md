OpenIO Browser
===

Setup
---

```sh
git clone https://github.com/vdombrovski/oio-browser && cd oio-browser
docker run -td --net=host --name sds openio/sds
docker exec -ti sds openio account create BROWSER --oio-ns OPENIO
apt install -y npm virtualenv
virtualenv env
source env/bin/activate
npm i && pip install -r requirements.txt
./copy-deps.sh
python2 app.py -u http://127.0.0.1:6006 -n OPENIO -a BROWSER -p 8080
```

Head to http://[HOST_IP]:8080 to see the UI

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

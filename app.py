from flask import Flask, send_from_directory, request, jsonify, Response
from oio.api.object_storage import ObjectStorageAPI
import optparse
import mimetypes


def parse():
    parser = optparse.OptionParser()
    parser.add_option("-n", "--namespace", help="Namespace to use")
    parser.add_option("-u", "--url", help="OIO-Proxy IP:PORT")
    parser.add_option("-a", "--account", help="Account to use")
    parser.add_option("-p", "--port", help="OpenIO browser ports")
    options, _ = parser.parse_args()
    return options

def get_extensions_for_type(general_type):
    for ext in mimetypes.types_map:
        if mimetypes.types_map[ext].split('/')[0] == general_type:
            yield ext


def init_sds_osapi(ns, url):
    try:
        return ObjectStorageAPI(ns, url)
    except Exception as e:
        raise Exception('Could not access API at %s' % url)

options = parse()

PROXY_URL = options.url
BROWSER_PORT = options.port or 8000
if not options.url:
    raise ValueError('Please set oioproxy url using --url parameter')
NAMESPACE = options.namespace or 'OPENIO'
ACCOUNT = options.account or 'default'
API = init_sds_osapi(NAMESPACE, PROXY_URL)

# Create some containers for now
#API.container_create(ACCOUNT, "Documents")
#API.container_create(ACCOUNT, "Cat Videos")
#API.container_create(ACCOUNT, "Work")
API.container_create(ACCOUNT, "img")
API.container_create(ACCOUNT, "static")
API.object_create(ACCOUNT, "static", file_or_path="./no_image.png")

app = Flask(__name__, static_url_path='')


@app.route('/')
def index_alias():
    return send_from_directory('static', 'index.html')


@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)


@app.route('/api/containers/<cont>/objects', methods=['POST'])
def upload_object(cont):
    if 'file' not in request.files:
        return "400"
    f = request.files['file']
    if f.filename == '':
        return "400"
    API.object_create(ACCOUNT, cont.strip(), file_or_path=f,
                      obj_name=f.filename.strip())
    return "200"


@app.route('/api/containers/<cont>/objects/<obj>/download')
def download_object(cont, obj):
    meta, stream = API.object_fetch(ACCOUNT, cont, obj=obj)
    headers = {
        "Content-Disposition": "attachment; filename=%s" % meta['name']
    }
    return Response(stream, direct_passthrough=True,
                    mimetype=meta['mime_type'], headers=headers)

@app.route('/api/containers/<cont>/objects/<obj>/preview')
def preview_object(cont, obj):
    try:
        meta, stream = API.object_fetch(ACCOUNT, cont, obj=obj)
        ext = obj.split(".")
        ext = '.' + ext[len(ext)-1].lower()
        mimetypes.init()
        img_type = tuple(get_extensions_for_type('image'))
        if ext in img_type:
            headers = {
                "Content-Disposition": "filename=%s" % meta['name']
            }
            return Response(stream, direct_passthrough=True,
                    mimetype=mimetypes.types_map[ext], headers=headers)
        else:
            meta, stream = API.object_fetch(ACCOUNT, "static", obj="no_image.png")
            ext = ".png"
            headers = {
                "Content-Disposition": "filename=%s" % meta['name']
            }
            return Response(stream, direct_passthrough=True,
                    mimetype=mimetypes.types_map[ext], headers=headers)
    except Exception as e:
        meta, stream = API.object_fetch(ACCOUNT, "static", obj="no_image.png")
        ext = ".png"
        headers = {
                "Content-Disposition": "filename=%s" % meta['name']
            }
        return Response(stream, direct_passthrough=True,
                    mimetype=mimetypes.types_map[ext], headers=headers)


@app.route('/api/containers/<cont>/objects/search/<prefix>', methods=['GET'])
@app.route('/api/containers/<cont>/objects/<marker>', methods=['GET'])
@app.route('/api/containers/<cont>/objects/', methods=['GET'])
@app.route('/api/containers/<cont>/objects', methods=['GET'])
def list_objects(cont, marker=None, prefix=None):
    res = API.object_list(ACCOUNT, cont, limit=20000, marker=marker,
                          prefix=prefix, properties=True)
    return jsonify(**res)


@app.route('/api/containers/<marker>', methods=['GET'])
@app.route('/api/containers/', methods=['GET'])
@app.route('/api/containers', methods=['GET'])
def list_containers(marker=None):
    listing, info = API.container_list(ACCOUNT, limit=20, marker=marker)
    return jsonify({'containers': listing, 'info': info})


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=BROWSER_PORT)

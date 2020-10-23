  
from flask import Flask, request, jsonify
from waitress import serve
from data_access import *


app = Flask(__name__)


@app.route('/api/layout', methods=['GET', 'POST'])
def collection():
    if request.method == 'GET':
        all_layouts = get_all_layouts()
        return json.dumps(all_layouts)
    elif request.method == 'POST':
        data = request.form
        result = add_layout(data['layout_id'], data['name'])
        return jsonify(result)


@app.route('/api/layout/<layout_id>', methods=['GET', 'PUT', 'DELETE'])
def resource(layout_id):
    if request.method == 'GET':
        song = get_single_layout(layout_id)
        return json.dumps(song)
    elif request.method == 'PUT':
        data = request.form
        result = edit_layout_name(layout_id, data['name'])
        return jsonify(result)
    elif request.method == 'DELETE':
        result = delete_layout(layout_id)
        return jsonify(result)


if __name__ == '__main__':
    serve(app, port=8000)
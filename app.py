  
from flask import Flask, request, jsonify
from waitress import serve
from data_access import *


app = Flask(__name__)

#LAYOUT ROUTES
@app.route('/api/layout', methods=['GET', 'POST'])
def layout_collection():
    if request.method == 'GET':
        all_layouts = get_all_layouts()
        return json.dumps(all_layouts)
    elif request.method == 'POST':
        data = request.form
        result = add_layout(data['layout_id'], data['name'])
        return jsonify(result)


@app.route('/api/layout/<layout_id>', methods=['GET', 'PUT', 'DELETE'])
def layout_resource(layout_id):
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

#DECODER ROUTES
@app.route('/api/layout/<layout_id>/decoder', methods=['GET', 'POST'])
def decoder_collection(layout_id):
    if request.method == 'GET':
        all_decoders = get_all_decoders(layout_id)
        return json.dumps(all_decoders)
    elif request.method == 'POST':
        data = request.form
        result = add_decoder(layout_id, data['decoder_nr'], data['value'])
        return jsonify(result)

@app.route('/api/layout/<layout_id>/decoder/<decoder_nr>', methods=['GET', 'PUT', 'DELETE'])
def decoder_resource(layout_id, decoder_nr):
    if request.method == 'GET':
        song = get_single_decoder(layout_id,decoder_nr)
        return json.dumps(song)
    elif request.method == 'PUT':
        data = request.form
        result = edit_decoder_value(layout_id, decoder_nr, data['value'])
        return jsonify(result)
    elif request.method == 'DELETE':
        result = delete_decoder(layout_id, decoder_nr)
        return jsonify(result)


if __name__ == '__main__':
    serve(app, port=8000)
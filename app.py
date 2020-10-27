  
from flask import Flask, request, jsonify
from waitress import serve
from data_access import *
from app_config import *


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
        layout = get_single_layout(layout_id)
        return json.dumps(layout)
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
        decoder = get_single_decoder(layout_id,decoder_nr)
        return json.dumps(decoder)
    elif request.method == 'PUT':
        data = request.form
        result = edit_decoder_value(layout_id, decoder_nr, data['value'])
        return jsonify(result)
    elif request.method == 'DELETE':
        result = delete_decoder(layout_id, decoder_nr)
        return jsonify(result)

#SCREEN ROUTES
@app.route('/api/layout/<layout_id>/screen', methods=['GET', 'POST'])
def screen_collection(layout_id):
    if request.method == 'GET':
        all_screens = get_all_screens(layout_id)
        return json.dumps(all_screens)
    elif request.method == 'POST':
        data = request.form
        result = add_screen(layout_id, data['screen_nr'], data['fullscreen'])
        return jsonify(result)

@app.route('/api/layout/<layout_id>/decoder/<screen_nr>', methods=['GET', 'PUT', 'DELETE'])
def screen_resource(layout_id, screen_nr):
    if request.method == 'GET':
        screen = get_single_screen(layout_id, screen_nr)
        return json.dumps(screen)
    elif request.method == 'PUT':
        data = request.form
        result = edit_decoder_value(layout_id, screen_nr, data['fullscreen'])
        return jsonify(result)
    elif request.method == 'DELETE':
        result = delete_decoder(layout_id, screen_nr)
        return jsonify(result)

#LAYOUT AMOUNT ROUTES
@app.route('/api/settings/layout/amount', methods=['GET', 'PUT', 'DELETE'])
def settings_resource():
    if request.method == 'GET':
        setting = read_setting(Settings.layout_amount)
        return json.dumps(setting)
    elif request.method == 'PUT':
        data = request.form
        write_setting(Settings.layout_amount, data['amount'])
        return {'status': 1, 'message': 'Layout Amount Updated'}

if __name__ == '__main__':
    serve(app, port=8000)
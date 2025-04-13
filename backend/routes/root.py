from flask import request, jsonify
from flask_smorest import Blueprint
from backend.models.google_ai import GoogleAI

blp = Blueprint('root', __name__)


@blp.route('/health')
def health():
    return "This is health"

@blp.route('/health2')
def health():
    return "This is health2"

@blp.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image part'}), 400

    file = request.files['image']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file:
        ga = GoogleAI()
        invoice = ga.parse_invoice(file)
        invoice_json = invoice.model_dump_json(indent=2)
        return invoice_json, 200

    return jsonify({'error': 'Unknown error'}), 500
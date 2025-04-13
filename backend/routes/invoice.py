from flask import send_file
from flask.views import MethodView
from flask_smorest import Blueprint
from flask_marshmallow import Schema, fields
from models.google_ai import GoogleAI


blp = Blueprint('invoice', __name__, url_prefix='/api/invoice', description="Invoice operations")

class UploadNewInvoiceSchema(Schema):
    image = fields.File(required=True)

@blp.route('/<string:invoice_id>')
class GetInvoiceRoute(MethodView):

    def get(self, invoice_id):
        print(invoice_id)
        with open('../data/invoice.json', 'r') as file:
            data = file.read()
            return data, 200


@blp.route('/new')
class UploadNewInvoiceRoute(MethodView):

    @blp.arguments(UploadNewInvoiceSchema, location='files')
    def post(self, args):
        invoice_img = args['image']
        ga = GoogleAI()
        invoice = ga.parse_invoice(invoice_img)
        invoice_json = invoice.model_dump_json(indent=2)
        return invoice_json, 200


@blp.route('/image/<string:img_id>')
class GetInvoiceImageRoute(MethodView):

    def get(self, img_id):
        print(img_id)
        return send_file('../data/invoice.jpg', mimetype='image/jpg')
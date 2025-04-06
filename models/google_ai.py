import io
from google import genai
import PIL.Image
from app.config import Config
from models.models import Invoice


class GoogleAI:

    def __init__(self):
        self.client = genai.Client(api_key=Config.API_KEY)

    def parse_invoice(self, invoice_img):
        prompt = """
        Extract information from an invoice image and return it in JSON format.
    
        You should identify key details from the invoice such as invoice number, date, total amount, items listed with their descriptions, and any other relevant information typically found on an invoice.
    
        # Steps
    
        1. **Image Processing**: Use an OCR (Optical Character Recognition) tool to convert the image content into text.
        2. **Information Extraction**: Analyze the extracted text to identify key elements such as:
            - Invoice Number
            - Date
            - Vendor Information
            - Customer Information
            - Itemized List of Products or Services (including descriptions, quantities, and prices)
            - Subtotal, Total Amount, Taxes, and any Discounts
        3. **Data Structuring**: Organize these details into a structured JSON format.
    
        # Output Format
    
        The output should be a structured JSON object containing all the extracted information. Here is the recommended structure:
    
        ```json
        {
            "invoice_number": "[INVOICE_NUMBER]",
            "date": "[DATE]",
            "vendor": {
                "name": "[VENDOR_NAME]",
                "address": "[VENDOR_ADDRESS]"
            },
           "table": "[TABLE_CODE]",
            "diners": "[DINERS_NUM]",
            "items": [
                {
                    "name": "[ITEM_NAME]",
                    "quantity": "[QUANTITY]",
                    "unit_price": "[UNIT_PRICE]",
                    "price": "[PRICE]"
                }
                // Repeat for each item...
            ],
            "subtotal": "[SUBTOTAL]",
            "taxes_percent": "[TAXES_PERCENT]",
            "taxes": "[TAXES]",
            "total": "[TOTAL]",
            "discounts": "[DISCOUNTS]"
        }
        ```
    
        # Examples
    
        - **Input**: An image of a sample invoice containing various necessary details.
        - **Output**: 
    
        ```json
        {
            "invoice_number": "INV123456",
            "date": "2025-10-22",
            "vendor": {
                "name": "ABC Supplies",
                "address": "123 Elm St, Springfield"
            },
           "table": "T6",
            "diners": "10",
            "items": [
                {
                    "name": "Tika Massala",
                    "quantity": "2",
                    "unit_price": "12.00",
                    "price": "24.00"
                },
                {
                    "description": "Beer",
                    "quantity": "1",
                    "unit_price": "7.00",
                    "price": "7.00"
                }
            ],
            "subtotal": "285.00",
           "taxes_percent": "10%",
            "taxes": "22.80",
            "total": "307.80",
            "discounts": "10.00"
        }
        ```
    
        # Notes
    
        - Verify the accuracy of the OCR tool to ensure all text is correctly extracted.
        - Different invoices may have varied layouts; adapt accordingly to capture all required information.
        - Handle any anomalies like missing fields or illegible text gracefully.
        - If some of this fields are missing fill the gap with "None"
        - If you don't find the unit price in the invoice, remove it from the json
        - The date should be higher than 2025 and follow this format %Y-%m-%d
        """

        #image = PIL.Image.open('images/drinks.jpg')
        image = PIL.Image.open(io.BytesIO(invoice_img.read()))

        response = self.client.models.generate_content(
            model="gemini-2.0-flash",
            contents=[image, prompt],
            config={
                'response_mime_type': 'application/json',
                'response_schema': Invoice
            })

        try:
            invoice = response.parsed
            is_total_ok = invoice.check_total()
            print("The total amount make sense: ", is_total_ok)
            return invoice
        except Exception as e:
            print(e)

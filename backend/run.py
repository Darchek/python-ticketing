import os

from flask import send_from_directory

from app import create_app

app = create_app()



@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_static(path):
    if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')




if __name__ == '__main__':
    print("Server running on port 5000")
    app.run(debug=True, use_reloader=False, host='0.0.0.0', port=5000)
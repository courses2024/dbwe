from flask import render_template, request, jsonify
from app import app, db
from werkzeug.http import HTTP_STATUS_CODES

def api_error_response(status_code, message=None):
    payload = {'error': HTTP_STATUS_CODES.get(status_code, 'Unknown error')}
    if message:
        payload['message'] = message
    return payload, status_code

@app.errorhandler(404)
def not_found_error(error):
    if request.accept_mimetypes.accept_json and \
    not request.accept_mimetypes.accept_html:
        return api_error_response(404, 'The requested resource was not found')
    else:
        return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    if request.accept_mimetypes.accept_json and \
    not request.accept_mimetypes.accept_html:
        return api_error_response(500, 
               'An internal server error occurred, the administrator has been notified')
    return render_template('500.html'), 500

def bad_request(message):
    return api_error_response(400, message)



from flask import jsonify


def response(code, service, message, data, status_code):
    response_message = (
        jsonify(
            {
                "status": {"code": code, "service": service, "message": message},
                "data": data,
            }
        ),
        status_code,
    )

    return response_message

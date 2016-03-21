
# status_code: [success:0, warn:1, error:2]
def response_message(status_code, message):
    resp_message = {
        "status": status_code,
        "msg": message
    }
    return resp_message

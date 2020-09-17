# coding=utf-8


def join_match_queue(user):

    try:
        status = True
        message = 'success'
    except Exception as e:
        status = False
        message = str(e)

    result = {
        'status': status,
        'message': message
    }

    return result


def quit_match_queue(user):

    try:
        status = True
        message = 'success'
    except Exception as e:
        status = False
        message = str(e)

    result = {
        'status': status,
        'message': message
    }

    return result


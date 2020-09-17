# coding=utf-8




def user_login(user_name, password):
    user = None
    try:
        user = {
                'name': 'zhangsan',
                'rank': 123,
                'token': 'token_test'
            }
        status = True
        message = 'success'
    except Exception as e:
        status = False
        message = str(e)


    result = {
        'status': status,
        'message': message,
        'user': user
    }

    return result



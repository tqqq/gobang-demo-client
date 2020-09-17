# coding=utf-8
import time




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


def get_match(user):


    while True:
        time.sleep(1)
        print(str(user))
        try:
            match = {
                'match_id': 100,
                'player1':{
                    'id': 10,
                    'name': 'zhangsan',
                    'rank': 1100
                },
                'player2': {
                    'id': 11,
                    'name': 'lisi',
                    'rank': 1200
                },
                'create_time': '2020-09-10 20:00:00',
                'status': 'PREPARING'
            }
            status = True

            if status:
                result = {
                    'match': match,
                    'status': status
                }
                return result
        except Exception as e:
            result = {
                'match': None,
                'status': False
            }
            return result






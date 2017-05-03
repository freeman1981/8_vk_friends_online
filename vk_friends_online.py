import vk


APP_ID = -1  # чтобы получить app_id, нужно зарегистрировать своё приложение на https://vk.com/dev


def get_user_login():
    # for testing
    # return '***'
    return input('Please enter vk login: ')


def get_user_password():
    # for testing
    # return '***'
    return input('Please enter vk password: ')


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends'
    )
    api = vk.API(session)
    vk_online_friends_ids = api.friends.getOnline()
    vk_online_friends = api.users.get(user_ids=','.join(str(item) for item in vk_online_friends_ids))
    return vk_online_friends


def output_friends_to_console(vk_online_friends):
    for vk_online_friend in vk_online_friends:
        print('{} {}'.format(vk_online_friend['first_name'], vk_online_friend['last_name']))

if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)

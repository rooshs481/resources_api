from app.models import Key


FAKE_EMAIL = 'test@example.org'
FAKE_APIKEY = 'abcdef1234567890'


def create_fake_key(session, **kwargs):
    kwargs['email'] = kwargs.get('email', FAKE_EMAIL)
    kwargs['apikey'] = kwargs.get('apikey', FAKE_APIKEY)
    key = Key(**kwargs)
    session.add(key)
    session.commit()
    return key


def apikey_commit(client, email, password, **kwargs):

    response = client.post(
        'api/v1/apikey',
        **kwargs,
        json=dict(
            email=email,
            password=password
        ),
    )

    return response
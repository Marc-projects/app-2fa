import jwt, os

def verify_jwt(token: str) -> dict:
    SECRET_KEY_2FA = os.environ.get('SECRET_KEY_2FA')
    try:
        decoded = jwt.decode(token, SECRET_KEY_2FA, algorithms=['HS256'])
        return decoded['user']
    except jwt.ExpiredSignatureError:
        print("Token expiré")
        return None
    except jwt.InvalidTokenError:
        print("Token invalide")
        return None
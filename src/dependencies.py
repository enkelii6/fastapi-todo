from fastapi import HTTPException, status
from fastapi.requests import Request


async def get_user_id(request: Request):
    user_id = request.headers.get('x-user-id', None)
    if not user_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    return user_id

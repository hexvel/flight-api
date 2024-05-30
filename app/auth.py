from fastapi import HTTPException


def verify_api_key(api_key: str):
    if api_key != "secret":
        raise HTTPException(status_code=403, detail="Forbidden")

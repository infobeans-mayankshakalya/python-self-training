from fastapi import Request, HTTPException

def authorizeAPI(request: Request):
    api_auth = request.headers.get("X-Api-key")
    if not api_auth:
        raise HTTPException(status_code=400, detail="Missing API Key header")
    if api_auth != 'mytoken':
        raise HTTPException(status_code=402, detail="Unauthorized access.")
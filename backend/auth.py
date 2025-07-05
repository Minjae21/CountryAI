from fastapi.security import OAuth2AuthorizationCodeBearer
from msal import ConfidentialClientApplication
import os
from fastapi import Depends, HTTPException, APIRouter
from dotenv import load_dotenv
import jwt
from fastapi.responses import RedirectResponse

load_dotenv()

# config
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
TENANT_ID = os.getenv("TENANT_ID")
AUTHORITY = f"https://login.microsoftonline.com/{TENANT_ID}"
SCOPES = ["https://graph.microsoft.com/Calendars.Read"]
REDIRECT_URI = "http://localhost:8000/auth/callback"

token_cache = {}

# init MSAL application
def get_auth_client():
    return ConfidentialClientApplication(
        client_id=CLIENT_ID,
        client_credential=CLIENT_SECRET,
        authority=AUTHORITY
    )

# main token access function
def get_access_token():
    if "access_token" in token_cache:
        return token_cache["access_token"]

    app = get_auth_client()
    accounts = app.get_accounts()

    if accounts:
        result = app.acquire_token_silent(scopes=SCOPES, account=accounts[0])
        if "access_token" in result:
            token_cache.update(result)
            return result["access_token"]

    auth_url = app.get_authorization_request_url(
        scopes=SCOPES,
        redirect_uri=REDIRECT_URI
    )
    raise HTTPException(
        status_code=401,
        detail="Not authenticated",
        headers={"Location": auth_url}
    )

debug_router = APIRouter()

@debug_router.get("/debug/token")
async def debug_token(token: str = Depends(get_access_token)):
    try:
        decoded = jwt.decode(token, options={"verify_signature": False})
        return {
            "scopes": decoded.get("scp", "No scopes found"),
            "roles": decoded.get("roles", "No roles found"),
            "audience": decoded.get("aud"),
            "issuer": decoded.get("iss"),
            "expires": decoded.get("exp"),
            "issued_at": decoded.get("iat")
        }
    except Exception as e:
        return {"error": str(e)}

auth_router = APIRouter()

@auth_router.get("/login")
async def login():
    auth_url = get_auth_client().get_authorization_request_url(
        scopes=SCOPES,
        redirect_uri=REDIRECT_URI
    )
    return RedirectResponse(auth_url)

@auth_router.get("/auth/callback")
async def auth_callback(code: str):
    result = get_auth_client().acquire_token_by_authorization_code(
        code=code,
        scopes=SCOPES,
        redirect_uri=REDIRECT_URI
    )
    if "access_token" not in result:
        raise HTTPException(status_code=400, detail="Authentication failed")

    token_cache.update(result)
    return {"status": "authenticated"}

@auth_router.get("/clear-tokens")
async def clear_tokens():
    token_cache.clear()
    return {"status": "token cache cleared"}
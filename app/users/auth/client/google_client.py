from dataclasses import dataclass
import httpx

from app.users.auth.schema import GoogleUserData
from app.settings import Settings


@dataclass
class GoogleClient:
    settings: Settings
    async_client: httpx.AsyncClient

    async def get_user_info(self, code: str) -> GoogleUserData:
        """
        Get user info after auth.
        """
        access_token = await self._get_user_access_token(code=code)
        try:
            user_info = await self.async_client.get(
                "https://www.googleapis.com/oauth2/v3/userinfo",
                headers={"Authorization": f"Bearer {access_token}"},
            )
            print(f"Google API response: {user_info.json()}")
            data = user_info.json()
            data["id"] = data.pop("sub")
            data["verified_email"] = data.pop("email_verified")
            return GoogleUserData(**data, access_token=access_token)
        except Exception as e:
            print(f"Error getting user info: {e}")
            raise

    async def _get_user_access_token(self, code: str) -> str:
        """
        Get access token.
        """
        data = {
            "code": code,
            "client_id": self.settings.GOOGLE_CLIENT_ID,
            "client_secret": self.settings.GOOGLE_SECRET_KEY,
            "redirect_uri": self.settings.GOOGLE_REDIRECT_URI,
            "grant_type": "authorization_code",
        }
        try:
            response = await self.async_client.post(
                self.settings.GOOGLE_TOKEN_URL,
                data=data,
                headers={
                    "Content-Type": "application/x-www-form-urlencoded",
                },
            )
            return response.json()["access_token"]
        except Exception as e:
            print(f"Error getting access token: {e}")
            raise

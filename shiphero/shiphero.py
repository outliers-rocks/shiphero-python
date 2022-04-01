
import requests

from pydantic.dataclasses import dataclass
from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation 
from .shiphero_schema import shiphero_schema as schema

@dataclass
class Shiphero:
    """
    Cliente de Shiphero 
    """
    username: str
    password: str
    auth_url: str = "https://public-api.shiphero.com/auth"
    graphql_url: str = "https://public-api.shiphero.com/graphql"

    def __post_init__(self):
        self._auth_token, self._refresh_auth_token = self._create_token()
        self.endpoint = self._init_endpoint()
        self.query = Operation(schema.Query)
        self.mutation = Operation(schema.Mutation)

    
    def _create_token(self) -> tuple:
        token_url = f"{self.auth_url}/token"
        payload = {
            "username": self.username,
            "password": self.password
        }
        auth_request = requests.post(token_url, json=payload)
        if auth_request.status_code != 200:
            return auth_request

        access_token = auth_request.json()["access_token"]
        refresh_token = auth_request.json()["refresh_token"]

        return access_token, refresh_token
    
    def _refresh_token(self) -> None:

        refresh_url = f"{self.auth_url}/refresh"
        payload = {
            "refresh_token": self._refresh_token
        }
        refresh_request = requests.post(refresh_url, json=payload)
        if refresh_request.status_code != 200:

            self._auth_token, self._refresh_auth_token = self._create_token()

        self._auth_token = refresh_request.json()["access_token"]

    def _get_header(self) -> dict:
        """
        Configuración del header
        :return: dict()
        """
        return {
        'Authorization': f'Bearer {self._auth_token}'
        }

    def _init_endpoint(self) -> HTTPEndpoint:
        """
        Inicializa el endpoint
        :param session:
        :return: HTTPEndpoint
        """
        return HTTPEndpoint(
            self.graphql_url,
            base_headers=self._get_header()
        )
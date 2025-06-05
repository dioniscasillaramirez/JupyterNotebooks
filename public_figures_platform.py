"""
Plataforma para el análisis y comparación de figuras públicas con
módulos de conexión a diferentes redes sociales.

Este código es un ejemplo básico de cómo estructurar una plataforma
que obtenga información de redes sociales para comparar métricas como
seguidores, publicaciones y otros datos públicos.
"""

from dataclasses import dataclass
from typing import Optional, Dict, Any
import requests

# Conectores a redes sociales
class SocialMediaConnector:
    """Clase base para conectores de redes sociales."""

    def fetch_profile(self, handle: str) -> Dict[str, Any]:
        """Obtiene información de un perfil dado un identificador."""
        raise NotImplementedError


class TwitterConnector(SocialMediaConnector):
    """Ejemplo de conector para Twitter usando requests o tweepy."""

    def __init__(self, bearer_token: str):
        self.bearer_token = bearer_token

    def fetch_profile(self, handle: str) -> Dict[str, Any]:
        headers = {"Authorization": f"Bearer {self.bearer_token}"}
        url = f"https://api.twitter.com/2/users/by/username/{handle}"
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()


class FacebookConnector(SocialMediaConnector):
    """Ejemplo de conector para Facebook Graph API."""

    def __init__(self, access_token: str):
        self.access_token = access_token

    def fetch_profile(self, handle: str) -> Dict[str, Any]:
        url = f"https://graph.facebook.com/v17.0/{handle}"
        params = {"access_token": self.access_token}
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()


class InstagramConnector(SocialMediaConnector):
    """Conector simplificado para Instagram Graph API."""

    def __init__(self, access_token: str):
        self.access_token = access_token

    def fetch_profile(self, handle: str) -> Dict[str, Any]:
        url = f"https://graph.instagram.com/{handle}"  # id de usuario
        params = {"access_token": self.access_token}
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()


@dataclass
class PublicFigure:
    name: str
    twitter_handle: Optional[str] = None
    facebook_handle: Optional[str] = None
    instagram_handle: Optional[str] = None


class AnalysisPlatform:
    """Plataforma principal para obtener y comparar datos."""

    def __init__(self,
                 twitter_connector: Optional[TwitterConnector] = None,
                 facebook_connector: Optional[FacebookConnector] = None,
                 instagram_connector: Optional[InstagramConnector] = None,
                 ):
        self.twitter_connector = twitter_connector
        self.facebook_connector = facebook_connector
        self.instagram_connector = instagram_connector

    def fetch_all(self, figure: PublicFigure) -> Dict[str, Dict[str, Any]]:
        data = {}
        if figure.twitter_handle and self.twitter_connector:
            data['twitter'] = self.twitter_connector.fetch_profile(figure.twitter_handle)
        if figure.facebook_handle and self.facebook_connector:
            data['facebook'] = self.facebook_connector.fetch_profile(figure.facebook_handle)
        if figure.instagram_handle and self.instagram_connector:
            data['instagram'] = self.instagram_connector.fetch_profile(figure.instagram_handle)
        return data

    def compare_followers(self, figures: list[PublicFigure]) -> Dict[str, int]:
        """Devuelve un diccionario con el total de seguidores por figura."""
        results = {}
        for fig in figures:
            followers = 0
            profiles = self.fetch_all(fig)
            if 'twitter' in profiles:
                followers += int(profiles['twitter'].get('data', {}).get('public_metrics', {}).get('followers_count', 0))
            if 'facebook' in profiles:
                followers += int(profiles['facebook'].get('followers_count', 0))
            if 'instagram' in profiles:
                followers += int(profiles['instagram'].get('followers_count', 0))
            results[fig.name] = followers
        return results


if __name__ == "__main__":
    # Ejemplo de uso
    twitter = TwitterConnector(bearer_token="TU_TOKEN_AQUI")
    facebook = FacebookConnector(access_token="TU_TOKEN_AQUI")
    instagram = InstagramConnector(access_token="TU_TOKEN_AQUI")

    platform = AnalysisPlatform(twitter, facebook, instagram)

    figuras = [
        PublicFigure(name="Figura1", twitter_handle="user1"),
        PublicFigure(name="Figura2", twitter_handle="user2", instagram_handle="id_user2"),
    ]

    resultados = platform.compare_followers(figuras)
    for nombre, seguidores in resultados.items():
        print(f"{nombre}: {seguidores} seguidores totales")

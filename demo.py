"""Demostración de la plataforma de análisis usando conectores simulados."""

from public_figures_platform import PublicFigure, AnalysisPlatform
from mock_connectors import (
    MockTwitterConnector,
    MockFacebookConnector,
    MockInstagramConnector,
)


def main():
    twitter = MockTwitterConnector()
    facebook = MockFacebookConnector()
    instagram = MockInstagramConnector()

    platform = AnalysisPlatform(twitter, facebook, instagram)

    figuras = [
        PublicFigure(name="Figura1", twitter_handle="user1", facebook_handle="fb1", instagram_handle="ig1"),
        PublicFigure(name="Figura2", twitter_handle="user2", facebook_handle="fb2", instagram_handle="ig2"),
    ]

    resultados = platform.compare_followers(figuras)
    for nombre, seguidores in resultados.items():
        print(f"{nombre}: {seguidores} seguidores totales")


if __name__ == "__main__":
    main()

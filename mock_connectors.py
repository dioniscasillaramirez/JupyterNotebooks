from public_figures_platform import SocialMediaConnector

MOCK_TWITTER_DATA = {
    "user1": {"data": {"public_metrics": {"followers_count": 1000}}},
    "user2": {"data": {"public_metrics": {"followers_count": 1500}}},
}

MOCK_FACEBOOK_DATA = {
    "fb1": {"followers_count": 800},
    "fb2": {"followers_count": 1200},
}

MOCK_INSTAGRAM_DATA = {
    "ig1": {"followers_count": 500},
    "ig2": {"followers_count": 700},
}

class MockTwitterConnector(SocialMediaConnector):
    def __init__(self, data=MOCK_TWITTER_DATA):
        self.data = data

    def fetch_profile(self, handle: str):
        return self.data.get(handle, {"data": {"public_metrics": {"followers_count": 0}}})

class MockFacebookConnector(SocialMediaConnector):
    def __init__(self, data=MOCK_FACEBOOK_DATA):
        self.data = data

    def fetch_profile(self, handle: str):
        return self.data.get(handle, {"followers_count": 0})

class MockInstagramConnector(SocialMediaConnector):
    def __init__(self, data=MOCK_INSTAGRAM_DATA):
        self.data = data

    def fetch_profile(self, handle: str):
        return self.data.get(handle, {"followers_count": 0})

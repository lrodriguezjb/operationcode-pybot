import os

MENTOR_CHANNEL = os.environ.get("MENTOR_CHANNEL") or "mentors-internal"
COMMUNITY_CHANNEL = os.environ.get("COMMUNITY_CHANNEL") or "greetings"
MODERATOR_CHANNEL = os.environ.get("MODERATOR_CHANNEL") or "moderators"
TICKET_CHANNEL = os.environ.get("TICKET_CHANNEL") or "oc-project-leads"
APP_TOKEN = os.environ.get("APP_TOKEN") or "123"
YELP_TOKEN = os.environ.get("YELP_TOKEN") or "token"
PYBACK_HOST = os.environ.get("PYBACK_HOST") or "pyback"
PYBACK_PORT = os.environ.get("PYBACK_PORT") or 8000
PYBACK_TOKEN = os.environ.get("PYBACK_TOKEN") or "token"
PORT = os.environ.get("SIRBOT_PORT", 5000)
HOST = os.environ.get("SIRBOT_ADDR", "0.0.0.0")
PYBOT_ENV = os.environ.get("PYBOT_ENV", "dev")
BACKEND_URL = os.environ.get("BACKEND_URL", "https://api.operationcode.org")
BACKEND_USERNAME = os.environ.get("BACKEND_USERNAME", "Pybot@test.test")
BACKEND_PASS = os.environ.get("BACKEND_PASS", "fakePassword")

BOT_URL = "https://github.com/OperationCode/operationcode-pybot"

slack_configs = {
    "token": os.environ.get("BOT_OATH_TOKEN"),
    "signing_secret": os.environ.get("SLACK_BOT_SIGNING_SECRET"),
    "verify": os.environ.get("VERIFICATION_TOKEN"),
    "bot_id": os.environ.get("SLACK_BOT_ID"),
    "bot_user_id": os.environ.get("SLACK_BOT_USER_ID"),
}

# Create a Github oauth app minimal example

Based on https://docs.github.com/en/developers/apps/building-oauth-apps/authorizing-oauth-apps

## Setup
- Create Github oauth app

## Install / Run

```
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
export APP_DEBUG=1
flask run
```
Visit http://127.0.0.1:5000/

Next steps: Consider the scopes needed for your app

pip uninstall -y -r <(pip freeze)
pip install aiohttp==3.9.0b0
pip install --no-dependencies py-cord
pip install flask flask_cors pytz
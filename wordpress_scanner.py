import re
import requests

class WordpressScanner:
    def __init__(self, domain):
        self.domain = domain

    def get_users(self):
        users_api_url = f'{self.domain}/wp-json/wp/v2/users'
        response = requests.get(users_api_url)
        users = response.json()
        return users

    def get_theme_name(self):
        response = requests.get(self.domain)
        html = response.text
        theme_start = html.find('/wp-content/themes/') + len('/wp-content/themes/')
        theme_end = html.find('/', theme_start)
        theme_name = html[theme_start:theme_end]
        return theme_name

    def get_plugins_name(self):
        response = requests.get(self.domain)
        html = response.text
        plugin_matches = re.findall('/wp-content/plugins/(.*?)/', html)
        plugins_names = list(set(plugin_matches)) # Remove duplicate plugin names
        return plugins_names
from urllib import request
from project import Project
import tomllib 

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url)
        print(content)
        conf = tomllib.load(content)
        print(conf["tool"]["poetry"].keys())
        poetry = conf["tool"]["poetry"]
        dev = poetry["group"]["dev"]
        

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(poetry["name"], poetry["description"],poetry["license"],poetry["authors"], poetry["dependencies"], dev["dependencies"])

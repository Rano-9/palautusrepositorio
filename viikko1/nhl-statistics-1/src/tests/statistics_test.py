import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )


    def test_search(self):
        tulos = self.stats._players
        haku = self.stats.search("Semenko")
        self.assertEqual(haku,tulos[0])
        self.assertNotEqual(haku,tulos[1])
        self.assertEqual(str(haku), "Semenko EDM 4 + 12 = 16")
        haku = self.stats.search("tyhjä")
        self.assertIsNone(haku)

    def test_team(self):
        tulos = {"EDM":3,"PIT":1,"DET":1,"PAT":0}
        for i in tulos.keys():
            haku = self.stats.team(i)
            self.assertEqual(len(haku),tulos[i])
    
    def test_top(self):
        haku = self.stats.top(4)
        self.assertEqual(len(haku),5)
        haku =self.stats.top(2)
        self.assertEqual(len(haku),3)
    

class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0
        self.score_dict = {0:"Love",1:"Fifteen",2:"Thirty",3:"Forty"}

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 = self.m_score1 + 1
        else:
            self.m_score2 = self.m_score2 + 1

    def get_score(self):
        score1 = self.m_score1
        score2 = self.m_score2
        erotus = score1 - score2
        if score1 < 4 and score2 < 4 or erotus == 0: 
            score = self.pistemuuntaja(score1,score2)
        else:
            score = self.voittomuuntaja(erotus)
        return score
    
    def pistemuuntaja(self, score1, score2):
        sanakirja = self.score_dict
        if score1 == score2:
            if score1 <= 2:
                score = f"{sanakirja[score1]}-All"
            else:
                score = "Deuce"
        else:
            score = f"{sanakirja[score1]}-{sanakirja[score2]}"
        
        
        return score
    
    def voittomuuntaja(self,erotus):
        if erotus < 0:
            voittaja = "player2"
        else:
            voittaja = "player1"
        if erotus == -1 or erotus == 1:
            score = f"Advantage {voittaja}"
        elif erotus != -1 or erotus != 1:
            score = f"Win for {voittaja}"
        return score
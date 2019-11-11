class Player:

    def __init__(self, is_playing):
        self.name = 'Player'
        self.is_playing = is_playing

    def guess(self):
        raise NotImplementedError

    @staticmethod
    def ask_for_help():
        print()

    @staticmethod
    def answer_would_you_like_play(answer):
        if answer == "Yes":
            return True
        else:
            return False

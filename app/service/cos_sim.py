class CosSimResult:
    def __init__(self, score):
        self.score = score

    def get_view_dict(self):
        for key, value in self.score.items():
            self.score[key] = {}
            self.score[key]["score"] = round(value, 6)
            name = key.split("__")
            self.score[key]["level"] = name[0].capitalize()
            self.score[key]["item"] = name[1].capitalize()

        return self.score


class Anime:
    """Models an anime"""
    def __init__(self, mal_id: int=None, rank: int=None, title: str=None, url: str=None, image_url: str=None, type: str=None, start_date: str=None, end_date: str=None, members: int=None, score: float=None):
        self.mal_id = mal_id
        self.rank = rank
        self.title = title
        self.url = url
        self.image_url = image_url
        self.type = type
        self.start_date = start_date
        self.end_date = end_date
        self.members = members
        self.score = score
    
    def __dir__(self) -> list:
        return ['mal_id', 'rank', 'title', 'url', 'image_url', 'type', 'start_date', 'end_date', 'members', 'score']
    
    def to_dict(self) -> dict:
        result = {}
        for key in dir(self):
            result[key] = self.__getattribute__(key)
        return result
    
    def to_prettified_dict(self) -> dict:
        return {
            'Rank': self.rank,
            'Title': self.title,
            'Image': self.image_url,
            'Type': self.type,
            'Start date': self.start_date,
            'End date': self.end_date,
            'Members': self.members,
            'Score': self.score,
            'MAL URL': self.url
        }

    def __from_dict(self, dikt: dict):
        attrs = dir(self)
        for key in dikt:
            if key in attrs:
                self.__setattr__(key, dikt[key])
    
    @classmethod
    def from_dict(cls, dikt: dict):
        result = cls()
        result.__from_dict(dikt)
        return result

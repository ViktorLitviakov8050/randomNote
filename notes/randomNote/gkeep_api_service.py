import gkeepapi
import random


class gkeepApiService:
    def __init__(self, login, password):
        self.gkeep = gkeepapi.Keep()
        self.gkeep.login(login, password)

    def get_random_note(self):
        notes = self.gkeep.all()
        return random.choice(notes)

    
note = gkeepApiService("seevz.savage@gmail.com", "chypmdseboinqkoy")

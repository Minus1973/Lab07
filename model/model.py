import copy
from functools import partial

from database.DAO import MeteoDao

class Model:
    def __init__(self):
        pass

    def calcola_umidita_media(self,mese):
        return MeteoDao.get_umidita_media_mese(mese)


import os
import time

class Utils:
    @staticmethod
    def limpar_tela():
        os.system('cls' if os.name == 'nt' else 'clear')
        time.sleep(1)
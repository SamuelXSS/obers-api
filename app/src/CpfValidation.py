import re

class ValidateCpf:
    def __init__(self, cpf):
        self.cpf = cpf
        print (self.cpf)

    def validate (self):
        if not self.cpf:
            return False
        
        new_cpf = self.calculator(self.cpf[:9])
        new_cpf = self.calculator(new_cpf)

        if new_cpf == self.cpf:
            return True
        return False

    @staticmethod
    def calculator(cpf):
        if not cpf:
            return False

        sequency = cpf[0] * len(cpf)

        if sequency == cpf:
            return False
        i = 0
        for key, multiply in enumerate(range(len(cpf)+1, 1, -1)):
            i += int(cpf[key]) * multiply

        rest = 11 - (i%11)
        rest = rest if rest <= 9 else 0

        return cpf + str(rest)

    @property
    def cpf(self):
        return self._cpf 

    @cpf.setter
    def cpf(self, cpf):
        self._cpf = self.formated(cpf)

    @staticmethod
    def formated(cpf):
        return re.sub('[^0-9]', '', cpf)       

class Cipher():
    def encode(self):
        pass

    def decode(self):
        pass


class Cipher1(Cipher):
    def __init__(self, msg):
        self.msg = msg.lower()
        self.shift = 2

    def encode(self):
        res = ''

        for c in self.msg:
            if c.isalpha():
                res += chr((ord(c) + self.shift - 97) % 26 + 97)
        self.msg = res

    def decode(self):
        res = ''

        for c in self.msg:
            res += chr((ord(c) - self.shift - 97) % 26 + 97)
        self.msg = res



class Cipher2(Cipher):
    def __init__(self, msg):
        self.msg = msg.lower()
        self.cipher = dict(zip('abcdefghijklmnopqrstuvwxyz', 'mnbvcxzadsgfhjklpoiuytrewq'))

    def encode(self):
        res = ''

        for c in self.msg:
            if c.isalpha():
                res += self.cipher[c]
        self.msg = res

    def decode(self):
        res = ''
        rev_cipher = {v: k for k,v in self.cipher.items()}

        for c in self.msg:
            res += rev_cipher[c]
        self.msg = res


class CipherDecorator(Cipher):
    def __init__(self, cipher):
        self.cipher = cipher

    @property
    def msg(self):
        return self.cipher.msg

    @msg.setter
    def msg(self, value):
        self.cipher.msg = value

    def encode(self):
        return self.cipher.encode()

    def decode(self):
        return self.cipher.decode()


class ValidationDecorator(CipherDecorator):
    def encode(self):
        if not self.cipher.msg:
            print("[VALIDATION] Warning: Empty message")

        if any(not(c.isalpha() or c.isspace()) for c in self.cipher.msg):
            print("[VALIDATION] Warning: Message contains special characters")
            return

        super().encode()

    def decode(self):
        if not self.cipher.msg:
            print("[VALIDATION] Warning: Empty message")

        if any(not(c.isalpha() or c.isspace()) for c in self.cipher.msg):
            return

        super().decode()


class LoggingDecorator(CipherDecorator):
    def encode(self):
        print(f"[LOG] Before encoding: '{self.cipher.msg}'")
        super().encode()
        print(f"[LOG] After encoding: '{self.cipher.msg}'")
    
    def decode(self):
        print(f"[LOG] Before decoding: '{self.cipher.msg}'")
        super().decode()
        print(f"[LOG] After decoding: '{self.cipher.msg}'")


a = Cipher1('TESTE')
l = LoggingDecorator(a)
c = ValidationDecorator(l)
c.encode()
c.decode()


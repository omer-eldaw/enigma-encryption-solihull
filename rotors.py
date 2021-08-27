

class Reflector(object):

    def __init__(self, wiring):
        self.wiring = wiring

    def encipher (self, key):
        shift = (ord(self.state) - ord('A'))
        index = (ord(key) - ord('A'))%26
        index = (index + shift)%26

        letter = self.wiring[index]
        out = chr(ord('A')+(ord(letter) - ord('A') +26 - shift)%26)
        return out


class Rotor(object):

    def __init__(self, wiring, notchs, state="A", ring="A"):
        self.wiring = wiring
        self.rwiring = ["0"] * 26
        for i in range(0, len(self.wiring)):
            self.rwiring[ord(self.wiring[i]) - ord('A')]= chr(ord('A') + i)
        
        self.notchs = notchs
        self.state = state
        self.ring = ring

    def encipher_right(self, key):
        shift = (ord(self.state) - ord(self.ring))
        index = (ord(key) - ord('A'))%26
        index = (index + shift)%26

        letter = self.wiring[index]
        out = chr(ord('A')+(ord(letter) - ord('A') +26 - shift)%26)

        return out

    def encipher_left(self, key):
        shift = (ord(self.state) - ord(self.ring))
        index = (ord(key) - ord('A'))%26
        index = (index + shift)%26

        letter = self.rwiring[index]
        out = chr(ord('A')+(ord(letter) - ord('A') + 26 - shift)%26)

        return out

    def notch_function(self, offset=1):
        self.state = chr((ord(self.state) + offset - ord('A')) % 26 + ord('A'))
        notchnext = self.state in self.notchs

    def is_in_turnover_pos(self):
        return chr((ord(self.state) + 1 - ord('A')) % 26 + ord('A')) in self.notchs





ROTOR_I = Rotor(wiring="VEOSIRZUJDQCKGWYPNXAFLTHMB",notchs="Y")
ROTOR_II = Rotor(wiring="UEMOATQLSHPKCYFWJZBGVXINDR",notchs="M")
ROTOR_III = Rotor(wiring="TZHXMBSIPNURJFDKEQVCWGLAOY",notchs="D")

UKW = Reflector(wiring="CIAGSNDRBYTPZFULVHEKOQXWJM")

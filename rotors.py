

class Reflector(object):

    def __init__(self, wiring):
        self.wiring = wiring

    def encipher (self, key):
        shift = (ord(self.state) - ord('A')) # If current rotor state was B, then the shift would be the ord(B) - which is 66 - minus the ord(A) = 1
        index = (ord(key) - ord('A'))%26 # The index value would then be later used to calculate what the ord(letter) would be. This is taken by calculating the (ord(letter) - ord(65)) % 26, simliar to how the caesar shift works.
        index = (index + shift)%26 # This would then be used in combination with the shift specified to give the index of the letter in the list selflwiring

        letter = self.wiring[index] # This would then return the letter of the index specified within the wiring of the specified rotor.
        out = chr(ord('A')+(ord(letter) - ord('A') +26 - shift)%26) # This would then take the ord(A)
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

    def is_in_turnover_pos(self):
        return chr((ord(self.state) + 1 - ord('A')) % 26 + ord('A')) in self.notchs



ENIGMA_D_COMMERCIAL_ROTOR_I = Rotor(wiring="LPGSZMHAEOQKVXRFYBUTNICJDW",notchs="G")
ENIGMA_D_COMMERCIAL_ROTOR_II = Rotor(wiring="SLVGBTFXJQOHEWIRZYAMKPCNDU",notchs="M")
ENIGMA_D_COMMERCIAL_ROTOR_III = Rotor(wiring="CJGDPSHKTURAWZXFMYNQOBVLIE",notchs="V")
ENIGMA_D_COMMERCIAL_REFLECTOR = Reflector(wiring="IMETCGFRAYSQBZXWLHKDVUPOJN")

ENIGMA_I_WEHRMACHT_LUFTWAFFE_ROTOR_I = Rotor(wiring="EKMFLGDQVZNTOWYHXUSPAIBRCJ", notchs="Y")
ENIGMA_I_WEHRMACHT_LUFTWAFFE_ROTOR_II = Rotor(wiring="AJDKSIRUXBLHWTMCQGZNPYFVOE", notchs="M")
ENIGMA_I_WEHRMACHT_LUFTWAFFE_ROTOR_III = Rotor(wiring="BDFHJLCPRTXVZNYEIWGAKMUSQO", notchs="D")
ENIGMA_I_WEHRMACHT_LUFTWAFFE_ROTOR_IV = Rotor(wiring="ESOVPZJAYQUIRHXLNFTGKDCMWB", notchs="R")
ENIGMA_I_WEHRMACHT_LUFTWAFFE_ROTOR_V = Rotor(wiring="VZBRGITYUPSDNHLXAWMJQOFECK", notchs="H")
ENIGMA_I_WEHRMACHT_LUFTWAFFE_REFLECTOR_A = Reflector(wiring="EJMZALYXVBWFCRQUONTSPIKHGD")
ENIGMA_I_WEHRMACHT_LUFTWAFFE_REFLECTOR_B = Reflector(wiring="YRUHQSLDPXNGOKMIEBFZCWVJAT")
ENIGMA_I_WEHRMACHT_LUFTWAFFE_REFLECTOR_C = Reflector(wiring="FVPJIAOYEDRZXWGCTKUQSBNMHL")

SONDER_ENGIMA_ROTOR_I = Rotor(wiring="VEOSIRZUJDQCKGWYPNXAFLTHMB",notchs="Y")
SONDER_ENGIMA_ROTOR_II = Rotor(wiring="UEMOATQLSHPKCYFWJZBGVXINDR",notchs="M")
SONDER_ENGIMA_ROTOR_III = Rotor(wiring="TZHXMBSIPNURJFDKEQVCWGLAOY",notchs="D")
SONDER_ENGIMA_REFLECTOR = Reflector(wiring="CIAGSNDRBYTPZFULVHEKOQXWJM")


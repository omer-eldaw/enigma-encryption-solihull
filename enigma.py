from rotors import *


class Enigma(object):

    def __init__(self, reflector, rotor1, rotor2, rotor3, initial_pos="AAA", plugboard="", ring="AAA"):
        

        self.reflector = reflector
        self.rotor1 = rotor1
        self.rotor2 = rotor2
        self.rotor3 = rotor3
        self.plugboard = plugboard

        self.rotor1.state = initial_pos[0]
        self.rotor2.state = initial_pos[1]
        self.rotor3.state = initial_pos[2]

        self.rotor1.ring = ring[0]
        self.rotor2.ring = ring[1]
        self.rotor3.ring = ring[2]

        self.reflector.state = 'A'

        plugboard_settings= [(i[0], i[1]) for i in plugboard.split()]

        alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        alpha_out = [" "] * 26
        for i in range(len(alpha)):
            alpha_out[i] = alpha[i]
        for k, v in plugboard_settings:
            alpha_out[ord(k)-ord('A')] = v
            alpha_out[ord(v)-ord('A')] = k

        self.transtab = str.maketrans(alpha, "".join(alpha_out))

    def encipher(self, plaintext_in):
        ciphertext = ''
        plaintext_in_upper = plaintext_in.upper()
        plaintext = plaintext_in_upper.translate(self.transtab)
        for i in plaintext:
            if not i.isalpha():
                ciphertext += i
                continue

            if self.rotor2.is_in_turnover_pos():
                self.rotor2.notch_function()
                self.rotor3.notch_function()
            if self.rotor1.is_in_turnover_pos():
                self.rotor2.notch_function()

            self.rotor1.notch_function()

            letter = self.rotor1.encipher_right(i)
            letter = self.rotor2.encipher_right(letter)
            letter = self.rotor3.encipher_right(letter)
            letter = self.reflector.encipher(letter)
            letter = self.rotor3.encipher_left(letter)
            letter = self.rotor2.encipher_left(letter)
            letter = self.rotor1.encipher_left(letter)
            ciphertext += letter

        res = ciphertext.translate(self.transtab)

        fres = ""
        for idx, char in enumerate(res):
            if plaintext_in[idx].islower():
                fres += char.lower()
            else:
                fres += char
        return fres
        
    def returnRotorPositions(self):
        current_position = [self.rotor1.state, self.rotor2.state, self.rotor3.state]
        return current_position



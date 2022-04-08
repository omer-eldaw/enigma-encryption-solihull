import enigma as ee
import rotors as ro


start = input("Welcome to the enigma encryption. If you want to know some valuable information about the enigma machine or need"
            " help on this program please type in !help, other wise just press enter to skip.\n")
if start == "!help":
    print("Very well. This program has a couple variations of the enigmea machine. (1) Swiss-K variant that was actually used by the Swiss Air Force. All the Swiss-K"
        " machines were actually based of the Enigma-D, which was what the Germans delivered to them. After they recieved them"
        " however, the Swiss changed the wiring of all cipher wheels, but left the reflector unchanged. The only known cipher wheel"
        " wirings are the ones found in the Swiss Airforce (which is what this enigma machine is based on).")
method = input("Enter whether you want to encrypt or decrypt: ")
if method.lower() == "encrypt":
    text = input(f"Enter the text you want to {method}: ")
    rotor_settings = input("Do you want to specify the enigma settings yourself (Y) or use default settings with no plugboard active (N): ")
    if rotor_settings.lower() == "y":
        rotor_pos = input("Enter the position of the rotors (1st rotor) (2nd rotor) (3rd rotor): ")
        plugboard_settings = input("Enter the plugboard settings:")
        encryption_enigma_machine = ee.Enigma(reflector = ro.ENIGMA_D_COMMERCIAL_REFLECTOR, rotor1 = ro.ENIGMA_D_COMMERCIAL_ROTOR_I, rotor2 =  ro.ENIGMA_D_COMMERCIAL_ROTOR_II, rotor3 = ro.ENIGMA_D_COMMERCIAL_ROTOR_III, initial_pos = rotor_pos, plugboard = plugboard_settings)
        encrypted_text = encryption_enigma_machine.encipher(text)
        print(encrypted_text)
    elif rotor_settings.lower() == "n":
        encryption_enigma_machine = ee.Enigma(reflector = ro.ENIGMA_D_COMMERCIAL_REFLECTOR, rotor1 = ro.ENIGMA_D_COMMERCIAL_ROTOR_I, rotor2 =  ro.ENIGMA_D_COMMERCIAL_ROTOR_II, rotor3 = ro.ENIGMA_D_COMMERCIAL_ROTOR_III, initial_pos = "AAA", plugboard = "")
        encrypted_text = encryption_enigma_machine.encipher(text)
        print(encrypted_text)

elif method.lower() == "decrypt":
    text = input(f"Enter the text you want to {method}: ")
    rotor_pos = input("Enter the position of the rotors (1st rotor) (2nd rotor) (3rd rotor): ")
    plugboard_settings = input("Enter the plugboard settings:")
    decryption_enigma_machine = ee.Enigma(reflector = ro.ENIGMA_D_COMMERCIAL_REFLECTOR, rotor1 = ro.ENIGMA_D_COMMERCIAL_ROTOR_I, rotor2 =  ro.ENIGMA_D_COMMERCIAL_ROTOR_II, rotor3 = ro.ENIGMA_D_COMMERCIAL_ROTOR_III, initial_pos = rotor_pos, plugboard = plugboard_settings)
    decrypted_text = decryption_enigma_machine.encipher(text)
    print(decrypted_text)

    # AV BS CG DL FU HZ IN KM OW RX





    
import enigma as ee
import rotors as ro


start = input("Welcome to the enigma encryption. If you want to know some valuable information about the enigma machine or need"
            " help on this program please type in !help, other wise just press enter to skip.\n")
if start == "!help":
    print("Very well. This enigma machine is the Swiss-K variant that was actually used by the Swiss Air Force. All the Swiss-K"
        " machines were actually based of the Enigma-D, which was what the Germans delivered to them. After they recieved them"
        " however, the Swiss changed the wiring of all cipher wheels, but left the reflector unchanged. The only known cipher wheel"
        " wirings are the ones found in the Swiss Airforce (which is what this enigma machine is based on).")
method = input("Enter whether you want to encrypt or decrypt: ")
text = input(f"Enter the text you want to {method}: ")
if method.lower() == "encrypt":
    rotor_settings = input("Do you want to specify the enigma settings yourself (Y) or use default settings (N): ")
    if rotor_settings.lower() == "y":
        encryption_enigma_machine = ee.Enigma(ro.UKW, ro.ROTOR_I, ro.ROTOR_II, ro.ROTOR_III, "ABC", "AV BS CG DL FU HZ IN KM OW RX")
        encrypted_text = encryption_enigma_machine.encipher(text)
        print(encrypted_text)
    elif rotor_settings.lower() == "n":
        pass

elif method.lower() == "decrypt":
    decryption_enigma_machine = ee.Enigma(ro.UKW, ro.ROTOR_I, ro.ROTOR_II, ro.ROTOR_III, "ABC", "AV BS CG DL FU HZ IN KM OW RX")
    decrypted_text = decryption_enigma_machine.encipher(text)
    print(decrypted_text)

    # AV BS CG DL FU HZ IN KM OW RX





    
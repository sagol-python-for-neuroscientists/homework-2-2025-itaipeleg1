MORSE_CODE = {'A': '.-',     'B': '-...',   'C': '-.-.',
              'D': '-..',    'E': '.',      'F': '..-.',
              'G': '--.',    'H': '....',   'I': '..',
              'J': '.---',   'K': '-.-',    'L': '.-..',
              'M': '--',     'N': '-.',     'O': '---',
              'P': '.--.',   'Q': '--.-',   'R': '.-.',
              'S': '...',    'T': '-',      'U': '..-',
              'V': '...-',   'W': '.--',    'X': '-..-',
              'Y': '-.--',   'Z': '--..',

              '0': '-----',  '1': '.----',  '2': '..---',
              '3': '...--',  '4': '....-',  '5': '.....',
              '6': '-....',  '7': '--...',  '8': '---..',
              '9': '----.',

              '.': '.-.-.-', ',': '--..--', ':': '---...',
              "'": '.----.', '-': '-....-',
              }

class MorseCode:
    '''
    A class to convert English text to Morse code and vice versa.
    '''

    def __init__(self, morse_code_dict: dict, in_path: str,out_path: str):
        '''
        params:
        Path: path to the file containing the text to be converted.
        morse_code_dict: dictionary containing the mapping between English letters and
        '''
        self.vocab = morse_code_dict
        self.path = in_path
        self.out_path = out_path
    
    def read_file(self):
        '''
        Read the file and return the content as a string.
        '''
        try:
            with open(self.path, 'r') as f: ##r stands for read mode
                return f.read()
        except FileNotFoundError:
            print(f"File {self.path} not found.")
            return None
    def translate_word(self, string: str):
        '''
        Takes a woed and returns the morse code translation of the woed
        '''
        return ''.join(self.vocab.get(c,'') for c in string.upper())
    
    def write_file(self, string: str):
        '''
        Takes a string and writes it to afile as a morse code.
        '''
        ## This will apply the function to word by word and join them with a newline character, string.splitlines() ##
        ## will split the string into lines and map will apply the function to each word in the line.
    

        morse_code = '\n'.join(
            map(
                lambda line: '\n'.join(map(self.translate_word, line.split())),
                string.splitlines()
            )
        ).rstrip()  # remove the last newline character




        try:        
            with open(self.out_path, 'w') as w:
                w.write(morse_code)  # join the morse code to string and write to file

        except Exception as e:
            print(f"An error occurred while writing to the file: {e}")
            return None
            

    def english_to_morse(self,
        input_file: str = "lorem.txt",
        output_file: str = "lorem_morse.txt"
    ):
        """Convert an input text file to an output Morse code file.

        Notes
        -----
        This function assumes the existence of a MORSE_CODE dictionary, containing a
        mapping between English letters and their corresponding Morse code.

        Parameters
        ----------
        input_file : str
            Path to file containing the text file to convert.
        output_file : str
            Name of output file containing the translated Morse code. Please don't change
            it since it's also hard-coded in the tests file.
        """
        ## Read the input string from the file
        script = self.read_file()

        ## convert the string to morse code
        self.write_file(script)

if __name__ == "__main__":
    morse_code = MorseCode(MORSE_CODE, "lorem.txt","lorem_morse.txt")
    morse_code.english_to_morse()
    print("Morse code conversion complete.")
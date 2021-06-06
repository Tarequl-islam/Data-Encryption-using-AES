
def key_expansion():
    return


def initial_rounds():
    return


def sub_byte():
    return


def shift_rows():
    return


def mix_columns():
    return


def add_round_key():
    return


def aes_encrypt():
    key_expansion()
    initial_rounds()
    number_of_rounds = 1
    
    for round in range(number_of_rounds): #apply round operations
        sub_byte()
        shift_rows()
        mix_columns()
        add_round_key()
    #final round
    sub_byte()
    shift_rows()
    mix_columns()
    return


message = "This text will be encrypted using aes cryptography!"
key = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

def make_out_word(out, word):
    middle = len(out)/2
    out_word = out[:middle] + word + out[middle:]
    return out_word

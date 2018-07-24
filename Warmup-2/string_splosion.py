def string_splosion(str):
    return ''.join([str[:i+1] for i, char in enumerate(str)])

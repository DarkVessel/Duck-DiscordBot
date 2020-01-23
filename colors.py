# Чёрный текст.
def out_black(text):
    print("\033[30m {}".format(text))

# Красный текст.
def out_red(text):
    print("\033[31m {}".format(text))

# Зелёный текст.
def out_green(text):
    print("\033[32m {}".format(text))

# Жёлтый текст.
def out_yellow(text):
    print("\033[33m {}".format(text))

# Синий текст.
def out_blue(text):
    print("\033[34m {}".format(text))

# Фиолетовый текст.
def out_purple(text):
    print("\033[35m {}".format(text))

# Серый текст.
def out_grey(text):
    print("\033[37m {}".format(text))

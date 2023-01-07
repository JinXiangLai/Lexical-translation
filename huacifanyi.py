import os
import pyperclip as clip
import string

last_text = ''
kPunc = string.punctuation + ' ' +'’'
#print(kPunc)

def translate_en2zh(cmd):
    os.system(cmd)
    print('========\n')

def char_is_valid(char:str) -> bool:
    return char.encode('utf-8').isalpha() or char.encode('utf-8').isdigit(
    ) or char.encode('utf-8').isspace() or (ord(char) in range(913,970))

def is_english_text(text: str) -> bool:
    for char in text:
        if char not in kPunc:
            if not char_is_valid(char):
                print(char, ' is not valid alpha')
                return False
    return True
# 'abc\nedf'只传入了abc
def change2not(text: str) -> str:
    text = text.lstrip()
    text = text.rstrip()
    if '\'' in text:
        text = text.replace('\'', ' no')  # can't --> can not
        print('1:',text)
    if '\r' in text:
        text = text.replace('\r','') #'\r\n'让光标回到首部然后输出，使得原有输出被覆盖
    if '-\n' in text:
        text = text.replace('\n', '')
        print('2:',text)
    if '\n' in text:
        text = text.replace('\n', ' ')
        print('3:',text)
    return text


def main():
    print('*******************************\n\
**Welcome to word translation**\n\
*******************************\n'                                  )
    trans_config = 'trans -e google -s en -t zh -show-original y -show-original-phonetics y\
         -show-translation y -no-ansi -show-translation-phonetics n -show-prompt-message n\
              -show-languages n -show-original-dictionary n -show-dictionary n -show-alternatives y %s'
    # -speak -player /usr/bin/rhythmbox
    clip.copy('')  # clear the clip
    while True:
        global last_text
        text = clip.waitForNewPaste()
        text = change2not(text)
        if not is_english_text(text):
            print('debug:', text)
            continue
        if text != last_text:
            cmd = trans_config % '\'%s\'' % text
            last_text = text

            translate_en2zh(cmd)


if __name__ == '__main__':
    main()

# 913~970是大小写希腊字母
# Α 913
# Β
# Γ
# Δ
# Ε
# Ζ
# Η
# Θ
# Ι
# Κ
# Λ
# Μ
# Ν
# Ξ
# Ο
# Π
# Ρ
# ΢
# Σ
# Τ
# Υ
# Φ
# Χ
# Ψ
# Ω
# Ϊ
# Ϋ
# ά
# έ
# ή
# ί
# ΰ

# α 945
# β 946
# γ 947
# δ 948
# ε 949
# ζ 950
# η 951
# θ 952
# ι 953
# κ 954
# λ 955
# μ 956
# ν 957
# ξ 958
# ο 959
# π 960
# ρ 961
# ς 962
# σ 963
# τ 964
# υ 965
# φ 966
# χ 967
# ψ 968
# ω 969

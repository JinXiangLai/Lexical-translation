import os
import pyperclip as clip

def translate_en2zh(cmd):
    #print(cmd)
    os.system(cmd)
    print('========\n')

def main():
    trans_config = 'trans -e google -s en -t zh -show-original y -show-original-phonetics y -show-translation y -no-ansi -show-translation-phonetics n -show-prompt-message n -show-languages n -show-original-dictionary n -show-dictionary n -show-alternatives y %s'
    while True:
        clip.copy('') #'Content to be translated'
        text = clip.paste()
        if len(text) > 0:
            #print("获取剪切板内容：" + text)
            cmd = trans_config%'\'%s\''%text
            print(cmd,'\n')
            translate_en2zh(cmd)
if __name__ == '__main__':
    main()

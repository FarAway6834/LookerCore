from os import system as s
from os import chdir as cd
from os.path import join as j
from os.path import dirname as d

def main():
    while 1:
        a = input('> ')
        b = a.split(' ')
        match b.pop(0):
            case 'show':
                s('python ' + j(d(__file__), 'python-ascii-image/ascii.py ' + ' '.join(b))
            case 'view':
                s('python ' + j(d(__file__), 'viewer.py') + ' ' + ' '.join(b))
            case 'cd':
                cd(' '.join(b))
            case 'exit':
                break
            case '?':
                  print('''
if you want 2 see shell's basic ?, use "?1",
if you want 2 see looker help, use "help looker"
''')
            case '?1':
                  s('?')
            case 'help':
                if b[0] == 'looker':
                    print('''
LOOKer v1.0 Dev Ver.

made by https://github.com/leegeunhyeok/python-ascii-image (MIT)

shell help:
    view : show file with color
    exit : exit
    cd : cd command in cmd/bash, chdir(change directory)
    
    etc things is sir's basic shell

looker.sh : MacOSX, WSL, Linux
looker.bat : Windows, MS-DOS (unforturally, python didn't support MS-DOS, so it dosen't work)

donate : KakaoBank 7777-02-5065138 (I'm child, who loves monney, if you like this free-app, give me a monney.)

github repo : https://githb.com/FarAway6834/Looker (MIT)
''')

            case _:
                s(a)

if __name__ == "__main__": main()

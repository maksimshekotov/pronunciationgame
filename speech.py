import speech_recognition as speech_recog
import random
import time
def info():
    global words
    global score
    words = {
        "easy": ['cheeze','wall','better','look'],
        "medium":['behave', 'unique', 'forever', 'should'],
        "hard":['undetectable', 'vocabulary', 'nevermind', 'communicate'],
        }
    score = 1
 
def mode():
    global chs
    print('какой уровень вы хотите выбрать,')
    while True:
        print('легкий[1] средний[2]')
        try:
            chs = int(input('сложный[3]'))
            if chs == 1:
                print('хорошо')
                print('вы выбрали легкий уровень, типо обучение ')
                break
            elif chs == 2:
                print('хорошо')
                print('вы выбрали средний уровень, ну нормально')
                break
            elif chs == 3:
                print('хорошо')
                print('вы выбрали сложный уровень, будет довольно трудно')
                break
            else:
                print('пожалуйста выберите номер от 1 до 3')
        except ValueError:
            print('пожалуйста выберите номер от 1 до 3')

def modechoose():
    print(chs)
    if score >= 4:
        print('вы закончили игру, поздровляю')
        cat()
    if chs == 1:
        if len(words['easy']) >= 0:
            easymode()
    elif chs == 2:
        if len(words['medium']) >= 0:
            mediummode()    
    elif chs == 3:
        if len(words['hard']) >= 0:   
            hardmode()

def easywords():
    global worde
    global we
    easyw = random.choice(words['easy'])
    time.sleep(1)
    if easyw == 'cheeze':
        worde = 'cheeze'
        we = 'чиз'
    if easyw == 'wall':
        worde = 'wall'
        we = 'вол'
    if easyw == 'better':
        worde = 'better'
        we = 'бэтэр'
    if easyw == 'look':
        worde = 'look'
        we = 'лук'
def easymode():
    while True:
        if len(words['easy']) == 0:
            print("слов больше не осталось, выберите другой уровень")
            score +1

            break
        else:
            easywords()
            print(worde)
            time.sleep(1)
            print(worde, 'произносится как', we)
            words["easy"].remove(worde)
            print(words["easy"])
            time.sleep(3)
            speake()
            time.sleep(1)
            print('вы хотите продолжить проходить этот уровень или нет')
            wee = input('да[д] или нет[н]')
            if wee == 'д':
                print('хорошо')
            elif wee == 'н':
                print('ну ладно')     
                break
    if len(words['easy']) == 0:
        mode()
        modechoose()

def spch():
    global mic
    global recog
    mic = speech_recog.Microphone()
    recog = speech_recog.Recognizer()
    with mic as audio_file:
        recog.adjust_for_ambient_noise(audio_file)
        audio = recog.listen(audio_file)
        try:
            return recog.recognize_google(audio, language="en-EN")
        except speech_recog.UnknownValueError:
            return None
        except speech_recog.RequestError as e:
            print(f"Ошибка сервиса распознавания: {e}")
            return None
def speake():
    global texte
    while True:
        try:
            print("скажите", worde)
            texte = spch()
            if texte is None:
                print('программа не поняла, что вы сказали')
                print('попробуйте ещё раз')
                continue
            print(f"вы сказали: {texte}")
            if texte == worde:
                print('вы правильно сказали')
                print(worde)
            else:
                print('вы не правильно произнесли')
                print('слово:', worde)
                print(worde, 'произносится как', we)
            break
        except Exception as e:
            print(f"Произошла ошибка: {e}")
            break


def speakm():
    global textm
    while True:
        try:
            print("скажите", wordm)
            textm = spch()
            if textm is None:
                print('программа не поняла, что вы сказали')
                print('попробуйте ещё раз')
                continue
            print(f"вы сказали: {textm}")
            if textm == wordm:
                print('вы правильно сказали')
                print(wordm)
            else:
                print('вы не правильно произнесли')
                print('слово:', wordm)
                print(wordm, 'произносится как', wm)
            break
        except Exception as e:
            print(f"Произошла ошибка: {e}")
            break
def mediumwords():
    global wordm
    global wm
    medw = random.choice(words['medium'])
    time.sleep(1)
    if medw == 'behave':
        wordm = 'behave'
        wm = 'бихэйв'
    if medw == 'unique':
        wordm = 'unique'
        wm = 'юник'
    if medw == 'forever':
        wordm = 'forever'
        wm = 'форэвэр'
    if medw == 'should':
        wordm = 'should'
        wm = 'шуд'    
def mediummode():
    
    while True:
        if len(words['medium']) == 0:
            print("слов больше не осталось, выберите другой уровень")
            score +1
            break
        else:
            mediumwords()
            print(wordm)
            time.sleep(1)
            print(wordm, 'произносится как', wm)
            words["medium"].remove(wordm)
            print(words["medium"])
            time.sleep(3)
            speake()
            time.sleep(1)
            print('вы хотите продолжить проходить этот уровень или нет')  
            wmm = input('да[д] или нет[н]')
            if wmm == 'д':
                print('хорошо')
            elif wmm == 'н':
                print('ну ладно')     
                break
    if len(words['medium']) == 0:
        mode()
        modechoose()
    mode()
    modechoose()


def hardwords():
    global wordh
    global wh
    hardw = random.choice(words['hard'])
    time.sleep(1)
    if hardw == 'undetectable':
        wordh = 'undetectable'
        wh = 'андетектабл'
    if hardw == 'vocabulary':
        wordh = 'vocabulary'
        wh = 'вокабулэри'
    if hardw == 'nevermind':
        wordh = 'nevermind'
        wh = 'нэвэрмаинд'
    if hardw == 'communicate':
        wordh = 'communicate'
        wh = 'комюникэит'   
def speakh():
    global texth
    while True:
        try:
            print("скажите", wordh)
            texth = spch()
            if texth is None:
                print('программа не поняла, что вы сказали')
                print('попробуйте ещё раз')
                continue
            print(f"вы сказали: {texth}")
            if texth == wordh:
                print('вы правильно сказали')
                print(wordh)
            else:
                print('вы не правильно произнесли')
                print('слово:', wordh)
                print(wordh, 'произносится как', wh)
            break
        except Exception as e:
            print(f"Произошла ошибка: {e}")
            break 
def hardmode():
    while True:
        if len(words['hard']) == 0:
            print("слов больше не осталось, выберите другой уровень")
            score +1
            break
        else:
            hardwords()
            print(wordh)
            time.sleep(1)
            print(wordh, 'произносится как', wh)
            words["easy"].remove(wordh)
            print(words["hard"])
            time.sleep(3)
            speake()
            time.sleep(1)
            print('вы хотите продолжить проходить этот уровень или нет')
            wee = input('да[д] или нет[н]')
            if wee == 'д':
                print('хорошо')
            elif wee == 'н':
                print('ну ладно')     
                break
    if len(words['hard']) == 0:
        mode()
        modechoose()

info()
mode()
modechoose()
def cat():
    time.sleep(0.5)
    print(' /\_/\ ')
    time.sleep(0.5)
    print('(=>w>=)')
    time.sleep(0.5)
    print('()   ()')
    time.sleep(0.5)
    print('|     |')
    time.sleep(0.5)
    print('|     |')
    time.sleep(0.5)
    print('()___()')
    time.sleep(0.5)
    print('  | | ')
    time.sleep(0.5)
    print('   \ \ ')
    time.sleep(0.5)
    print('    \__)')
    time.sleep(0.5)
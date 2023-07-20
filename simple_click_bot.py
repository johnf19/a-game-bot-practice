# -*- coding : UTF-8 -*-
import win32api
import win32con
import win32gui
import time
import datetime
import tkinter
from tkinter import messagebox as tkMessageBox
import os,re
from threading import Thread
from PIL import Image, ImageGrab

#print(' WoWS Auto Run Click Bot Version V2.2.4f (May,2023) ')
#print(' Do Not Use in non-coop battles ')
#github/johnf19





def get_wows(): #get world of warships program position
    wowsw = u'World Of Warships'
    handle = win32gui.FindWindow(0, wowsw)
    if handle == 0:
        return [0,0,0,0]
    else:
        return win32gui.GetWindowRect(handle)

def get_wgc():
    handle = (win32gui.FindWindow(0, u'Wargaming.net Game Center'))
    if handle == 0:
        return [0,0,0,0]
    else:
        return win32gui.GetWindowRect(handle)

def get_hash(img):
    img = img.resize((16, 16), Image.ANTIALIAS).convert('L')
    avg = sum(list(img.getdata())) / 256
    s = ''.join(map(lambda i: '0' if i < avg else '1', img.getdata()))
    return ''.join(map(lambda j: '%x' % int(s[j:j+4], 2), range(0, 256, 4)))
def get_hash_R(img):
    img = img.resize((16, 16), Image.ANTIALIAS).convert('1')
    avg = sum(list(img.getdata())) / 256
    s = ''.join(map(lambda i: '0' if i < avg else '1', img.getdata()))
    return ''.join(map(lambda j: '%x' % int(s[j:j+4], 2), range(0, 256, 4)))
def get_diff(hash1, hash2, n=20):
    diff = sum(ch1 != ch2 for ch1, ch2 in zip(hash1, hash2))
    b = False
    assert len(hash1) == len(hash2)
    if sum(ch1 != ch2 for ch1, ch2 in zip(hash1, hash2)) < n:
        b = True
    return b


def get_scrb(a=0, b=0, c=1100, d=700):
    screen = get_wgc()
    topx, topy = screen[0], screen[1]
    img = ImageGrab.grab((topx + (screen[2] - screen[0]) * a / 1100, topy + (screen[3] - screen[1]) * b / 700,
                                topx + (screen[2] - screen[0]) * c / 1100, topy + (screen[3] - screen[1]) * d / 700))
    hash = get_hash(img)
    #img2.save('C://Users/John/Desktop/1.jpg')
    return hash

def get_scr(a=0, b=0, c=1100, d=700):
    screen = get_wows()
    topx, topy = screen[0], screen[1]
    img = ImageGrab.grab((topx + (screen[2] - screen[0]) * a / 1296, topy + (screen[3] - screen[1]) * b / 759,
                                topx + (screen[2] - screen[0]) * c / 1296, topy + (screen[3] - screen[1]) * d / 759))
    hash = get_hash(img)
    #img2.save('C://Users/John/Desktop/1.jpg')
    return hash

def get_scr_R(a=0, b=0, c=1100, d=700):
    screen = get_wows()
    topx, topy = screen[0], screen[1]
    img = ImageGrab.grab((topx + (screen[2] - screen[0]) * a / 1296, topy + (screen[3] - screen[1]) * b / 759,
                                topx + (screen[2] - screen[0]) * c / 1296, topy + (screen[3] - screen[1]) * d / 759))
    hash = get_hash_R(img)
    #img2.save('C://Users/John/Desktop/1.jpg')
    return hash

def mouse(x, y, t = 0.2):
    try:
        screen = get_wows()
        topx, topy = screen[0], screen[1]
        xt = int(topx + (screen[2] - screen[0]) * x / 1296)
        yt = int(topy + (screen[3] - screen[1]) * y / 759)
        win32api.SetCursorPos((xt, yt))
        time.sleep(t)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, xt, yt, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, xt, yt, 0, 0)
        time.sleep(0.2)
    except:
        time.sleep(0.5)
        print_log('exception: mouse\(%s,%s\) failed!') %x, y

def mouse_track(x, y, z = 10):
    try:
        screen = get_wows()
        topx, topy = screen[0], screen[1]
        xt = int(topx + (screen[2] - screen[0]) * x / 1296)
        yt = int(topy + (screen[3] - screen[1]) * y / 759)
        i = 0
        while i <= z:
            xt = xt + i
            win32api.SetCursorPos((xt, yt))
            i+=1
            time.sleep(0.2)
    except:
        print_log('function: mouse_track failed')

def mouse_double(x, y):
    try:
        mouse(x, y)
        time.sleep(0.5)
        mouse(x, y)
    except:
        print_log('function: mouse_double failed')

def mouse_wgc(x, y):
    screen = get_wgc()
    topx, topy = screen[0], screen[1]
    xt = int(topx + (screen[2] - screen[0]) * x / 1100)
    yt = int(topy + (screen[3] - screen[1]) * y / 700)
    win32api.SetCursorPos((xt, yt))
    time.sleep(0.2)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, xt, yt, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, xt, yt, 0, 0)
    time.sleep(0.2)
def kbd(x):
    win32api.keybd_event(x,0,0,0)
    win32api.keybd_event(x,0,win32con.KEYEVENTF_KEYUP,0)
    time.sleep(0.1)

def quitbattle():
    kbd(27)
    time.sleep(1)
    mouse(100,100)
    mouse(644,312)
    time.sleep(1)
    mouse(575,445)
    time.sleep(5)

def quitwows():
    time.sleep(600)
    mouse(644,299)
    win32api.keybd_event(18,0,0,0)
    win32api.keybd_event(115,0,0,0)
    time.sleep(1)
    win32api.keybd_event(18,0,win32con.KEYEVENTF_KEYUP,0)
    win32api.keybd_event(115,0,win32con.KEYEVENTF_KEYUP,0)
    time.sleep(2)
    kbd(13)

def print_log(log_new, log_bef = 'ezbot hello world'):
    if log_new != log_bef:
        print(str(datetime.datetime.now())[:19], ' log:', log_new)
    return log_new


def play_wows():
    global flag_game_play
    flag_game_play = True
    battle = (578,37,717,82)
    ### HashTable of InGame Elements ###
    #battlehash = (['fffffffffffe00001ff81ff81ff81ff81ff81ff01ff808780000000000000000',
    #'ffffffffffff20001ff81ff81ff81ff81ff81ff01ff808700000000000000000','fffffffffffffffffe2fe007e007e007e007a000200000000000000000000000'])
    hash_notReady = 'ffff00000000000000001fd81ff81ff81ff81ff81ff81ff80000000000000000'
    hash_startBattle = 'ffff00000000000000001fd81ff81ff81ff81ff81ff81ff80000000000000000' #'ffff00000000000000001fd81ff81ff81ff81ff81ff81ff80000000000000000'
    hash_startBattle_alter = 'ffff00000000000000001ff81ff81ff81ff81ff81ff81ff80000000000000000'
    hash_noSkill = '0000fffffffffffffc3f57eb07e003c003e003e003e0018000000000ffff0000'
    hash_noCommander = '00000000ffff7fff7fff7fff7fdf7bdf03c003c003c001c0000007f00ff03ffc'
    shiptype = (18,511,31,520) #shiptype icon in battle
    stcruiser = 'ffe3ffc3ffc7ff87ff8fff0fff1fff1ffe1ffe3ffe3ffc3ffc7ff87ff87cf8fc' #cruiser icon
    stbb = 'ff18ff18fe31fe31fe31fc63fc63fce7f8c7f8c7f18ff18ff31fe31fe31fc63f' #battleship icon
    stcv = 'fff3fff3fff3fff3fff3fff3fff300030003fff3fff3fff3fff3fff3fff3fff2' #aircraftcarrier icon
    stdd = 'c000c000fc00ff80fff0fffcfffffffffffffffffffcffe0ff00fc00c000c000'
    logo = (84,569,185,660) #pattern displayed when sunk
    logohash = '010003800380038003c007e007c005800380018019d01df00fb00ff01fe007e0'
    logo2hash = 'e78fffdffe7ff21e619d43980e001000008171327bc49e4e8e0380018001c003'
    logo3hash = '00001ff01ff81ff81ff81ff81ff813f810f8107818181e181f081fc81ff81ff8'
    hash_badge = '0000010024a90100114205a0228000880902212009900890252206c809a02100'
    hash_badge_bot = '0000010024a90100114205a0228000880902212009900890252206c809a02100'
    badge = (460,596,571,689)

    botton_battleFinishedEsc = (1207,35,1231,47)
    hash_battleFinishedEsc = 'ffffffffffffffffc223c021cca1cca9c66fc26fc22fcf2fcc89cc89c621c223'
    login = (553,566,740,605) #login button
    loginhash = '000000000000000007f00ff80ff80ff80fd80ff00ff00ff80fe013383ffc3ffc'
    hash_login = '000000000000000007f00ff80ff80ff80fd80ff00ff00ff80fe013383ffc3ffc'
    hash_login_steam = '0001ffffffffffffffff07f00ff00ff00fd00ff00ff00ff00000000000000000'
    botton_menuEsc = (1236,55,1260,68)
    hash_menuEsc = 'e7f3ffffffffffffffff00000000000000000000000000000000000000000000'

    alwaysd = (896,154,898,159)
    alwaysdhash ='03ff03ff03ff01ff01ff00ff00ff00ff00ff00ff00ff00ff007f007f007f007f'
    bto = (1070,719,1175,725)
    signal = (691,113,705,121)
    signalhash = '01cf01cf01cf01cf01cf01cf01cf01cf01cf09cf09cf09cf09cff80ffc1ffc1f'
    menuesc = (539,403,756,438)

    hash_daily_reward='ffff800080000000000003d01ff81ff81ff81ff81ff800000000000000000000'
    ###New HashTable for RGB mode###
    hash_startBattle_R ='555520829658492524889b7555921ad9ad5456aa1d69aab41109a4a41252a909'
    hash_notReady_R = '5555208296584925249292a95aa825559a924a542aa995524849252492924849'
    ###New HashTable add on Nov 14 2022###
    hash_login_wgc = 'ffff00000000000000000ff00ff00ff00ff00ff00ff00ff00000000000000000'
    hash_warn_inactive = 'fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff'
    hash_loginInprogress = '09d40ff40ff60ff60ff60ce60c660c660fe60ff60ff60ff60fe68fe69ff69ff7'
    ### HashTable Fin. ###
    login_wgc = (548,424,747,471)
    warn_inactive = (0,0,100,100)

    try:
        mouse(640,360)
    except:
        print_log('mouse click no target')
        time.sleep(10)

    #####
    number_of_play = 1500 # play n battles.
    mode_ship_amount = 4 # play the first n ship(s) in slot.
    mode_primary_ship = 0 # ship slot 1 or 2 or 3 or 4; 0 is null with no primary ship.
    mode_first_battle_bonus = False # True or False, Bonus Cleaning mode.
    mode_ship_change = True # True or False, Change ship if sunk.
    #####


    esc = a = ship_now = count_logFailure = count_noMatch = gamark = rm = countold = count_gamePlayed = status = status_last = count_crash = count_squadronBack = con_count = 0
    log = log_old = ''

    if mode_first_battle_bonus == True:
        mode_ship_amount = 4
        mode_primary_ship = 0

    if mode_primary_ship == 0:
        shipchange = False
    else:
        shipchange = True

    ship_primary = mode_primary_ship*2 - 2
    flag_force_change = mode_first_battle_bonus
    flag_change_now = False
    print('bot started')
    print('Battles to play: ', number_of_play)
    while count_gamePlayed < number_of_play:

        sp = ship_primary
        sp_next = sp + 2
        if sp_next == mode_ship_amount*2:
                    sp_next = 0
        post = [battle,shiptype,botton_battleFinishedEsc]
        if flag_break == True:
            print('Bot Exited')
            time.sleep(1)
            flag_game_play = False
            quit()
            break
        if flag_pause == True:
            log = 'Bot Paused'
            time.sleep(10)
            break
        #if count_logFailure >= 2220:##!!!###
        #    os.popen('taskkill /F /IM \'World of Warships.exe\'')
        #    print_log('Too much login failure, kill wows and restart bot')
        #    time.sleep(5)
        #    t = Thread(target=game_start, args=())
        #    t.start()
        #    print_log('Stop previous thread')
        #    flag_game_play = False
        #    quit()
        if  count_noMatch > 100:
            kbd(27)
            count_noMatch = 0
        if count_gamePlayed == countold:
            pass
        else:
            print(str(datetime.datetime.now())[:19],'count:', count_gamePlayed)
        countold = count_gamePlayed
        for n in post:
            #print('recognizing:',n)
            if log != log_old:
                log_old = log
                print(str(datetime.datetime.now())[:19], ' log:', log)
            #if flag_break == False:
                #break
            hash1 = get_scr(*n)
            if get_diff(hash1, hash_startBattle):
                count_logFailure = count_noMatch = count_crash = 0
                hash2 = get_scr_R(578,37,717,82)
                if get_diff(hash2, hash_startBattle_R) or get_diff(hash2, hash_startBattle_alter):
                    time.sleep(2)
                    if shipchange:
                        log = 'try primary ship'
                        ship = (135,622,135,682,348,623,378,622)
                        mouse_double(ship[sp],ship[sp + 1]) #now the primary ship is choosed
                        shipchange = False
                        ship_now = sp
                        #a = sp_next #ship_next is after primary ship
                        continue
                    if flag_force_change:
                        flag_change_now = True
                        time.sleep(3)
                        continue
                    mouse(600,74)
                    time.sleep(2)
                    mouse_track(500,500)
                    time.sleep(0.5)
                    mouse(600,74)
                    time.sleep(2)
                    mouse_track(500,500)
                    time.sleep(1)
                    if get_diff(get_scr(530,565,610,595), hash_noSkill):
                        mouse(550, 570)
                        time.sleep(2)
                        mouse_track(500,500)
                    if get_diff(get_scr(505,545,634,575), hash_noCommander):
                        mouse(550,560)
                        time.sleep(2)
                        mouse_track(500,500)
                    print_log('mouse event2 battle start!\nplaying: slot %i'% int(ship_now/2 + 1))
                    con_count = 0
                    time.sleep(10)
                elif get_diff(hash2, hash_notReady_R) or flag_change_now: #ship change
                    print('ship now is SHIP ', ship_now, '(0/2/4/6)')
                    ship = (135,622,135,682,348,623,378,622)
                    if ship_now == sp: # if the playing ship is primary ship
                        print('ship change is off')
                        shipchange = False
                    if ship_now == mode_ship_amount*2 or ship_now >= 6:
                        ship_now = -2
                        flag_force_change = False
                        flag_change_now = False

                    if flag_change_now:
                        print_log('forcely change another ship')
                    mouse_double(ship[ship_now + 2],ship[ship_now + 3])
                   #print('mouse: ',(ship[ship_now + 2],ship[ship_now + 3]))
                    print('mouse event1 change ship')
                    ship_now += 2
                    print('ship change to SHIP ', ship_now, '(0/2/4/6)')
                    #a += 2
                    time.sleep(1)
                else:
                    print('unkown battle status, cannot start battle')
                break
            #elif get_diff(hash1, logohash) or get_diff(hash1, logo2hash) or get_diff(hash1, logo3hash):
            #   time.sleep(0.5)
            #    count_gamePlayed += 1
            #    if mode_primary_ship != 0:
            #        shipchange = True
            #    if mode_first_battle_bonus:
            #        flag_force_change = True
            #    kbd(27)
            #    time.sleep(1)
            #    mouse(100,100)
            #    mouse(654,342)
            #    time.sleep(1)
            #    mouse(575,445)
            #   time.sleep(2)
            #   print_log('quit battle')

            elif get_diff(hash1, stcruiser) or get_diff(hash1, stbb)or get_diff(hash1, stdd):
                count_logFailure = count_noMatch = count_crash = 0
                con_count += 1
                if get_diff(get_scr_R(460,596,571,689), hash_badge) and mode_ship_change:
                    log = 'ship destroyed'
                    time.sleep(0.5)
                    count_gamePlayed += 1
                    if mode_primary_ship != 0:
                        shipchange = True
                    if mode_first_battle_bonus:
                        flag_force_change = True
                    kbd(27)
                    time.sleep(1)
                    mouse(100,100)
                    mouse(65,342)
                    time.sleep(1)
                    mouse(575,445)
                    time.sleep(2)
                    print_log('quit battle')
                    con_count = 0
                    break
                elif con_count <= 25 and con_count >= 0:
                    kbd(87)
                    kbd(87)
                    #kbd(65)
                    #kbd(68)
                    kbd(87)
                    kbd(87)
                    kbd(87)
                    kbd(82)#p
                elif con_count < 0:
                    #print('elif')
                    log = 'still in battle, get return'
                    kbd(82)
                    time.sleep(10)
                else:
                    kbd(83)
                    kbd(83)
                    #kbd(65)
                    #kbd(68)
                    kbd(83)
                    kbd(83)
                    kbd(83)
                    kbd(82)#p
                    con_count = -25
                log ='moving!'
                    #kbd(68)
                    #kbd(84) #T
                mouse_track(500,500)
                count_crash = 0
                time.sleep(10)
                break
            elif get_diff(hash1, stcv):
                count_logFailure = count_noMatch = count_crash = 0
                count_squadronBack += 1
                log = 'playing cv'
                kbd(87)
                kbd(87)
                kbd(87)
                kbd(87)
                kbd(87)
                kbd(49)#squadron take off
                kbd(49)
                mouse_track(500,500)
                if count_squadronBack == 3:
                    kbd(70)#squadron back
                    count_squadronBack = 0
                time.sleep(5)
                break
            elif get_diff(hash1, hash_battleFinishedEsc):
                con_count = count_logFailure = count_noMatch = count_crash = 0
                gamark +=1
                count_gamePlayed += 1
                count_noMatch = 0
                if mode_primary_ship != 0:
                    shipchange = True
                if mode_first_battle_bonus:
                    flag_force_change = True
                kbd(27)
                print_log('battle finished!')
                time.sleep(5)
                break
            else:
                count_crash += 1
                if count_crash > 40:
                    count_crash = 0
                    if get_diff(get_scr(548,424,747,471), hash_login_wgc):
                        log = 'Disconnected. try log in'
                        mouse(600,450)
                        break
                    #elif get_diff(get_scr(10,10,100,100), hash_warn_inactive):
                        #mouse(500,500)
                        #break
                    elif get_diff(get_scr(599,711,699,722), hash_loginInprogress):
                        time.sleep(10)
                        break
                    else:
                        kbd(27)

            #elif get_diff(hash1, hash_login, 10):
            #    count_noMatch = 0
            #    mouse(100,100)
            #    try:
            #        mouse_track(550,550)
            #        mouse_double(600,580)
            #        time.sleep(2)
            #        count_logFailure += 1
            #    except:
            #        print('except event2, log in failure')
            #        game_start()
            #    print_log('log in')
            #    time.sleep(40)
            #elif get_diff(get_scr(548,441,745,490), hash_login_steam, 10):
            #    count_noMatch = 0
            #    mouse(100,100)
            #    try:
            #        mouse_track(550,450)
            #        mouse_double(600,480)
            #        time.sleep(2)
            #        count_logFailure += 1
            #    except:
            #        print('except event2, log in failure')
            #        game_start()
            #    print_log('log in[wgc or steam]')
            #    time.sleep(40)
            #else:
            #    mouse_track(600,300)
            #    count_noMatch += 1
            #    time.sleep(2)
    return

def execCmd(cmd):
    r = os.popen(cmd)
    text = r.read()
    r.close()

def out():
    print('out')

def game_start():
    if get_wows() == [0, 0, 0, 0]:
        tm = 0
        k = 0
        os.popen('start C://Users/john/Documents/Games/Wargaming.net/GameCenter/wgc.exe')
        while tm < 20:
            if get_diff(get_scrb(100, 620, 200, 660), 'ffffffff7fff1fff07ff01ff007f003f000f000f001f000f000e000e000a000a'):
                screen = get_wgc()
                topx, topy = screen[0], screen[1]
                win32api.SetCursorPos((int(topx + (screen[2] - screen[0]) * 110 / 1100), int(topy + (screen[3] - screen[1]) * 630 / 700)))
                time.sleep(0.2)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, int(topx + (screen[2] - screen[0]) * 110 / 1100), int(topy + (screen[3] - screen[1]) * 630 / 700), 0, 0)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, int(topx + (screen[2] - screen[0]) * 110 / 1100), int(topy + (screen[3] - screen[1]) * 630 / 700), 0, 0)
                time.sleep(0.2)
                print('launcher event1, start wgc and wows')
                break
            else:
                tm += 1
                time.sleep(10)
                print('launcher event1, start key ready pending, possibly the game is updating')
        if get_wgc() != [0, 0, 0, 0]:
            while k <= 2:
                if get_wows() != [0, 0, 0, 0] and get_wgc() != [0, 0, 0, 0]:
                    time.sleep(3)
                    os.popen('taskkill /F /IM wgc.exe')
                    time.sleep(5)
                    k += 1
                    print('launcher event2, start wows and kill wgc')
                else:
                    time.sleep(3)
    if get_wows() != [0, 0, 0, 0]:

        log = 'launcher event3, play wows'
        play_wows()

#def crash_control():
    #'C:\Users\john\Documents\Games\World_of_Warships_ASIA\bin\4365481\bin64'

if __name__ == '__main__':
    get_scr()
    top = tkinter.Tk()
    def __bot_stop():
        global flag_break
        p = 0
        while p < 10:
            flag_break = True
            p += 1
            time.sleep(1)
    def __bot_pause():
        global flag_pause
        p = 0
        while p < 10:
            flag_pause = True
            p += 1
            time.sleep(1)
    def stopbot():
        global flag_break
        flag_break = True
        Thread(target=__bot_stop, args=()).start()
        tkMessageBox.showinfo("机械近卫","bot stopped")

    def startbot():
        global flag_break, flag_pause, flag_game_play
        flag_break = flag_pause = False
        try:
            t = Thread(target=game_start, args=())
            t.start()
        except:
            flag_game_play = False
    def pausebot():
        global flag_pause
        flag_pause = True
        Thread(target=__bot_pause, args=()).start()
        tkMessageBox.showinfo("机械近卫","bot paused")





    B1 = tkinter.Button(top, text = "START  BOT", command = startbot)
    B1.pack()
    B2 = tkinter.Button(top, text ="PAUSE BOT", command = pausebot)
    B2.pack()
    B3 = tkinter.Button(top, text ="STOP  BOT", command = stopbot)
    B3.pack()
    top.title("SimpleClickB0T")
    top.geometry('250x80+5+5')
    top.mainloop()

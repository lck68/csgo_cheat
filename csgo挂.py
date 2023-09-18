from __future__ import print_function
import ctypes, sys # 管理员权限
import keyboard  # 键盘
import time
 
def is_admin():  # 定义获取管理员权限的函数
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
if is_admin():   # 如果是管理员运行
    
    ######## 主要部分代码开始

    def press_key(key):   # 定义按下按键抬起动作的函数
        keyboard.press(key)
        keyboard.release(key)

    def type_text(text):  # 定义一个输入字母的函数
        for char in text:
            press_key(char)
            time.sleep(0.05)

    def on_f1():  # 开启作弊
        type_text("`sv")
        keyboard.press('shift')
        keyboard.press('_')
        keyboard.release('_')
        keyboard.release('shift')
        type_text("cheats 1")
        press_key('enter')
        press_key('ESC')

    def on_f2():  # 无敌模式
        type_text("`god")
        press_key('enter')
        press_key('ESC')

    def on_f2A():  # 关无敌
        type_text("`god0")
        press_key('enter')
        press_key('ESC')

    def on_f5():  # 开启透视
        type_text("`cl")
        keyboard.press('shift')
        keyboard.press('_')
        keyboard.release('_')
        keyboard.release('shift')
        type_text("countbones 1")
        press_key('enter')
        press_key('ESC')

    def on_f5A():  # 关闭透视
        type_text("`cl")
        keyboard.press('shift')
        keyboard.press('_')
        keyboard.release('_')
        keyboard.release('shift')
        type_text("countbones 0")
        press_key('enter')
        press_key('ESC')

    def on_f6():  # 人物上色
        type_text("`r")
        keyboard.press('shift')
        keyboard.press('_')
        keyboard.release('_')
        keyboard.release('shift')
        type_text("drawothermodels 2")
        press_key('enter')
        press_key('ESC')

    def on_f6A():  # 关上色
        type_text("`r")
        keyboard.press('shift')
        keyboard.press('_')
        keyboard.release('_')
        keyboard.release('shift')
        type_text("drawothermodels 1")
        press_key('enter')
        press_key('ESC')

    def on_f11():  # 瞬间满血
        type_text("`ent")
        keyboard.press('shift')
        keyboard.press('_')
        keyboard.release('_')
        keyboard.release('shift')
        type_text("fire ")
        keyboard.press('shift')
        keyboard.press('!')
        keyboard.release('!')
        keyboard.release('shift')
        type_text("self addoutput ")
        keyboard.press('shift')
        keyboard.press('"')
        keyboard.release('"')
        keyboard.release('shift')
        type_text("health 100")
        keyboard.press('shift')
        keyboard.press('"')
        keyboard.release('"')
        keyboard.release('shift')
        press_key('enter')
        press_key('ESC')

    def on_f11A():  # 自杀
        type_text("`kill")
        press_key('enter')
        press_key('ESC')

    def on_f8():  # 无限弹药
        type_text("`sv")
        keyboard.press('shift')
        keyboard.press('_')
        keyboard.release('_')
        keyboard.release('shift')
        type_text("infinite")
        keyboard.press('shift')
        keyboard.press('_')
        keyboard.release('_')
        keyboard.release('shift')
        type_text("ammo 1")
        press_key('enter')
        press_key('ESC')

    def on_f8A():  # 关闭无限弹药
        type_text("`sv")
        keyboard.press('shift')
        keyboard.press('_')
        keyboard.release('_')
        keyboard.release('shift')
        type_text("infinite")
        keyboard.press('shift')
        keyboard.press('_')
        keyboard.release('_')
        keyboard.release('shift')
        type_text("ammo 0")
        press_key('enter')
        press_key('ESC')

    def on_f9():  # ct增伤
        type_text("`mp")
        keyboard.press('shift')
        keyboard.press('_')
        keyboard.release('_')
        keyboard.release('shift')
        type_text("damage")
        keyboard.press('shift')
        keyboard.press('_')
        keyboard.release('_')
        keyboard.release('shift')
        type_text("scale")
        keyboard.press('shift')
        keyboard.press('_')
        keyboard.release('_')
        keyboard.release('shift')
        type_text("ct")
        keyboard.press('shift')
        keyboard.press('_')
        keyboard.release('_')
        keyboard.release('shift')
        type_text("body 2.0")
        press_key('enter')
        press_key('ESC')

    def on_f9A():  # 关ct增伤
        type_text("`mp")
        keyboard.press('shift')
        keyboard.press('_')
        keyboard.release('_')
        keyboard.release('shift')
        type_text("damage")
        keyboard.press('shift')
        keyboard.press('_')
        keyboard.release('_')
        keyboard.release('shift')
        type_text("scale")
        keyboard.press('shift')
        keyboard.press('_')
        keyboard.release('_')
        keyboard.release('shift')
        type_text("ct")
        keyboard.press('shift')
        keyboard.press('_')
        keyboard.release('_')
        keyboard.release('shift')
        type_text("body 1.0")
        press_key('enter')
        press_key('ESC')

    def on_f10():  # t增伤
        type_text("`mp")
        keyboard.press('shift')
        keyboard.press('_')
        keyboard.release('_')
        keyboard.release('shift')
        type_text("damage")
        keyboard.press('shift')
        keyboard.press('_')
        keyboard.release('_')
        keyboard.release('shift')
        type_text("scale")
        keyboard.press('shift')
        keyboard.press('_')
        keyboard.release('_')
        keyboard.release('shift')
        type_text("t")
        keyboard.press('shift')
        keyboard.press('_')
        keyboard.release('_')
        keyboard.release('shift')
        type_text("body 2.0")
        press_key('enter')
        press_key('ESC')

    def on_f10A():  # 关t增伤
        type_text("`mp")
        keyboard.press('shift')
        keyboard.press('_')
        keyboard.release('_')
        keyboard.release('shift')
        type_text("damage")
        keyboard.press('shift')
        keyboard.press('_')
        keyboard.release('_')
        keyboard.release('shift')
        type_text("scale")
        keyboard.press('shift')
        keyboard.press('_')
        keyboard.release('_')
        keyboard.release('shift')
        type_text("t")
        keyboard.press('shift')
        keyboard.press('_')
        keyboard.release('_')
        keyboard.release('shift')
        type_text("body 1.0")
        press_key('enter')
        press_key('ESC')

    def on_f7():  # 无后座
        type_text("`weapon")
        keyboard.press('shift')
        keyboard.press('_')
        keyboard.release('_')
        keyboard.release('shift')
        type_text("accuracy")
        keyboard.press('shift')
        keyboard.press('_')
        keyboard.release('_')
        keyboard.release('shift')
        type_text("nospread 1;weapon")
        keyboard.press('shift')
        keyboard.press('_')
        keyboard.release('_')
        keyboard.release('shift')
        type_text("recoil")
        keyboard.press('shift')
        keyboard.press('_')
        keyboard.release('_')
        keyboard.release('shift')
        type_text("scale 0")
        press_key('enter')
        press_key('ESC')

    def on_f7A():  # 关无后座
        type_text("`weapon")
        keyboard.press('shift')
        keyboard.press('_')
        keyboard.release('_')
        keyboard.release('shift')
        type_text("accuracy")
        keyboard.press('shift')
        keyboard.press('_')
        keyboard.release('_')
        keyboard.release('shift')
        type_text("nospread 0;weapon")
        keyboard.press('shift')
        keyboard.press('_')
        keyboard.release('_')
        keyboard.release('shift')
        type_text("recoil")
        keyboard.press('shift')
        keyboard.press('_')
        keyboard.release('_')
        keyboard.release('shift')
        type_text("scale 2")
        press_key('enter')
        press_key('ESC')

    print("============================================")
    print("|| CS:GO 娱乐辅助器 测试版 仅限人机模式使用！||")
    print("============================================")
    print("||  作者：TG@lck88，软件仅供测试，请勿外传！ ||")
    print("============================================")
    print("||  ① 软件初始化：F1  （辅助启动）          ||")  # sv_cheats 1
    print("============================================")
    print("||  ② 无敌模式：F2    （锁定血量）          ||")  # god
    print("============================================")
    print("||  ③ 开启透视：F5    （显示骨骼透视）      ||")  # cl_countbones 1
    print("============================================")
    print("||  ④ 人物上色：F6    （人物上色透视）      ||")  # r_drawothermodels 2
    print("============================================")
    print("||  ⑤ 无后座力：F7    （取消所有抖动）      ||")  # weapon_accuracy_nospread 1;weapon_recoil_scale 0
    print("============================================")
    print("||  ⑥ 无限弹药：F8    （无限主弹夹免换弹）  ||")  # sv_infinite_ammo 1
    print("============================================")
    print("||  ⑦ 双倍伤害：F9     (对警ct伤害双倍)    ||")  # mp_damage_scale_ct_body 2.0
    print("============================================")
    print("||  ⑦ 双倍伤害：F10    (对匪t伤害双倍)     ||")  # mp_damage_scale_t_body 2.0
    print("============================================")
    print("||  ⑧ 瞬间满血：F11   （按一下直接回满血）  ||")  # ent_fire !self addoutput "health 100"
    print("============================================")
    print("||※ 按热键+Alt为关闭，例如关闭透视：F5+Alt ||")
    print("============================================")

    # 绑定热键
    keyboard.add_hotkey('F1', on_f1)
    keyboard.add_hotkey('F2', on_f2)
    keyboard.add_hotkey('F5', on_f5)
    keyboard.add_hotkey('F6', on_f6)
    keyboard.add_hotkey('F7', on_f7)
    keyboard.add_hotkey('F8', on_f8)
    keyboard.add_hotkey('F9', on_f9)
    keyboard.add_hotkey('F10', on_f10)
    keyboard.add_hotkey('F11', on_f11)
    keyboard.add_hotkey('F2+alt', on_f2A)
    keyboard.add_hotkey('F5+alt', on_f5A)
    keyboard.add_hotkey('F6+alt', on_f6A)
    keyboard.add_hotkey('F7+alt', on_f7A)
    keyboard.add_hotkey('F8+alt', on_f8A)
    keyboard.add_hotkey('F9+alt', on_f9A)
    keyboard.add_hotkey('F10+alt', on_f10A)
    keyboard.add_hotkey('F11+alt', on_f11A)
    keyboard.wait()

    ######## 主要部分代码结束
    
else:  # 如果不是管理员运行
    if sys.version_info[0] == 3:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    else:#in python2.x
        ctypes.windll.shell32.ShellExecuteW(None, u"runas", unicode(sys.executable), unicode(__file__), None, 1)


# 没事别乱改，有事联系Telegram @lck88

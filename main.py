import pgzrun
from datetime import datetime,date
from random import randint,choice
# https://xclient.info/s/
WIDTH = 1000
HEIGHT = 650

nowdate = str(date.today())
info = open("inf.txt",mode='r',encoding='utf-8')
i = info.readline()
infs = info.readline().split(";")
lastOpenDate = info.readline()
lst1 = ["name","exp","feeling","money","fish","speed","health","onduty","huazi","tea",'dkt','cyt','sft','ckrm','highsc','gmt']
inf = {}# only this is avaliable
for s in range(16):
    inf[lst1[s]]=infs[s]
info.close()
del infs
savetimer = 0
ui = 0
tmtea = 0
tmcy=0
side = ''
siui5 = ""
fishSide = ''
fishSpeed = 0
fishY = 0
tmfish = 0
tmyg = 1
tmsleep = 30
ygout = 330
wait = 60
fishing = 0
gofish = 0
scoreyg = 0
shoot = False

name = str(inf['name'])
exp = int(inf['exp'])
feeling = int(inf['feeling'])
money = int(inf['money'])
fish = int(inf['fish'])
speed = int(inf['speed'])
health = int(inf['health'])
onduty = int(inf['onduty'])
huazi = int(inf['huazi'])
tea = int(inf['tea'])
dkt = int(inf['dkt'])
cyt = int(inf['cyt'])
sft = int(inf['sft'])
ckrm = int(inf['ckrm']) # chalk remain
highsc = int(inf['highsc'])
gmt = int(inf['gmt'])
scoreyg = highsc
if nowdate != lastOpenDate:
    dkt = 0
    cyt = 0
    sft = 0
    gmt = 0
    ckrm = 77

saying1 = open('say.txt',mode='r',encoding='utf-8')
saying = saying1.readline().replace('n','\n').split('$')
#saying=saying
say = ''

kuai = Actor("1",center=(30,30))
kuai.x,kuai.y = 500,320
xcb = Actor("sk")
xcb.x,xcb.y = -120,-230
jyg = Actor('yg0')
jyg.x,jyg.y = -1233,-3211

buttom1 = Actor("but")
buttom1.x,buttom1.y = 900,140
but2 = Actor("but2")
but2.x,but2.y = 900,200
bk = Actor("back")
bk.x,bk.y = -123,-321
tofish = Actor("tofish")
tofish.x,tofish.y = -2222,-2222
torun = Actor("torun")
torun.x,torun.y = -1111,-1111
aim = Actor('aim')
aim.x,aim.y = -123,-321
chalk = Actor('chalk')
chalk.x,chalk.y = -123,-321

drinktea = Actor("hc")
cy = Actor('cy')
if dkt >= 7 or tea < 1:
    drinktea.x, drinktea.y = -230, -333
else:
    drinktea.x, drinktea.y = 230, 333
if cyt >= 7 or huazi < 1:
    cy.x, cy.y = -750, -333
else:
    cy.x, cy.y = 750, 333
sellTea = Actor("te")
sellTea.x,sellTea.y = -333,-222
sellY = Actor("hz")
sellY.x,sellY.y = -133,-322
sellF = Actor("fl")
sellF.x,sellF.y = -123,-321
sellck = Actor("ck")
sellck.x,sellck.y = -123,-321

j = Actor('j')
j.x,j.y = -222,-222
fishe = Actor("sfish")
fishe.x,fishe.y = -2323,-22
stop = Actor("stop")
stop.x,stop.y = -321,-123

def on_mouse_down(pos):
    global ui,say,saying,feeling,tmtea,tmfish,exp,dkt,tea,health,cyt,tmcy,huazi,money,fish,sft,shoot,X,Y,wait,ckrm,gmt,side
    if ui == 5:
        if ckrm > 0:
            shoot = True
            ckrm -= 1
            X = int(aim.x)
            Y = int(aim.y)
        else:
            pass
    if ui == 3:
        if pos[0] < 330:
            side = 'l'
        elif pos[0] > 570:
            side = 'r'
        else:
            side = ''
        if kuai.collidepoint(pos) and tmfish <=0:
            tmfish = 1
    if kuai.collidepoint(pos):
        a = choice(saying)
        say = a
        save()
    if drinktea.collidepoint(pos):
        if dkt < 7:
            animate(drinktea, pos=(kuai.x, kuai.y + 145))
            tmtea = 1
            dkt += 1
            tea -= 1
            health += 9
            feeling += 10
            exp += 2
        else:
            pass
    if cy.collidepoint(pos):
        if cyt < 7:
            animate(cy,pos=(kuai.x+60,kuai.y+90))
            tmcy = 1
            cyt += 1
            huazi -= 1
            health -= 10
            feeling += 7
            exp += 3
        else:
            pass
    if buttom1.collidepoint(pos):
        ui = 1
        tofish.x,tofish.y = 125,80
        torun.x,torun.y = 375,80
        save()
    if but2.collidepoint(pos):
        ui = 2
        sellY.x,sellTea.x,sellTea.y,sellY.y = 460,460,90,490
        sellF.x,sellF.y = 660,280
        sellck.x,sellck.y = 460,275
        save()
    if sellY.collidepoint(pos):
        if (money-5) > 0:
            money -= 5
            feeling-=9
            huazi += 1
        save()
    if sellTea.collidepoint(pos):
        if (money - 10)>0:
            money -= 10
            feeling -= 15
            tea += 1
        save()
    if sellF.collidepoint(pos):
        if fish >= 1 and sft < 30:
            money += 4
            feeling += 4
            fish -= 1
            sft += 1
        save()
    if sellck.collidepoint(pos):
        if gmt < 2:
            if (money-6)>0:
                money -= 6
                ckrm += 20
                gmt += 1
    if tofish.collidepoint(pos) and fish <= 20:
        ui = 3
        music.stop()
        music.play('bg')
        tofish.x,tofish.y = -213,-3211
        torun.x,torun.y = -132,-1111
        kuai.image = 'f2'
        j.x,j.y = 500,110
        kuai.x, kuai.y = 500, 50
    if torun.collidepoint(pos):
        ui = 5
        wait = 60
        music.stop()
        music.play('bg2')
        tofish.x, tofish.y = -213, -3211
        torun.x, torun.y = -132, -1111
        kuai.image = 'f2'
        kuai.x,kuai.y = 50,400
        chalk.x,chalk.y = 80,400
        jyg.x,jyg.y = -123,-321
    if bk.collidepoint(pos):
        if ui == 3 or ui == 5:
            music.stop()
            music.play('breaktime')
        ui = 0
        save()
        sellY.x, sellTea.x, sellTea.y, sellY.y = -460, -460, -490, -90
        stop.x,stop.y = -321,-123
        sellF.x,sellF.y = 1333,233
        sellck.x,sellck.y = -131,-323
        tofish.x,tofish.y = -231,-1111
        torun.x,torun.y = -132,-2222
        aim.x,aim.y = -123,-321
        chalk.x,chalk.y = -123,-321
        j.x,j.y = -2312,-222
        kuai.image = "1"
        jyg.x,jyg.y = -123,-321
        if dkt >= 7 or tea <1:
            pass
        else:
            drinktea.x, drinktea.y = 230, 333
        if cyt >= 7 or huazi < 1:
            pass
        else:
            cy.x, cy.y = 750, 333
def on_mouse_move(pos):
    global ui
    if ui == 5:
        if not shoot:
            kuai.angle = kuai.angle_to(pos)
            chalk.angle = chalk.angle_to(pos)
        aim.x,aim.y = pos
def on_key_down(key):
    global money,tea,huazi,ui,tmfish,side,siui5
    if ui == 3:
        if key == keys.RETURN and tmfish <=0:
            tmfish = 1
        if key == keys.LEFT:
            side = 'l'
        if  key == keys.RIGHT:
            side = 'r'
    if key == keys.S:
        save()
def on_key_up(key):
    global side,siui5
    if key == keys.LEFT or key == keys.RIGHT:
        side = ''
    if key == keys.DOWN or key == keys.UP:
        siui5 = ''
def save():
    global name,exp,feeling,money,fish,speed,health,onduty,huazi,tea,dkt,cyt,inf,nowdate,sft,ckrm,highsc,gmt
    inffile = open("inf.txt",mode = 'r',encoding='utf-8')
    line1 = inffile.readline()
    line2 = inffile.readline()
    line3 = inffile.readline()
    lst = [name,exp,feeling,money,fish,speed,health,onduty,huazi,tea,dkt,cyt,sft,ckrm,highsc,gmt]
    for i in range(len(lst)):
        lst[i] = str(lst[i])
    wr = ';'.join(lst)
    inffile.close()
    inffile = open("inf.txt",mode = 'w',encoding='utf-8')
    inffile.write(line1+wr+"\n"+nowdate)
    inffile.close()
def update():
    global ui,tmtea,tea,tmcy,huazi,tmfish,tmyg,dkt,cyt,savetimer,fishSide,fishSpeed,fishY,fishing,shoot,\
        X,Y,gofish,fish,side,health,feeling,exp,siui5,ygout,scoreyg,money,tmsleep,highsc,wait,ckrm,gmt
    if feeling >= 140:
        feeling = 70
        exp += 25
    if feeling <= 15:
        feeling = 30
        exp -= 15
    if health <= 25:
        health = 40
        exp -= 15
        save()
    if health >= 140:
        health = 100
        exp += 25
        save()
    if savetimer < 61:
        savetimer+=1
        if savetimer//60==1:
            save()
            savetimer = 0
    else:
        savetimer = 0
    if ui == 3:
        if fish > 20:
            ui = 0
            music.stop()
            music.play('breaktime')
        if tmfish == 0:
            if side == 'r' and kuai.right < 950:
                kuai.x += 3
                j.x += 3
            elif side == 'l' and kuai.left > 50:
                kuai.x -= 3
                j.x -= 3
        if not j.colliderect(fishe):
            if kuai.image != 'f2':
                kuai.image = 'f2'
            if tmfish > 0 and tmfish <= 540 // 6:
                tmfish += 1
                j.y += 6
            if tmfish > 540 // 6 and tmfish <= 540 // 6 * 2:
                j.y -= 6
                tmfish += 1
            if tmfish > 540 // 6 * 2:
                tmfish = 0
            if fishe.x in range(-46,1100):
                if fishing > gofish:
                    if fishSide == 'r':
                        fishe.x += fishSpeed
                    elif fishSide == 'l':
                        fishe.x -= fishSpeed
                else:
                    fishing += 1
            else:
                fishing = 0
                gofish = randint(60*3,60*8)
                fishSide = choice(['l','r'])
                fishSpeed = randint(4,12)
                fishY = randint(280,585)
                fishe.y = fishY
                if fishSide == 'r':
                    fishe.image = 'fishs'
                    fishe.x = -45
                else:
                    fishe.image = 'sfish'
                    fishe.x = 1095
        else:

            if j.y != 110:
                j.y -= 6
                tmfish = 0
                if kuai.image != 'f3':
                    kuai.image = 'f3'
                fishe.x,fishe.y = j.x,j.y
                fishing = 0
            else:
                fishe.x,fishe.y = -425,500
                gofish = randint(60 * 3, 60 * 8)
                fish += 1
                health += 5
                feeling += 5
                exp += 5
                fishing = 0
    if ui == 5:
        if ckrm ==0:
            aim.image = 'stop'
        if shoot:
            if chalk.colliderect(jyg):
                tmyg = 1
                ygout = randint(69-(scoreyg//15),219-(scoreyg//15))
                jyg.x, jyg.y = -123, -321
                if jyg.image == 'yg1':
                    scoreyg -= 10
                    if money > 10:
                        money -= 10
                        feeling -= 3
                        sounds.a.play()
                    tmsleep = 0
                elif jyg.image == 'yg4':
                    scoreyg += 5
                    feeling += 2
                    sounds.b.play()
                    money += 15
                else:
                    scoreyg += 1
                    feeling += 3
                    sounds.b.play()
            if chalk.x<X+5 and chalk.x > X -5:
                shoot = False
                chalk.x,chalk.y = kuai.x+40,kuai.y
            else:
                chalk.x += (X + 19 - chalk.x) / (10+(120-wait)//30)
            if chalk.y<Y+5 and chalk.y > Y -5:
                shoot = False
                chalk.x, chalk.y = kuai.x+40,kuai.y
            else:
                chalk.y += (Y + 19 - chalk.y) / (10+(120-wait)//30)
        if tmsleep < 22:
            tmsleep += 1
        if ygout >= tmyg:
            tmyg += 1
        else:
            jyg.x,jyg.y = randint(150,800),randint(50,600)
            ygout = ygout + wait+25
            if wait > 20:
                wait -= (scoreyg//50)/2
            jyg.image = choice(['yg0','yg1','yg2','yg3','yg4','yg1','yg2','yg0','yg3'])
        if scoreyg%10==0:
            money += 12
            scoreyg += 1
    if tmtea > 0:
        tmtea += 1
        if tmtea >= 81:
            tmtea = 0
            drinktea.x,drinktea.y = 230,333
            if dkt >= 7 or tea < 1:
                drinktea.x, drinktea.y = -123, -321
    if tmcy > 0:
        tmcy += 1
        if tmcy >= 81:
            tmcy = 0
            cy.x,cy.y = 750, 333
            if cyt >= 7 or huazi < 1:
                cy.x, cy.y = -123, -321
    if ui == 0:
        bk.x, bk.y = -900, 600
        kuai.x, kuai.y = 500, 320
        buttom1.x, buttom1.y = 900, 140
        but2.x, but2.y = 900, 200
    elif ui == 1 or ui == 2:
        kuai.x, kuai.y = -500, -320
        buttom1.x, buttom1.y = -900, -140
        but2.x, but2.y = -900, -200
        drinktea.x,drinktea.y = -123,-321
        cy.x, cy.y = -123, -321
        if ui == 1:
            pass
        else:
            xcb.x,xcb.y = 120,290

    if ui != 0:
        bk.x,bk.y = 920,615
    if ui != 2:
        xcb.x, xcb.y = -120, -230
    if ui != 3 and ui != 5:
        fishe.x = -3333
        j.x,j.y = -123,-333
        kuai.image = '1'
    if scoreyg > highsc:
        highsc = scoreyg
def draw():
    global ui,name,say,exp,scoreyg,tmsleep,highsc,ckrm
    buttom1.draw()
    but2.draw()
    screen.fill((12,13,14))
    if ui == 0:
        screen.draw.text(name, pos=(10, 0), fontname='a',color='blue')
        screen.draw.text("经验值：%s"%(exp), pos=(10, 27), fontname='a')
        screen.draw.text("心情：%s" % (feeling), pos=(10, 54), fontname='a')
        screen.draw.text(say,(300,500),fontname='a',fontsize=30,color='red')
        screen.draw.text("钱：%s" % (money), pos=(10, 81), fontname='a')
        screen.draw.text("健康：%s" % (health), pos=(10, 108), fontname='a')
    if ui == 2:
        screen.draw.text("茶：10",(300,100),fontname='a')
        screen.draw.text("烟：5", (300, 500), fontname='a')
        screen.draw.text("粉笔：6", (300, 300), fontname='a')
        screen.draw.text("卖鱼：4",(720,280), fontname='a',color='grey')
        screen.draw.text("钱：%s" % (money), pos=(10, 100), fontname='a')
        screen.draw.text("还有%s杯茶" % (tea), pos=(10, 2), fontname='a')
        screen.draw.text("还有%s根华子" % (huazi), pos=(10, 27), fontname='a')
        screen.draw.text('还有%s条鱼'%(fish),(10,54),fontname='a')
        screen.draw.text('还有%s根粉笔'%(ckrm),(10,79),fontname='a')
    if ui == 3:
        screen.draw.text(r"鱼：%s/21 条"%(fish),(10,1),fontname='a',color='orange')
        screen.draw.text("经验值：%s" % (exp), pos=(10, 27), fontname='a')
        screen.draw.text("健康：%s" % (health), pos=(10, 54), fontname='a')
        screen.draw.text("心情：%s" % (feeling), pos=(10, 79), fontname='a')
    if ui == 5:
        if tmsleep < 22:
            screen.fill((222,6,5))
        else:
            screen.fill((12,13,14))
        screen.draw.text("命中次数：%s" % (scoreyg), (10, 1), fontname='a', color='skyblue')
        screen.draw.text("剩余粉笔数：%s" % (ckrm), (10, 28), fontname='a', color='darkgreen')
        screen.draw.text("钱：%s" % (money), pos=(10, 55), fontname='a')
        screen.draw.text("经验值：%s" % (exp), pos=(10, 80), fontname='a')
        screen.draw.text("心情：%s" % (feeling), pos=(10, 101), fontname='a')
    screen.draw.text("抖音直播间：https://live.douyin.com/558122961351",(657,632),fontname='a',fontsize=14)
    kuai.draw()
    buttom1.draw()
    but2.draw()
    bk.draw()
    xcb.draw()
    drinktea.draw()
    cy.draw()
    sellY.draw()
    sellF.draw()
    sellTea.draw()
    j.draw()
    fishe.draw()
    tofish.draw()
    torun.draw()
    stop.draw()
    aim.draw()
    chalk.draw()
    jyg.draw()
    sellck.draw()
music.play("breaktime")
pgzrun.go()


import direct.directbase.DirectStart
from direct.directbase.DirectStart import base
from direct.task import Task
import math
from direct.interval.IntervalGlobal import Sequence
from panda3d.core import Point3

from panda3d.core import CollisionTraverser,CollisionNode,CollisionSphere
from pandac.PandaModules import Texture, TextureStage, CardMaker
from direct.showbase.DirectObject import DirectObject



class world (DirectObject):
    def __init__(self):
        base.setBackgroundColor(0,0,0)
        base.camera.setPos(0,15,1)
        base.camera.setHpr(0,180,180)
##################33
        self.colNode1 = CollisionNode("colNode1")
        colSphere1 = CollisionSphere(4.1, 30, 0, 1)
        self.colNode1.addSolid(colSphere1)
        self.colNP1 = render.attachNewNode(self.colNode1)
        self.colNP1.show()

        self.colNode2 = CollisionNode("colNode2")
        colSphere2 = CollisionSphere(5, 30, 50, 1)
        self.colNode2.addSolid(colSphere2)
        self.colNP2 = render.attachNewNode(self.colNode2)
        self.colNP2.show()



        ##############
        self.backgroundImage("model/sky.jpg")
        self.ob1 = loader.loadModel("model/gate/gate.egg")
        base.disableMouse()
        self.ob1.reparentTo(render)
        self.ob1.setScale(.003, .003, .003)
        self.ob1.setPos(0, 6,0)



        self.ob2 = loader.loadModel("model/Ground2/Ground2.egg")
        self.ob2.reparentTo(render)
        self.ob2.setScale(.2, .2, .01)
        self.ob2.setPos(0, 0, 0)

        self.ob3 = loader.loadModel("model/fence.egg")
        self.ob3.reparentTo(render)
        self.ob3.setScale(.2, .2, .2)
        self.ob3.setPos(3, 5.6, 0)

        self.ob3 = loader.loadModel("model/fence.egg")
        self.ob3.reparentTo(render)
        self.ob3.setScale(.2, .2, .2)
        self.ob3.setPos(4.5, 5.6, 0)

        self.ob3 = loader.loadModel("model/fence.egg")
        self.ob3.reparentTo(render)
        self.ob3.setScale(.2, .2, .2)
        self.ob3.setPos(5.8, 4.5, 0)
        self.ob3.setHpr(90, 0, 0)

        self.ob3 = loader.loadModel("model/fence.egg")
        self.ob3.reparentTo(render)
        self.ob3.setScale(.2, .2, .2)
        self.ob3.setPos(5.8, 2, 0)
        self.ob3.setHpr(90, 0, 0)

        self.ob3 = loader.loadModel("model/fence.egg")
        self.ob3.reparentTo(render)
        self.ob3.setScale(.2, .2, .2)
        self.ob3.setPos(5.8, -.5, 0)
        self.ob3.setHpr(90, 0, 0)

        self.ob3 = loader.loadModel("model/fence.egg")
        self.ob3.reparentTo(render)
        self.ob3.setScale(.2, .2, .2)
        self.ob3.setPos(5.8, -3, 0)
        self.ob3.setHpr(90, 0, 0)

        self.ob3 = loader.loadModel("model/fence.egg")
        self.ob3.reparentTo(render)
        self.ob3.setScale(.2, .2, .2)
        self.ob3.setPos(5.8, -5.5, 0)
        self.ob3.setHpr(90, 0, 0)

        self.ob3 = loader.loadModel("model/fence.egg")
        self.ob3.reparentTo(render)
        self.ob3.setScale(.2, .2, .2)
        self.ob3.setPos(5.8, -8, 0)
        self.ob3.setHpr(90, 0, 0)

        self.ob3 = loader.loadModel("model/fence.egg")
        self.ob3.reparentTo(render)
        self.ob3.setScale(.2, .2, .2)
        self.ob3.setPos(5.8, -10.5, 0)
        self.ob3.setHpr(90, 0, 0)

        self.ob3 = loader.loadModel("model/fence.egg")
        self.ob3.reparentTo(render)
        self.ob3.setScale(.2, .2, .2)
        self.ob3.setPos(5.8, -13, 0)
        self.ob3.setHpr(90, 0, 0)

        self.ob3 = loader.loadModel("model/fence.egg")
        self.ob3.reparentTo(render)
        self.ob3.setScale(.2, .2, .2)
        self.ob3.setPos(5.8, -15, 0)
        self.ob3.setHpr(90, 0, 0)

        self.ob3 = loader.loadModel("model/fence.egg")
        self.ob3.reparentTo(render)
        self.ob3.setScale(.2, .2, .2)
        self.ob3.setPos(5.8, -15.8, 0)
        self.ob3.setHpr(90, 0, 0)



###############
        self.ob3 = loader.loadModel("model/fence.egg")
        self.ob3.reparentTo(render)
        self.ob3.setScale(.2, .2, .2)
        self.ob3.setPos(-3, 5.6, 0)

        self.ob3 = loader.loadModel("model/fence.egg")
        self.ob3.reparentTo(render)
        self.ob3.setScale(.2, .2, .2)
        self.ob3.setPos(-4.5, 5.6, 0)

        self.ob3 = loader.loadModel("model/fence.egg")
        self.ob3.reparentTo(render)
        self.ob3.setScale(.2, .2, .2)
        self.ob3.setPos(-5.8, 4.5, 0)
        self.ob3.setHpr(90, 0, 0)

        self.ob3 = loader.loadModel("model/fence.egg")
        self.ob3.reparentTo(render)
        self.ob3.setScale(.2, .2, .2)
        self.ob3.setPos(-5.8, 2, 0)
        self.ob3.setHpr(90, 0, 0)

        self.ob3 = loader.loadModel("model/fence.egg")
        self.ob3.reparentTo(render)
        self.ob3.setScale(.2, .2, .2)
        self.ob3.setPos(-5.8, -.5, 0)
        self.ob3.setHpr(90, 0, 0)

        self.ob3 = loader.loadModel("model/fence.egg")
        self.ob3.reparentTo(render)
        self.ob3.setScale(.2, .2, .2)
        self.ob3.setPos(-5.8, -3, 0)
        self.ob3.setHpr(90, 0, 0)

        self.ob3 = loader.loadModel("model/fence.egg")
        self.ob3.reparentTo(render)
        self.ob3.setScale(.2, .2, .2)
        self.ob3.setPos(-5.8, -5.5, 0)
        self.ob3.setHpr(90, 0, 0)

        self.ob3 = loader.loadModel("model/fence.egg")
        self.ob3.reparentTo(render)
        self.ob3.setScale(.2, .2, .2)
        self.ob3.setPos(-5.8, -8, 0)
        self.ob3.setHpr(90, 0, 0)

        self.ob3 = loader.loadModel("model/fence.egg")
        self.ob3.reparentTo(render)
        self.ob3.setScale(.2, .2, .2)
        self.ob3.setPos(-5.8, -10.5, 0)
        self.ob3.setHpr(90, 0, 0)

        self.ob3 = loader.loadModel("model/fence.egg")
        self.ob3.reparentTo(render)
        self.ob3.setScale(.2, .2, .2)
        self.ob3.setPos(-5.8, -13, 0)
        self.ob3.setHpr(90, 0, 0)

        self.ob3 = loader.loadModel("model/fence.egg")
        self.ob3.reparentTo(render)
        self.ob3.setScale(.2, .2, .2)
        self.ob3.setPos(-5.8, -15, 0)
        self.ob3.setHpr(90, 0, 0)

        self.ob3 = loader.loadModel("model/fence.egg")
        self.ob3.reparentTo(render)
        self.ob3.setScale(.2, .2, .2)
        self.ob3.setPos(-5.8, -15.8, 0)
        self.ob3.setHpr(90, 0, 0)

        #################



        self.ob3 = loader.loadModel("model/fence.egg")
        self.ob3.reparentTo(render)
        self.ob3.setScale(.2, .2, .2)
        self.ob3.setPos(4.4, -17.1, 0)

        self.ob3 = loader.loadModel("model/fence.egg")
        self.ob3.reparentTo(render)
        self.ob3.setScale(.2, .2, .2)
        self.ob3.setPos(2, -17.1, 0)

        self.ob3 = loader.loadModel("model/fence.egg")
        self.ob3.reparentTo(render)
        self.ob3.setScale(.2, .2, .2)
        self.ob3.setPos(-.5, -17.1, 0)

        self.ob3 = loader.loadModel("model/fence.egg")
        self.ob3.reparentTo(render)
        self.ob3.setScale(.2, .2, .2)
        self.ob3.setPos(-3, -17.1, 0)

        self.ob3 = loader.loadModel("model/fence.egg")
        self.ob3.reparentTo(render)
        self.ob3.setScale(.2, .2, .2)
        self.ob3.setPos(-4.5, -17.1, 0)

        self.ob4 = loader.loadModel("model/Ground2/Ground2.egg")
        self.ob4.reparentTo(render)
        self.ob4.setScale(.01, .01, .01)
        self.ob4.setPos(0, -11.40, 0)

        self.ob5 = loader.loadModel("model/GroomedTree/GroomedTree.egg")
        self.ob5.reparentTo(render)
        self.ob5.setScale(.5, .5, .5)
        self.ob5.setPos(0, 0, 0)

        self.ob5 = loader.loadModel("model/GroomedTree/GroomedTree.egg")
        self.ob5.reparentTo(render)
        self.ob5.setScale(.5, .5, .5)
        self.ob5.setPos(5, 0, 0)

        self.ob5 = loader.loadModel("model/GroomedTree/GroomedTree.egg")
        self.ob5.reparentTo(render)
        self.ob5.setScale(.5, .5, .5)
        self.ob5.setPos(-5, 0, 0)

        self.ob5 = loader.loadModel("model/GroomedTree/GroomedTree.egg")
        self.ob5.reparentTo(render)
        self.ob5.setScale(.5, .5, .5)
        self.ob5.setPos(0, -5, 0)

        self.ob5 = loader.loadModel("model/GroomedTree/GroomedTree.egg")
        self.ob5.reparentTo(render)
        self.ob5.setScale(.5, .5, .5)
        self.ob5.setPos(0, -12, 0)

        self.ob5 = loader.loadModel("model/GroomedTree/GroomedTree.egg")
        self.ob5.reparentTo(render)
        self.ob5.setScale(.5, .5, .5)
        self.ob5.setPos(0, -18, 0)

        self.ob5 = loader.loadModel("model/HappyTree/HappyTree.egg")
        self.ob5.reparentTo(render)
        self.ob5.setScale(.02, .02, .02)
        self.ob5.setPos(0, -8,2.45)


        self.ob5 = loader.loadModel("model/GroomedTree/GroomedTree.egg")
        self.ob5.reparentTo(render)
        self.ob5.setScale(.5, .5, .5)
        self.ob5.setPos(5, 5, 0)

        self.ob5 = loader.loadModel("model/GroomedTree/GroomedTree.egg")
        self.ob5.reparentTo(render)
        self.ob5.setScale(.5, .5, .5)
        self.ob5.setPos(5, -5, 0)

        self.ob5 = loader.loadModel("model/GroomedTree/GroomedTree.egg")
        self.ob5.reparentTo(render)
        self.ob5.setScale(.5, .5, .5)
        self.ob5.setPos(5, -10, 0)

        self.ob5 = loader.loadModel("model/GroomedTree/GroomedTree.egg")
        self.ob5.reparentTo(render)
        self.ob5.setScale(.5, .5, .5)
        self.ob5.setPos(5, -15, 0)

        self.ob5 = loader.loadModel("model/GroomedTree/GroomedTree.egg")
        self.ob5.reparentTo(render)
        self.ob5.setScale(.5, .5, .5)
        self.ob5.setPos(5, 0, 0)
####################.5..5
        self.ob5 = loader.loadModel("model/GroomedTree/GroomedTree.egg")
        self.ob5.reparentTo(render)
        self.ob5.setScale(.5, .5, .5)
        self.ob5.setPos(3, 2.5, 0)

        self.ob5 = loader.loadModel("model/GroomedTree/GroomedTree.egg")
        self.ob5.reparentTo(render)
        self.ob5.setScale(.5, .5, .5)
        self.ob5.setPos(3, -2.5, 0)

        self.ob5 = loader.loadModel("model/GroomedTree/GroomedTree.egg")
        self.ob5.reparentTo(render)
        self.ob5.setScale(.5, .5, .5)
        self.ob5.setPos(3, -6.5, 0)

        self.ob5 = loader.loadModel("model/GroomedTree/GroomedTree.egg")
        self.ob5.reparentTo(render)
        self.ob5.setScale(.5, .5, .5)
        self.ob5.setPos(3, -10.5, 0)


        ##

        self.ob5 = loader.loadModel("model/GroomedTree/GroomedTree.egg")
        self.ob5.reparentTo(render)
        self.ob5.setScale(.5, .5, .5)
        self.ob5.setPos(-3, 2.5, 0)

        self.ob5 = loader.loadModel("model/GroomedTree/GroomedTree.egg")
        self.ob5.reparentTo(render)
        self.ob5.setScale(.5, .5, .5)
        self.ob5.setPos(-3, -2.5, 0)

        self.ob5 = loader.loadModel("model/GroomedTree/GroomedTree.egg")
        self.ob5.reparentTo(render)
        self.ob5.setScale(.5, .5, .5)
        self.ob5.setPos(-3, -6.5, 0)

        self.ob5 = loader.loadModel("model/GroomedTree/GroomedTree.egg")
        self.ob5.reparentTo(render)
        self.ob5.setScale(.5, .5, .5)
        self.ob5.setPos(-3, -10.5, 0)

#######################3
        self.ob5 = loader.loadModel("model/GroomedTree/GroomedTree.egg")
        self.ob5.reparentTo(render)
        self.ob5.setScale(.5, .5, .5)
        self.ob5.setPos(-5, 5, 0)

        self.ob5 = loader.loadModel("model/GroomedTree/GroomedTree.egg")
        self.ob5.reparentTo(render)
        self.ob5.setScale(.5, .5, .5)
        self.ob5.setPos(-5, -5, 0)

        self.ob5 = loader.loadModel("model/GroomedTree/GroomedTree.egg")
        self.ob5.reparentTo(render)
        self.ob5.setScale(.5, .5, .5)
        self.ob5.setPos(-5, -10, 0)

        self.ob5 = loader.loadModel("model/GroomedTree/GroomedTree.egg")
        self.ob5.reparentTo(render)
        self.ob5.setScale(.5, .5, .5)
        self.ob5.setPos(-5, -15, 0)

        # self.tex=loader.loadTexture("model/2.png")
        #self.cyl.setTexture(self.tex,1)
        #################boy###########3333

        self.ob7 = loader.loadModel("model/boy/boy.egg")
        self.ob7.reparentTo(base.camera)
        self.ob7.setScale(.07, .07, .07)
        self.ob7.setPos(0, 2, -1)
        self.tex=loader.loadTexture("model/2.png")
        self.ob7.setTexture(self.tex,1)

        #############################33
        self.ob6 = loader.loadModel("model/Pterodactyl/Pterodactyl.egg")
        self.ob6.reparentTo(render)
        self.ob6.setScale(3, 3, 3)
        self.ob6.setPos(0, 0, 7)
        self.ob6.setHpr(0, 0, 0)
        ##############################skeleton###
        self.ob8 = loader.loadModel("model/skeleton.egg")
        self.ob8.reparentTo(self.ob6)
        self.ob8.setScale(.08, .08, .08)
        self.ob8.setColor(.2,.6,.6,.5)
        self.ob8.setPos(0, 0,0)
        self.ob8.setHpr(0, 90, 180)

        Hprval = self.ob6.hprInterval(3, Point3(0, 0, 0), startHpr=Point3(0, 0, 0))

        val1 = self.ob6.posInterval(13, Point3(10, -15, 7), startPos=Point3(10, -15, 0))
        val2 = self.ob6.posInterval(13,Point3(10, 15, 7),startPos=Point3(10, -15, 7))

        Hprval1 = self.ob6.hprInterval(3,Point3(90, 0, 0),startHpr=Point3(0, 0,-45))
        val3 = self.ob6.posInterval(13, Point3(-10, 15, 7), startPos=Point3(10, 15, 7))
        Hprval2 = self.ob6.hprInterval(3, Point3(180, 0, 0), startHpr=Point3(90, 0, -45))
        val4 = self.ob6.posInterval(13, Point3(-10, -25, 7), startPos=Point3(-10, 15, 7))
        Hprval3 = self.ob6.hprInterval(3, Point3(270, 0, 0), startHpr=Point3(90, 0, -45))
        val5 = self.ob6.posInterval(13, Point3(10, -15, 0), startPos=Point3(-10, -25, 7))

        # Create and play the sequence that coordinates the intervals.
        self.spin = Sequence(Hprval,val1,val2,Hprval1,val3,Hprval2,val4,Hprval3,val5,name="pter")
        self.spin.loop()
#################key ##########
        self.keyMap = {
            "w": False
            , "s": False
            , "a": False,
            "d": False
            , "o": False
            , "c": False
            , "r": False
            , "t": False
        }
        self.accept("w", self.setkey, ["w", True])
        self.accept("s", self.setkey, ["s", True])
        self.accept("a", self.setkey, ["a", True])
        self.accept("d", self.setkey, ["d", True])
        self.accept("o", self.setkey, ["o", True])
        self.accept("c", self.setkey, ["c", True])
        self.accept("r", self.setkey, ["r", True])
        self.accept("t", self.setkey, ["t", True])

        self.accept("w-up", self.setkey, ["w", False])
        self.accept("s-up", self.setkey, ["s", False])
        self.accept("a-up", self.setkey, ["a", False])
        self.accept("d-up", self.setkey, ["d", False])
        self.accept("o-up", self.setkey, ["o", False])
        self.accept("c-up", self.setkey, ["c", False])
        self.accept("r-up", self.setkey, ["r", False])
        self.accept("t-up", self.setkey, ["t", False])
        taskMgr.add(self.cycleControl, "Cycle Control")
        self.an=10
        self.angledegrees =0
        base.camera.setH(1)
############camera control###################
    def cycleControl(self, task):
        dt = globalClock.getDt()


        if (dt > .20):
         return task.cont
        if (self.keyMap["w"] == True):

            base.camera.setY( base.camera, 15 * dt)
        elif (self.keyMap["s"] == True):

            base.camera.setY(base.camera, -15 * dt)

        elif (self.keyMap["a"] == True):

            base.camera.setH(base.camera.getH() + dt+1)
        elif (self.keyMap["d"] == True):

            base.camera.setH(base.camera.getH() + dt+-1)
        elif (self.keyMap["o"] == True):
            ob2
            self.backgroundImage("model/6.jpg")
            self.ob1.setPos(0,6,3)
        elif (self.keyMap["c"] == True):

            self.ob1.setPos(0,6,0)

        return task.cont

##############################
    def SpinCameraTask(self , task):
        angledegrees = task.time * 25.0
        angleradians = angledegrees * (math.pi / 180.0)
        base.camera.setPos(20 * math.sin(angleradians), -20.0 * math.cos(angleradians), 5)
        base.camera.setHpr(angledegrees,0, 0)
        return Task.cont

    def setkey(self, key, value):
        self.keyMap[key] = value

    def backgroundImage(self,image):
        bgTexture = loader.loadTexture(image)  # Load the background texture

        # Make a texture stage for the screen contents and set it to a decal overlay mode
        screenStage = TextureStage('screen')
        screenStage.setMode(TextureStage.MDecal)

        # Make a textre for the screen and a buffer to pipe the screen content into
        screenTexture = Texture()
        buffer = base.win.makeTextureBuffer("screen buffer", base.win.getXSize(), base.win.getYSize(), screenTexture, True)
        bufferCam = base.makeCamera(buffer, lens=base.cam.node().getLens())

        # Create a card in render2d to cover up render. Multitexture the card with the BG texture and the screen content texture
        cm = CardMaker('screencard')
        cm.setFrameFullscreenQuad()
        cm.setHasUvs(True)
        screenCard = render2d.attachNewNode(cm.generate())
        screenCard.setTexture(bgTexture)
        screenCard.setTexture(screenStage, screenTexture)

w=world()

#taskMgr.add(w.SpinCameraTask, "SpinCameraTask")
run()

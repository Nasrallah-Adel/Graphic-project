import direct.directbase.DirectStart
from direct.directbase.DirectStart import base
from direct.task import Task
import math
from direct.interval.IntervalGlobal import Sequence
from panda3d.core import Point3

from panda3d.core import CollisionTraverser,CollisionNode,CollisionSphere
from pandac.PandaModules import Texture, TextureStage, CardMaker
from direct.showbase.DirectObject import DirectObject

mySound1 = base.loader.loadSfx("happ.ogg")

class world (DirectObject):
    def __init__(self):
        mySound1.play()
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

        self.ob15 = loader.loadModel("model/GroomedTree/GroomedTree.egg")
        self.ob15.reparentTo(render)
        self.ob15.setScale(.5, .5, .5)
        self.ob15.setPos(0, 0, 0)

        self.ob25 = loader.loadModel("model/GroomedTree/GroomedTree.egg")
        self.ob25.reparentTo(render)
        self.ob25.setScale(.5, .5, .5)
        self.ob25.setPos(5, 0, 0)

        self.ob35 = loader.loadModel("model/GroomedTree/GroomedTree.egg")
        self.ob35.reparentTo(render)
        self.ob35.setScale(.5, .5, .5)
        self.ob35.setPos(-5, 0, 0)

        self.ob45 = loader.loadModel("model/GroomedTree/GroomedTree.egg")
        self.ob45.reparentTo(render)
        self.ob45.setScale(.5, .5, .5)
        self.ob45.setPos(0, -5, 0)

        self.ob55 = loader.loadModel("model/GroomedTree/GroomedTree.egg")
        self.ob55.reparentTo(render)
        self.ob55.setScale(.5, .5, .5)
        self.ob55.setPos(0, -12, 0)

        self.ob65 = loader.loadModel("model/GroomedTree/GroomedTree.egg")
        self.ob65.reparentTo(render)
        self.ob65.setScale(.5, .5, .5)
        self.ob65.setPos(0, -18, 0)

        self.ob75 = loader.loadModel("model/HappyTree/HappyTree.egg")
        self.ob75.reparentTo(render)
        self.ob75.setScale(.02, .02, .02)
        self.ob75.setPos(0, -8,2.45)


        self.ob85 = loader.loadModel("model/GroomedTree/GroomedTree.egg")
        self.ob85.reparentTo(render)
        self.ob85.setScale(.5, .5, .5)
        self.ob85.setPos(5, 5, 0)

        self.ob95 = loader.loadModel("model/GroomedTree/GroomedTree.egg")
        self.ob95.reparentTo(render)
        self.ob95.setScale(.5, .5, .5)
        self.ob95.setPos(5, -5, 0)

        self.ob51 = loader.loadModel("model/GroomedTree/GroomedTree.egg")
        self.ob51.reparentTo(render)
        self.ob51.setScale(.5, .5, .5)
        self.ob51.setPos(5, -10, 0)

        self.ob52 = loader.loadModel("model/GroomedTree/GroomedTree.egg")
        self.ob52.reparentTo(render)
        self.ob52.setScale(.5, .5, .5)
        self.ob52.setPos(5, -15, 0)

        self.ob53 = loader.loadModel("model/GroomedTree/GroomedTree.egg")
        self.ob53.reparentTo(render)
        self.ob53.setScale(.5, .5, .5)
        self.ob53.setPos(5, 0, 0)
####################.5..5
        self.ob54 = loader.loadModel("model/GroomedTree/GroomedTree.egg")
        self.ob54.reparentTo(render)
        self.ob54.setScale(.5, .5, .5)
        self.ob54.setPos(3, 2.5, 0)

        self.ob55 = loader.loadModel("model/GroomedTree/GroomedTree.egg")
        self.ob55.reparentTo(render)
        self.ob55.setScale(.5, .5, .5)
        self.ob55.setPos(3, -2.5, 0)

        self.ob56 = loader.loadModel("model/GroomedTree/GroomedTree.egg")
        self.ob56.reparentTo(render)
        self.ob56.setScale(.5, .5, .5)
        self.ob56.setPos(3, -6.5, 0)

        self.ob57 = loader.loadModel("model/GroomedTree/GroomedTree.egg")
        self.ob57.reparentTo(render)
        self.ob57.setScale(.5, .5, .5)
        self.ob57.setPos(3, -10.5, 0)


        ##

        self.ob58 = loader.loadModel("model/GroomedTree/GroomedTree.egg")
        self.ob58.reparentTo(render)
        self.ob58.setScale(.5, .5, .5)
        self.ob58.setPos(-3, 2.5, 0)

        self.ob59 = loader.loadModel("model/GroomedTree/GroomedTree.egg")
        self.ob59.reparentTo(render)
        self.ob59.setScale(.5, .5, .5)
        self.ob59.setPos(-3, -2.5, 0)

        self.ob510 = loader.loadModel("model/GroomedTree/GroomedTree.egg")
        self.ob510.reparentTo(render)
        self.ob510.setScale(.5, .5, .5)
        self.ob510.setPos(-3, -6.5, 0)

        self.ob511 = loader.loadModel("model/GroomedTree/GroomedTree.egg")
        self.ob511.reparentTo(render)
        self.ob511.setScale(.5, .5, .5)
        self.ob511.setPos(-3, -10.5, 0)

#######################3
        self.ob512 = loader.loadModel("model/GroomedTree/GroomedTree.egg")
        self.ob512.reparentTo(render)
        self.ob512.setScale(.5, .5, .5)
        self.ob512.setPos(-5, 5, 0)

        self.ob513 = loader.loadModel("model/GroomedTree/GroomedTree.egg")
        self.ob513.reparentTo(render)
        self.ob513.setScale(.5, .5, .5)
        self.ob513.setPos(-5, -5, 0)

        self.ob514 = loader.loadModel("model/GroomedTree/GroomedTree.egg")
        self.ob514.reparentTo(render)
        self.ob514.setScale(.5, .5, .5)
        self.ob514.setPos(-5, -10, 0)

        self.ob515 = loader.loadModel("model/GroomedTree/GroomedTree.egg")
        self.ob515.reparentTo(render)
        self.ob515.setScale(.5, .5, .5)
        self.ob515.setPos(-5, -15, 0)


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
        self.a=False
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
        taskMgr.add(self.control, "Cycle Control")

        self.an=10
        self.angledegrees =0
        base.camera.setH(1)

        self.cameras = []
        self.activeCam = 0
        self.cameras = [base.cam, base.makeCamera(base.win)]
        self.cameras[1].node().getDisplayRegion(0).setActive(0)
        self.activeCam = 0
        self.cameras[0].setPos(0, -30, 6)
        self.cameras[1].setPos(30, 100, 20)
        self.cameras[1].lookAt(self.ob7)

        # second camera
        self.cameras1 = []
        self.activeCam1 = 0
        self.cameras1 = [base.cam, base.makeCamera(base.win)]
        self.cameras1[1].node().getDisplayRegion(0).setActive(0)
        self.activeCam1 = 0
        self.cameras1[0].setPos(0, -30, 6)
        self.cameras1[1].setPos(-80, 100, 20)
        self.cameras1[1].lookAt(self.ob2)
############camera control###################
    def toggleCam(self, task):
        if (self.keyMap["r"] == True):
            self.cameras[self.activeCam].node().getDisplayRegion(0).setActive(0)
            self.activeCam = not self.activeCam
            self.cameras[self.activeCam].node().getDisplayRegion(0).setActive(1)

        return task.again

    def toggleCam1(self, task):
        if (self.keyMap["t"] == True):
            self.cameras1[self.activeCam1].node().getDisplayRegion(0).setActive(0)
            self.activeCam1 = not self.activeCam1
            self.cameras1[self.activeCam1].node().getDisplayRegion(0).setActive(1)

        return task.again
    def control(self, task):

        dt = globalClock.getDt()
        if (self.keyMap["o"] == True):
            self.a = True
            mySound1.stop()
            mySound = base.loader.loadSfx("horr.ogg")
            mySound.play()
            self.ob6 = loader.loadModel("model/Pterodactyl/Pterodactyl.egg")
            self.ob6.reparentTo(render)
            self.ob6.setScale(3, 3, 3)
            self.ob6.setPos(0, 0, 7)
            self.ob6.setHpr(0, 0, 0)
            ##############################skeleton###
            self.ob8 = loader.loadModel("model/skeleton.egg")
            self.ob8.reparentTo(self.ob6)
            self.ob8.setScale(.08, .08, .08)
            self.ob8.setColor(.2, .6, .6, .5)
            self.ob8.setPos(0, 0, 0)
            self.ob8.setHpr(0, 90, 180)

            Hprval = self.ob6.hprInterval(3, Point3(0, 0, 0), startHpr=Point3(0, 0, 0))

            val1 = self.ob6.posInterval(13, Point3(10, -15, 7), startPos=Point3(10, -15, 0))
            val2 = self.ob6.posInterval(13, Point3(10, 15, 7), startPos=Point3(10, -15, 7))

            Hprval1 = self.ob6.hprInterval(3, Point3(90, 0, 0), startHpr=Point3(0, 0, -45))
            val3 = self.ob6.posInterval(13, Point3(-10, 15, 7), startPos=Point3(10, 15, 7))
            Hprval2 = self.ob6.hprInterval(3, Point3(180, 0, 0), startHpr=Point3(90, 0, -45))
            val4 = self.ob6.posInterval(13, Point3(-10, -25, 7), startPos=Point3(-10, 15, 7))
            Hprval3 = self.ob6.hprInterval(3, Point3(270, 0, 0), startHpr=Point3(90, 0, -45))
            val5 = self.ob6.posInterval(13, Point3(10, -15, 0), startPos=Point3(-10, -25, 7))

            # Create and play the sequence that coordinates the intervals.
            self.spin = Sequence(Hprval, val1, val2, Hprval1, val3, Hprval2, val4, Hprval3, val5, name="ptra")
            self.spin.loop()
#################3skull@########
            self.ob16 = loader.loadModel("model/Ghost/Ghost.egg")
            self.ob16.reparentTo(render)
            self.ob16.setScale(.003, .003, .003)
            self.ob16.setPos(0, 5, 0)

            self.ob26 = loader.loadModel("model/Ghost/Ghost.egg")
            self.ob26.reparentTo(render)
            self.ob26.setScale(.003, .003, .003)
            self.ob26.setPos(0, -5, 0)

            self.ob36 = loader.loadModel("model/Ghost/Ghost.egg")
            self.ob36.reparentTo(render)
            self.ob36.setScale(.003, .003, .003)
            self.ob36.setPos(5, 0, 0)

            self.ob46 = loader.loadModel("model/Ghost/Ghost.egg")
            self.ob46.reparentTo(render)
            self.ob46.setScale(.003, .003, .003)
            self.ob46.setPos(-5, 0, 0)
             ##################333
            Hprval = self.ob16.hprInterval(3, Point3(0, 0, 0), startHpr=Point3(0, 0, 0))

            valu1 = self.ob16.posInterval(13, Point3(5, 0, 1), startPos=Point3(5, -7, 1))
            valu2 = self.ob16.posInterval(13, Point3(-5, 0, 1), startPos=Point3(5, 0, 1))

            Hprvalue1 = self.ob16.hprInterval(3, Point3(180, 0, 0), startHpr=Point3(90, 0, 0))
            valu3 = self.ob16.posInterval(13, Point3(-5, -7, 1), startPos=Point3(-5, 0, 1))
            Hprvalue2 = self.ob16.hprInterval(3, Point3(180, 0, 0), startHpr=Point3(90, 0, 0))
            valu4 = self.ob16.posInterval(13, Point3(5, -7, 1), startPos=Point3(-5, -7, 1))
            Hprvalue3 = self.ob16.hprInterval(3, Point3(270, 0, 0), startHpr=Point3(90, 0, -45))
            self.spin = Sequence(Hprval, valu1, valu2, Hprvalue1, valu3, Hprvalue2, valu4, Hprvalue3, name="ptr")
            self.spin.loop()

            ##
            Hprval = self.ob26.hprInterval(3, Point3(0, 0, 0), startHpr=Point3(0, 0, 0))

            valu1 = self.ob26.posInterval(13, Point3(5, 0, 1), startPos=Point3(5, -7, 1))
            valu2 = self.ob26.posInterval(13, Point3(-5, 0, 1), startPos=Point3(5, 0, 1))

            Hprvalue1 = self.ob26.hprInterval(3, Point3(180, 0, 0), startHpr=Point3(90, 0, 0))
            valu3 = self.ob26.posInterval(13, Point3(-5, -7, 1), startPos=Point3(-5, 0, 1))
            Hprvalue2 = self.ob26.hprInterval(3, Point3(180, 0, 0), startHpr=Point3(90, 0, 0))
            valu4 = self.ob26.posInterval(13, Point3(5, -7, 1), startPos=Point3(-5, -7, 1))
            Hprvalue3 = self.ob26.hprInterval(3, Point3(270, 0, 0), startHpr=Point3(90, 0, -45))
            self.spin = Sequence(Hprval,valu4, valu1, valu2, Hprvalue1, valu3, Hprvalue2,  Hprvalue3, name="ptsr")
            self.spin.loop()
            ##
            Hprval = self.ob36.hprInterval(3, Point3(0, 0, 0), startHpr=Point3(0, 0, 0))

            valu1 = self.ob36.posInterval(13, Point3(5, 0, 1), startPos=Point3(5, -7, 1))
            valu2 = self.ob36.posInterval(13, Point3(-5, 0, 1), startPos=Point3(5, 0, 1))

            Hprvalue1 = self.ob36.hprInterval(3, Point3(180, 0, 0), startHpr=Point3(90, 0, 0))
            valu3 = self.ob36.posInterval(13, Point3(-5, -7, 1), startPos=Point3(-5, 0, 1))
            Hprvalue2 = self.ob36.hprInterval(3, Point3(180, 0, 0), startHpr=Point3(90, 0, 0))
            valu4 = self.ob36.posInterval(13, Point3(5, -7, 1), startPos=Point3(-5, -7, 1))
            Hprvalue3 = self.ob36.hprInterval(3, Point3(270, 0, 0), startHpr=Point3(90, 0, -45))
            self.spin = Sequence(Hprval, valu3, valu4, Hprvalue1, valu1, Hprvalue2, valu2, Hprvalue3, name="pr")
            self.spin.loop()

            ###

            Hprval = self.ob46.hprInterval(3, Point3(0, 0, 0), startHpr=Point3(0, 0, 0))

            valu1 = self.ob46.posInterval(13, Point3(5, 0, 1), startPos=Point3(5, -7, 1))
            valu2 = self.ob46.posInterval(13, Point3(-5, 0, 1), startPos=Point3(5, 0, 1))

            Hprvalue1 = self.ob46.hprInterval(3, Point3(180, 0, 0), startHpr=Point3(90, 0, 0))
            valu3 = self.ob46.posInterval(13, Point3(-5, -7, 1), startPos=Point3(-5, 0, 1))
            Hprvalue2 = self.ob46.hprInterval(3, Point3(180, 0, 0), startHpr=Point3(90, 0, 0))
            valu4 = self.ob46.posInterval(13, Point3(5, -7, 1), startPos=Point3(-5, -7, 1))
            Hprvalue3 = self.ob46.hprInterval(3, Point3(270, 0, 0), startHpr=Point3(90, 0, -45))
            self.spin = Sequence(Hprval, valu2, valu3, Hprvalue1, valu4, Hprvalue2, valu1, Hprvalue3, name="prcc")
            self.spin.loop()


        return task.cont
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
            self.tex=loader.loadTexture("model/7.jpg")
            self.ob2.setTexture(self.tex, 1)
            self.ob4.setTexture(self.tex, 1)
            self.ob15.setColor(.9, .01, .01, 2)
            self.ob25.setColor(.9, .01, .01, 2)
            self.ob35.setColor(.9, .01, .01, 2)
            self.ob45.setColor(.9, .01, .01, 2)
            self.ob55.setColor(.9, .01, .01, 2)
            self.ob65.setColor(.9, .01, .01, 2)
            self.ob75.setColor(.9, .01, .01, 2)
            self.ob85.setColor(.9, .01, .01, 2)
            self.ob95.setColor(.9, .01, .01, 2)
            self.ob51.setColor(.9, .01, .01, 2)
            self.ob52.setColor(.9, .01, .01, 2)
            self.ob53.setColor(.9, .01, .01, 2)
            self.ob54.setColor(.9, .01, .01, 2)
            self.ob55.setColor(.9, .01, .01, 2)
            self.ob56.setColor(.9, .01, .01, 2)
            self.ob57.setColor(.9, .01, .01, 2)
            self.ob58.setColor(.9, .01, .01, 2)
            self.ob59.setColor(.9, .01, .01, 2)
            self.ob510.setColor(.9, .01, .01, 2)
            self.ob511.setColor(.9, .01, .01, 2)
            self.ob512.setColor(.9, .01, .01, 2)
            self.ob513.setColor(.9, .01, .01, 2)
            self.ob514.setColor(.9, .01, .01, 2)
            self.ob515.setColor(.9, .1, .1, 2)



            self.backgroundImage("model/9.jpg")
            val1 = self.ob1.posInterval(13, Point3(0, 6, 3), startPos=Point3(0, 6, 0))
            self.spin = Sequence( val1, name="pter")
            self.spin.start()
            self.ob1.setPos(0,6,3)

            ##############################

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
taskMgr.add(w.toggleCam, "toggle camera")
taskMgr.add(w.toggleCam1, "toggle camera1")
#taskMgr.add(w.SpinCameraTask, "SpinCameraTask")
run()

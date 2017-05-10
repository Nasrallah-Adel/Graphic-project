import direct.directbase.DirectStart
from direct.task import Task
import math
class world:
    def __init__(self):
        base.setBackgroundColor(0,0,0)
        self.ob1 = loader.loadModel("model/gate/gate.egg")
        base.disableMouse()
        self.ob1.reparentTo(render)
        self.ob1.setScale(.003, .003, .003)
        self.ob1.setPos(0, 6,0)

        self.ob2 = loader.loadModel("model/Ground2/Ground2.egg")
        self.ob2.reparentTo(render)
        self.ob2.setScale(.01, .01, .01)
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


    def SpinCameraTask(self , task):
        angledegrees = task.time * 20.0
        angleradians = angledegrees * (math.pi / 180.0)
        base.camera.setPos(20 * math.sin(angleradians), -20.0 * math.cos(angleradians), 3)
        base.camera.setHpr(angledegrees,0, 0)
        return Task.cont

w=world()
taskMgr.add(w.SpinCameraTask, "SpinCameraTask")
run()

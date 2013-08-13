from math import pi, sin, cos
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor

class FliSim(ShowBase):

	#self.i = 0
	def __init__(self):
		ShowBase.__init__(self)
		self.setBackgroundColor(0, 0, 0)

		self.plane = self.loader.loadModel("./models/plane/boeing707")
		self.plane.setScale(0.07, 0.07, 0.07)
		self.plane.setPos(0, 7, 3.0)
		self.plane.reparentTo(self.render)

		self.environ = self.loader.loadModel("./models/sky/skysphere")
		self.i = -16
		self.environ.reparentTo(self.render)

		self.environ.setScale(0.038, 0.038, 0.038)
		self.environ.setPos(0, 0, 0)

		self.taskMgr.add(self.cameraTask, "cameraTask")

	def cameraTask(self, task):
		if(str(self.i) == str(-4.0)):
			self.i = -16

		self.i = self.i+0.1
		self.camera.setPos(0, self.i, 5)
		self.plane.setPos(0, self.i+12, 3.0)
		print(str(self.i))
		return Task.cont

sim = FliSim()
sim.run()
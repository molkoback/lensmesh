import trimesh

class LensParamException(Exception):
	pass

class Lens:
	def __init__(self, D, R1, R2, Tc, accuracy=6):
		if D <= 0.0 or Tc <= 0.0:
			raise LensParamException()
		self.D = D
		self.R1 = R1
		self.R2 = R2
		self.Tc = Tc
		self.accuracy = accuracy
		self.mesh = self._create()
	
	def _cylinder(self, radius, height):
		return trimesh.creation.cylinder(
			radius=radius,
			height=height,
			sections=4**self.accuracy
		)
	
	def _sphere(self, radius):
		return trimesh.creation.icosphere(
			subdivisions=self.accuracy,
			radius=radius
		)
	
	def _create(self):
		# Create lens base cylinder
		lens = self._cylinder(self.D/2, self.Tc)
		
		# Bottom side
		if self.R1 != 0.0 and self.R1 != float("inf"):
			sphere = self._sphere(abs(self.R1))
			if self.R1 > 0.0:
				sphere.apply_translation([0, 0, self.R1-self.Tc/2])
				lens = lens.intersection(sphere)
			else:
				sphere.apply_translation([0, 0, self.R1])
				lens = lens.difference(sphere)
		
		# Top side
		if self.R2 != 0.0 and self.R2 != float("inf"):
			sphere = self._sphere(abs(self.R2))
			if self.R2 < 0.0:
				sphere.apply_translation([0, 0, self.R2+self.Tc/2])
				lens = lens.intersection(sphere)
			else:
				sphere.apply_translation([0, 0, self.R2])
				lens = lens.difference(sphere)
		
		return lens
	
	def save(self, fn):
		self.mesh.export(fn)

class PlanoConvex(Lens):
	def __init__(self, D, R, Tc, **kwargs):
		if R < 0.0:
			raise LensParamException()
		super().__init__(D, R, 0.0, Tc, **kwargs)

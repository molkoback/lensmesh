import trimesh

class Lens:
	def __init__(self, accuracy=6):
		self.accuracy = accuracy
		self.mesh = None
	
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
	
	def save(self, fn):
		self.mesh.export(fn)

class PlanoConvex(Lens):
	def __init__(self, D, R, Tc, Te, **kwargs):
		super().__init__(**kwargs)
		
		self.D = D
		self.R = R
		self.Tc = Tc
		self.Te = Te
		
		self.mesh = self._create()
	
	def _create(self):
		# Create cylinder
		cylinder = self._cylinder(self.D/2, self.Te)
		
		# Create sphere slice
		sphere = self._sphere(self.R)
		sphere_slice = trimesh.intersections.slice_mesh_plane(
			sphere,
			[0, 0, -1],
			[0, 0, self.Tc - self.Te - self.R]
		)
		
		# Move the slice
		sphere_slice.apply_translation([0, 0, self.R - self.Te - self.Te])
		
		# Combine
		return (sphere_slice + cylinder).convex_hull

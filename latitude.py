import math

MERCURY_RADIUS = 2439.7 * 1000#meters
VENUS_RADIUS = 6051.8 * 1000#meters
EARTH_RADIUS = 6371 * 1000 #meters
MOON_RADIUS = 1738.1 * 1000#meters
MARS_RADIUS = 3396.2 * 1000#meters
CERES_RADIUS = 469.73 * 1000#meters
PLUTO_RADIUS = 1188.3 * 1000#meters
CHARON_RADIUS = 606.0 * 1000#meters

RADII = {
	"mercury" : 2439.7 * 1000.0,#meters
	"venus" : 6051.8 * 1000.0,#meters
	"earth" : 6371.0 * 1000.0,#meters
	"moon" : 1738.1 * 1000.0,#meters
	"mars" : 3396.2 * 1000.0,#meters
	"ceres" : 469.73 * 1000.0,#meters
	"pluto" : 1188.3 * 1000.0,#meters
	"charon" : 606.0 * 1000.0,#meters
	"vesta" : 525.4 * 1000.0#meters
}
#TODO make the interface consistent with the lenm thing
class Latitude:
	def __init__(self, planet, radius=0):
		self.eq_radius = RADII.get(planet,radius)
		self.planet = planet
		print("self.eq_radius: "+str(self.eq_radius))
		#print(self.eq_radius == 0)
		#if self.eq_radius == 0:
		#	raise Exception("Unknown planet: "+planet+". Try using the alternate constructor with radius parameter")
		self.eq_circumference = self.eq_radius * 2 * math.pi
		self.eq_arcsec = self.eq_circumference / 360 / 60 / 60

	'''
	def __init__(self, planet, radius):
		self.eq_radius = radius
		self.planet = planet
		self.eq_circumference = self.eq_radius * 2 * math.pi
		self.eq_arcsec = self.eq_circumference / 360 / 60 / 60
	'''

	def get_eq_circumference(self):
		return self.eq_circumference

	def get_eq_deg_lenm(self):
		return self.eq_circumference / 360

	def get_eq_arcmin_lenm(self):
		return self.eq_circumference / 360 / 60

	def get_eq_arcsec_lenm(self):
		return self.eq_arcsec

	def get_lat_deg(self, latang):
		radians = latang * math.pi / 180
		lat_radius = self.eq_radius * math.cos(radians)
		lat_circumference = lat_radius * 2 * math.pi
		return lat_circumference / 360

	def get_lat_arcmin(self, latang):
		radians = latang * math.pi / 180
		lat_radius = self.eq_radius * math.cos(radians)
		lat_circumference = lat_radius * 2 * math.pi
		return lat_circumference / 360 / 60

	def get_lat_arcsec(self, latang):
		radians = latang * math.pi / 180
		lat_radius = self.eq_radius * math.cos(radians)
		lat_circumference = lat_radius * 2 * math.pi
		return lat_circumference / 360 / 60 / 60

	def get_lat_scale_factor(self, latang):
		return self.get_lat_arcsec(latang) / self.eq_arcsec

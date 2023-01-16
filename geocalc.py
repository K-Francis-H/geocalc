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

class Position:
	def __init__(self, lat, lon, use_eq_arcsec=False):
		if (not isinstance(lat, float) and  not isinstance(lat, int)) or (not isinstance(lon, float) and not isinstance(lon, int)):
			raise Exception('Latitude and Longitude must be type float or int')
		if lat < -90.0 or lat > 90.0:
			raise Exception('Latitude must be on range [ -90.0, 90.0 ], provided lat is '+str(lat))
		if lon < -180.0 or lon > 180.0:
			raise Exception('Longitude must be on range [ -180.0, 180.0 ], provided lon is '+str(lon))
		self.lat = lat
		self.lon = lon
		self.arc_len = Latitude('earth')
		self.eq_arcsec = self.arc_len.get_eq_arcsec_lenm()
		self.use_eq_arcsec = use_eq_arcsec

	def go_north(self, distance, unit='m'):
		arcsec =  self.eq_arcsec
		distance = convert_unit_to_meters(distance,unit)
		self.lat = self.lat + (distance / arcsec / 60 / 60)

	def go_south(self, distance, unit='m'):
		arcsec =  self.eq_arcsec
		distance = convert_unit_to_meters(distance,unit)
		self.lat = self.lat - (distance / arcsec / 60 / 60)

	def go_east(self, distance, unit='m'):
		arcsec = self.eq_arcsec if(self.use_eq_arcsec) else self.arc_len.get_lat_arcsec(self.lat)
		distance = convert_unit_to_meters(distance,unit)
		self.lon = self.lon + (distance / arcsec / 60 / 60)

	def go_west(self, distance, unit='m'):
		arcsec = self.eq_arcsec if(self.use_eq_arcsec) else self.arc_len.get_lat_arcsec(self.lat)
		distance = convert_unit_to_meters(distance,unit)
		self.lon = self.lon + (distance / arcsec / 60 / 60)

	def get(self):
		return (self.lat, self.lon)

	@staticmethod
	def convert_unit_to_meters(q, unit):
		if unit == 'm':
			return q
		switch={
			'km': 1000,
			'mi': 1609.344,
			'nm': 1852.001  
		}
		return q*switch.get(unit)
	

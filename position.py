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
		self.arc_len = latitude.Latitude('earth')
		self.eq_arcsec = arc_len.get_eq_arcsec_lenm()

	def go_north(self, distance, unit='km'):
		arcsec =  self.eq_arcsec
		self.lat = self.lat + (distance / arcsec / 60 / 60)
		print('todo')

	def go_south(self, distance, unit='km'):
		arcsec =  self.eq_arcsec
		self.lat = self.lat - (distance / arcsec / 60 / 60)
		print('todo')

	def go_east(self, distance, unit='km'):
		arcsec = self.eq_arcsec if(use_eq_arcsec) else arc_len.get_lat_arcsec(lat)
		self.lon = self.lon + (distance / arcsec / 60 / 60)
		print('todo')

	def go_west(self, distance, unit='km'):
		arcsec = self.eq_arcsec if(use_eq_arcsec) else arc_len.get_lat_arcsec(lat)
		self.lon = self.lon + (distance / arcsec / 60 / 60)
		print('todo')

	def get(self):
		return (lat, lon)
	

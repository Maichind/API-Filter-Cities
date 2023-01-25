class CitiesModel:
    def __init__(self, id, name, ascii, alt_name, lat, long, feat_class, feat_code, country, cc2, admin1, admin2, admin3, admin4, 
                population, elevation, dem, tz, modified_at):
        self.id = id
        self.name = name
        self.ascii = ascii
        self.alt_name = alt_name
        self.lat = lat
        self.long = long
        self.feat_class = feat_class
        self.feat_code = feat_code
        self.country = country
        self.cc2 = cc2
        self.admin1 = admin1
        self.admin2 = admin2
        self.admin3 = admin3
        self.admin4 = admin4
        self.population = population
        self.elevation = elevation
        self.dem = dem
        self.tz = tz
        self.modified_at = modified_at    

    def toDB(self):
        return {
            "id": self.id,
            "name": self.name,
            "ascii": self.ascii,
            "alt_name": self.alt_name,
            "lat": self.lat,
            "long": self.long,
            "feat_class": self.feat_class,
            "feat_code": self.feat_code,
            "country": self.country,
            "cc2": self.cc2,
            "admin1": self.admin1,
            "admin2": self.admin2,
            "admin3": self.admin3,
            "admin4": self.admin4,
            "population": self.population,
            "elevation": self.country,
            "dem": self.dem,
            "tz": self.tz,
            "modified_at": self.modified_at
        }

import swisseph as swe
from astro.geoname import search
import pytz, datetime, math

swe.set_ephe_path("ephe")


class Calculator:
    def __init__(self, name, year, month, day, hours, minutes, city, nat=""):
        self.name = name
        self.year = year
        self.month = month
        self.day = day
        self.hours = hours
        self.minutes = minutes
        self.city = city
        self.nation = nat

        self.j_day = self.get_jd()
        self.city_long = self.get_city_data()[1]
        self.city_lat = self.get_city_data()[2]

    def get_city_data(self):
        city_data = search(self.city, self.nation)[0]

        city_long = float(city_data["lng"])
        city_lat = float(city_data["lat"])
        time_zone = city_data["timezonestr"]
        # self.country_code = city_data["countryCode"]

        return time_zone, city_long, city_lat

    def get_utc(self):
        time_zone = self.get_city_data()[0]
        local_time = pytz.timezone(time_zone)
        input_datetime = datetime.datetime(self.year, self.month,
                                           self.day, self.hours, self.minutes, 0)
        local_datetime = local_time.localize(input_datetime, is_dst=None)
        utc_datetime = local_datetime.astimezone(pytz.utc)

        return utc_datetime

    def get_jd(self):
        """ Calculates julian day from the utc time."""
        utc = self.get_utc()
        time_utc = utc.hour + utc.minute / 60
        j_day = float(swe.julday(utc.year, utc.month, utc.day,
                                 time_utc))

        return j_day

    def __repr__(self):
        return f"Astrological data for: {self.name}, {self.utc} UTC"

    def transform_minutes(self, position):
        minutes = divmod(position * 3600, 60)[0]
        deg, minutes = divmod(minutes, 60)
        if minutes < 10:
            minutes /= 10
        if minutes >= 10:
            minutes /= 100
        return deg + minutes

    def calculate_position(self, degree):
        if degree < 30:
            degree = self.transform_minutes(degree)
            return {"sign": "Ari", "pos": degree, "abs_pos": degree}
        elif degree < 60:
            calculated_degree = self.transform_minutes(degree - 30)
            return {"sign": "Tau", "pos": calculated_degree, "abs_pos": degree}
        elif degree < 90:
            calculated_degree = self.transform_minutes(degree - 60)
            return {"sign": "Gem", "pos": calculated_degree, "abs_pos": degree}
        elif degree < 120:
            calculated_degree = self.transform_minutes(degree - 90)
            return {"sign": "Can", "pos": calculated_degree, "abs_pos": degree}
        elif degree < 150:
            calculated_degree = self.transform_minutes(degree - 120)
            return {"sign": "Leo", "pos": calculated_degree, "abs_pos": degree}
        elif degree < 180:
            calculated_degree = self.transform_minutes(degree - 150)
            return {"sign": "Vir", "pos": calculated_degree, "abs_pos": degree}
        elif degree < 210:
            calculated_degree = self.transform_minutes(degree - 180)
            return {"sign": "Lib", "pos": calculated_degree, "abs_pos": degree}
        elif degree < 240:
            calculated_degree = self.transform_minutes(degree - 210)
            return {"sign": "Sco", "pos": calculated_degree, "abs_pos": degree}
        elif degree < 270:
            calculated_degree = self.transform_minutes(degree - 240)
            return {"sign": "Sag", "pos": calculated_degree, "abs_pos": degree}
        elif degree < 300:
            calculated_degree = self.transform_minutes(degree - 270)
            return {"sign": "Cap", "pos": calculated_degree, "abs_pos": degree}
        elif degree < 330:
            calculated_degree = self.transform_minutes(degree - 300)
            return {"sign": "Aqu", "pos": calculated_degree, "abs_pos": degree}
        elif degree < 360:
            calculated_degree = self.transform_minutes(degree - 330)
            return {"sign": "Pis", "pos": calculated_degree, "abs_pos": degree}

    def calculate_houses(self):
        houses_data = swe.houses(self.j_day, self.city_lat,
                                 self.city_long)
        houses_list = []
        houses_degree_ut = houses_data[0]
        for i in range(12):
            house = self.calculate_position(houses_degree_ut[i])
            houses_list.append(house)
        return houses_list

    def calculate_planets_degree(self):
        planets_degrees = []
        for i in range(11):
            planet_degree = swe.calc(self.j_day, i)[0][0]
            planets_degrees.append(planet_degree)

        chiron_deg = swe.calc(self.j_day, 15)[0][0]
        # planets_degrees[10] = North node
        south_node_deg = planets_degrees[10] - 180
        ascmc = swe.houses(self.j_day, self.city_lat,
                           self.city_long)[1]
        vertex_deg = ascmc[3]
        sunmooon_deg = (planets_degrees[0] + planets_degrees[1]) / 2

        if abs(planets_degrees[0] - sunmooon_deg) > 90:
            sunmooon_deg = sunmooon_deg - 180
        planets_degrees.extend([chiron_deg, south_node_deg, vertex_deg, sunmooon_deg])

        return planets_degrees

    def calculate_planets_positions(self):
        planets_names = ["Sun", "Moon", "Mercury", "Venus", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto",
                         "North Node", "Chiron", "South Nod", "Vertex", "Sun/Moon"]

        planets_degs = self.calculate_planets_degree()
        planet_positions_list = []
        for i in range(len(planets_degs)):
            planet_position = self.calculate_position(planets_degs[i])
            planet_positions_list.append(planet_position)

        return planet_positions_list

    def for_every_planet(self, houses_list, deg_planet):
        def point_between(lower_limit, upper_limit, comparable):
            p1 = lower_limit.get("abs_pos")
            p2 = upper_limit.get("abs_pos")
            p3 = comparable.get("abs_pos")
            """Finds if a point is between two other in a circle
            args: first point, second point, point in the middle"""
            p1_p2 = math.fmod(p2 - p1 + 360, 360)
            p1_p3 = math.fmod(p3 - p1 + 360, 360)
            if (p1_p2 <= 180) != (p1_p3 > p1_p2):
                return True
            else:
                return False

        if point_between(houses_list[0], houses_list[1],
                         deg_planet):
            return "1st House"
        elif point_between(houses_list[1], houses_list[2],
                           deg_planet):
            return "2nd House"
        elif point_between(houses_list[2], houses_list[3],
                           deg_planet):
            return "3rd House"
        elif point_between(houses_list[3], houses_list[4],
                           deg_planet):
            return "4th House"
        elif point_between(houses_list[4], houses_list[5],
                           deg_planet):
            return "5th House"
        elif point_between(houses_list[5], houses_list[6],
                           deg_planet):
            return "6th House"
        elif point_between(houses_list[6], houses_list[7],
                           deg_planet):
            return "7th House"
        elif point_between(houses_list[7], houses_list[8],
                           deg_planet):
            return "8th House"
        elif point_between(houses_list[8], houses_list[9],
                           deg_planet):
            return "9th House"
        elif point_between(houses_list[9], houses_list[10],
                           deg_planet):
            return "10th House"
        elif point_between(houses_list[10], houses_list[11],
                           deg_planet):
            return "11th House"
        elif point_between(houses_list[11], houses_list[0],
                           deg_planet):
            return "12th House"

    def calculate_houses_for_planets(self, planets_positions, houses_list):
        houses_for_planets = []
        for i in range(len(planets_positions)):
            house = self.for_every_planet(houses_list, planets_positions[i])
            houses_for_planets.append(house)

        return houses_for_planets

    def get_all(self):
        self.calculate_houses_for_planets()

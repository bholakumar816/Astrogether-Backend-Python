# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import timeit

from astro.natal_chart import Calculator
import swisseph as swe
from astro.aspect_values import aspects_points

user1 = Calculator("Dani", 1991, 12, 17, 14, 26, "Sofia", "BG")
user2 = Calculator("Tsveti", 1991, 8, 13, 14, 00, "Krumovgrad", "BG")

user11 = Calculator("Bori", 1991, 12, 17, 16, 43, "Krumovgrad", "BG")
user21 = Calculator("Georgi", 1990, 1, 9, 23, 45, "Sofia", "BG")

def print_2(*args):
    print(args)

class UserSynastry:
    planets_names = ["Sun", "Moon", "Mercury", "Venus", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto",
                     "North Node", "Chiron", "South Node", "Vertex", "Sun/Moon", "1", "4", "7", "10"]

    def __init__(self, user: Calculator):
        self.user = user
        self.planets = user.calculate_planets_positions()
        self.houses = user.calculate_houses()
        self.planets_and_houses = self.planets + [self.houses[0], self.houses[3], self.houses[6], self.houses[9]]

    def calculate_synastry_with_user(self, other_user):
        planets1_houses2 = user1.calculate_houses_for_planets(self.planets, other_user.houses)
        planets2_houses1 = user2.calculate_houses_for_planets(other_user.planets, self.houses)
        asc_1_2 = self.user.calculate_houses_for_planets([self.houses[0]], other_user.houses)
        asc_2_1 = self.user.calculate_houses_for_planets([other_user.houses[0]], self.houses)

        return self.calculate_synastry(planets1_houses2, planets2_houses1, asc_1_2, asc_2_1, self.planets_and_houses,
                                       other_user.planets_and_houses)

    def calculate_synastry(self, planets1_houses2, planets2_houses1, asc_1_2, asc_2_1, planets_and_houses1,
                           planets_and_houses2):
        try:
            length = len(self.planets_and_houses)
            total = 0
            points_list = []
            for index_user1 in range(length):
                for index_user2 in range(length):
                    (current_total, current_points_list) = self.calculate_result_for_indices(
                        index_user1, index_user2,
                        planets_and_houses1,
                        planets_and_houses2)
                    total += current_total
                    points_list += current_points_list
            if '7th House' in (planets1_houses2[0], planets2_houses1[0]):
                points_list.append(4)
                total += 4
            if '1st House' in (planets1_houses2[0], planets2_houses1[0]):
                points_list.append(3)
                total += 3
            if planets1_houses2[1] == "1st House" or planets2_houses1[1] == "1st House":
                points_list.append(3)
                total += 3
            if planets1_houses2[1] == "7th House" or planets2_houses1[1] == "7th House":
                points_list.append(3)
                total += 3
            if planets1_houses2[3] == "1st House" or planets2_houses1[3] == "1st House":
                points_list.append(2)
                total += 2
            if planets1_houses2[3] == "7th House" or planets2_houses1[3] == "7th House":
                points_list.append(3)
                total += 3
            if planets1_houses2[5] == "7th House" or planets2_houses1[5] == "7th House":
                points_list.append(2)
                total += 2
            if asc_1_2[0] == "7th House" or asc_2_1[0] == "7th House":
                points_list.append(3)
                total += 3

            indices2 = len([i for i, x in enumerate(points_list) if x == 2])
            indices_minus2 = len([i for i, x in enumerate(points_list) if x == -2])
            indices3 = len([i for i, x in enumerate(points_list) if x == 3])
            indices_minus3 = len([i for i, x in enumerate(points_list) if x == -3])
            indices4 = len([i for i, x in enumerate(points_list) if x == 4])
            indices_minus4 = len([i for i, x in enumerate(points_list) if x == -4])
            indices5 = len([i for i, x in enumerate(points_list) if x == 5])
            is_match = False
            if (indices4 >= 1 or indices5 >= 1) and ((indices3 + indices4 + indices5) >= 5) \
                    and indices_minus4 == 0 \
                    and indices_minus3 <= 3 \
                    and 3 <= indices_minus2 <= 7:
                is_match = True

            is_soulmate = is_match and indices5 >= 1
            return {
                    "status" : 200,
                    "message": "Compared successfully !",
                    "data" : {
                        "Total": total,
                        "Match" : is_match,
                        "Soulmate" : is_soulmate
                    }
                }
        except Exception as e:
            return {
                "status" : 400,
                "message": str(ex)
            }

    def calculate_result_for_indices(self, index_user1, index_user2, planets_and_houses1, planets_and_houses2):
        total = 0
        points_list = []
        aspect_name = self.calculate_aspect(index_user1, index_user2, planets_and_houses1, planets_and_houses2)
        if aspect_name:
            planet_name1 = self.planets_names[index_user1]
            planet_name2 = self.planets_names[index_user2]

            planets_relation = f"{planet_name1}-{planet_name2}"
            if planets_relation in aspects_points and \
                    aspect_name in aspects_points[planets_relation]:
                planet_category = aspects_points[planets_relation]
                points = planet_category[aspect_name]
                total += points
                # print_2("\n",
                #       self.planets_names[index_user1],
                #       aspect_name, self.planets_names[index_user2], points)

                points_list.append(points)
            reverse_planet_category = None
            if planet_name1 is not planet_name2:
                reverse_planets_relation = f"{planet_name2}-{planet_name1}"
                reverse_planet_category = aspects_points.get(reverse_planets_relation)

            if reverse_planet_category is not None and planet_name1 is not planet_name2:
                points = reverse_planet_category.get(aspect_name)
                if points is not None:
                    total += points
                    points_list.append(points)
                    # print_2("\n",
                    #       self.planets_names[index_user1],
                    #       aspect_name, self.planets_names[index_user2], points)
            return (total, points_list)
        return (0, [])

    def calculate_aspect(self, index_user1, index_user2, planets_and_houses1, planets_and_houses2):
        distance = abs(swe.difdeg2n(planets_and_houses1[index_user1]["abs_pos"],
                                    planets_and_houses2[index_user2]["abs_pos"]))
        if index_user1 == 4 and index_user2 == 4:
            pass
        if distance <= 10:
            return "Conjunction"
        elif 172 <= distance <= 188:
            return "Opposition"
        elif 84 <= int(distance) <= 96:
            return "Square"
        elif 114 <= int(distance) <= 126:
            return "Trine"
        elif 55 <= int(distance) <= 65:
            return "Sextile"
        elif 29 <= int(distance) <= 31:
            return "Semi-sextile"
        elif 44 <= int(distance) <= 46:
            return "Semi-square"
        elif 133.5 <= int(distance) <= 136.5:
            return "Sesqui-square"
        elif 148 <= int(distance) <= 152:
            return "Quincunx"
        elif 71 <= int(distance) <= 73:
            return "Quintile"
        elif 143 <= int(distance) <= 145:
            return "Bi-quintile"
        else:
            return None


class Synastry:
    def __init__(self, user1, user2):
        planets_user1 = user1.calculate_planets_positions()
        houses_user1 = user1.calculate_houses()
        planets_user2 = user2.calculate_planets_positions()
        houses_user2 = user2.calculate_houses()
        self.pl_ho_info1 = planets_user1 + [houses_user1[0]] + [houses_user1[3]] + [houses_user1[6]] + [houses_user1[9]]
        self.pl_ho_info2 = planets_user2 + [houses_user2[0]] + [houses_user2[3]] + [houses_user2[6]] + \
                           [houses_user2[9]]

        self.planets1_houses2 = user1.calculate_houses_for_planets(planets_user1, houses_user2)
        self.planets2_houses1 = user2.calculate_houses_for_planets(planets_user2, houses_user1)
        self.asc_2_1 = user1.calculate_houses_for_planets([houses_user2[0]], houses_user1)
        self.asc_1_2 = user1.calculate_houses_for_planets([houses_user1[0]], houses_user2)


def getUserSynastry(name, year, month, day, hours, minutes, city, nat=""):
    user = Calculator(name, year, month, day, hours, minutes, city, nat)
    return UserSynastry(user)

def compareUsers(user1,user2):
    try:
        name1 = user1.get('name','') 
        year1 = user1.get('year') 
        month1 = user1.get('month') 
        day1 = user1.get('day') 
        hours1 = user1.get('hours') 
        minutes1 = user1.get('minutes') 
        city1 = user1.get('city','') 
        nat1 = user1.get('country_code','')
        user1 = Calculator(name1, year1, month1, day1, hours1, minutes1, city1, nat1)
        userSynastry1 = UserSynastry(user1)

        name2 = user2.get('name','') 
        year2 = user2.get('year') 
        month2 = user2.get('month') 
        day2 = user2.get('day') 
        hours2 = user2.get('hours') 
        minutes2 = user2.get('minutes') 
        city2 = user2.get('city','') 
        nat2 = user2.get('country_code','')
        user2 = Calculator(name2, year2, month2, day2, hours2, minutes2, city2, nat2)
        userSynastry2 = UserSynastry(user2)

        temp = userSynastry1.calculate_synastry_with_user(userSynastry2)
        return temp
    except Exception as ex:
            return {
                "status" : 400,
                "message": str(ex)
            }

def run():
    userSynastry1 = UserSynastry(user11)
    userSynastry2 = UserSynastry(user21)
    temp = userSynastry1.calculate_synastry_with_user(userSynastry2)
    return temp

if __name__ == "__main__":
    run()


# import cProfile, pstats, io
#
# pr = cProfile.Profile()
#
# pr.enable()
#
# # timeit.timeit(run, number=1)
# run()
# pr.disable()
# s = io.StringIO()
#
# sortby = pstats.SortKey.CUMULATIVE
# ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
# ps.print_stats()
# print(s.getvalue())

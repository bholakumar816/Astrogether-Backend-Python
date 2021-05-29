
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from astro.natal_chart import Calculator

def output(user):
    planets = user.calculate_planets_positions()
    houses = user.calculate_houses()
    planets_houses = user.calculate_houses_for_planets(planets, houses)
    finale = ("-----------------------------------------------------\n")
    finale += ("NAME: " + user.name + "\n")
    finale += ("PLANET     POSITION\n")
    finale += ("                      \n")
    finale += (f"Sun:       {planets[0]['sign']} {round(planets[0]['pos'], 3)} in {planets_houses[0]}\n")
    finale += (f"Moon:      {planets[1]['sign']} {round(planets[1]['pos'], 3)} in {planets_houses[1]}\n")
    finale += (f"Mercury:   {planets[2]['sign']} {round(planets[2]['pos'], 3)} in {planets_houses[2]}\n")
    finale += (f"Venus:     {planets[3]['sign']} {round(planets[3]['pos'], 3)} in {planets_houses[3]}\n")
    finale += (f"Mars:      {planets[4]['sign']} {round(planets[4]['pos'], 3)} in {planets_houses[4]}\n")
    finale += (f"Jupiter:   {planets[5]['sign']} {round(planets[5]['pos'], 3)} in {planets_houses[5]}\n")
    finale += (f"Saturn:    {planets[6]['sign']} {round(planets[6]['pos'], 3)} in {planets_houses[6]}\n")
    finale += (f"Uranus:    {planets[7]['sign']} {round(planets[7]['pos'], 3)} in {planets_houses[7]}\n")
    finale += (f"Neptune:   {planets[8]['sign']} {round(planets[8]['pos'], 3)} in {planets_houses[8]}\n")
    finale += (f"Pluto:     {planets[9]['sign']} {round(planets[9]['pos'], 3)} in {planets_houses[9]}\n")
    finale += (f"North node:     {planets[10]['sign']} {round(planets[10]['pos'], 3)} in {planets_houses[10]}\n")
    finale += (f"Chiron:     {planets[11]['sign']} {round(planets[11]['pos'], 3)} in {planets_houses[11]}\n")
    finale += (f"South node:     {planets[12]['sign']} {round(planets[12]['pos'], 3)} in {planets_houses[12]}\n")
    finale += (f"Vertex:     {planets[13]['sign']} {round(planets[13]['pos'], 3)} in {planets_houses[13]}\n")
    finale += (f"Sun/Moon:     {planets[14]['sign']} {round(planets[14]['pos'], 3)} in {planets_houses[14]}\n")

    finale += ("\nPLACIDUS HAUSES\n")
    finale += (f"House 1(Ascendant):     {houses[0]['sign']}  {round(houses[0]['pos'], 3)}\n")
    finale += (f"House 2:     {houses[1]['sign']}  {round(houses[1]['pos'], 3)}\n")
    finale += (f"House 3:     {houses[2]['sign']}  {round(houses[2]['pos'], 3)}\n")
    finale += (f"House 4(IC):     {houses[3]['sign']}  {round(houses[3]['pos'], 3)}\n")
    finale += (f"House 5:     {houses[4]['sign']}  {round(houses[4]['pos'], 3)}\n")
    finale += (f"House 6:     {houses[5]['sign']}  {round(houses[5]['pos'], 3)}\n")
    finale += (f"House 7(Descendant):     {houses[6]['sign']}  {round(houses[6]['pos'], 3)}\n")
    finale += (f"House 8:     {houses[7]['sign']}  {round(houses[7]['pos'], 3)}\n")
    finale += (f"House 9:     {houses[8]['sign']}  {round(houses[8]['pos'], 3)}\n")
    finale += (f"House 10(MC):    {houses[9]['sign']}  {round(houses[9]['pos'], 3)}\n")
    finale += (f"House 11:    {houses[10]['sign']}  {round(houses[10]['pos'], 3)}\n")
    finale += (f"House 12:    {houses[11]['sign']}  {round(houses[11]['pos'], 3)}\n")
    finale += ("\n")
    return finale

user = Calculator("Iskra", 1995, 4, 4, 11, 45, "Sofia", "BG")
# user = Calculator("Doncho", 1989, 6, 22, 21, 15, "Sofia", "BG")


if __name__ == "__main__":
    print(output(user))

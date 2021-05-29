Conjunction = "Conjunction"
Trine = "Trine"
Sextile = "Sextile"
Square = "Square"
Opposition = "Opposition"
Quincunx = "Quincunx",
Semisquare = "Semi-square"
Semisextile = "Semi-sextile"
SesquiSquare = "Sesqui-square"


class AspectPoint:
    def __init__(self, conjunction, trine, sextile, square, oposition):
        self.conjunction = conjunction
        self.trine = trine


aspects_points = {
    "Sun-Sun": {
        Conjunction: 1,
        Trine: 3,
        Sextile: 3,
        Square: -2,
        Opposition: 2
    },
    "Sun-Moon": {
        Conjunction: 4,
        Sextile: 5,
        Trine: 5,
        Square: -4,
        Opposition: 2
    },
    "Sun-Mercury": {
        Conjunction: 2,
        Sextile: 2,
        Trine: 2,
        Square: -1,
        Opposition: -1
    },
    "Sun-Venus": {
        Conjunction: 4,
        Trine: 3,
        Sextile: 2,
        Square: -1,
        Opposition: -1,
        Quincunx: -1
    },
    "Sun-Mars": {
        Conjunction: 4,
        Trine: 3,
        Sextile: 3,
        Square: -2,
        Opposition: -2,
        Quincunx: -2
    },
    "Sun-Jupiter": {
        Conjunction: 4,
        Sextile: 4,
        Trine: 4,
        Square: 1,
        Opposition: 1
    },
    "Sun-Saturn": {
        Sextile: 3,
        Conjunction: -3,
        Square: -3,
        Opposition: -3
    },
    "Sun-Uranus": {
        Sextile: 2,
        Trine: 2,
        Conjunction: -1,
        Square: -1,
        Opposition: -1
    },
    "Sun-Neptune": {
        Conjunction: -2,
        Square: -2,
        Opposition: -2,
        Sextile: 1,
        Trine: 1
    },
    "Sun-Pluto": {
        Conjunction: 1,
        Sextile: 1,
        Trine: 1,
        Square: -3,
        Opposition: -3
    },
    "Sun-Chiron": {
        Conjunction: 3,
        Trine: 3,
        Sextile: 3
    },
    "Sun-1": {
        Conjunction: -3,
        Sextile: 2,
        Trine: 2,
        Square: -2
    },
    "Sun-7": {
        Conjunction: 5
    },
    "Sun-4": {
        Conjunction: 2
    },
    "Sun-Vertex": {
        Conjunction: 4,
        Opposition: 4
    },
    "Sun-North Node": {
        Conjunction: 4,
        Sextile: 2,
        Trine: 2,
        Square: 2
    },
    "Sun-South Node": {
        Conjunction: 3,
        Sextile: 2,
        Trine: 2,
        Square: 2
    },
    "Sun-Sun/Moon": {
        Conjunction: 4,
        Square: 4,
        Opposition: 4,
        Semisquare: 4
    },
    "Moon-Moon": {
        Sextile: 4,
        Trine: 5,
        Square: -4,
        Quincunx: -4,
        Opposition: -2
    },
    "Moon-Mercury": {
        Conjunction: 2,
        Sextile: 2,
        Trine: 2,
        Square: -2,
        Opposition: -2
    },
    "Moon-Venus": {
        Conjunction: 3,
        Sextile: 3,
        Trine: 3,
        Square: -2,
        Opposition: -2
    },
    "Moon-Mars": {
        Conjunction: -2,
        Sextile: 3,
        Trine: 3,
        Square: -3,
        Opposition: -3
    },
    "Moon-Jupiter": {
        Conjunction: 3,
        Sextile: 3,
        Trine: 3,
        Square: 1,
        Opposition: 1
    },
    "Moon-Saturn": {
        Sextile: 3,
        Trine: 3,
        Square: -4,
        Conjunction: -3,
        Opposition: -3
    },
    "Moon-Uranus": {
        Conjunction: -1,
        Sextile: 2,
        Trine: 2,
        Square: -2,
        Opposition: -2,
        Quincunx: -2
    },
    "Moon-Neptune": {
        Conjunction: -1,
        Sextile: -1,
        Trine: -1,
        Square: -3,
        Opposition: -3
    },
    "Moon-Pluto": {
        Conjunction: 1,
        Sextile: 2,
        Trine: 2,
        Square: -3,
        Opposition: -3
    },
    "Moon-Chiron": {
        Conjunction: 3,
        Trine: 3,
        Sextile: 3
    },
    "Moon-1": {
        Conjunction: -3,
        Sextile: 3,
        Trine: 3,
        Square: -2
    },
    "Moon-7": {
        Conjunction: 2
    },
    "Moon-4": {
        Conjunction: 4
    },
    "Moon-Vertex": {
        Conjunction: 4,
        Opposition: 4
    },
    "Moon-North Node": {
        Conjunction: 4,
        Trine: 2,
        Sextile: 2,
        Square: 2
    },
    "Moon-South Node": {
        Conjunction: 3,
        Trine: 2,
        Sextile: 2,
        Square: 2
    },
    "Moon-Sun/Moon": {
        Conjunction: 4,
        Semisquare: 4,
        Square: 4,
        Opposition: 4
    },
    "Mercury-Mercury": {
        Sextile: 2,
        Conjunction: 2,
        Trine: 2,
        Square: -3,
        Opposition: -2
    },
    "Mercury-Venus": {
        Conjunction: 2,
        Sextile: 2,
        Trine: 2,
        Square: -1,
        Opposition: -1,
        Quincunx: -1
    },
    "Mercury-Mars": {
        Conjunction: -1,
        Sextile: 2,
        Trine: 2,
        Square: -2,
        Opposition: -2,
        Quincunx: -2
    },
    "Mercury-Jupiter": {
        Conjunction: 3,
        Sextile: 3,
        Trine: 3,
        Square: 1,
        Opposition: 1,
        Quincunx: 1
    },
    "Mercury-Saturn": {
        Conjunction: -2,
        Square: -2,
        Opposition: -2,
        Quincunx: -2,
        Sextile: 1,
        Trine: 1
    },
    "Mercury-Uranus": {
        Conjunction: 1,
        Square: 1,
        Opposition: 1,
        Quincunx: 1,
        Sextile: 1,
        Trine: 1
    },
    "Mercury-Neptune": {
        Sextile: 1,
        Trine: 1,
        Square: -3,
        Opposition: -3,
        Quincunx: -3
    },
    "Mercury-Pluto": {
        Conjunction: 1,
        Square: 1,
        Opposition: 1,
        Quincunx: 1,
        Sextile: 1,
        Trine: 1
    },
    "Mercury-1": {
        Conjunction: 2,
        Sextile: 1,
        Trine: 1,
        Square: -1
    },
    "Mercury-7": {
        Conjunction: 2,
    },
    "Mercury-4": {
        Conjunction: 2,
    },
    "Mercury-10": {
        Conjunction: 2,
    },
    "Mercury-Vertex": {
        Conjunction: 1,
        Opposition: 1
    },
    "Mercury-North Node": {
        Conjunction: 1,
        Square: 1,
        Opposition: 1,
        Quincunx: 1,
        Sextile: 1,
        Trine: 1,
        Semisquare: 1,
        Semisextile: 1
    },
    "Mercury-South Node": {
        Conjunction: 1,
        Square: 1,
        Opposition: 1,
        Quincunx: 1,
        Sextile: 1,
        Trine: 1,
        Semisquare: 1,
        Semisextile: 1
    },
    "Venus-Venus": {
        Conjunction: 3,
        Sextile: 3,
        Trine: 3,
        Opposition: 3,
        Square: 1,
    },
    "Venus-Mars": {
        Conjunction: 1,
        Sextile: 1,
        Trine: 1,
        Square: 2,
        Opposition: 2
    },
    "Venus-Jupiter": {
        Conjunction: 3,
        Trine: 2,
        Sextile: 2,
        Opposition: 1
    },
    "Venus-Saturn": {
        Conjunction: 2,
        Sextile: 3,
        Trine: 3,
        Square: -4,
        Opposition: -3,
        Semisquare: -3,
        SesquiSquare: -3
    },
    "Venus-Uranus": {
        Conjunction: 1,
        Sextile: 2,
        Trine: 2,
        Square: -2,
        Opposition: -2,
        Semisquare: -2,
        SesquiSquare: -2
    },
    "Venus-Neptune": {
        Conjunction: 2,
        Trine: 2,
        Sextile: 2,
        Square: -3,
        Opposition: -3,
        Quincunx: -3
    },
    "Venus-Pluto": {
        Conjunction: 2,
        Trine: 2,
        Sextile: 2,
        Square: -2,
        Opposition: -2,
        Semisquare: -2,
        SesquiSquare: -2
    },
    "Venus-Chiron": {
        Conjunction: 3,
        Trine: 3,
        Sextile: 3
    },
    "Venus-1": {
        Conjunction: 3,
        Sextile: 2,
        Trine: 2,
        Square: 1
    },
    "Venus-7": {
        Conjunction: 4
    },
    "Venus-4": {
        Conjunction: 2
    },
    "Venus-10": {
        Conjunction: 2
    },
    "Venus-Vertex": {
        Conjunction: 2,
        Opposition: 2
    },
    "Venus-North Node": {
        Conjunction: 2,
        Sextile: 2,
        Trine: 2,
        Square: 2,
        Opposition: 2,
    },
    "Venus-South Node": {
        Conjunction: 2,
        Sextile: 2,
        Trine: 2,
        Square: 2,
        Opposition: 2,
    },
    "Venus-Sun/Moon": {
        Conjunction: 3,
        Semisquare: 3,
        Square: 3,
        Opposition: 3
    },
    "Mars-Mars": {
        Conjunction: 2,
        Sextile: 2,
        Trine: 2,
        Square: -2,
        Opposition: -2,
        Quincunx: -2
    },
    "Mars-Jupiter": {
        Conjunction: 2,
        Sextile: 2,
        Trine: 2,
        Square: 2,
        Opposition: 2,
    },
    "Mars-Saturn": {
        Square: -4,
        Opposition: -4,
        Quincunx: -4,
        Conjunction: -3,
        Sextile: 1,
        Trine: 1
    },
    "Mars-Uranus": {
        Conjunction: 1,
        Sextile: 1,
        Trine: 1,
        Square: -2,
        Opposition: -2
    },
    "Mars-Neptune": {
        Sextile: 1,
        Trine: 1,
        Conjunction: -2,
        Square: -2,
        Opposition: -2
    },
    "Mars-Pluto": {
        Conjunction: 2,
        Trine: 2,
        Sextile: 2,
        Square: -3,
        Opposition: -3
    },
    "Mars-1": {
        Conjunction: 2,
        Sextile: 2,
        Trine: 2,
        Square: -1
    },
    "Mars-7": {
        Conjunction: 4
    },
    "Mars-Vertex": {
        Conjunction: 2,
        Opposition: 2
    },
    "Mars-North node": {
        Conjunction: 1,
        Sextile: 1,
        Trine: 1,
        Square: 1,
        Opposition: 1,
    },
    "Mars-South node": {
        Conjunction: 1,
        Sextile: 1,
        Trine: 1,
        Square: 1,
        Opposition: 1,
    },
    "Mars-Sun/Moon": {
        Conjunction: 3,
        Semisquare: 3,
        Square: 3,
        Opposition: 3
    },
    "Jupiter-Jupiter": {
        Conjunction: 2,
        Sextile: 2,
        Trine: 2,
        Square: 2,
        Opposition: 2,
    },
    "Jupiter-Saturn": {
        Conjunction: 1,
        Sextile: 1,
        Trine: 1,
        Sextile: -2,
        Opposition: -2,
        Square: -2
    },
    "Jupiter-Uranus": {
        Conjunction: 1,
        Sextile: 1,
        Trine: 1,
        Square: 1,
        Opposition: 1,
    },
    "Jupiter-Neptune": {
        Conjunction: 1,
        Sextile: 1,
        Trine: 1,
        Square: -1,
        Opposition: -1
    },
    "Jupiter-Pluto": {
        Conjunction: 1,
        Trine: 1,
        Sextile: 1,
        Square: -2,
        Opposition: -2
    },
    "Jupiter-1": {
        Conjunction: 2,
        Sextile: 1,
        Trine: 1,
        Square: 1
    },
    "Jupiter-7": {
        Conjunction: 3
    },
    "Jupiter-Vertex": {
        Conjunction: 2,
        Opposition: 2
    },
    "Jupiter-South Node": {
        Conjunction: 1,
        Sextile: 1,
        Trine: 1,
        Square: 1,
        Opposition: 1,
    },
    "Jupiter-North Node": {
        Conjunction: 1,
        Sextile: 1,
        Trine: 1,
        Square: 1,
        Opposition: 1,
    },
    "Saturn-Saturn": {
        Sextile: 1,
        Trine: 1,
        Square: -1,
        Opposition: -1
    },
    "Saturn-1": {
        Conjunction: -2,
        Square: -2,
        Opposition: -2,
        Sextile: 1,
        Trine: 1
    },
    "Saturn-Vertex": {
        Conjunction: -2,
        Opposition: -2
    },
    "Saturn-South Node": {
        Conjunction: -2,
        Square: -2
    },
    "Saturn-North Node": {
        Conjunction: -2,
        Square: -2
    },
    "Uranus-7": {
        Conjunction: -3
    },
    "Uranus-Vertex": {
        Conjunction: -3
    },
    "Neptune-7": {
        Conjunction: -2
    },
    "Neptune-1": {
        Conjunction: -2
    },
    "Neptune-Vertex": {
        Conjunction: -2
    },
    "Pluto-7": {
        Conjunction: 1
    },
    "Pluto-Vertex": {
        Conjunction: 1
    },
    "1-1": {
        Conjunction: 1,
        Sextile: 2,
        Trine: 2,
        Square: -2,
        Opposition: 3
    },
    "1-North Node": {
        Conjunction: 2,
        Trine: 2,
        Sextile: 2,
        Square: 2
    },
    "1-South Node": {
        Conjunction: 3,
        Trine: 2,
        Sextile: 2,
        Square: 2
    },
    "1-Sun/Moon": {
        Conjunction: 3,
        Semisquare: 3,
        Square: 3,
        Opposition: 3
    },
    "Vertex-Sun/Moon": {
        Conjunction: 3,
        Semisquare: 3,
        Square: 3,
        Opposition: 3
    },
    "Vertex-North Node": {
        Conjunction: 2
    },
    "Vertex-South Node": {
        Conjunction: 2
    },
    "North Node-4": {
        Conjunction: 3
    },
    "North Node-10": {
        Conjunction: 3
    },
    "South Node-4": {
        Conjunction: 3
    },
    "South Node-10": {
        Conjunction: 3
    },
    "South Node-South Node": {
        Conjunction: 3,
        Trine: 4,
        Sextile: 3,
        Quincunx: -3,
        Square: -4,
        Opposition: 2
    }
}

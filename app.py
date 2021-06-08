import os
from flask import Flask, jsonify, request
from astro.synastry import getUserSynastry, compareUsers

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(error):
    return jsonify({
        "status": 404,
        "message": "Wrong request method / route"
    })

@app.route('/',methods=["POST"])
def index():
    if request.method == 'POST':
        try:
            req_data = request.json
            print(req_data)
            if not req_data == None:
                _name = req_data.get('name','') 
                _year = req_data.get('year') 
                _month = req_data.get('month') 
                _day = req_data.get('day') 
                _hours = req_data.get('hours') 
                _minutes = req_data.get('minutes') 
                _city = req_data.get('city','') 
                _nat = req_data.get('country_code','')

                data = getUserSynastry(_name, _year, _month, _day, _hours, _minutes, _city, _nat)
                return jsonify({
                    "planets_names": data.planets_names,
                    "user": data.user.__dict__,
                    "planets": data.planets,
                    "houses" : data.houses,
                    "planets_and_houses" : data.planets_and_houses
                })
            else:
                return jsonify({
                    "status": 400,
                    "message": "No data provided",
                })

        except Exception as ex:
            return jsonify({
                "status": 400,
                "message": str(ex),
            })

    return jsonify({
        "status": 405,
        "message": "Wrong request method"
    })

@app.route('/compare',methods=["POST"])
def compare():
    if request.method == 'POST':
        try:
            req_data = request.json
            # print(req_data.get('user1',{}))
            if not req_data.get('user1') == None and not req_data.get('user2') == None:
                

                data = compareUsers(req_data.get('user1',{}),req_data.get('user2',{}))
                if not data:
                    return jsonify({
                    "status": 400,
                    "message": "Something went wrong",
                    })

                return jsonify(data)
            else:
                return jsonify({
                    "status": 400,
                    "message": "please provid users data",
                })

        except Exception as ex:
            return jsonify({
                "status": 400,
                "message": str(ex)
            })

    return jsonify({
        "status": 405,
        "message": "Wrong request method"
    })

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port,debug=True)

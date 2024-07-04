from flask import Flask, render_template, request

# from servise.add import add_contacts

app = Flask(__name__)

car1 = {
    "id": "1",
    "number": "235-55-987",
    "problems": [],
    "urgent": True,
    "image": "https://cdn.globalso.com/forthingmotor/Dongfeng-Forthing-Electric-Suv-Thunder-Ev-Sales-in-Europe4.jpg",
}
car2 = {
    "id": "2",
    "number": "545-55-222",
    "problems": [],
    "urgent": True,
    "image": "https://t4.ftcdn.net/jpg/04/36/90/21/360_F_436902182_MyIDnh1EwT4MwN7UStL0IIpL5rO8Zsam.jpg",
}
car3 = {
    "id": "3",
    "number": "625-55-587",
    "problems": [],
    "urgent": False,
    "image": "https://mg-israel.co.il/wp-content/uploads/2019/09/MG_ZS_EV_red.jpg",
}

cars = [car1, car2, car3]


@app.route("/")
def cars_list():
    return render_template("car_list.html", car_list=cars)

    # final_str = ""
    # for car in cars:
    #     final_str += f"<p>{car['number']}</p>"

    # return final_str


@app.route("/single_car/<id>")
def single_car(id):
    for car in cars:
        if car["id"] == id:
            return render_template('single_car.html', car = car)
    return render_template("single_car.html", car=None)

    
    # return (
    #     f"<p>number:{cars[index]['number']} <br> Problems:{cars[index]['problems']}</p>"
    # )


@app.route("/add_car/")
def add_car():
    print("****** Adding car")
    return render_template("add_car.html")


@app.route("/add_to_list/", methods=["POST", "GET"])
def add_to_list():
    print("****** Adding to list", request.form["cNumber"])
    return "Added to list:" + request.form["cNumber"]


@app.route("/urgent_cars/")
def urgent_cars():
    print("****** I am in urgent cars function")
    urgent_cars_list = [car for car in cars if car["urgent"]]
    print(f"****** Urgent cars list: {urgent_cars_list}")
    return render_template("urgent_cars.html", cars=urgent_cars_list)



if __name__ == "__main__":
    app.run(debug=True, port=9000)

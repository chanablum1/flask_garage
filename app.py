from flask import Flask, render_template

# from servise.add import add_contacts

app = Flask(__name__)

car1 = {
    "id": "1",
    "number": "235-55-987",
    "problems": [],
    "image": "https://img-optimize.toyota-europe.com/resize/ccis/680x680/zip/il/configurationtype/visual-for-grade-selector/product-token/aa41e8ae-82b4-4f15-8172-3bc596cc7762/grade/05fcd071-f774-48cd-9059-ac659904e114/body/74469257-47ae-46eb-859d-2c693e6726ca/fallback/true/padding/50,50,50,50/image-quality/70/day-exterior-4.png",
}
car2 = {
    "id": "2",
    "number": "235-55-222",
    "problems": [],
    "image": "https://t4.ftcdn.net/jpg/04/36/90/21/360_F_436902182_MyIDnh1EwT4MwN7UStL0IIpL5rO8Zsam.jpg",
}

cars = [car1, car2]


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
    return "Adding car"


if __name__ == "__main__":
    app.run(debug=True, port=9000)

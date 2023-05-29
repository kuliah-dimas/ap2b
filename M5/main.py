from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

menus = []

def generate_id():
    return max([menu["id"] for menu in menus]) + 1 if menus else 1

@app.route("/")
def show_menus():
    return render_template("index.html", menus=menus)

@app.route("/add", methods=["GET", "POST"])
def add_menu():
    if request.method == "POST":
        name = request.form["name"]
        price = int(request.form["price"])
        menus.append({"id": generate_id(), "name": name, "price": price})
        return redirect(url_for('show_menus'))
    else:
        return render_template("add.html")


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_menu(id):
    menu = next((menu for menu in menus if menu["id"] == id), None)
    if menu is None:
        return redirect(url_for('show_menus'))
    if request.method == "POST":
        menu["name"]= request.form["name"]
        menu["price"]= int(request.form["price"])
        return redirect(url_for("show_menus"))
    else:
        return render_template("edit.html", menu=menu)

@app.route("/delete/<int:id>")
def delete_menu(id):
    menu = next((menu for menu in menus if menu["id"] == id), None)
    if menu is not None:
        menus.remove(menu)
    return redirect(url_for("show_menus"))

if __name__ == "__main__":
    app.run(debug=False, port=8000)

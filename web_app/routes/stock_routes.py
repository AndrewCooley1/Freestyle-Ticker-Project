# web_app/routes/weather_routes.py

from flask import Blueprint, request, render_template
from app.stock import lookup_ticker
stock_routes = Blueprint("stock_routes", __name__)


@stock_routes.route("/")
def home():
    print("Home")
    return render_template("stocks.html")

@stock_routes.route("/handle_request", methods=["POST"])
def post_handler():
    print("handler...")


    print("FORM DATA:", dict(request.form))
    request_data = dict(request.form)

    symbol = request_data.get("ticker")
    

    results = lookup_ticker(ticker)
    x=len(results)


    if results:
        return render_template("results.html", x=x)
    else:
        return redirect("/")


from flask import Blueprint, request, jsonify

from app.stock import lookup_ticker

stockdata_routes = Blueprint("stockdata_routes", __name__)

@stockdata_routes.route("/ticker")








#def weather_forecast_api():
    #print("WEATHER FORECAST (API)...")
    #print("URL PARAMS:", dict(request.args))

    country_code = request.args.get("country_code") or "US"
    zip_code = request.args.get("zip_code") or "20057"

    results = get_hourly_forecasts(country_code=country_code, zip_code=zip_code)
    if results:
        return jsonify(results)
    else:
        return jsonify({"message":"Invalid Geography. Please try again."}), 404
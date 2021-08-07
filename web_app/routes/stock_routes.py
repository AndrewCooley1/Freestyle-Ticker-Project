# web_app/routes/stock_routes.py
from flask import Blueprint, request, render_template
#from app.stock import lookup_ticker

stock_routes = Blueprint("stock_routes", __name__)

@stock_routes.route('/')
@stock_routes.route("/home")

def index():
    print("HOME...")
    return "Welcome Home"


























#@stock_routes.route("/hello")
#def hello_world():
    #print("HELLO...", dict(request.args))
    # NOTE: `request.args` is dict-like, so below we're using the dictionary's `get()` method,
    # ... which will return None instead of throwing an error if key is not present
    # ... see also: https://www.w3schools.com/python/ref_dictionary_get.asp
    #name = request.args.get("name") or "World"
    #message = f"Hello, {name}!"
    #return message
    #return render_template("hello.html", message=message)











































#from flask import Blueprint, request, render_template
#from app.stock import lookup_ticker

#stock_routes = Blueprint("stock_routes", __name__)


#@stock_routes.route("/")
#def home():
    #print("Home...")
    #return render_template("stock.html")

#@stock_routes.route("/handle_request", methods=["POST"])
#def post_handler():
    #print("handler...")


    #print("FORM DATA:", dict(request.form))
    #request_data = dict(request.form)

# do we need a request.args function?

    #symbol = request_data.get("ticker")
    

    #results = lookup_ticker(ticker)
    #x=len(results)


    #if results:
        #return render_template("results.html", x=x)
    #else:
        #return redirect("/")

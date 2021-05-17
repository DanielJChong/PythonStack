from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    # Return the string 'Hello World!' as a response
    return render_template("index.html")

@app.route("/<name>/<times>")
def hello_person(name, times):
    print("*"*80)
    print("in hello_person function")
    print(name)
    return render_template("index.html", some_name=name, num_times=int(times))

# @app.route('/success')
# def success():
#     return "success"

# @app.route('/hello/<int:num>')      #When you want to print multiple times.
# def say_hello(num):
#     return "Hello " * num

# @app.route('/hello/<name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
# def hello(name):
#     print(name)
#     return "Hello, " + name

# @app.route('/users/<username>/<id>') # for a route '/users/____/____', two parameters in the url get passed as username and id
# def show_user_profile(username, id):
#     print(username)
#     print(id)
#     return "username: " + username + ", id: " + id


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module  
    app.run(debug=True)    # Run the app in debug mode.
from flask import Flask, jsonify, request 

app = Flask(__name__) 

@app.route('/', methods = ['GET', 'POST']) 
def home(): 
	if(request.method == 'GET'): 
		return jsonify({"api1": "This api1 is split the given string from behind at n regular interval --> /api1/'input_string' " ,"api2":"api2 is calculate the frequency of each unique string in a given list  --> /api2/'input_string'/'number' "})

#API1 (First API)- split the given string(from request) from behind at n regular interval and return the output as a API response
@app.route('/api1/<string:str>/<int:num>', methods = ['GET']) 
def api1(str,num): 
	a = str
	n = num
	b = ""
	c = a[::-1]
	for i in range(0,len(c),n):
		b += c[i:i+n]
		b +=" "
	return jsonify((b[::-1]))

#API2( Second API) - calculate the frequency of each unique string in a given list
@app.route('/api2/<string:str>', methods = ['GET']) 
def api2(str): 
	i = str.lower()
	l = set(i.split())
	dict = {}
	for j in l:
		count = i.count(j)
		dict[j] = count
	return jsonify(dict)

# driver function 
if __name__ == '__main__': 
	app.run(debug = True)
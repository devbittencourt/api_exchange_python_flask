from flask import Flask, render_template, request, jsonify
import requests
import json


app = Flask(__name__)

# Exemplo de dados
dados = [
    {'id': 1, 'nome': 'Dev_Bittencourt', 'email': 'devbittencourt0@gmail.com', 'site': 'https://linkr.bio/devBITTENCOURT'},
    {'id': 2, 'nome': 'Maria', 'email': 'Exemplo_maria@gmail.com', 'site': 'https://www.Exemplo_maria.com'},
    {'id': 3, 'nome': 'Pedro', 'email': 'Exemplo_pedro@hotmail.com', 'site': 'https://www.Exemplo_pedro.com'}
]

url = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"
response = requests.get(url)
data = response.json()
#data2= data



@app.route('/', methods=['GET'])
def doc():
    
    doc = """
    <!DOCTYPE html>
    <html>
    <head>
    	<title>db API Documentation</title>
    	<style>
    		h1 {
    			text-align: center;
    			margin-top: 50px;
    		}
    		table {
    			margin: auto;
    			border-collapse: collapse;
    			text-align: center;
    			width: 80%;
    			margin-top: 50px;
    			margin-bottom: 50px;
    		}
    		th, td {
    			padding: 10px;
    			border: 1px solid black;
    		}
    		th {
    			background-color: #cccccc;
    		}
            p, pre, h2 {
                font-size: 18px;
            }
    	</style>
    </head>
    <body>
    	<h1>API Documentation</h1>
    	<h2 style="text-align:center;">Introduction</h2>
    	<p style="text-align:center;">The API provides access to data of a list of people. Each person is represented by a JSON object that contains an ID, a name, an email, and a website. Additionally, we also used a real-world case to obtain the exchange rates for USD, EUR, and BTC, where we applied the request to a real API to obtain the data. Use the buttons below to navigate the API.</p>

			<div style="text-align: center;">
				<button style="display:inline-block; margin:0 10px;" onclick="window.location.href = window.location.href + '/dados'">Get Data</button>
				<button style="display:inline-block; margin:0 10px;" onclick="window.location.href = window.location.href + '/dados/1'">Get Data id 1</button>
				<button style="display:inline-block; margin:0 10px;" onclick="window.location.href = window.location.href + '/c'">Get Exchange Rates</button>
				<button style="display:inline-block; margin:0 10px;" onclick="window.location.href = window.location.href + '/e'">Explanation of page Exchange </button>
				<button style="display:inline-block; margin:0 10px;" onclick="window.location.href='https://linkr.bio/devBITTENCOURT'">My website! </button>
			</div>

    	<h2 style="text-align:center;">Resources</h2>

			<table>
    		<thead>
    			<tr>
    				<th>Resource</th>
    				<th>HTTP Method</th>
    				<th>Description</th>
    			</tr>
    		</thead>
    		<tbody>
    			<tr>
    				<td>/data</td>
    				<td>GET</td>
    				<td>Returns all data as a JSON list. (Available)</td>
    			</tr>
    			<tr>
    				<td>/data/&lt;id&gt;</td>
    				<td>GET</td>
    				<td>Returns a specific data with the ID provided as a route parameter. (Available)</td>
    			</tr>
    			<tr>
    				<td>/</td>
    				<td>POST</td>
    				<td>Adds a new data provided in the request body as a JSON object. (Soon)</td>
    			</tr>
    			<tr>
    				<td>/data/&lt;id&gt;</td>
    				<td>PUT</td>
    				<td>Updates an existing data with the ID provided as a route parameter. (Soon)</td>
    			</tr>
    			<tr>
    				<td>/data/&lt;id&gt;</td>
    				<td>DELETE</td>
    				<td>Deletes an existing data with the ID provided as a route parameter. (Soon)</td>
    			</tr>

    		</tbody>
    	</table>
    	<h2 style="text-align:center;">Usage Examples</h2>
    	<p style="text-align:center;">Example JSON object to add a new data:</p>
    	<pre>
    		{
    			"id": 1,
    			"name": "Dev_Bittencourt",
    			"email": "devbittencourt0@gmail.com",
    			"website": "https://linkr.bio/devBITTENCOURT"
    		}
    	</pre>
    	<p style="text-align:center;">URL to send a POST request to add a new data:</p>
    	<pre style="text-align:center;">http://localhost:5000/(Soon)</pre>
    </body>
    </html>
    """
    return doc


# Rota para retornar todos os dados
@app.route('/dados', methods=['GET'])
def get_dados():
    return jsonify(dados)

# Rota para retornar um dado específico pelo ID
@app.route('/dados/<int:dado_id>', methods=['GET'])
def get_dado(dado_id):
    dado = [dado for dado in dados if dado['id'] == dado_id]
    if len(dado) == 0:
        return jsonify({'erro': 'Dado não encontrado'})
    return jsonify(dado[0])


@app.route('/e')
def exp():
	
	if response.status_code != 200:      
		return jsonify({'error': 'Failed to retrieve exchange rate data'})
	else:


			explic='''

			<!DOCTYPE html>
			<html>
			<head>
				<title>Explanation of Exchange Rates API Code</title>
				<style>
					h1 {
						text-align: center;
						margin-top: 50px;
									color: #333;
					}
							p {
									font-size: 20px;
									text-align: center;
									margin-top: 20px;
							}
							ul {
									margin-top: 50px;
									list-style: none;
									text-align: center;
									font-size: 24px;
							}
							li {
									margin-top: 10px;
									color: #333;
							}
							span {
									font-weight: bold;
							}
							body {
									background-color: #f7f7f7;
							}
				</style>
			</head>
			<body>
				<h1>Explanation of Exchange Rates API Code</h1>
				<p>The following code defines a route for a Flask application that retrieves the latest exchange rates from an external API and displays them on a webpage.</p>
				<p>The code first converts the exchange rate data from a Python dictionary to a JSON string using the <code>json.dumps()</code> function.</p>
					<p>The HTML code defines a webpage with a background image and a heading. The exchange rates are displayed in an unordered list with each rate displayed as a list item with a corresponding currency code. The exchange rate values are updated using JavaScript to extract the relevant values from the JSON string and insert them into the appropriate HTML element using the <code>document.getElementById()</code> method.</p>
				<ul>
					<li>USD-BRL: <span id="usd"></span></li>
					<li>EUR-BRL: <span id="eur"></span></li>
					<li>BTC-BRL: <span id="btc"></span></li>
				</ul>
					<script>
							var rates = ''' + json.dumps(data) + ''';
							document.getElementById("usd").innerHTML = rates.USDBRL.bid;
							document.getElementById("eur").innerHTML = rates.EURBRL.bid;
							document.getElementById("btc").innerHTML = rates.BTCBRL.bid;
					</script>
			</body>
			</html>
			'''

	return explic


@app.route('/c')
def get_exchange_rates():


		
	if response.status_code != 200:
		return jsonify({'error': 'Failed to retrieve exchange rate data'})
	
	else:
			html = '''
					<html>
							<head>
									<title>Exchange Rates</title>
							</head>
							<body>
							<style>
									body {
											background-image: url('https://s2.glbimg.com/2yO3evIMd4GHV0Q5U0pTRtLpXyE=/0x0:1200x675/924x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_63b422c2caee4269b8b34177e8876b93/internal_photos/bs/2023/S/I/UkOVaRTs2si3jvFrSPSA/ilustra-dolar-real.jpeg');
											background-size: cover;
									}
									h1 {
											color: white;
									}
							</style>
							<style>
									body {
											font-size: 120%;
									}
							</style>
									<h1>Latest Exchange Rates</h1>
									<p>The following exchange rates were returned from the API:</p>
									<ul>
											<li>USD-BRL: <span id="usd"></span></li>
											<li>EUR-BRL: <span id="eur"></span></li>
											<li>BTC-BRL: <span id="btc"></span></li>
									</ul>
									<script>
											var rates = ''' + json.dumps(data) + ''';
											document.getElementById("usd").innerHTML = rates.USDBRL.bid;
											document.getElementById("eur").innerHTML = rates.EURBRL.bid;
											document.getElementById("btc").innerHTML = rates.BTCBRL.bid;
									</script>
							</body>
					</html>
			'''
	return html




app.run()
# basic attempt of getting around the authentication, but i don't have access to the actual beta on steam so no idea how a valid auth response looks, atm it only responds with the error message the official api would give
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world'
#https://prod.rbg-services.com
@app.route('/configuration/public/applications/0e67af76-2839-4451-880b-471a48757e09/configuration', methods=['GET'])
#?tags=platform-steam&tags=version-82811&tags=steam-branch-public
def configuration():
    if(request.method == 'GET'):
       data = {
	"config": {
		"applicationId": "0e67af76-2839-4451-880b-471a48757e09",
		"environment": "prod",
		"data": {
			"services": {
				"auth": "https://{environment}.rbg-services.com/auth",
				"configuration": "https://{environment}.rbg-services.com/configuration",
				"entity": "https://{environment}.rbg-services.com/entity",
				"game-server-utils": "https://{environment}.rbg-services.com/game-server-utils",
				"inventory": "https://{environment}.rbg-services.com/inventory",
				"matchmaking": "https://{environment}.rbg-services.com/matchmaking",
				"presence": "https://{environment}.rbg-services.com/presence",
				"rta": "https://{environment}.rbg-services.com/rta",
				"rta-ws": "wss://{environment}.rbg-services.com/rta-ws",
				"relationship": "https://{environment}.rbg-services.com/relationship",
				"party": "https://{environment}.rbg-services.com/party",
				"analytics": "https://{environment}.rbg-services.com/analytics",
				"communitysift": "https://apidemo.communitysift.com",
				"stats": "https://{environment}.rbg-services.com/stats"
			},
			"featureSwitches": {
				"validate_text_chat": 'false',
				"play_enabled": 'false',
				"rejoin": 'false',
				"cheats_enabled_by_default": 'false'
			},
			"gameConfig": {
				"RBGameplaySettings.NightVisionMaxBattery": {
					"defaultValues": {
						"bOverrideEasyValue": 'false',
						"easyValue": 1,
						"normalValue": 101,
						"bOverrideHardValue": 'false',
						"hardValue": 100,
						"bOverrideVeryHardValue": 'false',
						"veryHardValue": 100
					},
					"bOverrideFor1P": 'false',
					"values1P": {
						"bOverrideEasyValue": 'true',
						"easyValue": 1,
						"normalValue": 101,
						"bOverrideHardValue": 'false',
						"hardValue": 100,
						"bOverrideVeryHardValue": 'false',
						"veryHardValue": 100
					},
					"bOverrideFor2P": 'false',
					"values2P": {
						"bOverrideEasyValue": 'true',
						"easyValue": 100,
						"normalValue": 101,
						"bOverrideHardValue": 'true',
						"hardValue": 100,
						"bOverrideVeryHardValue": 'true',
						"veryHardValue": 100
					},
					"bOverrideFor3P": 'false',
					"values3P": {
						"bOverrideEasyValue": 'true',
						"easyValue": 100,
						"normalValue": 101,
						"bOverrideHardValue": 'true',
						"hardValue": 100,
						"bOverrideVeryHardValue": 'true',
						"veryHardValue": 100
					},
					"valueType": "FloatByDifficulty",
					"valueName": "RBGameplaySettings.NightVisionMaxBattery",
					"defaultName": "RBGameplaySettings.NightVisionMaxBattery",
					"bCustomName": 'false'
				},
				"RBGameplaySettings.PlayerDefaultMaxHealth": {
					"easy": 1,
					"normal": 2,
					"hard": 3,
					"veryhard": 4
				}
			},
			"idle_timeout": 3600,
			"settings": {
				"lobby_backfill_max_number_of_players": 8,
				"matchmaking_ticket_expiration_time_seconds": 500,
				"trial_matchmaking_ticket_expiration_time_seconds": 500,
				"player_data_suffix": "_closedbeta",
				"configuration_refresh_time_minutes": 60,
				"matchmaking_regions": ["us-east-1", "us-west-1", "sa-east-1", "eu-central-1", "ap-northeast-2", "ap-southeast-1"]
			}
		}
	}
}
    return jsonify(data)

@app.route('/auth/public/sessions', methods=['POST'])
def sessions():
	if(request.method == 'POST'):
		data = {
	"operationId": "4282be4a-5f9f-1429-07ca-85b17bb61804",
	"service": "auth",
	"errorCode": 15,
	"message": "Unexpected response format when processing steam authentication. Params key not found in body.",
	"debug": {
		"message": "com.redbarrelsgames.core.auth.exceptions.NotAuthorizedException: Unexpected response format when processing steam authentication. Params key not found in body.",
		"stackTrace": ["com.redbarrelsgames.auth.providers.http.HttpSteamAuthenticationProvider.lambda$getSteamId$2(HttpSteamAuthenticationProvider.java:89)", "io.vertx.ext.web.client.impl.HttpContext.handleDispatchResponse(HttpContext.java:400)", "io.vertx.ext.web.client.impl.HttpContext.execute(HttpContext.java:387)", "io.vertx.ext.web.client.impl.HttpContext.next(HttpContext.java:365)", "io.vertx.ext.web.client.impl.HttpContext.fire(HttpContext.java:332)"]
	}
}
	return jsonify(data)

@app.route('/entity', methods=['GET'])
def entity():
	if(request.method == 'GET'):
		data = {}
	return jsonify(data)

@app.route('/game-server-utils', methods=['GET'])
def gameserverutils():
	if(request.method == 'GET'):
		data = {}
	return jsonify(data)

@app.route('/inventory', methods=['GET'])
def inventory():
	if(request.method == 'GET'):
		data = {}
	return jsonify(data)

@app.route('/matchmaking', methods=['GET'])
def matchmaking():
	if(request.method == 'GET'):
		data = {}
	return jsonify(data)

@app.route('/presence', methods=['GET'])
def presence():
	if(request.method == 'GET'):
		data = {}
	return jsonify(data)

@app.route('/rta', methods=['GET'])
def rta():
	if(request.method == 'GET'):
		data = {}
	return jsonify(data)

@app.route('/rta-ws', methods=['GET'])
def rtaws():
	if(request.method == 'GET'):
		data = {}
	return jsonify(data)

@app.route('/relationship', methods=['GET'])
def relationship():
	if(request.method == 'GET'):
		data = {}
	return jsonify(data)

@app.route('/party', methods=['GET'])
def party():
	if(request.method == 'GET'):
		data = {}
	return jsonify(data)

@app.route('/analytics', methods=['GET'])
def analytics():
	if(request.method == 'GET'):
		data = {}
	return jsonify(data)

@app.route('/stats', methods=['GET'])
def stats():
	if(request.method == 'GET'):
		data = {}
	return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

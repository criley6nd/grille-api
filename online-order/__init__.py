import logging
import azure.functions as func
import mysql.connector
import json
import requests

config = {
  'host':'duncangrille.mysql.database.azure.com',
  'user':'grille_admin',
  'password':'Dubbuff$5',
  'database':'duncan_grille',
  'client_flags': [mysql.connector.ClientFlag.SSL],
  'ssl_ca': 'cert.pem'
}

async def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    # Connect to MySQL
    q = 'select * from orders limit 5'
    try:
        logging.info(req.get_json()['sql'])
        q = req.get_json()['sql']
    except:
        logging.info("No json data")
    cnx = mysql.connector.connect(**config  
    )
    logging.info(cnx)
    # Show databases
    cursor = cnx.cursor()
    cursor.execute(q)
    cnx.commit()
    result_list = cursor.fetchall()
    # Build result response text
    result_str_list = []
    for row in result_list:
        r = []
        for e in row:
            r.append(str(e))
        result_str_list.append(r)

    localurl = 'http://localhost:7071'
    produrl = 'https://duncan-grille-api.azurewebsites.net'
    url = f'{localurl}/api/listener'
    r= requests.post(url, json={'task': 'placeorder'})
    return func.HttpResponse(
        body=json.dumps(result_str_list),
        status_code=200
    )

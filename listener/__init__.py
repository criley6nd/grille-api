import logging
import azure.functions as func
import mysql.connector
import json
import time

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
    task = ''
    try:
        logging.info(req.get_json()['task'])
        task = req.get_json()['task']
    except:
        logging.info("No json data")
        return func.HttpResponse(
            status_code=400
        )
    cnx = mysql.connector.connect(**config )
    logging.info(cnx)
    # Show databases
    print("in function")
    c = ''
    if task == 'placeorder':
        c = 'update new_order set placed = 1;'
        cursor = cnx.cursor()
        cursor.execute(c)
        cnx.commit()
        return func.HttpResponse(
            status_code=200
        )
    
    elif task == 'reset':
        c = 'update new_order set placed = 0;'
        cursor = cnx.cursor()
        cursor.execute(c)
        cnx.commit()
        return func.HttpResponse(
            status_code=200
        )
    
    elif task == 'listen':
        c = 'select * from new_order;'

        cursor = cnx.cursor()
        cursor.execute(c)
        result_list = cursor.fetchall()
        
        
        return func.HttpResponse(
            body=json.dumps(result_list[0]),
            status_code=200
        )
    
    return func.HttpResponse(
            status_code=400
        )
        


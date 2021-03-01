from typing import Optional
from fastapi import FastAPI, Form, Request
from fastapi.responses import PlainTextResponse, HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
from joblib import load
from pydantic import BaseModel
import random
import uvicorn
from fastapi.responses import JSONResponse
from logging import basicConfig
import logging

app = FastAPI()
logging.basicConfig(filename='journal.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

@app.get("/welcome")
async def welcome():
    result = {'Message': "Bonjour, ceci est la beta d'un algorithm d'analyse de sentiment",  "Status Code": 200}
    logging.info("réalisé le 5/02/21" )
    return result

@app.post("/sentiment")
async def sentiment(token:str,text:str):
    print("test " + token)
    #return {"token":token, "text":text}
    if token != "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9":
        response = {"Message" : "Token Invalide", "Status Code": 422} 
        logging.error("token invalide, erreur 422")    
        return response    

    clf_pipe = load('pipeline_optimiser.joblib')
    prediction = clf_pipe.predict([text])[0]
    prediction = "Positif" if prediction == 1 else "Négatif"
    logging.info("application reussi")
    return ({
                "text" : text,
                "prediction" : prediction,
                "Status Code": 200
        }
        )
    


if __name__ == "__main__":
    uvicorn.run("example:app", host="127.0.0.1", port=8000, log_level="info")




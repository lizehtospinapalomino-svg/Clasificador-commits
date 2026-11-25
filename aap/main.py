from fastapi import FastAPI
from pydantic import BaseModel
import os, re 

app= FasTAPI(title="Clasificador de Comits - Perfil C") 

class Commit (BaseModel) :
    mensaje: str 
 
def clasificador_eco(mensaje:str): 
    m=mensaje.lower() 
 if "fix" in m oe "error" in m or "corrige" in m: 
  return "fix" 
if "feat" in m or "nueva" in m:
  return "feat"
  if "docs" in m or "readme" in m: 
    returm "docs"
  return "chore"   

@app.post("/clasificar")
def clasificar(c: Commit): 
  tipo = clasificador_eco(c.mensaje)
  return {"tipo": tipo, 
  "mensaje_eco": f"{tipo}: {c.mensaje}"}

   

          
          


          
  
  
     










  

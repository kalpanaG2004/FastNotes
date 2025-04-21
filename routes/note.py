from fastapi import APIRouter
from models.note import Note
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
from config.db import conn
from schemas.note import noteEntity, notesEntity
from fastapi.templating import Jinja2Templates
from bson import ObjectId


note = APIRouter()
templates = Jinja2Templates(directory="templates")

@note.get("/", response_class=HTMLResponse)
async def read_home(request: Request):
    # docs = conn.notes.notes.find_one({})
    # print(docs)
    # OR
    docs = conn.notes.notes.find({})
    newDocs = []
    for doc in docs:
        newDocs.append({
            "id": doc.get("_id"),  # Use .get() to avoid KeyError
            "title": doc.get("title"),  # Default to "Untitled" if missing
            "desc": doc.get("desc"),  
            "important": doc.get("important")  # Default to False if missing
        })
    # return templates.TemplateResponse(request=request, name="index.html")
    return templates.TemplateResponse("index.html", {"request": request, "newDocs": newDocs})

@note.post("/")
async def create_item(request: Request):
    form = await request.form()
    
    title = str(form.get("title")).strip()
    desc = str(form.get("desc")).strip()
    important = form.get("important") == "on"

    note_data = {
        "title": title,
        "desc": desc,
        "important": important
    }

    result = conn.notes.notes.insert_one(note_data)
    # return {"Success": True}
    return RedirectResponse("/", status_code=303)

@note.get("/delete/{id}")
async def delete_note(id: str):
    conn.notes.notes.delete_one({"_id": ObjectId(id)})
    return RedirectResponse("/", status_code=303)

@note.put("/update/{id}")
async def update_note(id: str, request: Request):
    data = await request.json()
    title = data.get("title", "").strip()
    desc = data.get("desc", "").strip()
    important = data.get("important", False)

    conn.notes.notes.update_one(
        {"_id": ObjectId(id)},
        {"$set": {
            "title": title,
            "desc": desc,
            "important": important
        }}
    )
    return JSONResponse(content={"success": True})
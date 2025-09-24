from fastapi import APIRouter

router = APIRouter()

data = {
    "id": 0,
    "title": "string",
    "content": "string",
    "is_public": True,
    "is_completed": True,
    "created_at": "2025-09-24T12:53:15.914Z",
    "updated_at": "2025-09-24T12:53:15.914Z"
}


@router.post("/")  # POST /notes/ — создать заметку
async def notes():
    return {"message": "not implemented"}


@router.get("/")
async def notes():
    return {"message": "not implemented"}


@router.get('/notes/{note_id}')
async def get_note(note_id: int):
    return {"message": "not implemented", "id": note_id}


@router.patch("/notes/{note_id}")
async def note_update(note_id):
    return {"message": "not implemented", "id": note_id}


@router.delete("/notes/{note_id}")
async def note_delete(note_id):
    return {"message": "not implemented", "id": note_id}

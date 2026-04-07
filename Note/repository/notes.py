from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from .. import models, schemas

# Get all notes for current user with pagination
def get_all(db: Session, limit: int, skip: int, current_user: models.User):  # updated
    notes = (
        db.query(models.Note)
        .filter(models.Note.user_id == current_user.id)
        .limit(limit)
        .offset(skip)
        .all()
    )
    return notes

# Create a new note
def create(request: schemas.NoteCreate, db: Session, current_user: models.User):  # updated
    new_note = models.Note(
        title=request.title,
        body=request.body,
        user_id=current_user.id
    )
    db.add(new_note)
    db.commit()
    db.refresh(new_note)
    return new_note

# Delete a note by id (only if it belongs to current user)
def destroy(id: int, db: Session, current_user: models.User):  # updated
    note_query = db.query(models.Note).filter(
        models.Note.id == id,
        models.Note.user_id == current_user.id
    )
    note = note_query.first()
    if not note:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Note not found"
        )

    note_query.delete(synchronize_session=False)
    db.commit()
    return {"detail": "Note deleted"}

# Update a note by id (only if it belongs to current user)
def update(id: int, request: schemas.NoteCreate, db: Session, current_user: models.User):  # updated
    note_query = db.query(models.Note).filter(
        models.Note.id == id,
        models.Note.user_id == current_user.id
    )
    note = note_query.first()
    if not note:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Note not found"
        )

    note_query.update(request.dict())
    db.commit()
    db.refresh(note)
    return note

# Get a single note by id (only if it belongs to current user)
def show(id: int, db: Session, current_user: models.User):  # updated
    note = (
        db.query(models.Note)
        .filter(models.Note.id == id, models.Note.user_id == current_user.id)
        .first()
    )
    if not note:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Note not found"
        )
    return note
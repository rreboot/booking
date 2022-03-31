from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from booking import crud, schemas
from booking.api.deps import get_db

router = APIRouter()


@router.get('/complex/', response_model=list[schemas.Complex])
def read_complex_list(db: Session = Depends(get_db)):
    complex_list = crud.get_complex_list(db)
    return complex_list


@router.post('/complex/', response_model=schemas.Complex)
def create_complex(complex: schemas.ComplexCreate, db: Session = Depends(get_db)):
    return crud.create_complex(db, complex)

from sqlalchemy.orm import Session

from booking import models, schemas


def get_complex_list(db: Session):
    return db.query(models.Complex).all()


def create_complex(db: Session, complex: schemas.ComplexCreate):
    db_complex = models.Complex(
        name=complex.name,
        description=complex.description,
        interval=complex.interval,
        price=complex.price
    )
    db.add(db_complex)
    db.commit()
    db.refresh(db_complex)

    return db_complex

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from infra.database import get_db
from domain.gecko import Gecko

router = APIRouter(
    prefix="/api/gecko",
)


@router.get("/")
def gecko_list(db: Session = Depends(get_db)):
    _gecko_list = db.query(Gecko).order_by(Gecko.create_date.desc()).all()
    return _gecko_list

from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import Session

from infra.database import get_db
from domain.gecko import Gecko
from src.api.dto.gecko_dto import GeckoRequestDto

router = APIRouter(
    prefix="/api/gecko",
)


@router.get("/")
def gecko_list(db: Session = Depends(get_db)):
    _gecko_list = db.query(Gecko).order_by(Gecko.create_date.desc()).all()
    return _gecko_list


@router.post("/")
def gecko_create(db: Session = Depends(get_db), gecko_dto: GeckoRequestDto = Body(embed=True)):
    gecko = Gecko(name=gecko_dto.name, price=gecko_dto.price, owner_id=gecko_dto.owner_id)
    db.add(gecko)
    db.commit()
    return gecko

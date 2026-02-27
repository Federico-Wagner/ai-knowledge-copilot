from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class EchoRequest(BaseModel):
    message: str


@router.get("/health")
async def health():
    return {"status": "ok"}


@router.post("/echo")
async def echo(request: EchoRequest):
    return {"echo": request.message}
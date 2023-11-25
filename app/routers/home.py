from fastapi import APIRouter
import logging

router = APIRouter(prefix='/home', tags=['home'])
LOGGER = logging.getLogger(__name__)

@router.get('/')
def welcome():
    LOGGER.info('home welcome')
    return 'home welcome'

@router.get('/test')
def test():
    LOGGER.info('test')
    return 'test'
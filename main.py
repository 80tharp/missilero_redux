from fastapi import FastAPI
from missilero.user import router as user_router
from missilero.system import router as system_router

app = FastAPI(title='Missilero Docs',
              version='1.0'
              )


app.include_router(user_router.router)

app.include_router(system_router.router)
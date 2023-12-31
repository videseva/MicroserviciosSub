from fastapi import FastAPI
from routes.notification import notification_api
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="notification API",
    description="a REST API using python and mysql",
    version="0.0.1",
  
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(notification_api)
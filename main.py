from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import questions
from database import create_tables

app = FastAPI()

# Include the item router
app.include_router(questions.router)

# Configure CORS
origins = [
    "http://localhost",
    "http://localhost:3000",  # Update with your React app's URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Create the database tables
create_tables()

# Start the application with uvicorn
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)

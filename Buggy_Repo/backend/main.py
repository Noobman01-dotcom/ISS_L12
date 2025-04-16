from fastapi import FastAPI
from routes.items import router as items_router
from routes.analytics import router as analytics_router
from routes.quiz import router as quiz_router

# FIXED: Added title, description, and version to FastAPI app for better API documentation
app = FastAPI(
    title="Multi-Page FastAPI App",
    description="A FastAPI application with multiple routers",
    version="1.0.0"
)

app.include_router(items_router, prefix="/items")
# FIXED: Added missing prefix to analytics_router - routes should be consistently organized
app.include_router(analytics_router, prefix="/analytics")
# FIXED: Added missing prefix to quiz_router - routes should be consistently organized
app.include_router(quiz_router, prefix="/quiz")

# FIXED: Replaced inappropriate comment with proper documentation
# Home route provides a welcome message
@app.get("/")  # FIXED: Changed route from "/home" to root "/" for better UX
async def get_home():
    return {"message": "Welcome to the Multi-Page FastAPI App!"}

from fastapi import FastAPI

app = FastAPI(
    title="SafeSphere AI",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "SafeSphere AI Backend Running"
    }
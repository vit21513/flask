import uvicorn




if __name__ == '__main__':
    uvicorn.run(
        "task2:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )


    @app.post("/tasks", response_model=list[Task])
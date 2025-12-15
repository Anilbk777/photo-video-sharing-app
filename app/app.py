from fastapi import FastAPI 

app = FastAPI
text_posts = {"1":{"title":"New Post", "content": "cool test post"}}

@app.get("/")
def root():
    return {"message": "Hello FastAPI"}


@app.get("/post")
def get_all_posts():
    return text_posts
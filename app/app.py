from fastapi import FastAPI ,HTTPException

app = FastAPI
text_posts = {"1":{"title":"New Post", "content": "cool test post"}}

@app.get("/")
def root():
    return {"message": "Hello FastAPI"}


@app.get("/post")
def get_all_posts():
    return text_posts


@app.get("/posts/{id}")
def get_post(id: int):

    if id not in text_posts:
        raise HTTPException(status_code=404, details="Post Not Found")
    return text_posts.get(id)
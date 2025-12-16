from fastapi import FastAPI ,HTTPException

app = FastAPI
text_posts = {
    
    "1":{"title":"New Post 1", "content": "cool test post 1"},
    "2":{"title":"New Post 2", "content": "cool test post 2"},
    "3":{"title":"New Post 3", "content": "cool test post 3"}

              }

@app.get("/")
def root():
    return {"message": "Hello FastAPI"}


@app.get("/post")
def get_all_posts(limit: int=None):
    if limit:
        return text_posts[:limit]
    return text_posts


@app.get("/posts/{id}")
def get_post(id: int):

    if id not in text_posts:
        raise HTTPException(status_code=404, details="Post Not Found")
    
    return text_posts.get(id)


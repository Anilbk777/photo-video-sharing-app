from fastapi import FastAPI ,HTTPException
from app.schemas import PostCreate, PostResponse

app = FastAPI()
text_posts = {
    
    "1":{"title":"New Post 1", "content": "cool test post 1"},
    "2":{"title":"New Post 2", "content": "cool test post 2"},
    "3":{"title":"New Post 3", "content": "cool test post 3"},
    "4":{"title":"New Post 3", "content": "cool test post 4"}

              }

@app.get("/")
def root():
    return {"message": "Hello FastAPI"}


@app.get("/post")
def get_all_posts(limit: int = None):
    if limit:
        return list(text_posts.values())[:limit]
    return text_posts


@app.get("/posts/{id}")
def get_post(id: int) -> PostResponse:

    if id not in text_posts:
        raise HTTPException(status_code=404, details="Post Not Found")
    
    return text_posts.get(id)

@app.post("/posts")
def create_post(post: PostCreate) -> PostResponse:
    new_post = {"title": post.title, "content":post.content}
    text_posts[max(text_posts.keys()) + 1] = new_post
    return new_post



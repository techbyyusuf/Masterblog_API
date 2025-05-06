# 📝 Blog API with Flask

This is a simple RESTful API built with Flask to manage blog posts. It supports creating, reading, updating, deleting, and searching posts. The posts are stored in memory as a list of dictionaries.

## 🚀 Features

- `GET /api/posts`: Get a list of all blog posts
- `POST /api/posts`: Create a new blog post
- `PUT /api/posts/<id>`: Update an existing post (title and/or content)
- `DELETE /api/posts/<id>`: Delete a post by ID
- `GET /api/posts/search?title=...&content=...`: Search posts by title or content (case-insensitive)

## 📦 Request & Response Examples

### Create a Post

`POST /api/posts`

```json
{
  "title": "My First Post",
  "content": "This is a blog post created with Flask."
}
```

### Update a Post

`PUT /api/posts/1`

```json
{
  "title": "Updated Title"
}
```

### Search Posts

`GET /api/posts/search?title=flask&content=api`

Returns a list of posts where the title or content contains the search term (case-insensitive).

---

## 🛠️ How to Run

1. Make sure you have Python 3 installed.
2. Install Flask:

```bash
pip install flask
```

3. Run the application:

```bash
python app.py
```

4. Access the API at `http://localhost:5002`

---

## 📄 Notes

- This app uses an in-memory list (`POSTS`). Data will reset when the server restarts.
- The project is for educational/demo purposes and does not include a database or authentication.

---

## 💡 Future Improvements

- Connect to a real database (e.g., SQLite, PostgreSQL)
- Add pagination to `GET /api/posts`
- Add user authentication
- Validate input fields (title/content length, type, etc.)

---

## 📬 Contact

For feedback or questions, feel free to reach out or open an issue!

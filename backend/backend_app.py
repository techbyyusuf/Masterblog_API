from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

POSTS = [
    {"id": 1, "title": "First post", "content": "This is the first post."},
    {"id": 2, "title": "Second post", "content": "This is the second post."},
]


@app.route('/api/posts', methods=['GET', 'POST'])
def get_posts():
    if request.method == 'POST':
        try:
            data = request.get_json()

            if not data or not data.get('title'):
                return jsonify({'error': 'Title is missing!'}), 400
            if not data.get('content'):
                return jsonify({'error': 'Content is missing!'}), 400

            new_post = {
                'id': max(post['id'] for post in POSTS) + 1 if POSTS else 1,
                'title': data['title'],
                'content': data['content']
            }

            POSTS.append(new_post)
            return jsonify(new_post), 201

        except Exception as error:
            return jsonify({'error': str(error)}), 500

    return jsonify(POSTS)


@app.route('/api/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    try:
        for i, post in enumerate(POSTS):
            if post['id'] == post_id:
                del POSTS[i]
                return jsonify({'message': f'Post with id {post_id} has been deleted successfully.'}), 200

        return jsonify({'error': f'No post with the id {post_id} found!'}), 404

    except Exception as error:
        return jsonify({'error': str(error)}), 500


@app.route('/api/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    for post in POSTS:
        if post['id'] == post_id:
            data = request.get_json()

            new_title = data.get('title')
            new_content = data.get('content')

            if new_title:
                post['title'] = new_title
            if new_content:
                post['content'] = new_content

            return jsonify(post), 200

    return jsonify({'error': f'Post with id {post_id} not found'}), 404


@app.route('/api/posts/search', methods=['GET'])
def search_posts():
    searched_title = request.args.get('title')
    searched_content = request.args.get('content')

    if not searched_title and not searched_content:
        return jsonify([]), 200

    if searched_title and searched_content:
        filtered_posts = [
            post for post in POSTS if (
                    searched_title.lower() in post['title'].lower() or
                    searched_content.lower() in post['content'].lower())
      ]
        return jsonify(filtered_posts), 200

    elif searched_title:
        filtered_posts = [
            post for post in POSTS if searched_title.lower() in post['title'].lower()
        ]
        return jsonify(filtered_posts), 200

    elif searched_content:
        filtered_posts = [
            post for post in POSTS if searched_content.lower() in post['content'].lower()
        ]
        return jsonify(filtered_posts), 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=True)

from flask import Flask, request, jsonify
import redis

app = Flask(__name__)
redis_client = redis.Redis(host='db', port=6379, db=0, decode_responses=True)

@app.route('/add_points', methods=['POST'])
def add_points():
    data = request.get_json()
    club_name = data.get('club_name')
    points = data.get('points')
    if club_name and points is not None:
        redis_client.zadd('football_clubs', {club_name: points}, incr=True)
        return jsonify({'message': f'Points added to {club_name}'}), 200
    else:
        return jsonify({'error': 'Club name and points are required'}), 400


@app.route('/get_clubs', methods=['GET'])
def get_clubs():
    clubs = redis_client.zrevrange('football_clubs', 0, -1, withscores=True)    
    clubs_list = [
        {
            'club_name': club[0].decode('utf-8') if isinstance(club[0], bytes) else club[0], 
            'points': float(club[1])
        } for club in clubs
    ]    
    clubs_sorted = sorted(clubs_list, key=lambda x: (-x['points'], x['club_name']))
    return jsonify(clubs_sorted), 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)

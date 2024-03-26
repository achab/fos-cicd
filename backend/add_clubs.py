import requests

with open('ranking.txt', 'r') as f:
    for line in f.readlines():
        club_name, points = line.strip().split(',')
        data = {'club_name': club_name, 'points': int(points)}
        response = requests.post('http://localhost:5000/add_points', json=data)
        if response.status_code == 200:
            print(f"Added {points} for {club_name}")
        else:
            print(f"Failed to add points for {club_name}")
            print(f"Response status code: {response.status_code}")
            print(f"Response content: {response.content}")

print("Finished adding points for all clubs")
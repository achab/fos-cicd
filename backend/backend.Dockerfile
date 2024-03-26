FROM python:3.7-alpine
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "backend.py"] && ["python", "add_clubs.py"] 

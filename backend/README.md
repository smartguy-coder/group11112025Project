# migrations

-    ~/Desktop/group11112025Project/backend/app    libs !4 ···· ✔  backend   3.12    19:31:58  
╰─ uv run alembic init migrations
- inside docker container
╰─ alembic revision --autogenerate -m 'init'
- inside docker container
╰─ alembic upgrade head
- inside docker container
╰─ alembic downgrade -1

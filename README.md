# FastAPI Dockerized Project

## Local Development

```bash
docker-compose up --build
```

App will be available at http://localhost:8000

## Production Build

```bash
docker build -t fastapi-app .
docker run -d -p 8000:8000 fastapi-app
```

## Logs

Logs are written to the `logs/app.log` file.

## Deploying to AWS

1. Push this repo to your GitHub or CodeCommit.
2. Use AWS ECS, EC2, or Elastic Beanstalk to deploy the Docker image.
3. For ECS/Beanstalk, set up a task/service using the production Dockerfile.
4. Make sure to map port 8000 and set up security groups.

## Nginx (Optional)

For production, you may want to use Nginx as a reverse proxy. See `nginx.conf` for a sample config. 
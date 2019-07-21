# Celebrity Match Backend
docker-flask-json scaffolds a Hello World Python Flask json api app with docker and docker-compose.

## Check `docker` Installation

```bash
docker -v
docker-compose -v
```

## Clone and Run `celebrity-twin-backend`

```bash
git clone https://github.com/sinmat/celebrity-twin-backend.git
cd celebrity-twin-backend
docker-compose up
```

### Access the Web App

Open `localhost:5000/data?q={"name":"World"}` in a web browser

```json
{"result":"Hello World!"}
```

## Resources
- [Python](https://www.python.org/)
- [Flask](http://flask.pocoo.org/)
- [docker](https://www.docker.com/)
- [docker-compose](https://docs.docker.com/compose/overview/)
- [python docker image](https://hub.docker.com/_/python/)

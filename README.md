# Obers-API

### Getting started

1 - Clone the repository
`git clone https://github.com/SamuelXSS/obers-api`

2 - Backend Docker Build
```sh
$ cd app/src
$ docker build -t obers-api:v1 .
$ docker run --publish 9095:9095 --detach --name api obers-api:v1
```

Testing API health: 
```sh
curl "0.0.0.0:9095/health"
```
3 - Frontend
```sh
$ cd public
$ yarn OR npm install
$ ng serve
```




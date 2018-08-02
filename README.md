# restapi-example-Django


### 개발버전 패키지 설치
`pip install -r requirements/development.txt`


### 프로덕션 버전 패키지 설치
`pip install -r requirements.txtpip install -r`

### 환경변수
- `env.example` 참조
- Docker 환경변수 `./docker/prod/docker.env.example` 참조


### Docker-Compose

- Docker-compose 이용하여 프로덕션 환경 셋팅
- 호스트 80 포트와 80포트 연결

```bash
$ cd docker
$ docker-compose up -d
```
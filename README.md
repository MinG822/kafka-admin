# Kafka Admin 기능 확인

## 목적
카프카 토픽과 그룹을 confluent kafka 패키지로 확인하기

## 환경 & 의존성
- mac os
- python: 3.10.6
- confluentinc/cp-zookeeper:7.0.1
- confluentinc/cp-kafka:7.0.1
- confluent-kafka: 1.9.2

## 실행파일
- dashboard.py : 브로커와 토픽 메타데이터 확인
- create_topic.py : conf 에 세팅된 TOPIC_NAME 과 INITIAL_PARTITION으로 토픽을 생성
- delete_topic.py : conf 에 세팅된 TOPIC_NAME 으로 토픽삭제, 토픽이 없을 경우 에러발생
- create_partition.py : conf 에 세팅된 TOPIC_NAME 의 토픽을 INCREASED_PARTITION 만큼 증가, 토픽이 없거나 기존의 파티션보다 작으면 에러발생

## 실행방법
- 테스트하려는 환경에 맞춰 conf 파일 변경, 또는 환경 변수 세팅
```
python3 dashboard.py
python3 create_topic.py
python3 dashboard.py
python3 create_partition.py
python3 dashboard.py
pythno3 delete_topic.py
python3 dashboard.py
```
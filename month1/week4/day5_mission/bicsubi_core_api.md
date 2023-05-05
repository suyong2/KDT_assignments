# Mission 1. My New Assistant
## Core Mission

API 문서

GET /whoami

사용자 이름 "suyong2"를 반환합니다.


Response
{
    "name": "suyong2"
}

GET /echo?string={문자열}

입력 문자열 값을 반환합니다.


Response
{
    "value": "string"
}


POST /weapons

주어진 이름과 재고로 새로운 weapon를 만듭니다.


request 본문
{
    "name": "string",
    "stock": "integer"
}

Response
새로 생성된 weapons의 세부 정보가 포함된 JSON 개체를 반환합니다.
{
    "weapons": [
        {
            "id": "integer",
            "name": "string",
            "stock": "integer"
        }
    ]
}


GET /weapons 가져오기

모든 weapons의 세부 정보를 반환합니다.


Response
모든 weapons의 세부 정보가 포함된 JSON 개체를 반환합니다.
{
    "weapons": [
        {
            "id": "integer",
            "name": "string",
            "stock": "integer"
        },
        ...
    ]
}


PUT /weapons/{id}

id로 식별되는 특정 weapons의 세부 정보를 업데이트합니다.


request 본문
{
    "name": "string",
    "stock": "integer"
}

Response
지정된 weapons의 업데이트된 세부 정보가 포함된 JSON 개체를 반환합니다.
{
    "weapons": [
        {
            "id": "integer",
            "name": "string",
            "stock": "integer"
        },
        ...
    ]
}

DELETE /weapons/{id}

id로 식별되는 특정 weapons를 삭제합니다.


Response
지정된 weapons의 업데이트된 세부 정보가 포함된 JSON 개체를 반환합니다.
{
    "weapons": [
        {
            "id": "integer",
            "name": "string",
            "stock": "integer"
        },
        ...
    ]
}



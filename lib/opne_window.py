from obswebsocket import obsws

# OBS WebSocket 서버에 연결
ws = obsws("localhost", 4455, "QyyCJmsrsl9yMl4v")  # OBS의 주소와 포트 번호 입력
ws.connect()

# 텍스트 소스 변경
scene_name = "bits"  # 텍스트를 변경할 장면 이름 입력
source_name = "bits msg"  # 텍스트를 변경할 소스 이름 입력
new_text = "New Text"  # 새로운 텍스트 입력


# SetSourceSettings 요청 보내기
source_settings = {"text": new_text}
ws.call("SetTextGDIPlusProperties")

# 연결 종료
ws.disconnect()
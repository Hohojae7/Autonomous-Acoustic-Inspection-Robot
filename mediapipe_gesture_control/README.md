# MediaPipe Gesture Control

Jetson Orin Nano에 연결된 카메라에서 손을 인식하고 TurtleBot3 수동 조작 명령을 제공하는 Flask 애플리케이션입니다.

## 구성

```text
mediapipe_gesture_control/
├── src/             캡처, MediaPipe 추론, 후처리, 제스처 판정, Flask 서버
├── configs/         카메라와 제스처 파라미터
├── models/weights/  MediaPipe Hand Landmarker 모델 위치
├── scripts/         서버 실행과 모델 다운로드 도구
├── tests/           하드웨어 없이 실행하도록 작성된 제스처 단위 테스트
├── docs/            최종 제스처와 제어권 전환 설명
└── requirements.txt
```

핵심 진입점은 `python -m src.server.app`입니다. 서버는 `/cmd`, `/video_feed`, `/health` 엔드포인트를 제공하며 ROS 2 쪽 `cmd_vel_bridge.py`가 `/cmd`를 읽습니다.

`hand_landmarker.task`는 저장소에 포함하지 않습니다. `python scripts/download_weights.py`로 내려받도록 구성되어 있습니다.

기존 Python 모듈의 `src.*` import 구조를 보존하기 위해 내부 `src/` 폴더 이름은 바꾸지 않았습니다.

이 디렉터리는 ROS 2 패키지가 아니라 독립 AI 서비스입니다. ROS 2 연동 코드는 `src/turtlebot3_inspection_control/ros2_bridge/cmd_vel_bridge.py`에 있으며, 최종 제스처 표는 [`docs/GESTURES.md`](docs/GESTURES.md)에 정리했습니다.

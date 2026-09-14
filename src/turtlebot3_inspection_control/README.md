# turtlebot3_inspection_control

기존 `ros2_bridge/`에서 최종 비-Safety 통합에 필요한 ROS 2 노드만 모은 ament_python 패키지입니다.

| 파일 | 역할 |
| --- | --- |
| `cmd_vel_bridge.py` | MediaPipe Flask 서버 명령을 ROS 2 속도 명령으로 변환 |
| `cmd_vel_mux.py` | Nav2, 제스처, 조이스틱, 장갑 입력 중 활성 속도 소스를 선택 |
| `wifi_glove_teleop.py` | ESP32·MPU6050 UDP 장갑 입력을 Twist로 변환 |
| `glove_gyro.py` | 장갑 패킷 파싱과 보정 공용 함수 |
| `waypoint_handoff_mission.py` | 자율주행과 수동 조작 사이의 웨이포인트 핸드오프 |
| `waypoint_coordinate_sampler.py` | 웨이포인트 좌표 수집 도구 |

최종 통합에서 Wi-Fi 장갑은 컨트롤러 모드에 묶였습니다. 스틱을 실제로 움직일 때는 조이스틱이 우선하고, 스틱이 중립이면 장갑 입력을 선택합니다. 장갑 입력이 0.35초 이상 끊기면 장갑 노드가 정지 명령을 냅니다.

`test/`에는 브리지·MUX·장갑 단위 테스트와 control 미션·bringup launch를 함께 확인하는 웨이포인트 통합 테스트가 있습니다.

핵심 노드 내용은 기존 통합 폴더에서 최대한 그대로 옮겼습니다. 기존 직접 실행 방식에 맞춘 실제 장비 경로와 실행 체인은 복구하지 않았으므로 재배치 후 실행을 보장하지 않습니다.

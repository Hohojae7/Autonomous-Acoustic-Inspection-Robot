# 소음 이상 감지 현장 검증 요약

2026-08-23 Jetson Orin Nano에서 C270 웹캠 내장 마이크, TurtleBot3 OpenCR, LiDAR와 전체 시연 구성을 함께 구동하며 남긴 최종 검증 결과를 정리했습니다. 아래 내용은 당시 하드웨어 세션의 기록이며 재배치된 저장소의 실행 보장을 뜻하지 않습니다.

## 검증 구성

- 첫 번째 C270 마이크를 PortAudio 장치 `0`으로 사용
- 캡처 48 kHz, 모델 입력 16 kHz, 3초 판정 창, 임계값 0.500
- OpenCR는 `/dev/ttyACM0`, LDS-03 LiDAR는 `/dev/ttyUSB0` 사용
- 소음 상태는 `/sound_anomaly_node/state`, LED 모드는 `/opencr_led_status`에서 확인

## 판정 및 LED 결과

| 입력 상태 | 이상 확률 예시 | 판정 | LED 모드 |
| --- | ---: | --- | ---: |
| 초기 정상 소리 | 0.438 | `NORMAL` | 2, GPIO 50 초록 점멸 |
| 이상 소리 | 0.519 / 0.550 | `ABNORMAL` | 3, GPIO 51 빨강 점멸 |
| 정상 복귀 | 0.478 / 0.450 | `NORMAL` | 2, GPIO 50 초록 점멸 |

이상 소리 입력 시 빨강 LED로 전환되고 이후 정상 상태로 복귀하는 것을 실제 장비에서 확인했습니다.

## 안정화 반영

- C270 입력 blocksize를 48,000(약 1초), 큐를 16블록, 처리 주기를 0.25초로 조정했습니다. 해당 값은 `turtlebot3_inspection_bringup/launch/sound_anomaly_with_led.launch.py`에 남아 있습니다.
- `gearbox_svm_runtime_sklearn_1_7.joblib`을 scikit-learn 1.7.2 런타임용으로 보존했습니다. 원본과 120개 특징 고정 입력의 `predict_proba` 및 모델 메타데이터가 같은지 비교했고, 호환 사본 재로딩 시 버전 경고가 없음을 확인했습니다.
- 단독 실행기는 기존 TurtleBot3/OpenCR 프로세스를 재사용하고 ROS discovery 안정화 시간을 두도록 조정했습니다.

최종 45초 이상 재검증에서 소음 노드와 TurtleBot3·LiDAR 프로세스가 함께 유지됐고, `InconsistentVersionWarning`, 오디오 큐 포화, 입력 overflow, 추론 실패가 새 로그에 나타나지 않았습니다. `NORMAL` 상태와 LED 모드 2도 토픽에서 확인했습니다.

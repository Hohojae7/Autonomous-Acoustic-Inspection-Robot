<div align="center">

# Autonomous Acoustic Inspection Robot (AAIR)

### 협소·위험 구역 자율순찰 이상음 감지 로봇

TurtleBot3가 지정 구역을 자율 순찰하고 설비음을 수집·분석하여<br />
정상·이상 상태를 판정하고 현장에 알리는 산업 점검 로봇 프로젝트

<p>
  <img src="https://img.shields.io/badge/ROS_2-Humble-22314E?style=for-the-badge&logo=ros&logoColor=white" alt="ROS 2 Humble" />
  <img src="https://img.shields.io/badge/ROBOTIS-TurtleBot3_Burger-00A6D6?style=for-the-badge" alt="TurtleBot3 Burger" />
  <img src="https://img.shields.io/badge/NVIDIA-Jetson_Orin_Nano-76B900?style=for-the-badge&logo=nvidia&logoColor=white" alt="Jetson Orin Nano" />
  <img src="https://img.shields.io/badge/Acoustic_AI-MFCC_%2B_SVM-F5A623?style=for-the-badge" alt="MFCC and SVM" />
</p>

<a href="https://www.youtube.com/watch?v=Mjf2t31ZWa0">
  <img src="https://img.shields.io/badge/YouTube-Project_Demo-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="프로젝트 시연 영상" />
</a>

</div>

---

## 1. 프로젝트 소개

> AAIR는 **자율순찰**, **설비음의 실시간 정상·이상 판정**, **작업자 수동 개입**, **결과 알림**을 하나의 TurtleBot3 플랫폼에서 운용한 프로젝트입니다.<br />
> 작업자의 반복적인 위험 구역 접근과 청감 중심의 설비 점검을 줄이고, 동일한 절차와 기준으로 1차 점검을 수행하는 것을 목표로 합니다.

산업 현장에는 작업자가 직접 접근하기 어렵거나 장시간 머물기 부담스러운 협소 구역이 존재합니다. AAIR는 TurtleBot3 Burger에 자율주행, 음향 AI, 수동 보조제어를 결합하여 작업자가 현장에 들어가기 전에 설비 상태를 먼저 확인할 수 있도록 구성했습니다.

| 현장 문제 | 시스템 대응 | 구현 방식 |
| --- | --- | --- |
| 협소·위험 구역의 반복적인 직접 점검 | 작업자의 현장 노출 시간 감소 | SLAM 지도와 Nav2 기반 Waypoint 자율순찰 |
| 작업자마다 달라질 수 있는 점검 절차 | 반복 가능한 순찰·점검 흐름 구성 | 지정 경로 순찰과 동일한 음향 판정 Pipeline 운용 |
| 고소음 환경의 청감 중심 판단 | 설비음 기반 1차 이상 판정 보조 | Microphone, MFCC 특징 추출, SVM 이진 분류 |
| 자율주행 예외 상황과 좁은 통로 | 작업자 수동 개입과 자율주행 복귀 | MediaPipe 손 제스처, IMU 장갑, AUTO/MANUAL 전환 |

---

## 2. 프로젝트 목표

- 협소·위험 구역의 반복적인 1차 점검을 이동 로봇 기반 자율순찰로 수행
- 지정 경로 순찰과 동일한 음향 처리 과정을 적용해 반복 가능한 점검 절차 구현
- 자율순찰이 어려운 구간에서 제스처 또는 IMU 장갑으로 수동 제어한 뒤 자율주행 복귀
- 설비음의 정상·이상 상태를 판정하고 ROS 2 Terminal 및 Green/Red LED로 결과 출력
- 센서 입력, 이동 제어, 음향 판정, 상태 출력을 ROS 2 기반 하나의 운용 흐름으로 통합

---

## 3. 주요 기능

| 구분 | 주요 내용 |
| --- | --- |
| **3-1. 자율순찰** | **지도 생성 및 위치 추정**: SLAM Toolbox로 지도를 생성하고 AMCL로 현재 위치를 추정<br />**Waypoint 주행**: Nav2 `FollowWaypoints`와 `NavigateToPose`를 이용해 지정 경로를 순찰<br />**순찰 복귀**: 최종 시나리오 기준 A-B-C-D-A 구간의 이동과 제어권 전환 수행 |
| **3-2. 음향 이상 감지** | **실시간 음향 입력**: Webcam 내장 마이크의 입력을 연속 수집하여 일정 구간 단위로 처리<br />**특징 추출 및 분류**: 설비음에서 MFCC 특징을 계산하고 SVM으로 `NORMAL`과 `ABNORMAL` 분류<br />**상태 발행**: 이상 확률과 판정 상태를 ROS 2 Topic으로 발행 |
| **3-3. 결과 확인 및 경고** | **현장 표시**: 정상 상태는 Green LED, 이상 상태는 Red LED로 구분<br />**상태 확인**: ROS 2 Terminal Log와 Topic을 통해 판정 상태와 이상 확률 확인<br />**위치 확인**: RViz2에서 지도, 로봇 위치, 이동 경로 확인 |
| **3-4. 수동 보조제어** | **손 제스처 제어**: MediaPipe Hand Landmarker의 손 랜드마크를 제어 명령으로 변환<br />**IMU 장갑 제어**: ESP32와 MPU6050이 측정한 손목의 Roll·Pitch를 Wi-Fi UDP로 전송<br />**조이스틱 지원**: 컨트롤러 모드에서 조이스틱과 IMU 장갑 입력을 선택적으로 사용 |
| **3-5. 통합 운용** | **AUTO/MANUAL 전환**: 자율순찰 중 작업자 개입이 필요한 구간에서 제어권 전환<br />**속도 명령 통합**: Nav2, 제스처, 조이스틱, 장갑의 속도 명령을 MUX로 조정<br />**웹 모니터링**: Flask 서버의 MJPEG 영상과 JSON 상태 API를 브라우저에서 확인 |

---

## 프로젝트 시연

### 모듈별 기능

<div align="center">
  <table>
    <tr>
      <td align="center" width="50%" valign="top">
        <img src="./docs/images/demo/01_autonomous_navigation.gif" width="100%" alt="TurtleBot3가 웨이포인트 구간을 자율 주행하는 시연" /><br />
        <strong>SLAM · AMCL · Nav2 자율주행</strong><br />
        <sub>AMCL로 위치를 추정하며 Nav2 웨이포인트 구간을 자율 주행합니다.</sub>
      </td>
      <td align="center" width="50%" valign="top">
        <img src="./docs/images/demo/02_mediapipe_gesture_control.gif" width="100%" alt="손가락 제스처로 TurtleBot3를 조작하는 시연" /><br />
        <strong>MediaPipe 손 제스처 제어</strong><br />
        <sub>카메라가 손 포즈를 인식해 TurtleBot3의 이동과 회전을 제어합니다.</sub>
      </td>
    </tr>
    <tr>
      <td align="center" width="50%" valign="top">
        <img src="./docs/images/demo/03_normal_sound_green_led.gif" width="100%" alt="정상음 판정 후 녹색 LED가 점멸하는 시연" /><br />
        <strong>정상음 판정 · Green LED</strong><br />
        <sub>MFCC · SVM 정상 판정 결과를 OpenCR의 녹색 외부 LED로 표시합니다.</sub>
      </td>
      <td align="center" width="50%" valign="top">
        <img src="./docs/images/demo/04_abnormal_sound_red_led.gif" width="100%" alt="이상음 판정 후 빨간 LED가 점멸하는 시연" /><br />
        <strong>이상음 판정 · Red LED</strong><br />
        <sub>MFCC · SVM 이상 판정 결과를 OpenCR의 빨간 외부 LED로 표시합니다.</sub>
      </td>
    </tr>
    <tr>
      <td align="center" width="50%" valign="top">
        <img src="./docs/images/demo/05_narrow_passage_gesture_control.gif" width="100%" alt="TurtleBot3가 제스처 제어로 테이블 아래 협소 통로를 통과하는 시연" /><br />
        <strong>MediaPipe 협소 구간 주행</strong><br />
        <sub>제스처 수동 제어로 테이블 아래 협소 통로를 한 번에 통과합니다.</sub>
      </td>
      <td align="center" width="50%" valign="top">
        <img src="./docs/images/demo/06_imu_glove_control.gif" width="100%" alt="ESP32와 MPU6050 장갑으로 TurtleBot3를 조작하는 시연" /><br />
        <strong>ESP32 · MPU6050 Wi-Fi 장갑</strong><br />
        <sub>손목 기울기 입력을 Wi-Fi로 전달해 TurtleBot3를 수동 조작합니다.</sub>
      </td>
    </tr>
  </table>
</div>

### 시연 영상

---

<div align="center">

#### SW 파일럿 2기 로보틱스 1팀 스마트팩토리 소음 탐지 및 순찰 로봇

<a href="https://www.youtube.com/watch?v=Mjf2t31ZWa0">
  <img src="https://img.youtube.com/vi/Mjf2t31ZWa0/hqdefault.jpg" width="70%" alt="AAIR 프로젝트 시연 영상" />
</a>

<br />

<a href="https://www.youtube.com/watch?v=Mjf2t31ZWa0">
  <img src="https://img.shields.io/badge/YouTube-시연_영상_보기-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="YouTube에서 시연 영상 보기" />
</a>

</div>

---

### 시스템 아키텍처

#### Hardware Architecture

TurtleBot3 Burger의 이동 플랫폼과 Jetson Orin Nano를 중심으로 LiDAR, Camera, Microphone, OpenCR, LED, IMU 장갑을 연결했습니다. 완성된 플랫폼 구성을 보여주는 블록 다이어그램이며 세부 회로도는 포함하지 않았습니다.

<p align="center">
  <img src="./docs/images/hardware-architecture.png" width="90%" alt="AAIR 하드웨어 아키텍처" />
</p>

#### Software Architecture

ROS 2 Topic과 Action을 중심으로 Navigation, Patrol Control, Manual Control, Sound AI, Result/Alert 기능을 분리하고 필요한 Interface만 연결했습니다.

<p align="center">
  <img src="./docs/images/software-architecture.png" width="90%" alt="AAIR 소프트웨어 아키텍처" />
</p>

> 위 이미지는 최종발표에서 정의한 목표 아키텍처입니다. 현재 정리된 Source에서는 Navigation과 Sound Anomaly Node가 함께 실행되지만, Waypoint 도착 시점에만 음향 검사를 요청하는 Trigger는 별도 결합되어 있지 않습니다.

---

## 4. 시스템 구성

본 시스템은 **이동·연산 플랫폼**, **자율주행**, **음향 이상 감지**, **수동 보조제어**, **결과 출력**의 다섯 영역으로 구성됩니다.

### 하드웨어 구성

| 구성요소 | 역할 | 주요 연결 |
| --- | --- | --- |
| **TurtleBot3 Burger / OpenCR** | 차동구동 이동 플랫폼, Motor 및 Odometry 제어 | ROS 2, Dynamixel, USB |
| **Jetson Orin Nano** | ROS 2 Navigation, 음향 추론, 제스처 인식, 웹 서버 실행 | USB, Wi-Fi |
| **LDS-03 LiDAR** | 주변 거리 측정, 지도 작성, 위치 추정 | `/scan`, USB |
| **Dual Webcam / C270 내장 Microphone** | 두 대의 카메라를 이용한 손 제스처 영상과 설비음 입력 | USB, MJPEG |
| **Green / Red LED** | 정상·이상 판정 상태 표시 | OpenCR GPIO |
| **ESP32 + MPU6050 장갑** | 손목 자세 측정 및 수동 주행 명령 생성 | I2C, Wi-Fi UDP |
| **Game Controller** | 컨트롤러 모드의 수동 조작 입력 | USB, `/cmd_vel_joy` |

### 소프트웨어 및 데이터 흐름

| 계층 / 구성요소 | 역할 | 주요 Interface |
| --- | --- | --- |
| **SLAM Toolbox / AMCL / Nav2** | 지도 생성, 위치 추정, 경로 계획, Waypoint 이동 | `/scan`, `/odom`, `NavigateToPose`, `FollowWaypoints` |
| **Patrol Controller** | Waypoint와 운용 모드 관리, 자율·수동 구간의 제어권 전환 | Nav2 Action, mode state |
| **MediaPipe Gesture Engine** | 손 랜드마크 추론, 제스처 판정, 영상·상태 제공 | Flask `/cmd`, `/video_feed`, `/health` |
| **ROS 2 Control Bridge / MUX** | HTTP·UDP 입력을 `Twist`로 변환하고 활성 속도 소스를 선택 | `/cmd_vel_gesture`, `/cmd_vel_joy`, `/cmd_vel_glove`, `/cmd_vel_muxed` |
| **Sound Anomaly Node** | 마이크 입력, MFCC 특징 추출, SVM 정상·이상 분류 | `/sound_anomaly_node/state`, `/sound_anomaly_node/anomaly_probability` |
| **Result / Alert** | Terminal 상태 출력과 OpenCR LED 제어 | `/opencr_led_status` |
| **RViz2 / Web Browser** | 로봇 위치·경로 및 카메라·제어 상태 모니터링 | ROS 2 Visualization, MJPEG, JSON |

---

## 5. 개발 포인트

- **다중 제어 입력의 충돌 방지**: Nav2, 손 제스처, 조이스틱, IMU 장갑이 각자 별도 `cmd_vel` Topic을 사용하고, MUX가 선택한 하나의 명령만 TurtleBot3에 전달하도록 구성했습니다.
- **AUTO/MANUAL 제어권 전환**: A-B 구간의 Nav2 주행을 마친 뒤 B-C는 손 제스처, C-D는 컨트롤러 모드로 제어권을 넘기고, D 지점에서 새로운 Nav2 Goal을 발행해 A로 복귀하도록 상태기계를 구성했습니다.
- **음향 AI와 현장 출력의 연결**: 음향을 MFCC 특징으로 변환해 SVM으로 판정하고, 결과를 ROS 2 Topic과 OpenCR LED까지 전달하여 소프트웨어 판정을 현장에서 바로 확인할 수 있도록 했습니다.
- **제스처 엔진과 ROS 2의 분리**: MediaPipe 인식 파이프라인은 Flask 서비스로 독립 실행하고, ROS 2 Bridge가 HTTP 상태를 읽어 속도 명령으로 변환하도록 구성해 인식부와 로봇 제어부의 결합도를 낮췄습니다.
- **무선 장갑의 입력 안정화**: ESP32가 MPU6050 자세 데이터를 20 Hz UDP로 전송하고, 수신이 0.35초 이상 끊기면 정지 명령을 유지하도록 Fail-safe를 적용했습니다.
- **실기 환경의 통합 문제 해결**: Jetson 전원 공급 안정화, USB 장치 수 정리, Headless Display 구성, Odom/TF 재초기화, Nav2 복귀 로직 단순화를 통해 최종 시연 환경을 안정화했습니다.

---

## 6. 테스트 결과

> 정량 지표와 공개 범위는 팀 검토 후 추가할 예정입니다.

---

## 7. 담당 역할

> 팀원별 담당 기능과 통합 범위는 팀 협의 후 작성할 예정입니다.

<!--
| 이름 | 담당 역할 |
| --- | --- |
| 팀원 | 담당 기능 및 산출물 |
-->

---

## 8. 기술 스택

| 구분 | 기술 및 도구 |
| --- | --- |
| **Robot Platform** | TurtleBot3 Burger, Jetson Orin Nano, OpenCR, LDS-03 LiDAR |
| **Robotics / Middleware** | ROS 2 Humble, SLAM Toolbox, AMCL, Nav2, RViz2, `rclpy`, `rclcpp` |
| **Perception / Vision** | MediaPipe Hand Landmarker, OpenCV, Dual Camera Pipeline |
| **Acoustic AI** | MFCC, SVM, scikit-learn, librosa, NumPy, SoundDevice, Joblib |
| **Application / Monitoring** | Flask, MJPEG Streaming, HTTP/JSON API |
| **Embedded / Communication** | ESP32, MPU6050, Arduino, I2C, Wi-Fi UDP, GPIO |
| **Languages / Build** | Python, C++, Arduino C++, Bash, CMake, ament, colcon |

---

## 9. 프로젝트 의의

AAIR의 의미는 TurtleBot3에 개별 기능을 하나씩 붙인 데 있지 않습니다. **환경 인지와 이동, 설비음 판정, 작업자의 수동 개입, 결과 알림을 실제 운용 순서에 맞춰 하나의 로봇 시스템으로 연결했다는 점**에 있습니다.

작업자가 협소·위험 구역에 반복적으로 진입하고 경험적인 청감에 의존하던 1차 점검을, 로봇의 지정 경로 순찰과 일관된 음향 판정으로 보조했습니다. 또한 모든 구간을 자율주행만으로 처리한다고 가정하지 않고, 예외 상황에서 작업자가 제스처나 IMU 장갑으로 개입한 뒤 다시 자율주행으로 복귀하는 현실적인 운용 구조를 구현했습니다.

개발 과정에서는 Navigation, AI, Embedded, Web 기술을 각각 구현하는 데 그치지 않고 전원, USB 장치, Odom/TF, 입력 충돌과 같은 실제 하드웨어 통합 문제를 해결했습니다. 이 과정을 통해 로봇 프로젝트의 완성도는 단일 알고리즘보다 **여러 기능을 안정적으로 연결하고 끝까지 동작시키는 시스템 통합**에서 결정된다는 점을 확인했습니다.

---

## 10. 아쉬웠던 점 및 개선 방향

- **현장 데이터 확장**: 설비별 정상·이상 음원을 다시 수집하고 재학습하여 실제 환경에서의 판정 신뢰도 개선
- **점검 이력 관리**: 로봇 Pose, Timestamp, 판정 결과를 DB에 저장하고 Dashboard에서 조회하는 기능 추가
- **장시간 운용 검증**: 반복 순찰, 제어권 전환, 위치 추정 복구를 장시간 조건에서 검증하고 Recovery Logic 보완
- **배포 환경 정리**: 기존 시연 장비의 절대경로를 현재 저장소 구조에 맞게 수정하고 재현 가능한 실행 절차 제공
- **Firmware 보존**: 최종 시연에 사용한 OpenCR LED Firmware 원본을 확보하고 Build·Upload 절차 문서화

> 세부 회고와 우선순위는 팀원 의견을 반영해 최종 확정할 예정입니다.

### 10-1. 저장소 구조

```text
.
├── src/                           ROS 2 패키지
├── mediapipe_gesture_control/     MediaPipe 제스처 인식 Flask 애플리케이션
├── firmware/                      ESP32 장갑 및 OpenCR 관련 자료
├── scripts/                       최종 시연·기능별 실행 및 설치 스크립트
├── docs/                          프로젝트 문서와 README 이미지
└── tools/opencr_updater/          OpenCR 업데이트 도구와 보관 바이너리
```

| 경로 | 주요 내용 |
| --- | --- |
| [`src/turtlebot3_inspection_bringup`](src/turtlebot3_inspection_bringup) | TurtleBot3, Nav2, Sound AI 통합 Launch와 지도·RViz 설정 |
| [`src/turtlebot3_inspection_control`](src/turtlebot3_inspection_control) | 속도 MUX, 제스처 Bridge, Wi-Fi 장갑, Waypoint Handoff |
| [`src/turtlebot3_waypoint_patrol`](src/turtlebot3_waypoint_patrol) | A-B-C-D-A Waypoint 순찰 Node |
| [`src/sound_anomaly_node`](src/sound_anomaly_node) | MFCC·SVM 학습·추론 코드와 ROS 2 Sound Anomaly Node |
| [`mediapipe_gesture_control`](mediapipe_gesture_control) | MediaPipe Hand Landmarker, Camera Pipeline, Flask Server |
| [`firmware/esp32_mpu6050_glove`](firmware/esp32_mpu6050_glove) | ESP32·MPU6050 Wi-Fi UDP 장갑 Firmware |
| [`scripts/final_demo`](scripts/final_demo) | 최종 비-Safety 통합 시연 실행 Chain |

> 이 저장소는 당시 여러 Workspace에 흩어진 결과물을 역할별로 재배치한 정리본입니다. 기존 실행 파일에는 시연 장비의 절대경로가 남아 있어 현재 구조에서의 Build와 실행은 별도 확인이 필요합니다.

프로젝트의 최종 동작 흐름은 [`docs/PROJECT_CONTEXT.md`](docs/PROJECT_CONTEXT.md), 제스처와 제어권 전환은 [`mediapipe_gesture_control/docs/GESTURES.md`](mediapipe_gesture_control/docs/GESTURES.md), 음향 감지 검증 기록은 [`src/sound_anomaly_node/docs/VALIDATION.md`](src/sound_anomaly_node/docs/VALIDATION.md)에서 확인할 수 있습니다.

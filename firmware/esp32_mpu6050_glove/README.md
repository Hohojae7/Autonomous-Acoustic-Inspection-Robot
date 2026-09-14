# ESP32 MPU6050 장갑 송신기

`esp32_mpu6050_glove.ino`는 제공한 `esp32_test_code_bundle.pdf`의
`main/esp32_test.c`를 Arduino IDE에서 바로 올릴 수 있게 옮긴 것이다. MPU6050의
자세를 20Hz로 USB 직렬과 Wi-Fi UDP로 보낸다. Wi-Fi 수신 노드가 데이터를 TurtleBot3의
`/cmd_vel_glove`로 변환한다. 게임 컨트롤러와 USB 데이터 케이블은 필요 없다.

## 배선

ESP32 기본 I2C 핀을 쓴다.

| MPU6050 | ESP32 |
| --- | --- |
| VCC | **3V3** |
| GND | GND |
| SDA | GPIO 21 |
| SCL | GPIO 22 |
| INT | 연결하지 않음 |

이 원본 코드는 MPU6050 주소 `0x68`만 사용한다. AD0는 GND에 둬야 하며, GPIO 21/22
이외의 핀은 탐색하지 않는다. 5V I2C 신호는 ESP32 핀에 연결하지 않는다.

## 업로드와 주행

1. Arduino IDE에서 보드를 ESP32 Dev Module로 선택하고 이 `.ino` 파일을 연다.
2. `wifi_config.h`에는 장갑과 TurtleBot 컴퓨터가 함께 접속할 **하나의 Wi-Fi**만
   설정한다. 펌웨어는 부팅마다 이전 AP 설정을 지우고 이 SSID/비밀번호로만
   연결을 시도하므로 다른 Wi-Fi에는 자동 연결하지 않는다. 수신 컴퓨터 IP는 ROS
   수신기가 자동 발견하므로 고정 IP를 맞출 필요가 없다. 이 파일에는 비밀번호가
   있으므로 공유하지 않는다.
3. 업로드 뒤 장갑 ESP32에는 배터리나 USB 전원만 연결한다. TurtleBot 컴퓨터와
   데이터 USB로 연결하지 않는다.
4. 장갑은 처음 약 2초 동안 수평 중립 자세로 유지한다. ESP32 자이로 보정 후 ROS
   중립 보정이 이어진다.
5. 바퀴를 든 상태에서 기록용 실행기를 확인한다. 이 실행기는 당시 절대경로를 포함하므로 재배치 후 실행을 보장하지 않는다.

   ```bash
   bash scripts/component_demos/run_glove_wifi_drive.sh --usb-port /dev/ttyACM0
   ```

앞으로 기울이면 전진, 뒤로 기울이면 후진, 오른쪽/왼쪽 기울이면 우/좌회전이다.
방향이 반대면 실행 명령에 `--invert-pitch` 또는 `--invert-roll`을 넣는다.
Wi-Fi 연결이나 MPU6050 읽기가 끊기면 ESP32가 값 전송을 멈추며, ROS 노드와 mux가
0.35초 안에 정지 명령을 유지한다. ESP32의 직렬 모니터에 `MPU6050 not detected`가
계속 나오면 LED 점등과 무관하게 I2C 통신이 안 되는 상태이므로 주행을 시작하면 안 된다.

## 최종 통합 규칙

- ESP32 업로드 때 사용한 `/dev/ttyUSB0`은 전체 시스템 구동 중 LDS-03 LiDAR가 사용하는 포트였다. 업로드 후 장갑은 데이터 USB에서 분리하고 별도 전원으로 사용한다.
- 최종 실행기는 장갑 수신 노드에 `--invert-pitch`와 `--controller-mode-only`를 적용했다.
- 장갑은 OK 사인으로 들어가는 컨트롤러 모드에서만 주행 명령을 낸다.
- 컨트롤러 모드에서 조이스틱 스틱이 움직이는 동안에는 조이스틱이 우선하고, 스틱이 중립이면 장갑 입력을 사용한다.
- 수신 후 약 2초간 중립 자세를 보정하며 UDP 입력이 0.35초 이상 끊기면 정지한다.

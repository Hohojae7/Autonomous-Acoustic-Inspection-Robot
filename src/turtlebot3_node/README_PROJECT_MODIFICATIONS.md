# Project-specific TurtleBot3 node changes

이 폴더는 ROBOTIS TurtleBot3 소스 중 프로젝트가 수정한 `turtlebot3_node` 패키지만 보존한 것입니다.

프로젝트에서는 `/opencr_led_status` 토픽을 받아 OpenCR 제어 테이블 주소 51에 LED 상태를 전달하도록 subscriber와 제어 테이블 정의를 추가했습니다. 원본 라이선스는 같은 폴더의 `LICENSE`를 따릅니다.

이 수정과 짝을 이루는 최종 커스텀 OpenCR 펌웨어 소스·바이너리는 기존 프로젝트 폴더에서 발견되지 않았습니다.

# Final demo launcher chain

최종 비-Safety 통합 실행은 다음 파일 순서로 연결됐습니다.

1. `desktop/TurtleBot3_전체실행.desktop`
2. `desktop/TurtleBot3_전체실행.sh`
3. `runtime/turtlebot3_전체실행.sh`
4. `runtime/run_navigation_gesture_joystick.sh`

루트 래퍼가 마지막 인수로 `--with-sound`를 전달하므로 당시 최종 체인에서는 소음 감지가 활성화됐습니다.

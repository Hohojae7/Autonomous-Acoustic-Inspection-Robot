# Sound anomaly model artifacts

- `gearbox_svm_source.joblib`은 기존 ROS 2 패키지가 기본으로 보관하던 모델입니다.
- `gearbox_svm_runtime_sklearn_1_7.joblib`은 실제 통합 폴더에 따로 있던 런타임 호환 모델입니다.
- 두 JSON 파일은 라이브 윈도우와 source-to-target 평가 기록입니다.

두 `joblib` 파일은 로컬 정리본에 보존되어 있지만, 최종 사용 모델과 재배포 범위를 팀에서 확인하기 전까지 공개 저장소에서는 제외합니다. 평가용 JSON은 모델 동작 기록으로 함께 공개합니다.

모델을 다시 생성하려면 원본 데이터셋을 준비한 뒤 `../scripts/train_machine.py`를 사용합니다.

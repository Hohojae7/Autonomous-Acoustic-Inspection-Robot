# Sound anomaly model artifacts

이 폴더에는 프로젝트 시연에서 사용한 기어박스 소음 이상 감지 SVM 산출물을 함께 보존합니다. 두 모델 모두 완성된 산업용 모델이 아니라 공개 MIMII 데이터로 만든 프로토타입입니다.

| 파일 | 역할 | SHA-256 |
| --- | --- | --- |
| `gearbox_svm_source.joblib` | ROS 2 노드의 기본 모델 | `0a5ac434a7a40ab49d9d5c68665fdeca7e10e801c4b6c589a5c8d531c462bbac` |
| `gearbox_svm_runtime_sklearn_1_7.joblib` | Jetson의 scikit-learn 1.7 계열 런타임용 호환 사본 | `00d298a64fa72648fc4688cc3bfdbe79f0ee3ed719594a7cee770aae3134ce05` |

두 JSON 파일은 라이브 윈도우 및 source-to-target 평가 기록입니다. 런타임 호환 사본의 생성·비교 내역은 [`../docs/VALIDATION.md`](../docs/VALIDATION.md)에 정리했습니다.

학습에는 Hitachi의 [MIMII Dataset](https://zenodo.org/records/3384388)을 사용했습니다. 원본 데이터셋은 CC BY-SA 4.0으로 배포되며, 원음 WAV와 학습용 압축파일은 이 저장소에 포함하지 않습니다.

`joblib`은 pickle 기반 형식이므로 출처를 신뢰할 수 있는 파일만 로드해야 합니다. 위 해시를 사용하면 저장소에 기록된 모델과 파일이 같은지 확인할 수 있습니다.

모델을 다시 생성하려면 원본 데이터셋을 준비한 뒤 `../scripts/train_machine.py`를 사용합니다.

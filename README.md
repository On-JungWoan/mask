# 1. Installation

- 아래 shell 파일은 CUDA 11.7을 기준으로 작성되었습니다.
- CUDA 버전이 11.7이 아닌 경우 저한테 말씀해주세요.

```shell
bash -i shell/setup.sh
```

<br>
<br>

# 2. Run server

- 아래 shell 파일을 터미널에 입력하여 나온 local URL 주소를 인터넷 주소창에 붙여넣기 해주세요.
- 만약 아무런 창도 뜨지 않는다면 public URL을 사용해주세요.

```
bash -i shell/masking.sh [할당받은 시퀀스 이름]

# ex) bash -i shell/masking.sh arctic_s03_ketchup_grab_01_1
```

<p align="center"><img width="80%" src="https://github.com/user-attachments/assets/11ce02ae-49e9-486c-863f-8852b7e51c64" /></p>

<p align="center"><img width="45%" src="https://github.com/user-attachments/assets/7818478d-2dbe-4f81-ae34-17e70ce3237c" /></p>

<br>
<br>

# 3. Masking

## 3-1. Set img dir

- 한 시퀀스 당 이미지 50장이 포함되어 있습니다.

<p align="center"><img width="80%" src="https://github.com/user-attachments/assets/d91b9809-2c0b-4d5b-8045-40f9eb231829" /></p>

<br>

## 3-2. Set frame idx

- 슬라이더를 움직여 손(또는 오브젝트)이 가장 잘 보이는 프레임을 선택합니다.

<p align="center"><img width="80%" src="https://github.com/user-attachments/assets/810b89f1-027c-41b7-89a5-abcc697639da" /></p>

<br>

## 3-3. Extract SAM features

- SAMv2의 feature를 추출합니다.
- 마스킹 도중 프레임을 변경하고 싶을때는 `Reset -> Get SAM features` 해주어야 합니다.

<p align="center"><img width="80%" src="https://github.com/user-attachments/assets/38f13835-a63e-4fcf-be99-499abf37982f" /></p>

<br>

## 3-4. Masking

- `Input Frame` 영역을 클릭하여 마스킹을 진행합니다.
- `Toggle positive`와 `Toggle negative` 버튼을 적절히 활용하여 알맞은 영역에 마스킹이 생성될 수 있도록 합니다.
- 일반적으로, 좋은 마스킹 퀄리티를 위해서 충분한 수의 샘플링 포인트를 지정하는 것이 좋습니다.
- 마스킹은 왼손, 오른손, 오브젝트에 대해 따로따로 진행합니다.

<p align="center"><img width="80%" src="https://github.com/user-attachments/assets/1cf345a1-c039-4435-b91e-b69c267834aa" /></p>

<br>

## 3-5. Tracking

- 마스크의 형태가 어느정도 잡혔으면, `Submit mask for tracking` 버튼을 클릭하여 마스크 트래킹을 진행합니다.

<p align="center"><img width="80%" src="https://github.com/user-attachments/assets/4be67649-f278-4b0b-b60e-8ccb8171ad4e" /></p>

<br>

## 3-6. Tracking

- 출력된 Masked video를 확인합니다.
- 결과물이 만족스럽다면,
    - `Path to save masks`의 경로 뒤에 본인이 작업한 컴포넌트의 이름(`left` or `right` or `object`)을 작성합니다.
- 결과물이 만족스럽지 않다면,
    - [3-3. Extract SAM features](#3-3-extract-sam-features)부터 다시 시작합니다.
    - 이 때, `Reset` 버튼과 `Get SAM features` 버튼을 꼭 눌러줘야합니다.

<p align="center"><img width="80%" src="https://github.com/user-attachments/assets/221503e3-b2ec-4cbf-b0f7-b6da3f8b05c2" /></p>


<br>

## 3-7. Save

- `Save masks` 버튼을 눌러 마스크를 저장합니다.
- `results` 폴더 하위에 작업물이 제대로 저장되었는지 확인해주세요.

<p align="center"><img width="80%" src="https://github.com/user-attachments/assets/0d34b1da-ebbc-4891-9c6c-e5aab518009e" /></p>

<p align="center"><img width="80%" src="https://github.com/user-attachments/assets/8817ff12-988c-480f-ae53-235503a462cd" /></p>

<p align="center"><img width="80%" src="https://github.com/user-attachments/assets/86e5e695-7e5b-4162-83c2-464997aedaf4" /></p>


<br>

## 3-8. Repeat

- [3-1. Set img dir](#3-1-set-img-dir)로 돌아가서 해당 작업을 반복합니다.

<br>
<br>

# FYI

- 마스크 퀄리티가 모델 성능에 직접적으로 영향을 미치기 떄문에(특히 오브젝트), 많이 바쁘시더라도 이 부분은 좀 신경써주시면 감사하겠습니다.
- 마스크 퀄리티는 아래 gif 정도로 맞춰주시면 됩니다.

<p align="center"><img width="80%" src="https://github.com/user-attachments/assets/acf6fdbf-ca3b-4dd5-b73c-802f34a36a64" /></p>

<p align="center"><img width="80%" src="https://github.com/user-attachments/assets/e8e66860-e9c7-4ca0-aa42-fbc60bf05315" /></p>

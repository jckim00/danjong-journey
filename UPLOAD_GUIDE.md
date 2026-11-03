# 단종 답사기 원본 업로드 안내

원본 HTML 6개를 GitHub Desktop으로 저장소의 source 폴더에 넣고 Commit → Push하면 GitHub Actions가 사진을 추출·압축하여 docs 폴더에 게시용 파일을 생성합니다.

## 업로드할 파일 이름
- 01_02_gyeongbokgung.html
- 03_04_sayuksin_jeongeopwon.html
- 05_sareung.html
- 06_cheongnyeongpo_gwanpungheon.html
- 07_jangneung.html
- 08_jongmyo_yeongnyeongjeon.html

## 방법
1. GitHub Desktop에서 jckim00/danjong-journey 저장소를 Clone합니다.
2. PC의 저장소 폴더 안에 source 폴더를 만들고 위 이름으로 HTML 6개를 복사합니다.
3. GitHub Desktop에서 Commit 후 Push합니다.
4. GitHub Actions의 Build Danjong Pages 작업이 완료되면 docs 폴더를 확인합니다.
5. Settings → Pages → Deploy from a branch → main /docs → Save를 선택합니다.

원본의 역사 서사와 디자인 CSS는 보존하며, HTML에 내장된 Base64 이미지만 별도 파일로 추출합니다. 긴 변 1800px WebP 압축을 시도하며 압축 결과가 더 크거나 실패하면 원본 이미지 형식을 보존합니다.

참고: GitHub 웹 업로드는 대용량 파일 제한이 있으므로 GitHub Desktop을 권장합니다. 65MB HTML은 GitHub 권장 크기 50MB를 넘지만 차단 한도 100MB 이내입니다.

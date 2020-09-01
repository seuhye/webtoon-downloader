# naver-webtoon-downloader
현재 네이버 웹툰에서 연재 중인 어떤 작품을,  
본인이 원하는 구간을 지정하여 다운로드 받을 수 있는 크롤러
  
# 작품 선택
다운 받고 싶은 작품의 아무 회차의 html 소스에서 titleID를 검색하여,  
NaverWebtoonDownloader.py의 titleID 변수에 할당
  
# 범위 선택
대부분의 작품이 1부 000화, 2부 000화 등 챕터 별로 구분이 되어 있지만,  
네이버 웹툰이 제공해주는 리모컨에는 챕터를 상관하지 않고 몇 화인지 알려줌.  
리모컨이 알려주는 정보를 토대로 NaverWebtoonDownloader.py의 no_MAX 값과 for문의 range를 조절
  
## Notes
2020-08-30 : 마루마루用 branch 생성/개발 완료
  
# 기타
코드 작성 초기에 Selenium을 사용하였기 때문에 그냥 남겨두었지만,  
실제로는 비동기식 데이터를 받아올 일이 없기 때문에 그다지 의미가 있지는 않음.

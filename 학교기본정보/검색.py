import json

# School_DB.json 데이터 파일을 읽어옵니다.
with open('초중고.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 검색 정보 입력
search_query = input("찾을 정보를 입력하세요 (예: 시도교육청명, 학교명, 학교종류명, 시도명): ")

# 학교를 찾는 함수
def find_schools_by_query(query):
    found_schools = []
    for school in data["records"]:
        # 입력된 검색어를 쉼표로 분리하여 각각의 검색 조건으로 활용합니다.
        query_terms = [term.strip() for term in query.split(',')]
        match = False
        for term in query_terms:
            term = term.lower()  # 입력된 검색어를 소문자로 변환
            # 각 학교 정보를 소문자로 변환하여 검색 조건과 부분 일치 여부를 확인합니다.
            school_info = (
                school["시도교육청코드"] +
                school["시도교육청명"] +
                school["학교명"] +
                school["학교종류명"] +
                school["시도명"] +
                school["관할조직명"] +
                school["설립명"] +
                school["도로명우편번호"] +
                school["도로명주소"] +
                school["도로명상세주소"] +
                school["전화번호"] +
                school["홈페이지주소"] +
                school["남녀공학구분명"] +
                school["팩스번호"] +
                school["고등학교구분명"] +
                school["산업체특별학급존재여부"] +
                school["고등학교일반전문구분명"] +
                school["특수목적고등학교계열명"] +
                school["입시전후기구분명"] +
                school["주야구분명"] +
                school["설립일자"] +
                school["개교기념일"] +
                school["수정일자"]
            ).lower()
            if term in school_info:
                match = True
            else:
                match = False
                break  # 하나라도 불일치하면 해당 학교는 선택하지 않음
        if match:
            found_schools.append(school)
    return found_schools

# 학교를 찾고 결과를 출력합니다.
found_schools = find_schools_by_query(search_query)
if found_schools:
    print("일치하는 학교를 찾았습니다:")
    for school in found_schools:
        print(json.dumps(school, ensure_ascii=False, indent=4))
else:
    print("입력한 정보와 일치하는 학교를 찾을 수 없습니다.")

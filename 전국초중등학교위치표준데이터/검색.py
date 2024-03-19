import json

# School_DB.json 데이터 파일을 읽어옵니다.
with open('전국초중등학교위치표준데이터(변환).json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 검색 정보 입력
search_query = input("찾을 정보를 입력하세요 (예: 고등학교, 교육지원청명, 경기도 화성시): ")

# 학교를 찾는 함수
def find_schools_by_query(query):
    found_schools = []
    for school in data["schools"]:
        # 입력된 검색어를 쉼표로 분리하여 각각의 검색 조건으로 활용합니다.
        query_terms = [term.strip() for term in query.split(',')]
        match = False
        for term in query_terms:
            term = term.lower()  # 입력된 검색어를 소문자로 변환
            # 각 학교 정보를 소문자로 변환하여 검색 조건과 부분 일치 여부를 확인합니다.
            school_info = (
                school["학교ID"] +
                school["학교명"] +
                school["학교급구분"] +
                school["설립일자"] +
                school["설립형태"] +
                school["본교분교구분"] +
                school["운영상태"] +
                school["소재지지번주소"] +
                school["소재지도로명주소"] +
                school["시도교육청코드"] +
                school["시도교육청명"] +
                school["교육지원청코드"] +
                school["교육지원청명"] +
                school["생성일자"] +
                school["변경일자"] +
                school["위도"] +
                school["경도"] +
                school["데이터기준일자"]
            ).lower()
            if term in school_info:
                match = True
            # 추가: 검색어가 지역 주소를 포함하면 일치로 간주
            elif term in school["소재지지번주소"].lower() or term in school["소재지도로명주소"].lower():
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
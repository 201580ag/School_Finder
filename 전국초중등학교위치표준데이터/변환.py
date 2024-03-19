import json

def save_school_info_as_json(records, output_file):
    # JSON 데이터를 저장할 리스트 초기화
    data = {"schools": []}
    
    # 각 학교 정보를 JSON 데이터에 추가
    for school in records:
        school_info = {
            "학교ID": school["학교ID"],
            "학교명": school["학교명"],
            "학교급구분": school["학교급구분"],
            "설립일자": school["설립일자"],
            "설립형태": school["설립형태"],
            "본교분교구분": school["본교분교구분"],
            "운영상태": school["운영상태"],
            "소재지지번주소": school["소재지지번주소"],
            "소재지도로명주소": school["소재지도로명주소"],
            "시도교육청코드": school["시도교육청코드"],
            "시도교육청명": school["시도교육청명"],
            "교육지원청코드": school["교육지원청코드"],
            "교육지원청명": school["교육지원청명"],
            "생성일자": school["생성일자"],
            "변경일자": school["변경일자"],
            "위도": school["위도"],
            "경도": school["경도"],
            "데이터기준일자": school["데이터기준일자"]
        }
        data["schools"].append(school_info)
    
    # JSON 파일로 저장
    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def main():
    with open("전국초중등학교위치표준데이터.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        records = data["records"]
        save_school_info_as_json(records, "전국초중등학교위치표준데이터(변환).json")

if __name__ == "__main__":
    main()

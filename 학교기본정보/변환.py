import json

def process_school_data(data):
    processed_data = {"records": []}
    
    for school in data:
        school_info = {
            "시도교육청코드": school["ATPT_OFCDC_SC_CODE"],
            "시도교육청명": school["ATPT_OFCDC_SC_NM"],
            "행정표준코드": school["SD_SCHUL_CODE"],
            "학교명": school["SCHUL_NM"],
            "영문학교명": school["ENG_SCHUL_NM"],
            "학교종류명": school["SCHUL_KND_SC_NM"],
            "시도명": school["LCTN_SC_NM"],
            "관할조직명": school["JU_ORG_NM"],
            "설립명": school["FOND_SC_NM"],
            "도로명우편번호": school["ORG_RDNZC"],
            "도로명주소": school["ORG_RDNMA"],
            "도로명상세주소": school["ORG_RDNDA"],
            "전화번호": school["ORG_TELNO"],
            "홈페이지주소": school["HMPG_ADRES"],
            "남녀공학구분명": school["COEDU_SC_NM"],
            "팩스번호": school["ORG_FAXNO"],
            "고등학교구분명": school["HS_SC_NM"],
            "산업체특별학급존재여부": school["INDST_SPECL_CCCCL_EXST_YN"],
            "고등학교일반전문구분명": school["HS_GNRL_BUSNS_SC_NM"],
            "특수목적고등학교계열명": school["SPCLY_PURPS_HS_ORD_NM"],
            "입시전후기구분명": school["ENE_BFE_SEHF_SC_NM"],
            "주야구분명": school["DGHT_SC_NM"],
            "설립일자": school["FOND_YMD"],
            "개교기념일": school["FOAS_MEMRD"],
            "수정일자": school["LOAD_DTM"]
        }
        processed_data["records"].append(school_info)
    
    return processed_data

def save_processed_data_as_json(processed_data, output_file):
    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(processed_data, file, ensure_ascii=False, indent=4)

def main():
    with open("학교기본정보 (고등학교).json", "r", encoding="utf-8") as file:
        data = json.load(file)
        processed_data = process_school_data(data)
        save_processed_data_as_json(processed_data, "고등학교.json")

if __name__ == "__main__":
    main()

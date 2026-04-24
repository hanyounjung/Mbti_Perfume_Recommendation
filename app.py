import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="MBTI AI 향수 추천",
    page_icon="🌸",
    layout="centered"
)

# -----------------------------
# 데이터
# -----------------------------
perfume_data = {
    "ISTJ": {
        "name": "클린 우드",
        "mood": "차분하고 신뢰감 있는 향",
        "top": "베르가못",
        "middle": "라벤더",
        "base": "시더우드",
        "ratio": "베르가못 3방울 + 라벤더 4방울 + 시더우드 3방울",
        "label": "오늘의 나는 조용하지만 단단한 향을 가진 사람"
    },
    "ISFJ": {
        "name": "소프트 플로럴",
        "mood": "따뜻하고 배려 깊은 향",
        "top": "오렌지",
        "middle": "장미",
        "base": "머스크",
        "ratio": "오렌지 3방울 + 장미 4방울 + 머스크 3방울",
        "label": "은은하게 오래 남는 다정한 향"
    },
    "INFJ": {
        "name": "딥 라벤더",
        "mood": "신비롭고 안정적인 향",
        "top": "레몬",
        "middle": "라벤더",
        "base": "샌달우드",
        "ratio": "레몬 2방울 + 라벤더 5방울 + 샌달우드 3방울",
        "label": "조용한 생각 속에서 피어나는 향"
    },
    "INTJ": {
        "name": "모던 시더",
        "mood": "지적이고 세련된 향",
        "top": "자몽",
        "middle": "유칼립투스",
        "base": "시더우드",
        "ratio": "자몽 3방울 + 유칼립투스 3방울 + 시더우드 4방울",
        "label": "계획적인 하루를 완성하는 차가운 우디향"
    },
    "ISTP": {
        "name": "쿨 민트",
        "mood": "시원하고 자유로운 향",
        "top": "민트",
        "middle": "유칼립투스",
        "base": "머스크",
        "ratio": "민트 4방울 + 유칼립투스 3방울 + 머스크 3방울",
        "label": "가볍지만 강한 존재감의 향"
    },
    "ISFP": {
        "name": "피치 블룸",
        "mood": "부드럽고 감성적인 향",
        "top": "복숭아",
        "middle": "자스민",
        "base": "바닐라",
        "ratio": "복숭아 4방울 + 자스민 3방울 + 바닐라 3방울",
        "label": "나만의 감성을 담은 달콤한 향"
    },
    "INFP": {
        "name": "드림 바닐라",
        "mood": "몽글몽글하고 따뜻한 향",
        "top": "오렌지",
        "middle": "일랑일랑",
        "base": "바닐라",
        "ratio": "오렌지 3방울 + 일랑일랑 3방울 + 바닐라 4방울",
        "label": "상상 속 이야기를 닮은 향"
    },
    "INTP": {
        "name": "허벌 그린",
        "mood": "개성 있고 깨끗한 향",
        "top": "레몬",
        "middle": "민트",
        "base": "샌달우드",
        "ratio": "레몬 3방울 + 민트 4방울 + 샌달우드 3방울",
        "label": "생각이 맑아지는 창의적인 향"
    },
    "ESTP": {
        "name": "시트러스 스파크",
        "mood": "활동적이고 생기 넘치는 향",
        "top": "자몽",
        "middle": "오렌지",
        "base": "머스크",
        "ratio": "자몽 4방울 + 오렌지 4방울 + 머스크 2방울",
        "label": "축제의 에너지를 담은 상큼한 향"
    },
    "ESFP": {
        "name": "프루티 팝",
        "mood": "밝고 사랑스러운 향",
        "top": "복숭아",
        "middle": "장미",
        "base": "바닐라",
        "ratio": "복숭아 4방울 + 장미 3방울 + 바닐라 3방울",
        "label": "어디서든 분위기를 밝히는 향"
    },
    "ENFP": {
        "name": "해피 오렌지",
        "mood": "자유롭고 긍정적인 향",
        "top": "오렌지",
        "middle": "자스민",
        "base": "머스크",
        "ratio": "오렌지 4방울 + 자스민 3방울 + 머스크 3방울",
        "label": "오늘의 설렘을 가득 담은 향"
    },
    "ENTP": {
        "name": "스파이시 민트",
        "mood": "톡톡 튀고 개성 있는 향",
        "top": "민트",
        "middle": "자몽",
        "base": "시더우드",
        "ratio": "민트 3방울 + 자몽 4방울 + 시더우드 3방울",
        "label": "새로운 아이디어처럼 톡 쏘는 향"
    },
    "ESTJ": {
        "name": "포멀 우드",
        "mood": "깔끔하고 단정한 향",
        "top": "베르가못",
        "middle": "유칼립투스",
        "base": "시더우드",
        "ratio": "베르가못 3방울 + 유칼립투스 3방울 + 시더우드 4방울",
        "label": "정돈된 하루를 시작하는 신뢰의 향"
    },
    "ESFJ": {
        "name": "로즈 머스크",
        "mood": "친근하고 포근한 향",
        "top": "오렌지",
        "middle": "장미",
        "base": "머스크",
        "ratio": "오렌지 3방울 + 장미 4방울 + 머스크 3방울",
        "label": "함께 있을 때 더 빛나는 따뜻한 향"
    },
    "ENFJ": {
        "name": "브라이트 자스민",
        "mood": "밝고 우아한 향",
        "top": "레몬",
        "middle": "자스민",
        "base": "샌달우드",
        "ratio": "레몬 3방울 + 자스민 4방울 + 샌달우드 3방울",
        "label": "사람들의 마음을 부드럽게 연결하는 향"
    },
    "ENTJ": {
        "name": "시그니처 우디",
        "mood": "강렬하고 자신감 있는 향",
        "top": "자몽",
        "middle": "베르가못",
        "base": "샌달우드",
        "ratio": "자몽 3방울 + 베르가못 3방울 + 샌달우드 4방울",
        "label": "목표를 향해 나아가는 리더의 향"
    },
}

mbti_list = list(perfume_data.keys())

# -----------------------------
# 화면 구성
# -----------------------------
st.title("🌸 MBTI AI 향수 추천 웹앱")
st.write("학교 축제에서 MBTI를 선택하면 나에게 어울리는 향수 조합을 추천해 줍니다.")

st.markdown("---")

col1, col2 = st.columns([1, 1])

with col1:
    mbti = st.selectbox("나의 MBTI를 선택하세요", mbti_list)

with col2:
    intensity = st.radio("향의 강도를 선택하세요", ["은은하게", "보통", "진하게"], horizontal=True)

st.markdown("---")

result = perfume_data[mbti]

st.subheader(f"✨ {mbti} 추천 향수")
st.success(f"향수 이름: {result['name']}")

st.write(f"**추천 분위기:** {result['mood']}")

st.info(f"""
**조향 노트**  
- 탑노트: {result['top']}  
- 미들노트: {result['middle']}  
- 베이스노트: {result['base']}
""")

st.warning(f"**기본 조향 비율:** {result['ratio']}")

# 강도별 안내
if intensity == "은은하게":
    st.write("🌿 **추천 사용량:** 향료 8방울 + 향수 베이스 10ml")
elif intensity == "보통":
    st.write("🌸 **추천 사용량:** 향료 10방울 + 향수 베이스 10ml")
else:
    st.write("🔥 **추천 사용량:** 향료 12방울 + 향수 베이스 10ml")

st.markdown("---")

st.subheader("🏷️ 나만의 향수 라벨 문구")
st.code(result["label"], language="text")

st.markdown("---")

st.subheader("📋 학생 조향 기록")
student_name = st.text_input("이름 또는 닉네임")
perfume_name = st.text_input("내가 붙이고 싶은 향수 이름", value=result["name"])

if st.button("추천 결과 저장용 표 만들기"):
    record = pd.DataFrame({
        "이름": [student_name],
        "MBTI": [mbti],
        "향수명": [perfume_name],
        "탑노트": [result["top"]],
        "미들노트": [result["middle"]],
        "베이스노트": [result["base"]],
        "향 강도": [intensity],
        "라벨 문구": [result["label"]]
    })
    st.dataframe(record, use_container_width=True)
    csv = record.to_csv(index=False).encode("utf-8-sig")
    st.download_button(
        label="CSV 다운로드",
        data=csv,
        file_name="mbti_perfume_record.csv",
        mime="text/csv"
    )

st.markdown("---")
st.caption("※ 실제 조향 시 피부에 직접 바르기 전 패치 테스트를 권장하며, 민감성 피부 학생은 사용에 주의하세요.")

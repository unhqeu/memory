
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="기억력 테스트",
    layout="centered"
)

html_code = r"""
<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>기억력 테스트</title>

<style>
*{box-sizing:border-box}
html,body{width:100%;height:100%;margin:0;overflow:hidden}
body {
  margin: 0;
  min-height: 100%;
  padding: 22px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: "Malgun Gothic", sans-serif;
  background: transparent;
  color: #26324b;
}
.screen {
  width: 100%;
  max-width: 800px;
  min-height: 490px;
  padding: 36px;
  background: white;
  border-radius: 26px;
  box-shadow: 0 12px 35px #30416e20;
}
.hidden{display:none!important}
.center{text-align:center}
.logo{font-size:clamp(38px,5vh,52px);line-height:1.1}
h1{font-size:clamp(27px,3.6vh,33px);color:#3949ab;margin:9px 0}
h2{font-size:clamp(21px,2.8vh,25px);margin:8px 0}
.subtitle{font-size:clamp(14px,1.9vh,17px);line-height:1.55;color:#68738b;margin:9px 0}
.info{display:flex;justify-content:center;gap:12px;flex-wrap:wrap;margin:clamp(14px,2vh,22px) 0}
.info div{background:#f0f3ff;border-radius:14px;padding:13px;min-width:125px;flex:0 1 150px}
.info strong{display:block;font-size:clamp(18px,2.5vh,22px);color:#3949ab;margin-bottom:5px}
.info span{font-size:clamp(12px,1.6vh,14px);color:#68738b}
button{font-family:inherit;cursor:pointer}
.primary{border:0;border-radius:13px;background:#4b5bdc;color:white;font-size:clamp(16px,2.2vh,18px);font-weight:bold;padding:13px 26px}
.primary:hover{background:#3444bd}
.secondary{padding:11px 18px;border:1px solid #d9def0;border-radius:11px;background:white;color:#3949ab;font-size:15px}
.topbar{display:flex;justify-content:space-between;align-items:center;gap:10px;flex-wrap:wrap;color:#68738b;font-size:14px}
.timer{background:#f0f3ff;color:#3949ab;border-radius:10px;padding:8px 11px;font-weight:bold}
.progress-bg{height:7px;background:#e9ecf5;border-radius:10px;overflow:hidden;margin:13px 0 18px}
.progress{height:100%;width:0;background:#4b5bdc;transition:width .2s}
.memory-card{min-height:0;height:clamp(135px,23vh,185px);display:flex;align-items:center;justify-content:center;text-align:center;background:#f5f7ff;border:2px solid #e6eaff;border-radius:17px;padding:20px;margin:17px 0;font-size:clamp(18px,2.5vh,22px);line-height:1.65;word-break:keep-all}
.question{font-size:clamp(20px,2.8vh,24px);line-height:1.5;margin:18px 0;word-break:keep-all}
.answers{display:grid;grid-template-columns:1fr 1fr;gap:11px;margin:17px 0}
.answer-btn{padding:13px 10px;min-height:52px;border:2px solid #e0e5f3;background:white;border-radius:12px;font-size:clamp(15px,2vh,17px);color:#26324b}
.answer-btn:hover:not(:disabled){border-color:#4b5bdc;background:#f3f5ff}
.answer-btn:disabled{cursor:default}
.answer-btn.correct{border-color:#239b69;background:#e5f8ee}
.answer-btn.wrong{border-color:#e45c69;background:#fff0f0}
.text-answer{display:flex;gap:9px;margin:18px 0}
.text-answer input{min-width:0;flex:1;padding:12px;border:2px solid #dfe4f2;border-radius:10px;font-size:16px}
.text-answer input:focus{outline:none;border-color:#4b5bdc}
.feedback{min-height:30px;text-align:center;font-size:18px;font-weight:bold;margin:12px 0}
.good{color:#168455}.bad{color:#d94350}
.result-score{font-size:clamp(44px,6vh,56px);font-weight:bold;color:#3949ab;margin:16px 0}
.rules{color:#778096;font-size:clamp(12px,1.6vh,14px);line-height:1.6;margin:12px 0}
#resultScreen .info{margin:14px 0}
@media(max-width:600px){
  body{padding:7px}
  .screen{padding:15px 12px;border-radius:16px}
  h1{font-size:26px}
  .subtitle{line-height:1.45}
  .info{gap:7px;margin:12px 0}
  .info div{min-width:0;flex:1 1 0;padding:9px 5px}
  .info span{font-size:11px}
  .answers{gap:7px}
  .answer-btn{padding:10px 5px;min-height:44px}
  .memory-card{height:clamp(120px,21vh,155px);padding:13px}
  .question{margin:11px 0}
}
@media(max-height:700px){
  body{padding:5px}
  .screen{padding:12px 16px;border-radius:15px}
  .logo{font-size:30px}
  h1{font-size:24px;margin:5px 0}
  h2{font-size:19px;margin:5px 0}
  .subtitle{font-size:13px;line-height:1.35;margin:5px 0}
  .info{margin:8px 0;gap:7px}
  .info div{padding:7px;min-width:110px}
  .rules{font-size:11px;line-height:1.35;margin:6px 0}
  .progress-bg{margin:8px 0 10px}
  .memory-card{height:clamp(100px,19vh,140px);margin:8px 0;padding:10px;font-size:17px}
  .question{font-size:18px;margin:8px 0}
  .answers{gap:7px;margin:8px 0}
  .answer-btn{min-height:40px;padding:8px;font-size:14px}
  .feedback{min-height:22px;font-size:16px;margin:5px 0}
  .result-score{font-size:38px;margin:8px 0}
  .primary{padding:9px 17px;font-size:15px}
}
</style>
</head>

<body>

<!-- 시작 화면 -->
<section class="screen center" id="startScreen">
  <div class="logo">🧠</div>
  <h1>기억력 테스트</h1>

  <p class="subtitle">
    기억한 정보를 바탕으로 퀴즈를 풀어 보세요!<br>
    날짜와 숫자부터 방향과 위치까지 기억력을 시험해 보세요.
  </p>

  <div class="info">
    <div><strong>10문제</strong><span>매번 무작위 출제</span></div>
    <div><strong>100점</strong><span>문제당 10점</span></div>
    <div><strong>2단계</strong><span>기억하기 → 퀴즈</span></div>
  </div>

  <button class="primary" onclick="startGame()">게임 시작하기 →</button>

  <p class="rules">
    기록형 5문제와 방향·위치형 5문제가 출제됩니다.<br>
    다시 시작하면 다른 문제 조합으로 도전할 수 있어요!
  </p>
</section>

<!-- 기억하기 화면 -->
<section class="screen hidden" id="memoryScreen">
  <div class="topbar">
    <span id="memoryCount">기억하기 1 / 10</span>
    <span class="timer" id="memoryTimer">경과 시간 0초</span>
  </div>

  <div class="progress-bg">
    <div class="progress" id="memoryProgress"></div>
  </div>

  <h2 class="center">내용을 잘 기억해 보세요!</h2>

  <div class="memory-card" id="memoryText"></div>

  <div class="center">
    <button class="primary" id="memoryNext" onclick="nextMemory()">다음 내용 →</button>
  </div>

  <p class="rules center">다음 버튼을 누르면 바로 새로운 내용이 나타납니다.</p>
</section>

<!-- 퀴즈 화면 -->
<section class="screen hidden" id="quizScreen">
  <div class="topbar">
    <span id="quizCount">문제 1 / 10</span>
    <span class="timer" id="quizTimer">경과 시간 0초</span>
  </div>

  <div class="progress-bg">
    <div class="progress" id="quizProgress"></div>
  </div>

  <div class="question" id="questionText"></div>

  <div class="answers" id="choiceArea"></div>

  <div class="text-answer hidden" id="textArea">
    <input id="textInput" type="text" placeholder="정답을 입력하세요">
    <button class="primary" id="submitText" onclick="submitTextAnswer()">확인</button>
  </div>

  <div class="feedback" id="feedback"></div>
</section>

<!-- 결과 화면 -->
<section class="screen center hidden" id="resultScreen">
  <div class="logo">🏆</div>
  <h1>테스트 완료!</h1>
  <p class="subtitle">이번 도전 결과</p>

  <div class="result-score" id="finalScore">0점</div>

  <div class="info">
    <div>
      <strong id="finalTime">0초</strong>
      <span>총 소요 시간</span>
    </div>
    <div>
      <strong id="correctCount">0 / 10</strong>
      <span>정답 개수</span>
    </div>
  </div>

  <p class="subtitle" id="resultMessage"></p>

  <button class="primary" onclick="startGame()">다른 문제로 재도전 ↻</button>
  <br><br>
  <button class="secondary" onclick="goHome()">처음 화면으로</button>
</section>

<script>
// 기록형 객관식 문제
const recordMC = [
{m:"학교 방송실 예약표에는 사용 날짜 7월 14일, 사용 시간 오후 1시 30분부터 2시 10분까지, 예약자 번호 24가 적혀 있었다.",q:"방송실 사용은 몇 시에 끝나는가?",a:"오후 2시 10분",o:["오후 1시 50분","오후 2시 10분","오후 2시 30분","오후 3시"]},
{m:"도서관 이용 신청서에는 날짜 8월 22일, 이용 시간 오전 10시부터 11시 40분까지, 신청 인원 18명, 담당 교사 김현정이 적혀 있었다.",q:"도서관 이용 신청 인원은 몇 명인가?",a:"18명",o:["12명","16명","18명","22명"]},
{m:"과학실 실험 예약표에는 6월 18일 오후 2시, 현미경 6대, 실험 조 번호 3조, 담당 학생 박지훈이라고 적혀 있었다.",q:"실험을 담당한 학생은 누구인가?",a:"박지훈",o:["김민수","박지훈","이서연","최도윤"]},
{m:"학교 축제 부스 신청서에는 운영 날짜 10월 16일, 오전 9시 20분부터 오후 3시까지, 부스 번호 12번, 신청 인원 5명이 기록되어 있었다.",q:"축제 부스 번호는 몇 번인가?",a:"12번",o:["5번","10번","12번","15번"]},
{m:"체육관 대관 확인서에는 9월 7일 오후 4시부터 5시 30분까지 사용하며, 예약 팀은 배드민턴부, 참가 인원은 14명이라고 적혀 있었다.",q:"체육관을 예약한 팀은 어디인가?",a:"배드민턴부",o:["농구부","배드민턴부","축구부","탁구부"]},
{m:"컴퓨터실 사용표에는 11월 3일 오전 9시 10분부터 10시까지, 컴퓨터 28대, 예약 학급 2학년 4반이라고 적혀 있었다.",q:"컴퓨터실을 예약한 학급은 어디인가?",a:"2학년 4반",o:["2학년 1반","2학년 2반","2학년 3반","2학년 4반"]},
{m:"체험학습 버스 배정표에는 출발 날짜 5월 21일, 출발 시간 오전 8시 20분, 버스 번호 3호차, 탑승 인원 32명이 적혀 있었다.",q:"버스에 탑승하는 인원은 몇 명인가?",a:"32명",o:["24명","28명","32명","36명"]},
{m:"도서 구매 신청서에는 신청 날짜 4월 9일, 과학 도서 12권, 문학 도서 8권, 담당 동아리 과학탐구반이라고 기록되어 있었다.",q:"신청한 과학 도서는 몇 권인가?",a:"12권",o:["8권","10권","12권","14권"]},
{m:"음악실 악기 대여표에는 대여 날짜 5월 8일, 기타 4대와 키보드 2대, 반납 시간 오후 4시 40분, 대여 동아리 밴드부라고 기록되어 있었다.",q:"대여한 키보드는 몇 대인가?",a:"2대",o:["1대","2대","4대","6대"]},
{m:"학교 행사 안내문에는 행사 날짜 10월 24일, 시작 시간 오전 10시 30분, 장소 시청각실, 참가비 3,000원, 신청 마감일 10월 18일이 적혀 있었다.",q:"신청 마감일은 언제인가?",a:"10월 18일",o:["10월 16일","10월 18일","10월 20일","10월 24일"]},
{m:"교내 프린터 사용 기록에는 7월 2일 오후 12시 40분, 출력 자료 35장, 컬러 출력 12장, 사용자 번호 17이 적혀 있었다.",q:"컬러로 출력한 종이는 몇 장인가?",a:"12장",o:["12장","17장","23장","35장"]},
{m:"진로 체험 신청서에는 체험 날짜 8월 13일, 출발 시간 오전 9시 15분, 방문 장소 반도체 연구소, 참가 학생 24명, 인솔 교사 2명이 기록되어 있었다.",q:"진로 체험에서 방문하는 장소는 어디인가?",a:"반도체 연구소",o:["과학관","반도체 연구소","시청","도서관"]},
{m:"운동장 사용 일정에는 4월 16일 오후 1시부터 2시 50분까지, 사용 학급 2학년 3반, 준비물 공 6개, 담당 학생 번호 15가 적혀 있었다.",q:"운동장 사용을 위해 준비한 공은 몇 개인가?",a:"6개",o:["4개","5개","6개","8개"]},
{m:"독서 토론 신청서에는 11월 19일 오전 10시 40분, 토론 도서 '소년이 온다', 참가 학생 16명, 진행 순서 2번째라고 적혀 있었다.",q:"토론할 책은 무엇인가?",a:"소년이 온다",o:["소나기","소년이 온다","운수 좋은 날","메밀꽃 필 무렵"]},
{m:"방송 장비 점검표에는 점검 날짜 6월 3일, 마이크 5개, 스피커 4대, 점검 완료 시간 오후 4시 25분, 담당자 번호 36이 기록되어 있었다.",q:"점검한 마이크는 몇 개인가?",a:"5개",o:["3개","4개","5개","6개"]},
{m:"수학 탐구 발표 신청서에는 발표 날짜 7월 9일, 발표 시간 오전 11시 10분, 주제 함수와 반도체 데이터, 발표 시간 8분, 신청 번호 42가 적혀 있었다.",q:"발표 시간은 몇 분인가?",a:"8분",o:["5분","6분","8분","10분"]},
{m:"과학실 대여 기록에는 9월 15일, 시약병 7개, 보호 안경 12개, 반납 예정 시간 오후 3시 40분, 담당 조 5조라고 적혀 있었다.",q:"대여한 보호 안경은 몇 개인가?",a:"12개",o:["7개","9개","12개","15개"]},
{m:"행사 물품표에는 행사 날짜 5월 30일, 의자 45개, 책상 12개, 안내판 3개, 설치 장소 본관 앞이라고 기록되어 있었다.",q:"준비한 안내판은 몇 개인가?",a:"3개",o:["2개","3개","12개","45개"]},
{m:"동아리실 예약 기록에는 8월 26일 오후 1시 40분부터 3시 10분까지, 예약 동아리 로봇제작반, 참가 학생 11명, 사용 공간 B실이라고 적혀 있었다.",q:"예약한 동아리는 어디인가?",a:"로봇제작반",o:["과학탐구반","로봇제작반","방송부","밴드부"]},
{m:"사진 촬영 신청서에는 촬영 날짜 10월 8일, 촬영 시간 오후 2시 20분, 촬영 장소 운동장, 촬영 장비 카메라 3대, 신청자 번호 19가 기록되어 있었다.",q:"사진 촬영 장소는 어디인가?",a:"운동장",o:["도서관","운동장","시청각실","과학실"]},
{m:"학생회 회의실 예약표에는 9월 12일 오후 3시부터 4시 20분까지, 예약 인원 9명, 회의 주제 축제 준비, 회의실 번호 204가 기록되어 있었다.",q:"예약한 회의실 번호는 몇 번인가?",a:"204번",o:["202번","203번","204번","205번"]},
{m:"급식 만족도 조사 결과에는 응답 날짜 6월 25일, 참여 학생 126명, 가장 선호한 메뉴 돈가스, 담당 학급 2학년 1반이라고 적혀 있었다.",q:"학생들이 가장 선호한 메뉴는 무엇인가?",a:"돈가스",o:["김치볶음밥","돈가스","불고기","비빔밥"]},
{m:"학교 도착 확인표에는 날짜 3월 11일, 도착 시간 오전 8시 35분, 방문 학생 27명, 인솔자 번호 14, 방문 장소 자연사박물관이라고 적혀 있었다.",q:"방문 학생은 몇 명인가?",a:"27명",o:["14명","24명","27명","32명"]},
{m:"실험실 예약표에는 12월 2일 오후 1시부터 2시 30분까지, 실험 장비 9개, 참여 인원 6명, 담당 조 2조라고 기록되어 있었다.",q:"실험 장비는 몇 개인가?",a:"9개",o:["6개","7개","9개","12개"]}
];

// 기록형 단답 문제
const recordText = [
{m:"발표회 일정표에는 날짜 12월 5일, 시작 시간 오후 1시 20분, 발표 시간 15분, 발표 순서 4번째라고 적혀 있었다.",q:"발표 순서는 몇 번째인가?",a:"4"},
{m:"물품 대여 기록에는 대여 날짜 3월 17일, 디지털카메라 2대, 반납 예정일 3월 20일, 대여자 번호 31이 적혀 있었다.",q:"대여자 번호는 몇 번인가?",a:"31"},
{m:"교내 인쇄 기록에는 신청 날짜 4월 12일, 흑백 출력 48장, 컬러 출력 16장, 사용자 번호 23이 기록되어 있었다.",q:"흑백 출력은 몇 장인가?",a:"48"},
{m:"강당 예약표에는 예약 날짜 9월 3일, 사용 시간 오후 2시부터 3시 30분까지, 예약 인원 38명, 예약 번호 52가 적혀 있었다.",q:"예약 번호는 몇 번인가?",a:"52"},
{m:"과학 행사 준비표에는 행사 날짜 6월 14일, 실험 키트 9개, 참가 조 4조, 시작 시간 오전 10시 20분이라고 적혀 있었다.",q:"실험 키트는 몇 개인가?",a:"9"},
{m:"동아리 신청서에는 신청 날짜 5월 19일, 참가 학생 17명, 지도 교사 이정민, 모임 장소 과학실이라고 기록되어 있었다.",q:"참가 학생은 몇 명인가?",a:"17"},
{m:"도서 반납표에는 반납 날짜 8월 30일, 책 6권, 반납 시간 오후 4시 15분, 이용자 번호 28이 적혀 있었다.",q:"이용자 번호는 몇 번인가?",a:"28"},
{m:"체육 행사 기록에는 날짜 10월 11일, 참가 팀 8팀, 심판 4명, 시작 시간 오전 9시 40분이라고 적혀 있었다.",q:"참가 팀은 몇 팀인가?",a:"8"},
{m:"교실 정리 점검표에는 점검 날짜 7월 18일, 책상 30개, 의자 31개, 담당 번호 16이 기록되어 있었다.",q:"담당 번호는 몇 번인가?",a:"16"},
{m:"진로 강연 안내에는 날짜 11월 7일, 시작 시간 오후 1시 50분, 강연 시간 40분, 신청 학생 62명이라고 적혀 있었다.",q:"신청 학생은 몇 명인가?",a:"62"}
];

// 방향·위치형 객관식 문제
const spatialMC = [
{m:"교실 문을 나와 오른쪽으로 돌면 정수기가 있고, 정수기를 지나 왼쪽으로 가면 보건실이 있다.",q:"교실 문을 나와 오른쪽으로 돌면 무엇이 있는가?",a:"정수기",o:["보건실","정수기","계단","교무실"]},
{m:"책상 위에는 연필, 지우개, 자가 왼쪽부터 순서대로 놓여 있었다. 자 아래에는 작은 메모지가 있었다.",q:"왼쪽부터 두 번째 물건은 무엇인가?",a:"지우개",o:["연필","지우개","자","메모지"]},
{m:"현관에서 직진하면 엘리베이터가 나오고, 엘리베이터 앞에서 왼쪽으로 가면 계단이 있다. 계단 옆에는 소화기가 있다.",q:"엘리베이터 앞에서 왼쪽으로 가면 무엇이 있는가?",a:"계단",o:["계단","정수기","보건실","주차장"]},
{m:"복도 게시판의 왼쪽에는 축제 포스터, 가운데에는 시간표, 오른쪽에는 동아리 모집 안내가 붙어 있었다.",q:"게시판 가운데에 붙어 있는 것은 무엇인가?",a:"시간표",o:["축제 포스터","시간표","동아리 모집 안내","급식표"]},
{m:"공원 입구에서 직진하면 분수대가 있고, 분수대 오른쪽에는 벤치가 세 개, 왼쪽에는 쓰레기통이 있다.",q:"분수대 왼쪽에는 무엇이 있는가?",a:"쓰레기통",o:["벤치","나무","쓰레기통","화장실"]},
{m:"신발장에는 검은 운동화, 흰 운동화, 파란 슬리퍼가 왼쪽부터 놓여 있었다. 검은 운동화 안에는 쪽지가 있었다.",q:"신발장 가운데에 놓인 것은 무엇인가?",a:"흰 운동화",o:["검은 운동화","흰 운동화","파란 슬리퍼","갈색 구두"]},
{m:"매점에서 과자 2개와 음료 1개를 샀다. 과자는 가방 앞주머니에, 음료는 가방 옆주머니에 넣었다.",q:"음료는 가방 어디에 넣었는가?",a:"옆주머니",o:["앞주머니","안쪽 주머니","옆주머니","가방 바깥"]},
{m:"복도 끝에서 오른쪽으로 돌면 음악실이 있고, 음악실 맞은편에는 미술실이 있다. 음악실 문 옆에는 초록색 안내판이 붙어 있다.",q:"음악실 맞은편은 어디인가?",a:"미술실",o:["과학실","교무실","미술실","도서관"]},
{m:"교무실 앞 탁자에는 흰색 봉투와 파란색 클립이 놓여 있었다. 봉투 아래에는 작은 열쇠가 있었다.",q:"봉투 아래에 있는 물건은 무엇인가?",a:"열쇠",o:["열쇠","연필","지우개","카드"]},
{m:"서랍 첫 번째 칸에는 가위, 두 번째 칸에는 테이프, 세 번째 칸에는 풀을 넣어 두었다. 서랍 바깥에는 노란 스티커가 붙어 있었다.",q:"서랍 두 번째 칸에 들어 있는 것은 무엇인가?",a:"테이프",o:["가위","테이프","풀","스티커"]},
{m:"버스 정류장 뒤쪽에 작은 편의점이 있고, 편의점 왼쪽에는 자전거 거치대가 있다. 편의점 오른쪽에는 약국이 있다.",q:"편의점 왼쪽에는 무엇이 있는가?",a:"자전거 거치대",o:["약국","자전거 거치대","버스","은행"]},
{m:"침대 옆 탁자에는 물컵이 있고, 탁자 아래에는 슬리퍼 한 켤레가 있었다. 창문 앞에는 회색 커튼이 걸려 있었다.",q:"탁자 아래에는 무엇이 있는가?",a:"슬리퍼",o:["물컵","책","슬리퍼","커튼"]},
{m:"학교 정문에서 왼쪽으로 가면 경비실이 있고, 경비실을 지나 직진하면 주차장이 나온다. 경비실 오른쪽에는 화단이 있다.",q:"경비실을 지나 직진하면 어디가 나오는가?",a:"주차장",o:["주차장","도서관","급식실","운동장"]},
{m:"책장에는 맨 아래 역사책, 가운데 과학책, 맨 위 소설책이 놓여 있었다. 책장 옆에는 작은 화분이 있었다.",q:"책장 가운데에 놓인 책은 무엇인가?",a:"과학책",o:["역사책","과학책","소설책","만화책"]},
{m:"카페 문을 나와 왼쪽으로 가면 꽃집이 있고, 꽃집 맞은편에는 약국이 있다. 꽃집 앞에는 분홍색 화분이 놓여 있었다.",q:"꽃집 맞은편에는 어디가 있는가?",a:"약국",o:["약국","은행","도서관","학교"]},
{m:"책상 왼쪽에는 휴대전화가, 오른쪽에는 물병이 놓여 있었다. 책상 아래에는 검은색 가방이 있고 의자 위에는 회색 재킷이 있었다.",q:"책상 오른쪽에 놓인 물건은 무엇인가?",a:"물병",o:["휴대전화","물병","가방","재킷"]},
{m:"엘리베이터에서 내린 뒤 왼쪽으로 가면 201호가 있고, 오른쪽으로 가면 202호가 있다. 엘리베이터 바로 앞에는 소화전이 있다.",q:"엘리베이터에서 내린 뒤 오른쪽으로 가면 몇 호인가?",a:"202호",o:["101호","201호","202호","203호"]},
{m:"급식실 입구 오른쪽에는 손 소독기가 있고, 왼쪽에는 식판 반납대가 있다. 반납대 뒤에는 물 마시는 곳이 있다.",q:"급식실 입구 왼쪽에는 무엇이 있는가?",a:"식판 반납대",o:["손 소독기","식판 반납대","정수기","출입문"]},
{m:"책장 첫 번째 칸에는 만화책, 두 번째 칸에는 과학책, 세 번째 칸에는 잡지가 있었다. 책장 맨 위에는 작은 시계가 놓여 있었다.",q:"책장 두 번째 칸에는 무엇이 있는가?",a:"과학책",o:["만화책","과학책","잡지","시계"]},
{m:"정류장에서 직진하면 횡단보도가 있고, 횡단보도를 건너 오른쪽으로 가면 빵집이 있다. 빵집 왼쪽에는 꽃집이 있다.",q:"횡단보도를 건너 오른쪽으로 가면 어디가 있는가?",a:"빵집",o:["빵집","꽃집","약국","학교"]},
{m:"책상 위 왼쪽에는 노트, 가운데에는 필통, 오른쪽에는 물병이 놓여 있었다. 노트 아래에는 시간표가 끼워져 있었다.",q:"책상 위 가운데에 있는 물건은 무엇인가?",a:"필통",o:["노트","필통","물병","시간표"]},
{m:"현관에서 오른쪽으로 가면 신발장이 있고, 신발장 맞은편에는 우산꽂이가 있다. 우산꽂이 옆에는 작은 의자가 있다.",q:"신발장 맞은편에는 무엇이 있는가?",a:"우산꽂이",o:["의자","우산꽂이","책장","정수기"]},
{m:"교실 앞 칠판 오른쪽에는 시계가 있고, 칠판 왼쪽에는 게시판이 있다. 게시판 아래에는 분리수거함이 놓여 있다.",q:"칠판 왼쪽에는 무엇이 있는가?",a:"게시판",o:["시계","게시판","분리수거함","책상"]},
{m:"공원 산책로에서 왼쪽 길은 연못으로 이어지고, 오른쪽 길은 놀이터로 이어진다. 놀이터 앞에는 빨간 벤치가 있다.",q:"산책로에서 오른쪽 길로 가면 어디가 나오는가?",a:"놀이터",o:["연못","놀이터","주차장","매점"]}
];

// 방향·위치형 단답 문제
const spatialText = [
{m:"가방 안에는 파란 필통이 있고, 필통 안에는 검은 펜 2개와 빨간 펜 1개가 들어 있었다.",q:"빨간 펜은 몇 개인가?",a:"1"},
{m:"필통에는 연필 3자루, 지우개 2개, 형광펜 4개가 들어 있었다. 겉면에는 고양이 그림이 있었다.",q:"형광펜은 몇 개인가?",a:"4"},
{m:"책상 왼쪽에는 노트 2권, 오른쪽에는 책 3권이 있었다. 책상 아래에는 가방 1개가 놓여 있었다.",q:"책상 위에 놓인 노트는 몇 권인가?",a:"2"},
{m:"서랍 첫 번째 칸에는 연필 5자루, 두 번째 칸에는 지우개 3개, 세 번째 칸에는 자 2개가 들어 있었다.",q:"두 번째 칸에 들어 있는 지우개는 몇 개인가?",a:"3"},
{m:"선반 위에는 작은 화분 2개와 큰 화분 1개가 있었다. 선반 아래에는 물뿌리개가 놓여 있었다.",q:"선반 위에 있는 화분은 모두 몇 개인가?",a:"3"},
{m:"책상 위에는 빨간 책 2권, 파란 책 4권, 초록 책 1권이 왼쪽부터 놓여 있었다.",q:"파란 책은 몇 권인가?",a:"4"},
{m:"가방 앞주머니에는 카드 3장, 옆주머니에는 열쇠 2개가 들어 있었다. 가방 안쪽에는 공책 1권이 있었다.",q:"가방 앞주머니의 카드는 몇 장인가?",a:"3"},
{m:"교실 창가에는 의자 4개가 놓여 있었고, 문 옆에는 우산 3개가 세워져 있었다.",q:"창가에 놓인 의자는 몇 개인가?",a:"4"},
{m:"탁자 위에는 물컵 2개와 접시 5개가 놓여 있었다. 탁자 아래에는 작은 상자 1개가 있었다.",q:"탁자 위에 놓인 접시는 몇 개인가?",a:"5"},
{m:"책장 첫 번째 칸에는 책 6권, 두 번째 칸에는 책 3권, 세 번째 칸에는 책 4권이 꽂혀 있었다.",q:"두 번째 칸에 꽂힌 책은 몇 권인가?",a:"3"}
];

let questions=[];
let memoryIndex=0;
let quizIndex=0;
let score=0;
let elapsedSeconds=0;
let clockInterval=null;
let clockPaused=false;
let answering=false;
let feedbackTimeout=null;

const $=id=>document.getElementById(id);

function shuffle(array){
  const result=[...array];
  for(let i=result.length-1;i>0;i--){
    const j=Math.floor(Math.random()*(i+1));
    [result[i],result[j]]=[result[j],result[i]];
  }
  return result;
}

function showScreen(id){
  ["startScreen","memoryScreen","quizScreen","resultScreen"]
    .forEach(s=>$(s).classList.add("hidden"));
  $(id).classList.remove("hidden");
}

function startGame(){
  clearInterval(clockInterval);
  clearTimeout(feedbackTimeout);

  const selectedRecordMC=shuffle(recordMC).slice(0,4);
  const selectedRecordText=shuffle(recordText).slice(0,1);
  const selectedSpatialMC=shuffle(spatialMC).slice(0,4);
  const selectedSpatialText=shuffle(spatialText).slice(0,1);

  questions=shuffle([
    ...selectedRecordMC.map(q=>({...q,type:"choice"})),
    ...selectedRecordText.map(q=>({...q,type:"text"})),
    ...selectedSpatialMC.map(q=>({...q,type:"choice"})),
    ...selectedSpatialText.map(q=>({...q,type:"text"}))
  ]).map(q=>({
    memory:q.m,
    question:q.q,
    answer:q.a,
    options:q.o,
    type:q.type
  }));

  memoryIndex=0;
  quizIndex=0;
  score=0;
  elapsedSeconds=0;
  clockPaused=false;
  answering=false;

  updateTimers();
  showScreen("memoryScreen");
  startClock();
  renderMemory();
}

function startClock(){
  clearInterval(clockInterval);
  clockInterval=setInterval(()=>{
    if(!clockPaused){
      elapsedSeconds++;
      updateTimers();
    }
  },1000);
}

function formatTime(total){
  const minutes=Math.floor(total/60);
  const seconds=total%60;
  if(minutes>0)return `${minutes}분 ${seconds}초`;
  return `${seconds}초`;
}

function updateTimers(){
  const time=formatTime(elapsedSeconds);
  $("memoryTimer").textContent=`경과 시간 ${time}`;
  $("quizTimer").textContent=`경과 시간 ${time}`;
}

function renderMemory(){
  $("memoryCount").textContent=`기억하기 ${memoryIndex+1} / 10`;
  $("memoryProgress").style.width=`${(memoryIndex+1)*10}%`;
  $("memoryText").textContent=questions[memoryIndex].memory;
  $("memoryNext").textContent=memoryIndex===9?"퀴즈 시작하기 →":"다음 내용 →";
}

function nextMemory(){
  if(memoryIndex<9){
    memoryIndex++;
    renderMemory();
  }else{
    showScreen("quizScreen");
    clockPaused=false;
    renderQuestion();
  }
}

function renderQuestion(){
  answering=false;
  const q=questions[quizIndex];

  $("quizCount").textContent=`문제 ${quizIndex+1} / 10`;
  $("quizProgress").style.width=`${quizIndex*10}%`;
  $("questionText").textContent=q.question;
  $("feedback").textContent="";
  $("feedback").className="feedback";
  $("choiceArea").innerHTML="";
  $("choiceArea").classList.add("hidden");
  $("textArea").classList.add("hidden");

  if(q.type==="choice"){
    $("choiceArea").classList.remove("hidden");
    shuffle(q.options).forEach(option=>{
      const button=document.createElement("button");
      button.className="answer-btn";
      button.textContent=option;
      button.onclick=()=>submitChoice(option,button);
      $("choiceArea").appendChild(button);
    });
  }else{
    $("textArea").classList.remove("hidden");
    $("textInput").value="";
    $("textInput").disabled=false;
    $("submitText").disabled=false;
  }
}

function normalize(value){
  return String(value).trim().replace(/\s+/g,"")
    .replace(/[.,!?。！？]/g,"").toLowerCase();
}

function submitChoice(selected,button){
  if(answering)return;
  answering=true;
  clockPaused=true;

  const q=questions[quizIndex];
  const correct=normalize(selected)===normalize(q.answer);

  document.querySelectorAll(".answer-btn").forEach(btn=>{
    btn.disabled=true;
    if(normalize(btn.textContent)===normalize(q.answer)){
      btn.classList.add("correct");
    }
  });

  if(!correct)button.classList.add("wrong");
  showFeedback(correct,q.answer);
}

function submitTextAnswer(){
  if(answering)return;

  const value=$("textInput").value.trim();

  if(value===""){
    $("feedback").textContent="정답을 입력해 주세요.";
    $("feedback").className="feedback bad";
    return;
  }

  answering=true;
  clockPaused=true;

  const q=questions[quizIndex];
  const correct=normalize(value)===normalize(q.answer);

  $("textInput").disabled=true;
  $("submitText").disabled=true;
  showFeedback(correct,q.answer);
}

$("textInput").addEventListener("focus",()=>clockPaused=true);
$("textInput").addEventListener("input",()=>clockPaused=true);
$("textInput").addEventListener("keydown",event=>{
  if(event.key==="Enter")submitTextAnswer();
});

function showFeedback(correct,answer){
  const feedback=$("feedback");

  if(correct){
    score+=10;
    feedback.textContent="정답!";
    feedback.className="feedback good";
  }else{
    feedback.textContent=`오답! 정답: ${answer}`;
    feedback.className="feedback bad";
  }

  feedbackTimeout=setTimeout(()=>{
    quizIndex++;
    if(quizIndex>=10){
      showResult();
    }else{
      clockPaused=false;
      renderQuestion();
    }
  },1100);
}

function showResult(){
  clearInterval(clockInterval);
  showScreen("resultScreen");

  $("quizProgress").style.width="100%";
  $("finalScore").textContent=`${score}점`;
  $("finalTime").textContent=formatTime(elapsedSeconds);
  $("correctCount").textContent=`${score/10} / 10`;

  let message;

  if(score===100){
    message="완벽해요! 모든 문제를 맞혔어요.";
  }else if(score>=70){
    message="잘했어요! 많은 내용을 기억했네요.";
  }else if(score>=40){
    message="좋아요! 다시 도전하면 더 높은 점수를 얻을 수 있어요.";
  }else{
    message="괜찮아요! 다른 문제 조합으로 다시 도전해 보세요.";
  }

  $("resultMessage").textContent=message;
}

function goHome(){
  clearInterval(clockInterval);
  clearTimeout(feedbackTimeout);
  showScreen("startScreen");
}
</script>
</body>
</html>

"""
st.markdown("""
<style>
.stApp,
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #e8edff, #d9f5f0);
}

[data-testid="stMainBlockContainer"] {
    padding-left: 0 !important;
    padding-right: 0 !important;
}
</style>
""", unsafe_allow_html=True)

components.html(
    html_code,
    height=650,
    scrolling=False
)

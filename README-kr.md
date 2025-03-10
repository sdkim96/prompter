# Prompter

프롬프트(특히 대규모 언어 모델에게 입력하는 프롬프트) 품질을 평가할 때는, 단순히 “결과물이 만족스러운가?”만 보는 것이 아니라 다양한 측면에서 프롬프트 자체가 얼마나 명확하고, 의도를 제대로 드러내고 있으며, 모델이 답변을 생성하기에 충분한 맥락과 형식을 갖추고 있는지를 점검하는 것이 중요합니다. 아래는 프롬프트 품질 평가에 활용할 수 있는 대표적인 기준들입니다:

⸻

1. 명확성 (Clarity)
	•	불필요하게 복잡하거나 애매한 표현은 없는지, 핵심 질문이나 요구사항이 명확히 드러나는지 확인합니다.
	•	예) “비즈니스 기획서를 작성해줘”보다는 “목표 시장, 경쟁사 분석, 재무 예측이 포함된 2페이지 분량의 비즈니스 기획서를 작성해줘”처럼 구체적으로 요청할수록 명확도가 올라갑니다.

체크포인트
	•	문장이 모호하지 않고 직관적인가?
	•	질문/요청 사항이 구체적이고 이해하기 쉬운가?
	•	누락된 정보 없이 모델이 답변을 구성하기 충분한가?

⸻

2. 목적성 (Purposefulness)
	•	해당 프롬프트가 무엇을 하고 싶은지를 잘 드러내고 있는지가 중요합니다.
	•	프롬프트를 통해 얻고자 하는 최종 산출물(문서, 요약, 코드 등) 혹은 **목표(문제 해결, 아이디어 수집 등)**가 확실해야 합니다.

체크포인트
	•	“무엇을 얻고 싶은가?”가 분명하게 드러나는가?
	•	답변 형태(예: 글 요약, 스텝 바이 스텝 절차, 코드 샘플)가 명시되어 있는가?

⸻

3. 충분한 맥락과 세부 지시사항 (Context & Instructions)
	•	모델이 정확한 답변을 주기 위해서는 적절한 배경 정보와 세부 지시사항이 필요합니다.
	•	예) “현재 A라는 데이터를 분석해서 B라는 결과를 도출해줘. 분석은 가능한 한 통계적인 근거를 들어주고, 그래프 예시도 제시해 줘.”처럼, 필요한 맥락과 예시를 포함하면 좋습니다.

체크포인트
	•	답변에 필요한 배경 지식이나 조건(예: 어떤 형식으로, 어떤 관점에서)을 충분히 제공했는가?
	•	“해야 할 것”과 “하지 않아야 할 것”에 대한 가이드가 명시되어 있는가?

⸻

4. 간결성 (Conciseness)
	•	필요한 정보를 과하게 나열해 지시사항이 산만해지지 않도록 주의합니다.
	•	너무 많은 내용을 한 번에 담으면 모델이 중심 포인트를 놓치거나, 혹은 오히려 간단히 설명해줄 것을 복잡하게 만들어 버릴 수 있습니다.

체크포인트
	•	너무 길고 복잡하게 작성되어 핵심 의도가 흐려지지 않았는가?
	•	여러 가지 질문을 동시에 담고 있다면, 서로 충돌하거나 혼란을 야기하지는 않는가?

⸻

5. 논리적 구조와 일관성 (Logical Structure & Consistency)
	•	프롬프트가 논리적으로 이어지도록 작성되어 있는지, 전에 제시한 가정이나 조건과 충돌하지 않는지 확인합니다.
	•	예) “3단계로 답변해줘”라고 해놓고 실제로는 2단계나 4단계에 관한 내용을 묻는 등 모순이 생기면 안 됩니다.

체크포인트
	•	처음에 제시한 지시사항과 뒤이어 나타나는 지시사항이 서로 충돌하지 않는가?
	•	단계별 질문(또는 요구사항)이 논리적인 순서를 이루고 있는가?

⸻

6. 적절한 톤과 스타일 (Tone & Style)
	•	상대가 누구인지(예: 전문가 vs. 초보자, 어린이 vs. 성인)에 따라, 어휘 선택과 설명 수준을 달리 해야 합니다.
	•	답변 형식(예: 에세이 스타일, 테이블 요약, 간단한 메모)도 명시해 주면 좋습니다.

체크포인트
	•	대상 독자의 수준에 맞는 언어와 스타일로 작성되었는가?
	•	전문적인 용어 사용 여부, 설명 강도, 예시 제시 방식 등이 요구사항과 일치하는가?

⸻

7. 출력 형식 제시 (Output Format)
	•	예를 들어 표, 리스트, 코드 블록, 논문 형식 등의 출력 양식을 지정해 주는 것은 모델이 답변을 더 구조적으로 제공하도록 돕습니다.
	•	“표로 만들어 줘”, “마크다운 형식으로 달아 줘”, “JSON 형태로 반환해 줘” 등 구체적인 출력 형식을 안내하면 해석의 여지가 줄어듭니다.

체크포인트
	•	출력이 어떤 형태이길 원하는가? (예: 숫자, 텍스트, 표, 코드 등)
	•	예시 포맷이 있다면 구체적으로 전달했는가?

⸻

8. 평가 기준 (Evaluation)
	•	프롬프트에 대한 모델 응답을 어떻게 평가할지 기준이 있으면, 그 기준에 따라 프롬프트를 보완할 수 있습니다.
	•	예) “답변이 정확한 사실에 기반했는지”, “참고 자료가 있는지”, “실행 가능한 코드인지” 등.

체크포인트
	•	“어떨 때 답변이 ‘좋은’ 것인가?”를 스스로 정의했는가?
	•	답변 결과물을 테스트할 수 있는 방법(예: 실제 코드 실행, 자료 조회)이 있는가?

⸻

9. 실제 응답 실험 및 반복 수정 (Iterative Refinement)
	•	하나의 프롬프트를 작성했다면, 실제 모델에 입력해 보고 결과물을 평가한 뒤 반복적으로 수정하는 과정이 매우 중요합니다.
	•	“무엇을 더 추가하면 모델이 더 좋은 답변을 낼까?” “어떤 부분이 과하거나 불필요할까?”를 주기적으로 점검합니다.

체크포인트
	•	피드백 루프를 통해 프롬프트를 조금씩 다르게 바꿔보며 최적의 버전을 찾았는가?
	•	다른 사람(사용자)이 동일 프롬프트를 사용했을 때도 일관되게 유사한 수준의 답변이 나오는가?

⸻

10. 윤리성 및 안전성 (Ethics & Safety)
	•	프롬프트가 민감하거나 위험한 주제를 다룰 때, 적절한 제한과 주의 문구를 포함하는지 확인합니다.
	•	예) 부적절한 콘텐츠를 만들거나 오해를 일으킬 수 있는 질의인지, 혹은 데이터 개인정보나 저작권 침해 요소가 없는지 등을 고려합니다.

체크포인트
	•	민감한 정보(개인정보, 특정 집단 차별 등을 유발할 수 있는 표현 등)가 포함되어 있지 않은가?
	•	오해의 소지가 있거나 위법한 내용을 요청하고 있지 않은가?

⸻

마무리

정리하자면, 프롬프트 퀄리티는 단순히 “길게 작성했다, 짧게 작성했다” 혹은 “몇 가지 키워드를 포함했다”가 아니라,
	1.	명확성,
	2.	목적성,
	3.	충분한 맥락/지시사항,
	4.	간결성,
	5.	논리적 구조와 일관성,
	6.	톤/스타일,
	7.	출력 형식 지정,
	8.	평가 기준,
	9.	반복적인 수정 과정,
	10.	윤리/안전성
등을 종합적으로 살피는 것이 핵심입니다.

이러한 기준을 바탕으로 자신의 프롬프트를 점검해 보면, “어떤 부분은 더 자세하게 안내해야겠다”, “어떤 표현이 모호해서 모델이 잘못 이해했겠구나” 등을 스스로 발견할 수 있고, 이를 통해 보다 효율적이고 정확한 답변을 이끌어낼 수 있습니다.
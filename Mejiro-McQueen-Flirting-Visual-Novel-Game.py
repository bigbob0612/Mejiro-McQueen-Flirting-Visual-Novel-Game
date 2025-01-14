import random
import time

class MacqueenFlirtingGame:
    def __init__(self):
        self.affection = 0
        self.turns = 0
        self.max_turns = 10
        self.player_name = ""
        self.conversation_history = []
        
        # 맥퀸의 성격 특성을 반영한 상태 변수들
        self.dessert_craving = 0  # 디저트에 대한 갈망도
        self.formal_mode = True   # 격식있는 모드인지
        self.hidden_hobbies = ["야구 관람", "영화 감상", "디저트"]
        
    def generate_response(self, choice, context):
        """맥퀸의 성격에 맞는 응답 생성"""
        responses = {
            "formal": [
                "후후... 트레이너씨도 꽤 매너가 있으시네요.",
                "메지로 가문의 일원으로서 그 말씀은 감사히 받도록 할게요.",
                "(살짝 미소지으며) 적절한 거리감이네요."
            ],
            "casual": [
                "(눈을 반짝이며) 어머, 그런 관심사가 있으셨나요?",
                "그렇게 솔직하게 말씀해주시다니... 조금 기쁘네요.",
                "(살짝 당황하며) 그렇게 직접적으로 말씀하시다니..."
            ],
            "dessert": [
                "(침을 삼키며) 디저트 이야기는... 잠시 접어두는 게 좋겠어요.",
                "디저트... 아니, 지금은 다이어트 중이니까요!",
                "(간절한 눈빛) 케이크 이야기는 금지예요..."
            ],
            "sports": [
                "(흥분을 감추며) 스포츠에 대해 관심이 있으신가요?",
                "야구... 아니, 그게 아니라 운동 경기 전반에 대해서...",
                "(꼬리가 흔들리는걸 감추며) 경기 이야기는 적당히..."
            ]
        }
        
        if "디저트" in choice:
            self.dessert_craving += 1
            response_type = "dessert"
        elif "스포츠" in choice or "운동" in choice:
            self.formal_mode = False
            response_type = "sports"
        elif self.formal_mode:
            response_type = "formal"
        else:
            response_type = "casual"
            
        return random.choice(responses[response_type])

    def calculate_affection_change(self, choice):
        """선택에 따른 호감도 변화 계산"""
        base_change = 0
        
        # 맥퀸의 성격을 반영한 호감도 변화
        if "예의" in choice or "격식" in choice:
            base_change += 10
        elif "영화" in choice or "야구" in choice:
            if self.formal_mode:
                base_change += 15  # 숨겨진 취미를 맞춘 경우 보너스
            else:
                base_change += 8
        elif "디저트" in choice:
            if self.dessert_craving < 2:
                base_change += 12
            else:
                base_change += 5  # 디저트 언급이 많으면 효과 감소
        
        return min(base_change, 20)  # 최대 20점으로 제한

    def get_choices(self):
        """현재 상황에 맞는 선택지 생성"""
        common_choices = [
            "격식있게 대화를 나눈다: '메지로 가문의 전통은 참으로 깊이가 있네요.'",
            "관심을 보인다: '최근에 재미있는 영화를 보셨나요?'",
            "칭찬한다: '오늘 특별히 우아해 보이세요.'"
        ]
        
        if not self.formal_mode:
            common_choices.extend([
                "야구 이야기를 꺼낸다: '어제 경기 보셨나요?'",
                "디저트 맛집을 추천한다: '새로 오픈한 케이크 전문점이...'",
            ])
        
        return common_choices

    def play(self):
        print("=== 메지로 맥퀸 플러팅 시뮬레이션 ===")
        self.player_name = input("트레이너님의 이름을 입력해주세요: ")
        print(f"\n메지로 맥퀸: '아라... 당신이 새로운 트레이너씨인가요? 메지로 맥퀸이라고 합니다.'")
        
        while self.turns < self.max_turns and self.affection < 100:
            print(f"\n현재 호감도: {self.affection}")
            print(f"남은 대화 기회: {self.max_turns - self.turns}")
            
            print("\n선택 가능한 대화:")
            choices = self.get_choices()
            for i, choice in enumerate(choices, 1):
                print(f"{i}. {choice}")
                
            try:
                choice_idx = int(input("\n선택하세요 (1-{}): ".format(len(choices)))) - 1
                chosen_dialogue = choices[choice_idx]
                
                response = self.generate_response(chosen_dialogue, self.conversation_history)
                affection_change = self.calculate_affection_change(chosen_dialogue)
                
                self.affection = min(100, self.affection + affection_change)
                self.turns += 1
                
                print(f"\n메지로 맥퀸: {response}")
                if affection_change > 0:
                    print(f"호감도가 {affection_change} 증가했습니다!")
                
                self.conversation_history.append((chosen_dialogue, response))
                
                # 특별 이벤트 체크
                if self.affection >= 50 and not self.conversation_history[-1][0].startswith("특별"):
                    print("\n[특별 이벤트 발생!]")
                    self._trigger_special_event()
                
            except (ValueError, IndexError):
                print("잘못된 선택입니다. 다시 선택해주세요.")
                continue
        
        self._show_ending()

    def _trigger_special_event(self):
        """특별 이벤트 발생"""
        events = [
            "메지로 맥퀸이 몰래 보관하던 야구 티켓을 떨어뜨립니다.",
            "디저트 가게 앞에서 망설이는 맥퀸과 마주칩니다.",
            "영화관 앞에서 우연히 맥퀸과 마주칩니다."
        ]
        event = random.choice(events)
        print(f"\n{event}")
        
        print("\n특별 선택지:")
        special_choices = [
            "1. 모른 척 지나간다",
            "2. 관심을 보이며 대화를 시도한다",
            "3. 상황에 맞는 특별한 제안을 한다"
        ]
        for choice in special_choices:
            print(choice)
            
        try:
            choice = int(input("\n선택하세요 (1-3): "))
            if choice == 3:
                self.affection += 15
                print("\n메지로 맥퀸: '어머... 트레이너씨... 이런 모습도 봐주시다니...'")
                self.formal_mode = False
            elif choice == 2:
                self.affection += 10
                print("\n메지로 맥퀸: '후후... 의외로 세심하신 분이네요.'")
            else:
                print("\n메지로 맥퀸: (살짝 실망한 듯한 표정을 짓습니다)")
        except ValueError:
            print("잘못된 선택입니다.")

    def _show_ending(self):
        """엔딩 표시"""
        if self.affection >= 100:
            print(f"\n축하합니다! 메지로 맥퀸의 마음을 얻는데 성공했습니다!")
            print("메지로 맥퀸: '트레이너씨... 앞으로도 잘 부탁드려요...'")
        else:
            print(f"\n아쉽게도 메지로 맥퀸의 마음을 얻는데 실패했습니다.")
            print(f"최종 호감도: {self.affection}")

if __name__ == "__main__":
    game = MacqueenFlirtingGame()
    game.play()

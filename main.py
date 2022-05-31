from davincicode.gameManager import GameManager
from davincicode.memberManager import MemberManager

import random


class Game:
    def __init__(self):
        self.gameMGR = None
        self.memberMGR = MemberManager()

    def run(self):
        option = int(input('=========== 다빈치 코드 ===========\n'
                           '1: 로그인 2: 회원가입\n'
                           '번호를 선택하세요 >> '))
        if option == 1:
            print()
            id = self.memberMGR.login()
            if id is None:
                print('로그인 실패! 게임을 종료합니다.')
            else:
                print()
                self.gameMGR = GameManager(id)
                print(str(id+'님'),'로그인 성공! 게임을 시작합니다. (Life ♥♥♥♥♥)')
                self.playGame()
        elif option == 2:
            print()
            id = self.memberMGR.signup()
            if id is None:
                print('회원가입 실패! 게임을 종료합니다.')
            else:
                self.gameMGR = GameManager(id)
                print(str(id+'님'), '회원가입 완료! 게임을 시작합니다. (Life ♥♥♥♥♥)')
                self.playGame()
        else:
            print('게임을 종료합니다.')

    def playGame(self):
        # 게임 진행
        while self.gameMGR.playerDTO.life > 0:
            if True not in self.gameMGR.gameDTO.hidden_card:
                break
            print()
            self.gameMGR.showCards()
            index = self.gameMGR.guess()
            if index != -1:
                # 추측이 맞았을 경우
                print('당신이 추측한 숫자가 맞습니다!',end='')
                self.gameMGR.openCard(index)
                self.gameMGR.showLife()
            else:
                # 추측이 틀린 경우
                print('삑- 틀렸습니다. 추측할 카드가 한 장 추가됩니다~^^',end='')
                self.gameMGR.addCard()
                self.gameMGR.loseLife()
                self.gameMGR.showLife()

                if self.gameMGR.playerDTO.life==3 or self.gameMGR.playerDTO.life==1:
                    print('너무 어려운가요? 카드를 하나 알려드릴게요~')
                    hint_index = random.randint(0, len(self.gameMGR.gameDTO.card_list)-1)

                    while not self.gameMGR.gameDTO.hidden_card[hint_index]:
                        hint_index = random.randint(0, len(self.gameMGR.gameDTO.card_list)-1)
                    self.gameMGR.openCard(hint_index)




        # 게임 결과
        print()
        life = self.gameMGR.playerDTO.life
        # 게임 점수 계산
        open_count=0
        for i in self.gameMGR.gameDTO.hidden_card:
            if not i:
                open_count+=1
        score = (open_count/len(self.gameMGR.gameDTO.hidden_card))*100
        # if score > 0:
        #     print('You Win!')
        print(self.gameMGR.playerDTO.id, '님의 점수는 ', round(score), '점 입니다.', sep='')
        # else:
        #     # 게임 오버
        #     print('-GAME OVER-')

        self.gameMGR.endGame(self.gameMGR.playerDTO.id, score)

        # 랭킹 출력
        print()
        self.gameMGR.showRanking()

Game().run()
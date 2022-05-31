from davincicode.gameDTO import GameDTO
from davincicode.playerDTO import PlayerDTO
from davincicode.rangeException import RangeException
from davincicode.recordDAO import RecordDAO
import random

class GameManager:
    def __init__(self, id):
        self.gameDTO = GameDTO()
        self.playerDTO = PlayerDTO(id)
        self.recordDAO = RecordDAO()

    def showCards(self):
        # 현재 카드 상태를 출력함 (숨김상태는 X로 표현)
        #hidden==True; X를 출력, hidden==False; 카드 숫자 출력
        for i,card in enumerate(self.gameDTO.card_list):
            if self.gameDTO.hidden_card[i]==True:
                print('X', end='\t')
            else:
                print(card, end='\t')

        print()
        #print(self.gameDTO.card_list) # 숫자 확인

    def loseLife(self):
        self.playerDTO.life -= 1

    def showLife(self):
        print(' (Life ', '♥'* self.playerDTO.life, '♡'*(5-self.playerDTO.life), ')', sep='')


    def guess(self):
        # 사용자에게 몇번째 카드를 추측할지, 어떤 숫자로 추측할지 입력받아서 맞는지 확인
        # 맞으면 True, 틀리면 False 리턴
        flag=True
        while flag:
            try:
                card_index = int(input(str('몇번째 카드를 추측하시겠습니까? (입력 범위: 1~' + str(len(self.gameDTO.card_list)) + '): '))) - 1

                if card_index < 0 or card_index >= len(self.gameDTO.card_list):
                    raise RangeException()

            except ValueError:
                print('숫자로 입력하세요.')
            except RangeException as e:
                print(e)
            else:
                flag=False


        flag=True
        while flag:
            try:
                card_n=int(input('어떤 숫자라고 예상하십니까? (입력 범위: 0~9): '))

                if card_n < 0 or card_n > 9:
                    raise RangeException()

            except ValueError:
                print('숫자로 입력하세요.')
            except RangeException as e:
                print(e)
            else:
                flag=False

        if self.gameDTO.card_list[card_index]==card_n:
            return card_index
        else:
            return -1

    def openCard(self,index):
        self.gameDTO.hidden_card[index]=False

    def addCard(self):
        ran_num = random.randint(0, 9)
        while ran_num in self.gameDTO.card_list:
            ran_num=random.randint(0,9)
        self.gameDTO.card_list.append(ran_num)
        self.gameDTO.card_list.sort()

        # card_list에서 방금 추가된 카드의 인덱스를 뽑고, hidden_list의 해당 인덱스에 True 추가.
        index=self.gameDTO.card_list.index(ran_num)
        self.gameDTO.hidden_card.insert(index, True)

    def endGame(self, id, score):
        # 사용자의 게임결과를 DB에 저장
        self.recordDAO.insertRecord(id, score)

    def showRanking(self):
        # 랭킹 조회
        rows = self.recordDAO.selectRanking()
        print('===== TOP 10 랭킹 =====')
        print('순위', '아이디', '점수', sep='\t')
        for i, row in enumerate(rows):
            print(str(i+1)+'위', row[0], str(str(row[1])+'점'), sep='\t')

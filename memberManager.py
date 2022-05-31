from davincicode.memberDAO import MemberDAO


class MemberManager:
    def __init__(self):
        self.memberDAO = MemberDAO()

    def login(self):
        # id와 pw를 입력받아 회원임을 확인한 후, 맞으면 id, 틀리면 None 리턴
        id=input('id를 입력하세요:')

        rows=self.memberDAO.checkId(id)
        if len(rows)>0:
            # pw check
            pw = input('비밀번호를 입력하세요:')
            row=self.memberDAO.selectMember(id)
            if pw==row[1]:
                return id
            else:
                print('잘못된 비밀번호 입니다.')
                return None
        else:
            print('존재하지 않는 id 입니다.')
            return None

    def signup(self):
        # id와 pw를 입력받아 DB에 저장
        id = input('id를 입력하세요:')
        rows = self.memberDAO.checkId(id)
        if len(rows) > 0:
            print('중복된 id 입니다.')
            return None
        else:
            pw = input('비밀번호를 입력하세요:')
            self.memberDAO.insertMember(id,pw)
            return id

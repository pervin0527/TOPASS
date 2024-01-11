MX = 1000005
dat = [-1] * MX
pre = [-1] * MX
nxt = [-1] * MX
unused = 1

def traverse():
    cur = nxt[0] # 시작점은 nxt[0]
    while cur != -1: # nxt[cur] == -1이면 다음 원소가 없음을 나타낸다.
        print(dat[cur], end=' ')
        cur = nxt[cur]  # 다음 노드로 이동.
    print("\n")

def insert(addr, num):
    global unused  # 전역 변수를 함수 내에서 수정하기 위해 선언
    dat[unused] = num  # 새 노드에 데이터를 저장
    pre[unused] = addr  # 새 노드의 이전 노드를 현재 노드로 설정
    nxt[unused] = nxt[addr]  # 새 노드의 다음 노드를 현재 노드의 다음 노드로 설정
    if nxt[addr] != -1:  # 현재 노드의 다음 노드가 존재하는 경우
        pre[nxt[addr]] = unused  # 현재 노드의 다음 노드의 이전 노드를 새 노드로 설정
    nxt[addr] = unused  # 현재 노드의 다음 노드를 새 노드로 설정
    unused += 1  # 사용하지 않은 다음 인덱스로 증가

def erase(addr):
    nxt[pre[addr]] = nxt[addr]  # 현재 노드의 이전 노드가 가리키는 다음 노드를 현재 노드의 다음 노드로 설정
    if nxt[addr] != -1:  # 현재 노드의 다음 노드가 존재하는 경우
        pre[nxt[addr]] = pre[addr]  # 현재 노드의 다음 노드의 이전 노드를 현재 노드의 이전 노드로 설정

insert(0, 10)  # 0번 노드 다음에 10을 삽입
insert(1, 20)  # 1번 노드 다음(새로운 노드)에 20을 삽입
insert(2, 30)
erase(1)       # 1번 노드 삭제
insert(4, 30)

traverse()
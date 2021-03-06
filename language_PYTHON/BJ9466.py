# 텀 프로젝트
import sys
input = sys.stdin.readline

T = int(input().rstrip())

def dfs(start):
    global cycle
    visited[start] = 1 # 방문처리 
    temp_cycle.append(start) # 팀원이 될 가능성이 있는 아이들
    end = student_list[start] # 선택당한 친구

    if end in temp_cycle: # cycle을 만드는지 체크
        if end not in cycle:
            cycle += temp_cycle[temp_cycle.index(end):]
        return
    else:
        dfs(end)


for i in range(T):
    N = int(input().rstrip())
    student_list =[0] + list(map(int, input().split()))
    visited = [0] * (N+1)
    cycle = []
    
    for i in range(1, len(student_list)):
        temp_cycle = []
        if visited[i] == 0: # 방문하지 않은 node라면 
            dfs(i)
    print(len(student_list)-1 - len(cycle))













# 틀린 풀이
# 1. 반례 2 3 4 5 6 2 
# for i in range(int(input().rstrip())):
#     # 초기화
#     student_num = int(input().rstrip())
#     student_list = [0] + list(map(int, input().split()))
#     student_who_has_team = []
#     visited = [0] * len(student_list)

#     for i in range(1, len(student_list)):
#         start = i
#         team_member = [start] # 팀 멤버 구성하는 애들 체크
#         visited[start] = 1 # 방문처리
#         q = deque() # 아래의 while 때문에 없어도 되지만, 초기화라는 점에서 넣어둔 코드
#         q.append(student_list[i]) 
              
#         while q:
#             end = q.popleft() 
#             if end == start: # 꼬리물기 되는 경우
#                 student_who_has_team.extend(team_member)
#                 break

#             if visited[end] == 0:  # 방문하지 않은 경우
#                 q.append(student_list[end]) 
#                 team_member.append(end)
#                 visited[end] = 1
    
#     print((len(student_list)-1) - len(student_who_has_team)) # 편의를 위해 임의로 len을 1늘렸었으므로, 다시 뺴줌

# 틀린 이유
# 1. 문제를 잘못읽음
# 알아둘것
# 1. index 활용하기
# 2. dfs설계 방식

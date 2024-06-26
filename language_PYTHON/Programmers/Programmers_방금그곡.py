
def change(m):
    m = m.replace("C#", "H")
    m = m.replace("D#", "I")
    m = m.replace("F#", "J")
    m = m.replace("G#", "K")
    m = m.replace("A#", "L")
    m = m.replace("B#", "M")

    return m


def solution(m, musicinfo_list: list):
    # 전처리 

    m = change(m)
    answer = []

    for index, music_info in enumerate(musicinfo_list):

        time = 0
        music_info = music_info.split(",")
        start_time, end_time, name, info = music_info[0], music_info[1], music_info[2], music_info[3]

        info = change(info)
        
        start_time = start_time.split(":")
        end_time = end_time.split(":")

        time = (int(end_time[0]) * 60 + int(end_time[1])) - (int(start_time[0]) * 60 + int(start_time[1]))
        
        if time < len(info):
            info = info[:time]
        
        if time > len(info):
            info = info * (time // len(info)) + info[: time % len(info)]


        if m in info:
            answer.append([time, index, name])


    if len(answer) == 0:
        return "(None)"
    
    answer.sort(key = lambda x: [-x[0], x[1]])

    return answer[0][2]

solution( "CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]	 )


# def isSame(m, melody_info):
#     for i in range(len(melody_info) - len(m) + 1):
#         check = melody_info[i: i + len(m)]
#         if check == m:
#             return True

#     return False

# def solution(m, musicinfos):
#     answer = []
#     new_music_infos = []

#     for music in musicinfos:
#         new_music = music.split(",")
        

#         end_time = new_music[1].split(":")

#         if end_time == "00:00":
#             end_time = "24:00"

#         end_time = int(end_time[0]) * 60 + int(end_time[1])
        
#         start_time = new_music[0].split(":")
#         start_time = int(start_time[0]) * 60 + int(start_time[1])

#         new_music_infos.append([end_time - start_time, new_music[2], new_music[3]])
    
#     # check
#     real_music_infos = []
#     for time, name, melody in new_music_infos:
#         index = 0
#         stack = []
#         melody_list = []
#         while index < len(melody):
#             if stack:
#                 if melody[index] == '#':
#                     stack.append(melody[index])
#                     melody_list.append("".join(stack))
#                     stack = [] # 스택 초기화
#                 else:
#                     melody_list.append(stack[0])
#                     stack = []
#                     stack.append(melody[index])
#             else:
#                 stack.append(melody[index])
            
#             index += 1
        
#         if stack:
#             melody_list.append(stack[0])
        
#         if time  < len(melody_list):
#             melody_list = melody_list[:time]
#         else:
#             melody_list = melody_list * (time // len(melody_list)) + melody_list[: time % len(melody_list)]

#         real_music_infos.append([time, name, melody_list])
    

#     new_m = []
#     index = 0
#     stack = []
#     while index < len(m):
#         if stack:
#             if m[index] == '#':
#                 stack.append(m[index])
#                 new_m.append("".join(stack))
#                 stack = [] # 스택 초기화
#             else:
#                 new_m.append(stack[0])
#                 stack = []
#                 stack.append(m[index])
#         else:
#             stack.append(m[index])

#         index += 1
        
#     if stack:
#         new_m.append(stack[0])
            
#     # # 비교후 조건에 맞는 거 체크
#     for index, music_info in enumerate(real_music_infos):
        
#         if isSame(new_m, music_info[2]):
#             answer.append([music_info[0], index, music_info[1]])  
        
            
#     if len(answer) == 0:
#         print("None")
#         return "(None)"
#     else:
#         answer.sort(key = lambda x: [-x[0], x[1]])
    
#     print(answer)
#     return answer[0][2]

# # solution("A", ["12:00,12:01,Sing,A", "12:00,12:01,Song,A"])
# # solution("A", ["12:00,12:01,Sing,A", "12:00,12:02,Song,A"] )
# # solution("A", ["12:00,12:01,Sing,A", "12:00,13:00,Song,A"])
# solution("ABA", ["12:00,13:00,Song,AB", "12:00,13:10,Song,AB", "12:00,14:00,Song,AB"] )
# # solution("BA", ["12:00,12:04,Song,A#B"] )
# # solution("A", ["12:00,12:01,Song,A#"])
# # solution("A#", ["12:00,12:01,Song,A#"])
# # solution("BA", ["12:00,12:02,Song,AB"] )
# # solution("BA", ["12:00,12:03,Song,AB"])
# # solution("A", ["12:00,12:01,Song,BA"])
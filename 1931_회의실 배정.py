import heapq
input = __import__("sys").stdin.readline

meeting_pq = []
for _ in range(int(input())):
    s, e = map(int, input().split())
    meeting_pq.append((e, s))

heapq.heapify(meeting_pq)
prev_meeting = heapq.heappop(meeting_pq)

count = 1
for _ in range(len(meeting_pq)-1):
    meeting = heapq.heappop(meeting_pq)

    if prev_meeting[0] > meeting[1]:
        continue

    count += 1
    prev_meeting = meeting

print(count)
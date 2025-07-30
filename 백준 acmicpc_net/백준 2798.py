# 백준 2798 블랙잭
# 5 21
# 5 6 7 8 9
# 완전탐색
# N, M = map(int, input().split())
# cards = list(map(int, input().split()))
#
# best_sum = 0
# for i in range(N):
#     for j in range(i + 1, N):
#         for k in range(j + 1, N):
#             total = cards[i] + cards[j] + cards[k]
#             if total <= M:
#                 best_sum = max(best_sum, total)
#
# print(best_sum)


from itertools import combinations
N, M = map(int, input().split())
cards = list(map(int, input().split()))

best = 0
for comb in combinations(cards, 3):
    total = sum(comb)
    if total <= M:
        best = max(best, total)
print(best)

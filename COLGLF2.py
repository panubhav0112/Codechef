for tc in range(int(input())):
  no_seasons = int(input())
  intro_len = list(map(int,input().split()))
  total_time = sum(intro_len)
  for ns in range(no_seasons):
    _,*ep_len = list(map(int,input().split()))
    total_time += sum(ep_len)-len(ep_len)*intro_len[ns]
  print(total_time)

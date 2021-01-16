testList = [1,2,3,4]

for number in testList : 
  print(number)


#for simple use
for i in range(10):
  print("안녕하세요",i+1,"번째 인사")

rainbow=["빨","주","노","초","파","남","보"]
for i in range(7):
  print("무지개의",i,"번째 색깔은",rainbow[i],"입니다")

days = [31,29,31,30,31,30,31,31,30,31,30,31]
for i in range(len(days)):
  print(i+1,"월의 날짜수는",days[i],"일 입니다.")


#favorite members
characters=["토마스","막스","정훈","블라드","유토"]
for i in range(len(characters)):
  print("에스디",i+1,"빠 최애는",characters[i])
# 섭씨로 37도를 화씨로 출력하고 다시 3도를 증가시켜 섭씨로 40도인 화씨를 출력

celsius = 37
fahrenhite = celsius * 9/5 + 32 # 화씨로 변환
print('섭씨: ' ,celsius ,' ,' ,'화씨: ' ,fahrenhite)

celsius += 3 # 섭씨 증가
fahrenhite = celsius * 9/5 + 32 # 화씨로 변환
print('섭씨: ' ,celsius ,' ,' ,'화씨: ' ,fahrenhite)

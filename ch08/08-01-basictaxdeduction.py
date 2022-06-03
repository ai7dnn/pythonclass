#‘1,200만원 초과 ~ 4,600만원 이하’ 구간의 누진공제액 계산
smoney = 12_000000 
rate1 = 6
rate2 = 15
deduction = smoney * (rate2 - rate1)/100
print('누진공제액 1: {:,.0f}'.format(deduction))

# ‘4,600만원 초과 ~ 8,800만원 이하’ 구간의 누진공제액 계산
rate1, rate2, rate3 = 6, 15, 24
smoney1, smoney2 = 12_000000, 46_000000 
deduction = smoney1 * (rate3 - rate1)/100 #1천2백만원에 대한 누진공제
deduction += (smoney2 - smoney1) * (rate3 - rate2)/100 #3천4백만원에 대한 누진공제
print('누진공제액 2: {:,.0f}'.format(deduction))

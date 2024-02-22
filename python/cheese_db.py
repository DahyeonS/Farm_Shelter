from farm.models import Cheese_detail

cheese_list = sorted([
    '고다', '고르곤졸라', '로크포르', '리코타', '림버거', '만체고', '모나스테로',
    '모짜렐라', '몬트레이 잭', '부라타', '브리', '블루 스틸', '블루',
    '스위스', '아시아고', '에멘탈', '체다', '파마산', '페타', '프로볼로네'
])

for cheese in cheese_list :
    c = Cheese_detail(name=cheese)
    c.save()
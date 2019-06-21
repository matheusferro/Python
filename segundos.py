segundo = input("Digite o valor em segundos: ")
seg = int(segundo)

hr = seg // 3600
dia = hr // 24
hr_final = hr % 24
seg_restante = seg % 3600
minuto = seg_restante // 60
seg_final = seg_restante % 60

segundo = seg % 60

print("{} dias, {} horas, {} minutos e {} segundos.".format(dia,hr_final,minuto, seg_final))
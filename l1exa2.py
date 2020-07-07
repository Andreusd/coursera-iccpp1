segundos_totais=int(input("Por favor, entre com o número de segundos que deseja converter:"))
dias = segundos_totais // 86400
segundos_restantes_dias = segundos_totais % 86400
horas = segundos_restantes_dias // 3600
segundos_restantes_horas = segundos_restantes_dias % 3600
minutos = segundos_restantes_horas // 60
segundos = segundos_restantes_horas % 60
print(dias,"dias,",horas,"horas,",minutos,"minutos e",segundos,"segundos.")

from tutor import Tutor
from pet import Pet
from servico import Servico
from agendamento import Agendamento

t1 = Tutor(1, "João", "99999-9999")
p1 = Pet(1, "Rex", "Cachorro", 5, t1)
s1 = Servico(1, "Banho", 80.0)

ag = Agendamento(1, p1, s1, "2030-05-10 14:00")

print(t1)
print(p1)
print(s1)
print(ag)

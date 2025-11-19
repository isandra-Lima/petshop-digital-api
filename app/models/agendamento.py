from datetime import datetime
from pet import Pet
from servico import Servico

class Agendamento:
    def __init__(self, id: int, pet: Pet, servico: Servico, data_horario: str):
        data_convertida = datetime.fromisoformat(data_horario)

        if data_convertida < datetime.now():
            raise ValueError("Não é possível agendar para uma data passada.")

        self.id = id
        self.pet = pet
        self.servico = servico
        self.data_horario = data_convertida

    def __repr__(self):
        return (f"Agendamento(id={self.id}, pet={self.pet.nome}, "
                f"servico={self.servico.nome}, data={self.data_horario})")

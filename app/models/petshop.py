class Petshop:
    def __init__(self):
        self.tutores = []
        self.pets = []
        self.servicos = []
        self.agendamentos = []

    def cadastrar_tutor(self, tutor):
        self.tutores.append(tutor)

    def cadastrar_pet(self, pet):
        self.pets.append(pet)

    def cadastrar_servico(self, servico):
        self.servicos.append(servico)

    def realizar_agendamento(self, agendamento):
        for ag in self.agendamentos:
            if ag.pet.id == agendamento.pet.id and ag.data_horario == agendamento.data_horario:
                raise ValueError("O pet já tem um agendamento nesse horário")
        
        self.agendamentos.append(agendamento)

    def listar_agendamentos(self):
        return self.agendamentos

    def listar_pets(self):
        return self.pets

    def listar_tutores(self):
        return self.tutores

    def listar_servicos(self):
        return self.servicos

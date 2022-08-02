# Sistema Web - Controle Acadêmico
Sistema Web para controle acadêmico desenvolvido em python e django com o objetivo de praticar as habilidades aprendidas com o django

# Requisitos do Sistema
### 1. Professor:
   - RF001: pode realizar cadastro/login como professor
   - RF002: pode cadastrar/excluir/atualizar/visualizar disciplina em curso
   - RF003: pode lançar notas do estudante
   - RF004: pode remover estudante da disciplina
   - RF005: pode aceitar ou recusar matrícula de estudante na disciplina
   <br/>
   
   - RNF001: depois que lançar a nota, o professor só pode visualizar
   - RNF002: os professores só podem acessar as disciplinas associadas ao seu perfil 

### 2. Estudante:
   - RF006: pode realizar cadastro/login como estudante
   - RF007: o estudante pode solicitar matricula em disciplina do curso
   <br/>
   
   - RNF003: o estudandte só pode realizar matricula na disciplina associada ao curso
   - RNF004: um estudante precisa estar associado a um curso para ser matriculado
   
### 3. Plataforma (curso e disciplina):
   - RF008: o curso pode conter professores e estudantes
   - RF009: pode aceitar cadastro de disciplinas
   <br/>

   - RNF005: a plataforma pode pode ser acessada sem autenticação, mas somente os cursos, as disciplinas e os professores associadas podem ser visualizados
   - RNF006: uma disciplina não pode existir sem um professor associado
   - RNF007: uma disciplina não pode existir sem estar associada a um curso

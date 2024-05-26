# TDD Project
Projeto para realizar a API com TDD

## Desafio Final
- Create
    - Mapear uma exceção, caso dê algum erro de inserção e capturar na controller
- Update
    - Modifique o método de patch para retornar uma exceção de Not Found, quando o dado não for encontrado
    - a exceção deve ser tratada na controller, pra ser retornada uma mensagem amigável pro usuário
    - ao alterar um dado, a data de updated_at deve corresponder ao time atual, permitir modificar updated_at também

- Filtros
    - cadastre produtos com preços diferentes
    - aplique um filtro de preço, assim: (price > 5000 and price < 8000)


Entregue 25/05/2024, quaisquer possíveis erros não mapeados podem ocorrer ao executar o fonte por conta de versões diferentes de ambiente.
OBSERVAÇÃO: adaptação realizada para aproveitar o UUID do MongoDB como entrada 'puuid' na ocasião a versão utilizada do MongoDB não permitia a inserção de ObjectID da forma apresentada.

- Este é um exemplo clássico usando o Mediator Pattern, nesse exercício vamos simular uma sala de bate papo.
- A classe ChatRoom tem que a responsabilidade de funcionar como nosso Mediator.
- O método person.receive() é responsável por registrar as mensagens.
- Para isso deverá ser implementado os 3 metodos a seguir com suas respectivas responsabilidades:
  - join() a responsabilidade desse método é:
    - Notificar os usuário que estão dentro do chat (lista peoples) de que um novo usuário entrou.
      - Para isso é necessário o método broadcast()
    - Atribuir o endereço de memória do chat ao objeto pessoa
    - Adicionar o objeto do tipo Pessoa dentro do objeto peoples.
  - message() a responsabilidade desse método é:
    - Enviar a mensagem diretamente para um determinado usuário
  - broadcast() a responsabilidade desse método é:
    - Funcionar como uma linha de trasmissão geral onde todos são notificados quando alguem entra através do método join()
    - ATENÇÃO!!! NÃO NOTIFICAR dentro do brodcast() o próprio usuário quando chamar o método Person.say().

- A saída deve fica da seguinte forma:
  [Jefté's chat session] room: Brenno joins the chat
  [Jefté's chat session] room: Bárbara joins the chat
  [Brenno's chat session] room: Bárbara joins the chat  
  [Brenno's chat session] Jefté: Hi room!
  [Bárbara's chat session] Jefté: Hi room!
  [Jefté's chat session] Brenno: Oh, hey Jefté, how are you?  
  [Bárbara's chat session] Brenno: Oh, hey Jefté, how are you?
  [Jefté's chat session] Brenno: Great.
  [Bárbara's chat session] Brenno: Great.
  [Jefté's chat session] Bárbara: Hi guys.
  [Brenno's chat session] Bárbara: Hi guys.
  [Jefté's chat session] room: Sabrina joins the chat
  [Brenno's chat session] room: Sabrina joins the chat  
  [Bárbara's chat session] room: Sabrina joins the chat  
  [Jefté's chat session] Sabrina: Meow ;P

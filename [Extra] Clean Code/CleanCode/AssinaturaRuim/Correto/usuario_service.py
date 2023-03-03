from usuario import Usuario


class UsuarioService:
    def __init__(self) -> None:
        self.usuarios: list[Usuario]
        self.usuarios.append(Usuario("Eduardo", "edu123", "1q234"))
    
    def buscar_usuario(self, usuario) -> Usuario:
        return self.usuarios[0] # Aqui teria o "where" buscando pelo nome.
        
    def login(self, usuario: str, senha: str):
        usuario: Usuario = self.usuarios[0] # Aqui teria o "where" buscando por usuário + senha.
        
        if (usuario != None):
            return usuario
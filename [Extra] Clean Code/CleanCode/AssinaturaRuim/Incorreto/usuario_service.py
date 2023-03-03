from usuario import Usuario


class UsuarioService:
    def __init__(self) -> None:
        self.usuarios: list[Usuario]
        self.usuarios.append(Usuario("Eduardo", "edu123", "1q234"))
    
    def BuscarUsuario(self, usuario: str, senha: str, logado: bool):
        if (not logado):
            usuario: Usuario = self.usuarios[0] # Aqui teria o "where" buscando por usuário + senha.
            
            if (usuario != None):
                return usuario
            
        else:
            usuario: Usuario = self.usuarios[0] # Aqui teria o "where" buscando pelo nome.
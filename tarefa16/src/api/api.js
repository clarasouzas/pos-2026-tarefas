const URL = "https://jsonplaceholder.typicode.com";

export function buscarUsuarios() {
  return fetch(`${URL}/users`)
    .then((response) => response.json());
}

export function buscarTarefas(idUsuario) {
  return fetch(`${URL}/users/${idUsuario}/todos`)
    .then((response) => response.json());
}
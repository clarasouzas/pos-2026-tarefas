const app = document.querySelector("#app");

let listaUsuarios;
let listaTarefas;
let infoUsuario;
let cardsUsuarios;

export function criarLayout() {
  const titulo = document.createElement("h1");
  titulo.className = "titulo";
  titulo.innerHTML = `<i class="bi bi-people-fill"></i> Usuários e Tarefas`;

  const container = document.createElement("div");
  container.className = "container";

  const colunaUsuarios = document.createElement("section");
  colunaUsuarios.className = "painel";

  const colunaTarefas = document.createElement("section");
  colunaTarefas.className = "painel";

  const tituloUsuarios = document.createElement("h2");
  tituloUsuarios.innerHTML = `<i class="bi bi-person-lines-fill"></i> Usuários`;

  const tituloTarefas = document.createElement("h2");
  tituloTarefas.innerHTML = `<i class="bi bi-list-check"></i> Tarefas`;

  cardsUsuarios = document.createElement("div");
  cardsUsuarios.className = "cards-usuarios";

  infoUsuario = document.createElement("div");
  infoUsuario.className = "info-usuario";

  listaTarefas = document.createElement("div");
  listaTarefas.className = "lista-tarefas";

  listaUsuarios = cardsUsuarios;

  colunaUsuarios.append(tituloUsuarios, cardsUsuarios);

  colunaTarefas.append(
    tituloTarefas,
    infoUsuario,
    listaTarefas
  );

  container.append(colunaUsuarios, colunaTarefas);

  app.append(titulo, container);
}

export function mostrarUsuarios(usuarios, callback) {
  listaUsuarios.innerHTML = "";

  usuarios.forEach((usuario) => {
    const card = document.createElement("div");
    card.className = "card-usuario";

    const avatar = document.createElement("div");
    avatar.className = "avatar";
    avatar.textContent = usuario.name.charAt(0);

    const dados = document.createElement("div");
    dados.className = "dados";

    dados.innerHTML = `
      <h3>${usuario.name}</h3>
    `;

    card.append(avatar, dados);

    card.addEventListener("click", () => {
      document
        .querySelectorAll(".card-usuario")
        .forEach((item) => item.classList.remove("ativo"));

      card.classList.add("ativo");

      callback(usuario);
    });

    listaUsuarios.append(card);
  });
}

export function mostrarResumo(usuario, tarefas) {
  const concluidas = tarefas.filter((tarefa) => tarefa.completed).length;
  const pendentes = tarefas.length - concluidas;

  infoUsuario.innerHTML = `
    <div class="cabecalho-usuario">
      <div class="avatar grande">
        ${usuario.name.charAt(0)}
      </div>

      <div>
        <h3>${usuario.name}</h3>
        <span>${usuario.company.name}</span>

        <p>
          <i class="bi bi-envelope"></i>
          ${usuario.email}
        </p>

        <p>
          <i class="bi bi-geo-alt"></i>
          ${usuario.address.city}
        </p>
      </div>
    </div>
  `;
}

export function mostrarTarefas(tarefas) {
  listaTarefas.innerHTML = "";

  tarefas.forEach((tarefa) => {
    const card = document.createElement("div");
    card.className = "card-tarefa";

    const icone = tarefa.completed
      ? `<i class="bi bi-check-circle-fill"></i>`
      : `<i class="bi bi-circle"></i>`;

    card.innerHTML = `
      <div class="${tarefa.completed ? "concluida" : "pendente"}">
        ${icone}
      </div>

      <p>${tarefa.title}</p>
    `;

    listaTarefas.append(card);
  });
}
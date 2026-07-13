import "./style.css";

import { buscarUsuarios, buscarTarefas } from "./api/api";
import {
  criarLayout,
  mostrarUsuarios,
  mostrarTarefas,
  mostrarResumo,
} from "./ui/dom";

criarLayout();

buscarUsuarios()
  .then((usuarios) => {
    mostrarUsuarios(usuarios, (usuario) => {
      buscarTarefas(usuario.id)
        .then((tarefas) => {
          mostrarResumo(usuario, tarefas);
          mostrarTarefas(tarefas);
        })
        .catch(() => {
          alert("Erro ao carregar as tarefas.");
        });
    });
  })
  .catch(() => {
    alert("Erro ao carregar os usuários.");
  });
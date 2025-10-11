# 🧮 Calculadora de CR

Este script calcula **a média necessária no semestre atual** para atingir o **CR (Coeficiente de Rendimento) desejado**.  
Caso a média necessária seja **maior que 10**, é informado o **CR máximo possível** se você tirar **10** em todas as disciplinas do semestre.

## Como usar?
Ao rodar, insira o seu CR atual (referente ao último período cursado), em seguida informe o período que você está cursando atualmente (no qual está matriculado) e, por fim, o CR que deseja alcançar ao concluir as disciplinas do período em andamento

## Parâmetros

| Parâmetro | Tipo  | Descrição |
|------------|--------|------------|
| `cra` | `float` | Seu CR atual |
| `p` | `int` | Seu período atual |
| `crf` | `float` | CR desejado ao final do semestre |

## Output

| Retorno | Tipo | Descrição |
|----------|------|------------|
| `media_necessaria` | `float` | Média necessária no semestre atual |

Se `media_necessaria > 10`, o programa retorna o **CR máximo possível** se a média for 10.

### Observações

A fórmula usada é válida para **minha instituição** e para cursos em que todas **as disciplinas têm o mesmo peso**.
Não estou considerando TCC ou Estágio obrigatório, que costumam ter peso maior (ainda não cheguei lá rs).

Sinta-se à vontade para adaptar o código ao seu contexto, criei esse cod porque estava cansada de fazer esse cálculo à mão toda vez.

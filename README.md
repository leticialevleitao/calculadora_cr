# 🧮 Calculadora de CR

Este script calcula **a média necessária no semestre atual** para atingir o **CR (Coeficiente de Rendimento) desejado**.  
Caso a média necessária seja **maior que 10**, o programa informa o **CR máximo possível** se você tirar **10** em todas as disciplinas do semestre.

## Parâmetros

| Parâmetro | Tipo  | Descrição |
|------------|--------|------------|
| `cra` | `float` | Seu CR atual |
| `p` | `int` | Seu período atual |
| `crf` | `float` | CR desejado ao final do semestre |

## Retorna

| Retorno | Tipo | Descrição |
|----------|------|------------|
| `media_necessaria` | `float` | Média necessária no semestre atual |

Se `media_necessaria > 10`, o programa retorna também o **CR máximo possível** se a média for 10.

### Observações

A fórmula usada é válida para **minha instituiçã**o e para cursos em que todas **as disciplinas têm o mesmo peso**.
Não estou considerando TCC ou Estágio obrigatório, que costumam ter peso maior (ainda não cheguei lá rs).

Sinta-se à vontade para adaptar o código ao seu contexto, criei esse cod porque estava cansada de fazer esse cálculo à mão toda vez.

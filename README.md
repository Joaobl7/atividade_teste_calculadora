Criamos uma estrutura chamada **Calculadora**.

Essa estrutura é uma **classe**, que nada mais é do que uma forma de **juntar várias funções** que fazem parte de um mesmo grupo — no caso, **operações matemáticas**.

### 🔧 O que cada função faz:

* `soma(a, b)` → retorna a soma de dois números.
* `subtrai(a, b)` → calcula a diferença entre dois números.
* `multiplica(a, b)` → retorna o produto (a multiplicação) dos dois.
* `divide(a, b)` → realiza a divisão e **gera um erro** se o segundo número for zero.
* `potencia(a, b)` → faz a potenciação, ou seja, eleva o número `a` à potência `b`.
* `raiz(x)` → calcula a raiz quadrada de um número e **avisa se ele for negativo**.
* `media(lista)` → retorna a média de uma lista de números. Se a lista estiver vazia, **gera um erro**.
* `modulo(x)` → devolve o valor absoluto (sem sinal negativo).
* `percentual(parte, total)` → calcula quantos por cento uma parte representa de um total. **Dá erro se o total for zero**.

---

## ✅ Os Testes com Pytest (`test_calculadora.py`)

Usamos o **pytest**, que é uma ferramenta para automatizar testes no Python.

Cada função da calculadora é testada para garantir que ela está funcionando como deveria.

### Exemplos de teste:

* `assert Calculadora.soma(3, 2) == 5` → verifica se a soma está certa.
* Também testamos **situações com erro**, como:

  * Dividir por zero.
  * Calcular raiz quadrada de número negativo.
  * Fazer média de uma lista vazia.
  * Calcular percentual com total igual a zero.

---

## 🔁 Como tudo se conecta

1. Você chama uma função da calculadora, como: `Calculadora.soma(4, 5)`.
2. Ela retorna o resultado correto (neste caso, `9`).
3. O pytest roda todos os testes automaticamente e mostra se **tudo está funcionando** como esperado.
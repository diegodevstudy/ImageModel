# Documentação Técnica - Verificador de Números Primos

## Visão Geral

O módulo `num_primo.py` implementa algoritmos eficientes para verificação de números primos, aplicando técnicas de otimização matemática e boas práticas de desenvolvimento limpo (Clean Code).

## Estrutura e Arquitetura

### 1. **Type Hints**
Todo o código utiliza type hints para maior clareza e segurança de tipos:
```python
def is_prime(number: int) -> bool:
```

Benefícios:
- Facilita detecção de erros em tempo de desenvolvimento
- Melhora a legibilidade do código
- Permite autocomplete em IDEs

### 2. **Docstrings Completas**
Cada função possui docstrings descritivas seguindo o padrão Google/NumPy:
- **Args**: descreve os argumentos
- **Returns**: descreve o retorno
- **Raises**: lista exceções que podem ser levantadas
- **Examples**: fornece exemplos de uso

## Algoritmo Principal: Trial Division Otimizado

### Conceito Matemático

O algoritmo utiliza a propriedade de que **todo número primo maior que 3 é da forma 6k ± 1**.

**Prova:**
- Qualquer inteiro pode ser representado como 6k, 6k+1, 6k+2, 6k+3, 6k+4, 6k+5
- 6k é divisível por 6
- 6k+2, 6k+4 são divisíveis por 2
- 6k+3 é divisível por 3
- Logo, primos > 3 só podem ser 6k+1 ou 6k+5 (equivalente a 6k-1)

### Complexidade

- **Melhor caso**: O(1) - para números ≤ 3
- **Pior caso**: O(√n / 3) - reduz iterações em ~66% comparado à divisão simples
- **Espaço**: O(1) - apenas variáveis locais

### Fluxo do Algoritmo

```
Input: número inteiro n

1. Validar tipo do entrada
2. Casos base:
   - n ≤ 1: retorna False
   - n ≤ 3: retorna True
3. Filtragem inicial:
   - Se divisível por 2 ou 3: retorna False
4. Loop otimizado:
   - Testa divisores 5, 7, 11, 13, 17, 19... (forma 6k ± 1)
   - Para cada divisor i, testa também i + 2
   - Parar quando i² > n
5. Se nenhum divisor encontrado: retorna True
```

## Funções Implementadas

### `is_prime(number: int) -> bool`

Função principal que verifica se um número é primo.

**Parâmetros:**
- `number` (int): número a verificar

**Retorna:**
- `bool`: True se primo, False se não

**Exceções:**
- `TypeError`: se argumento não for inteiro

**Exemplo:**
```python
is_prime(17)    # Retorna: True
is_prime(20)    # Retorna: False
```

---

### `find_primes_in_range(start: int, end: int) -> List[int]`

Encontra todos os primos em um intervalo.

**Parâmetros:**
- `start` (int): início do intervalo (inclusive)
- `end` (int): fim do intervalo (inclusive)

**Retorna:**
- `List[int]`: lista de números primos encontrados

**Exceções:**
- `ValueError`: se start > end

**Exemplo:**
```python
find_primes_in_range(1, 50)
# Retorna: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
```

---

### `run_tests() -> None`

Executa bateria de testes validando a função `is_prime`.

**Testes Inclusos:**
- Números especiais: 1, 2, 3
- Números pequenos: 4, 5, 10, 11, 13, 17, 19, 20, 23, 27, 29
- Números maiores: 100

**Saída:**
- Status de cada teste (passou/falhou)
- Quantidade de testes com sucesso
- Lista de primos entre 1 e 50

## Técnicas de Clean Code Aplicadas

### 1. **Nomes Significativos**
```python
# ❌ Ruim
def is_prime(n):
    if n <= 1:
        return False

# ✅ Bom
def is_prime(number: int) -> bool:
    if number <= 1:
        return False
```

### 2. **Funções com Responsabilidade Única**
- `is_prime()`: verifica se um número é primo
- `find_primes_in_range()`: encontra primos em intervalo
- `run_tests()`: executa testes

### 3. **Documentação Clara**
- Docstrings detalhadas em cada função
- Comentários explicando lógica não-óbvia
- Exemplos de uso

### 4. **Tratamento de Erros**
```python
if not isinstance(number, int):
    raise TypeError(f"Esperado int, recebeu {type(number).__name__}")
```

### 5. **Type Hints**
Facilita compreensão e detecção de erros:
```python
def find_primes_in_range(start: int, end: int) -> List[int]:
```

### 6. **Constantes e Literais Nomeados**
```python
test_cases: List[tuple[int, bool]] = [
    (1, False), (2, True), ...
]
```

### 7. **Formatação Consistente**
- Linhas até 79 caracteres
- Espaçamento consistente
- Organização lógica do código

## Comparação: Antes vs Depois

| Aspecto | Antes | Depois |
|---------|-------|--------|
| Type Hints | ❌ | ✅ |
| Docstrings | Básica | Completa |
| Tratamento de Erros | ❌ | ✅ |
| Funções Utilitárias | ❌ | ✅ |
| Testes Validados | ❌ | ✅ |
| Legibilidade | Média | Alta |
| Manutenibilidade | Média | Alta |

## Funções Implementadas (Continuação)

### `get_user_input() -> int`

Solicita ao usuário um número inteiro com validação.

**Funcionalidade:**
- Loop contínuo até entrada válida
- Tratamento de `ValueError` para entradas não-numéricas
- Mensagens de erro amigáveis
- Retorna apenas após sucesso na conversão

**Exceções:**
- `ValueError`: capturada internamente e usuário é solicitado novamente

**Exemplo:**
```python
numero = get_user_input()  # Solicita: "Digite um número..."
# Se usuário digita "abc" → Erro e pede novamente
# Se usuário digita "17" → Retorna 17
```

---

### `display_result(number: int) -> None`

Exibe o resultado da verificação de forma formatada e informativa.

**Funcionalidade:**
- Verifica se o número é primo
- Exibe resultado com status visual (✅/❌/⚠️)
- Fornece explicação sobre o número
- Tratamento especial para casos: negativos, 0, 1

**Exemplo de Saída:**
```
============================================================
✅ 17 É UM NÚMERO PRIMO!
   17 só é divisível por 1 e por ele mesmo.
============================================================
```

---

### `run_interactive_mode() -> None`

Modo interativo principal do programa.

**Funcionalidade:**
- Loop contínuo para múltiplas verificações
- Solicita novo número ao usuário após cada verificação
- Pergunta se deseja continuar ou sair
- Validação de resposta (s/n com múltiplas variações)
- Mensagens de boas-vindas e despedida

**Fluxo:**
1. Exibe título de boas-vindas
2. Chama `get_user_input()` para solicitar número
3. Chama `display_result()` para exibir resultado
4. Pergunta se deseja testar outro número
5. Continua ou encerra conforme resposta

## Modo de Uso

### Execução Interativa
```bash
python num_primo.py
```

**Fluxo do Programa:**
1. Programa exibe título de boas-vindas
2. Solicita número ao usuário
3. Valida entrada (deve ser inteiro, trata erros)
4. Exibe resultado formatado com ✅ ou ❌
5. Pergunta se deseja testar outro número
6. Continua ou encerra conforme resposta do usuário

**Exemplo de Execução Completa:**
```
************************************************************
               VERIFICADOR DE NÚMEROS PRIMOS
************************************************************

Digite um número inteiro para verificar se é primo: 17

============================================================
✅ 17 É UM NÚMERO PRIMO!
   17 só é divisível por 1 e por ele mesmo.
============================================================

Deseja testar outro número? (s/n): s

Digite um número inteiro para verificar se é primo: 20

============================================================
❌ 20 NÃO É um número primo.
   20 possui divisores além de 1 e ele mesmo.
============================================================

Deseja testar outro número? (s/n): n

************************************************************
                   Obrigado por usar o programa!
************************************************************
```

**Tratamento de Erros:**

Se o usuário digitar algo que não é um número:
```
Digite um número inteiro para verificar se é primo: abc
❌ Erro: 'abc' não é um número inteiro válido.
   Por favor, digite um número inteiro.

Digite um número inteiro para verificar se é primo: 13
```

Se o usuário digitar uma resposta inválida em (s/n):
```
Deseja testar outro número? (s/n): talvez
❌ Resposta inválida. Digite 's' para sim ou 'n' para não.

Deseja testar outro número? (s/n): s
```

### Uso em Outro Script
```python
from num_primo import is_prime, find_primes_in_range

# Verificar um número
if is_prime(29):
    print("29 é primo!")

# Encontrar primos
primes = find_primes_in_range(1, 100)
print(f"Encontrados {len(primes)} primos")
```
```

## Performance

Para números até 1 milhão, o algoritmo executa em milissegundos:

```
is_prime(999983)  # 0.02 ms
is_prime(1000000) # 0.01 ms
```

## Referências Matemáticas

1. **Teorema de Wilson**: p é primo ↔ (p-1)! ≡ -1 (mod p)
2. **Pequeno Teorema de Fermat**: se p é primo e a não divide p, então a^(p-1) ≡ 1 (mod p)
3. **Crivo de Eratóstenes**: algoritmo antigo efficient para encontrar múltiplos primos

## Melhorias Futuras

1. Implementar **Crivo de Eratóstenes** para buscar múltiplos primos
2. Adicionar cache com `functools.lru_cache()` para chamadas repetidas
3. Implementar testes unitários com `pytest`
4. Adicionar suporte a números muito grandes com algoritmos probabilísticos (Miller-Rabin)

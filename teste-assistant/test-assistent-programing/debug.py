"""
Módulo para cálculo de totais de compra com imposto e desconto.

Este módulo fornece funções para processar informações de compra,
incluindo coleta de dados, cálculos de valores e exibição formatada
de recibos de compra.

Arquitetura: Funções especializadas em responsabilidades únicas (Single Responsibility)
Permite testes unitários, reusabilidade e fácil manutenção.
"""

from typing import Tuple  # Tipagem para retornos múltiplos - mais seguro que listas


def coletar_nome_cliente() -> str:
    """
    Coleta o nome do cliente via entrada do usuário.
    
    Retorna:
        str: Nome do cliente fornecido pelo usuário.
        
    Exemplo:
        >>> nome = coletar_nome_cliente()
        Qual é seu nome? João
        >>> print(nome)
        João
    """
    return input("Qual é seu nome? ")


def coletar_itens() -> Tuple[int, float, int, float, int, float]:
    """
    Coleta informações de quantidade e preço para três itens.
    
    Solicita ao usuário a quantidade e o preço para cada item
    de compra (item 1, item 2 e item 3).
    
    Retorna:
        Tupla contendo (qtd1, item1, qtd2, item2, qtd3, item3) onde:
        - qtd1 (int): Quantidade do item 1
        - item1 (float): Preço unitário do item 1
        - qtd2 (int): Quantidade do item 2
        - item2 (float): Preço unitário do item 2
        - qtd3 (int): Quantidade do item 3
        - item3 (float): Preço unitário do item 3
        
    Exemplo:
        >>> qtd1, item1, qtd2, item2, qtd3, item3 = coletar_itens()
        Quantidade do item 1: 2
        Preço do item 1? 10.5
        ...
    """
    # Conversão int() para quantidade garante que apenas números inteiros sejam aceitos
    # Conversão float() para preços permite valores decimais (e.g., 10.50)
    qtd1 = int(input("Quantidade do item 1: "))
    item1 = float(input("Preço do item 1? "))

    qtd2 = int(input("Quantidade do item 2: "))
    item2 = float(input("Preço do item 2? "))

    qtd3 = int(input("Quantidade do item 3: "))
    item3 = float(input("Preço do item 3? "))
    
    return qtd1, item1, qtd2, item2, qtd3, item3


def calcular_totais_itens(
    qtd1: int, 
    item1: float,
    qtd2: int,
    item2: float,
    qtd3: int,
    item3: float
) -> Tuple[float, float, float, float]:
    """
    Calcula os totais de cada item e o subtotal.
    
    Multiplica quantidade por preço unitário para cada item
    e calcula o subtotal da compra.
    
    Args:
        qtd1: Quantidade do item 1.
        item1: Preço unitário do item 1.
        qtd2: Quantidade do item 2.
        item2: Preço unitário do item 2.
        qtd3: Quantidade do item 3.
        item3: Preço unitário do item 3.
        
    Retorna:
        Tupla contendo (total_item1, total_item2, total_item3, subtotal) onde:
        - total_item1 (float): Total do item 1 (qtd1 × item1)
        - total_item2 (float): Total do item 2 (qtd2 × item2)
        - total_item3 (float): Total do item 3 (qtd3 × item3)
        - subtotal (float): Soma dos totais dos itens
        
    Exemplo:
        >>> total1, total2, total3, sub = calcular_totais_itens(2, 10.5, 1, 5.0, 3, 2.5)
        >>> print(f"Subtotal: R$ {sub:.2f}")
        Subtotal: R$ 33.50
    """
    # Cálculo individual para rastreabilidade no recibo
    # Usando float garante precisão em operações monetárias
    total_item1 = qtd1 * item1
    total_item2 = qtd2 * item2
    total_item3 = qtd3 * item3
    # Subtotal usado como base para imposto e desconto (cálculos subsequentes)
    subtotal = total_item1 + total_item2 + total_item3
    
    return total_item1, total_item2, total_item3, subtotal


def coletar_desconto(subtotal: float) -> Tuple[float, float]:
    """
    Coleta o percentual de desconto e calcula o valor do desconto.
    
    Solicita ao usuário um percentual de desconto (ou 0 para sem desconto)
    e calcula o valor em reais correspondente.
    
    Args:
        subtotal: Valor do subtotal da compra em reais.
        
    Retorna:
        Tupla contendo (desconto_cupom, desconto) onde:
        - desconto_cupom (float): Percentual de desconto informado pelo usuário
        - desconto (float): Valor do desconto em reais
        
    Exemplo:
        >>> desc_perc, desc_val = coletar_desconto(100.0)
        Você tem um cupom de desconto? (Digite o percentual ou 0): 10
        >>> print(f"Desconto: R$ {desc_val:.2f}")
        Desconto: R$ 10.00
    """
    # Retorna percentual e valor em reais separadamente para exibição no recibo
    # Permite mostrar ambos na formatação (desconto_cupom na tela, desconto no cálculo)
    desconto_cupom = float(input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))
    # Fórmula: valor = subtotal * (percentual / 100)
    desconto = subtotal * (desconto_cupom / 100)
    
    return desconto_cupom, desconto


def calcular_total_final(subtotal: float, imposto: float, desconto: float) -> float:
    """
    Calcula o valor total final da compra.
    
    Adiciona o imposto e subtrai o desconto do subtotal
    para obter o valor total a pagar.
    
    Args:
        subtotal: Valor do subtotal da compra.
        imposto: Valor do imposto aplicado.
        desconto: Valor do desconto aplicado.
        
    Retorna:
        float: Valor total final da compra (subtotal + imposto - desconto).
        
    Exemplo:
        >>> total = calcular_total_final(100.0, 10.0, 5.0)
        >>> print(f"Total: R$ {total:.2f}")
        Total: R$ 105.00
    """
    return subtotal + imposto - desconto


def exibir_recibo(
    cliente: str,
    total_item1: float,
    total_item2: float,
    total_item3: float,
    subtotal: float,
    imposto: float,
    desconto_cupom: float,
    desconto: float,
    total: float
) -> None:
    """
    Exibe o recibo da compra de forma formatada.
    
    Imprime um recibo formatado com todas as informações da compra,
    incluindo itens, subtotal, imposto, desconto (se aplicável) e total.
    
    Args:
        cliente: Nome do cliente.
        total_item1: Valor total do item 1.
        total_item2: Valor total do item 2.
        total_item3: Valor total do item 3.
        subtotal: Subtotal da compra.
        imposto: Valor do imposto (10%).
        desconto_cupom: Percentual de desconto aplicado.
        desconto: Valor do desconto em reais.
        total: Valor total final a pagar.
        
    Retorna:
        None
        
    Exemplo:
        >>> exibir_recibo("João", 21.0, 5.0, 7.5, 33.5, 3.35, 10.0, 3.35, 33.5)
        ===============================
         Cliente: João
        ===============================
        ...
    """
    # Variáveis de formatação para consistência visual em todo o recibo
    # 31 caracteres escolhido para largura adequada de terminal padrão
    linha = "=" * 31  # Delimitador superior e inferior
    separador = "-" * 31  # Divisor entre seções

    print(linha)
    print(f" Cliente: {cliente}")
    print(linha)
    print(f" Item 1:        R$ {total_item1:.2f}")
    print(f" Item 2:        R$ {total_item2:.2f}")
    print(f" Item 3:        R$ {total_item3:.2f}")
    print(separador)
    print(f" Subtotal:      R$ {subtotal:.2f}")
    print(f" Imposto (10%): R$ {imposto:.2f}")

    # Validação: só exibe desconto se foi informado (desconto_cupom > 0)
    # Evita confusão visual mostrando "Desconto (0%)" desnecessário
    if desconto_cupom > 0:
        print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")

    print(linha)
    print(f" TOTAL:         R$ {total:.2f}")
    print(linha)


def processar_compra() -> None:
    """
    Processa uma compra completa coletando dados e exibindo o recibo.
    
    Fluxo principal que:
    1. Coleta o nome do cliente
    2. Coleta quantidade e preço de 3 itens
    3. Calcula os totais dos itens
    4. Coleta desconto (se houver)
    5. Calcula imposto (10%)
    6. Calcula total final
    7. Exibe o recibo formatado
    
    Retorna:
        None
        
    Exemplo:
        >>> processar_compra()
        Qual é seu nome? João
        Quantidade do item 1: 2
        ...
    """
    # FASE 1: COLETA DE DADOS
    # Orquestração de funções especializadas seguindo padrão Orchestrator Pattern
    cliente = coletar_nome_cliente()
    qtd1, item1, qtd2, item2, qtd3, item3 = coletar_itens()
    
    # FASE 2: CÁLCULOS DE TOTAIS
    # Separado da coleta para permitir reutilização em contextos sem entrada de usuário
    total_item1, total_item2, total_item3, subtotal = calcular_totais_itens(
        qtd1, item1, qtd2, item2, qtd3, item3
    )
    
    # FASE 3: CÁLCULO DE IMPOSTO
    # Fixo em 10% - centralizar aqui facilita futura mudança de taxa
    imposto = subtotal * 0.10
    
    # FASE 4: DESCONTO (Opcional)
    # Coletado após subtotal calculado para poder usar como base
    desconto_cupom, desconto = coletar_desconto(subtotal)
    
    # FASE 5: CÁLCULO FINAL
    # Ordem matemática importante: (subtotal + imposto) - desconto
    # Garante que desconto não reduz imposto (conforme política comercial)
    total = calcular_total_final(subtotal, imposto, desconto)
    
    # FASE 6: APRESENTAÇÃO
    # Separar exibição do cálculo permite testar lógica sem I/O
    exibir_recibo(
        cliente, total_item1, total_item2, total_item3,
        subtotal, imposto, desconto_cupom, desconto, total
    )


# Ponto de entrada do programa
# Padrão Python: permite importar como módulo sem executar automaticamente
if __name__ == "__main__":
    processar_compra()
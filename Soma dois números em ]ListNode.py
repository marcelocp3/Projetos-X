class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        dummy_head = ListNode(0)  # Nó fictício para iniciar a lista de resposta
        current = dummy_head
        
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Soma os valores e o carry
            soma = val1 + val2 + carry
            carry = soma // 10  # Atualiza o carry para a próxima iteração
            
            # Cria um novo nó com o valor da soma % 10
            current.next = ListNode(soma % 10)
            current = current.next
            
            # Avança para o próximo nó em l1 e l2
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return dummy_head.next  # Retorna a cabeça da nova lista


# O mesmo que o arquivo soma dois números, porém usando o método ListNode para criar a lista encadeada


# Exemplo de uso
# Criando as listas encadeadas l1 e l2
# l1 = ListNode(2, ListNode(4, ListNode(3)))  # 342
# l2 = ListNode(5, ListNode(6, ListNode(4)))  # 465

# sol = Solution()
# res = sol.addTwoNumbers(l1, l2)

# # Convertendo o resultado para uma lista para facilitar a visualização
# resultado = []
# while res:
#     resultado.append(res.val)
#     res = res.next

# print(resultado)  # Saída: [7, 0, 8] que representa 807 (342 + 465)


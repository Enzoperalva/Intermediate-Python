marketing = ["ana@email.com", "caio@email.com", "beatriz@email.com"]
vendas = ["caio@email.com", "rodrigo@email.com", "ana@email.com"]
suporte = ["beatriz@email.com", "marcos@email.com", "marcos@email.com"]

#Transformando eles em set
marketing = set(marketing)
vendas = set(vendas)
suporte = set(suporte)
#Fidelidade
emails_3_listas = marketing & vendas & suporte
emails_3_listas = ", ".join(emails_3_listas)
if not emails_3_listas:
    print('Não há e-mails nas 3 listas ao mesmo tempo')
else:
    print(f'O {emails_3_listas} está presente nas 3 listas!')

#Unificaca
todos_contatos = marketing | vendas | suporte
print(todos_contatos)

#Exclusividade Suporte
diferenca_sup1 = suporte - vendas - marketing
print(f'Os e-mails {diferenca_sup1} só estão na lista de suporte')

#Segurança
lista_cheia = marketing, vendas, suporte

for i in lista_cheia:
    i.discard('marcos@email.com')
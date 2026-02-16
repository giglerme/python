cid = input('Digite o nome de uma cidade: ')
cid= cid.lower()
cid = cid.replace('ã', 'a')
if cid.find('sao') == 0 or cid.find('santo') == 0 :
    print('Essa cidade começa com nome de santo.')
else:
    print('Essa cidade não começa com nome de santo.')
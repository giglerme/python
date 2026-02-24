cid = str(input('Digite o nome da cidade: ')).strip().lower()
print((cid[:5] == 'santo') or (cid[:3] == 'sao') or
      (cid[:5] == 'saint') or (cid[:3] == 'san') or
      (cid[:2] == 'st'))
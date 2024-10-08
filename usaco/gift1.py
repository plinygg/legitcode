"""
ID: your_id_here
LANG: PYTHON3
TASK: gift1
"""

fin = open('gift1.in','r')
np = int(fin.readline().strip())
dictOfMoney = { fin.readline().strip() : 0 for i in range(np) }

while(True):
	giver = fin.readline().strip()
	if(giver==""):
		break
	amount, divided = map(int, fin.readline().strip().split())
	receivers = [fin.readline().strip() for i in range(divided)]

	try:
		quotient, remainder = divmod(amount,divided)
	except:
		quotient = remainder = 0

	for receiver in receivers:
		dictOfMoney[receiver] += quotient
	dictOfMoney[giver] += -amount + remainder

with open('gift1.out','w') as fout:
	for name, money in dictOfMoney.items():
		fout.write(f"{name} {money}\n")
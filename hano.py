#汉诺塔程序

def move(from,to):
	print(from,'->',to)
def hanoi(n,src,tmp,dst):
	if n==1:
		move(src,dst)
	else:
		hano(n-1,src,dst,tmp)
		move(src,dst)
		hano(n-1,tmp,src,dst)
		

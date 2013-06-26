from celery import task

@task()
def add(x, y):
	print('Executing task id %r, args: %r kwargs: %r' % (add.request.id, add.request.args, add.request.kwargs))
	return x + y

@task()
def tsum(numbers):
	return sum(numbers)

@task()
def multiply(x,y):
	hasil = x*y
	return 'hsilnya adalah %d' % (hasil,)

def decorator_factory(args=None):
	def decorator(function):
		print(id(args),1)
		print(args)
		if args:
			def wrapper(args):
				print(id(args),2)
				print(args)
				result = function(args) +  args
				return result
			return wrapper
		print(777)
	return decorator

@decorator_factory(8)
def mais(args):
	print(args)
	return args
while True:
	print(mais(int(input('num: '))))
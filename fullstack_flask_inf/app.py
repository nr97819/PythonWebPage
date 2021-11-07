def index_creator(ch):
    def func(str):
        print('<{0}>{1}<{0}>'.format(ch, str))
    return func

list_data = 'SangWoo, Cho'

func1 = index_creator('h5')
print(func1)
func1(list_data)


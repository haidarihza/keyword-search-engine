import rabinkarp as rk
import readtext as rt
import timeit

start = timeit.default_timer()
#daftar list
simbol = [".", ",", "(", ")", "\"", "\'"]
ununique = ["dan", "itu", "ini", "karena", "oleh", "serta", "", "dia", "ia", "kamu", "mereka", "kita", "maupun", "bisa", "untuk",
            "dalam", "saya", "supaya", "pada", "kepada", "masih", "di", "ada", "yang", "bahwa", "dengan", "dalam", "lebih", "menurut",
            "menurutnya","dapat", "akan", "ke", "para", "bagi"]
list_kata = []

# A simple implementation of Priority Queue
# using Queue.
class PriorityQueue(object):
	def __init__(self):
		self.queue = []

	def __str__(self):
		return ' '.join([str(i) for i in self.queue])

	# for checking if the queue is empty
	def isEmpty(self):
		return len(self.queue) == 0

	# for inserting an element in the queue
	def insert(self, data):
		self.queue.append(data)

	# for popping an element based on Priority
	def delete(self):
		try:
			max = 0
			for i in range(len(self.queue)):
				if self.queue[i][1] > self.queue[max][1] :
					max = i
			item = self.queue[max]
			del self.queue[max]
			return item
		except IndexError:
			print()
			exit()

idx  = 0

def getkata(text, n) :
    global idx
    word = ""
    while ((idx < n) and (text[idx] != " ")) :
        if (text[idx] not in simbol) :
            word += text[idx]
        idx += 1
    idx += 1
    return word

if __name__ == '__main__':
    myQueue = PriorityQueue()
    text = rt.readtext()
    text = text.lower()
    n = len(text)
    print("Panjang string teks: ",n)
    prev_kata = ""
    while (idx < n) :
        kata = getkata(text, n)
        if ((kata not in ununique) and (kata not in list_kata)) :
            list_kata.append(kata)
            cnt = rk.search(kata, text)
            myQueue.insert((kata,cnt))
        if (kata not in ununique) and (prev_kata not in ununique) :
            frasa = prev_kata + " " + kata
            if frasa not in list_kata :
                list_kata.append(frasa)
                cnt = rk.search(frasa,text)
                myQueue.insert((frasa,cnt))
        prev_kata = kata
    print("Banyak kata: ", len(list_kata))
    for i in range (10) :
        print(myQueue.delete())

# All the program statements
stop = timeit.default_timer()
execution_time = stop - start

print("Program Executed in "+str(execution_time)) # It returns time in seconds
from random import randint
import pyperclip

def lister():
	user_input = None

	acceptables = ['1','2','3']

	while user_input not in acceptables:


		print("1.Copy to clipboard")
		print("2.Copy from clipboard")
		print("3.View Clipboard")

		user_input = input("Choose your choice: ")

	return user_input


def retreiver():
	file = open("clipboard.txt","r")
	user_choice = input("Which text you need to retreive , type the id number: ")
	for i in file:
		id_number = i.split(" ")[0]
		output_text = i[6:]
		output_text.join("") 
		if user_choice == id_number:
			pyperclip.copy(output_text)


def viewer():
	file = open("clipboard.txt" , "r")
	print("==================================")
	for i in file:
		print(i)
	print("==================================")


def id_randimizer():
	random_id = randint(100,500)
	return random_id


def writer(id):
	file = open("clipboard.txt","a")
	text = input("type the text u need to copy to clipboard: ")

	file.write(str(id)+" - "+text+"\n")




def main():

	while True:


		print("Welcome to PyCLip")
		user_choice = lister()

		if user_choice == "1":
			random_id = id_randimizer()
			writer(random_id)

		elif user_choice == "2":
			viewer()
			retreiver()

		elif user_choice == "3":
			viewer()

		print("\n")


if __name__ == "__main__":
	main()
#takes user inputed number values and converts them from one temperature scale to another
import tkinter
window = tkinter.Tk()
num = 0
def farentocels(finput):
	finput = int(ent.get())
	cresult = (finput - 32) * 5 // 9
	result.configure(text = str(finput) + " degrees Farenheit is " + str(cresult) + " degrees Celsius.")

def celstofaren(cinput):
	cinput = int(ent.get())
	fresult = cinput * 9 // 5 + 32
	result.configure(text =str(cinput) + " degrees Celsius is " + str(fresult) + " degrees Farenheit.")

window.geometry("400x400")
window.title("Temperature Converter")
window.wm_iconbitmap('C:\\Users\\Illuminati President\\Documents\\PythonS\\logo.ico')
ent = tkinter.Entry(window)
lbl = tkinter.Label(window, text="Type a temperature value you want to see converted to the alternate scale")
ftcbtn = tkinter.Button(window, text = "Convert to Celsius", command = lambda: farentocels(num))
ctfbtn = tkinter.Button(window, text = "Convert to Farenheit", command = lambda: celstofaren(num))
result = tkinter.Label(window, text = "")
lbl.pack()
ent.pack()
ftcbtn.pack()
ctfbtn.pack()
result.pack()
window.mainloop()
main()

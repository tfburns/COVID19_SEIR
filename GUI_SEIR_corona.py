#!/usr/bin/env python

# This is for python3 (function names associated with tkinter are different between python2 and python3)
from tkinter import *
import tkinter as tk
import tkinter.messagebox
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.backend_bases import key_press_handler
import matplotlib.pyplot as plt

def covid19SEIR(N,r,i,l,time,E0=0,I0=1,R0=0):
	# COVID19 version, in which people in lateycy period are infectious
	# initial state
	E = E0; I = I0; R = R0; S = N - (E + I + R)

	data = {'S':[S],'E':[E],'I':[I],'R':[R]}
	for t in range(time):
		h = 0.1 # h is the increment in Euler's method
		for j in range(int(1/h)):
			infectious = I + E # this is equal to I in the original model. but for COVID19, we assume I + E that asymptomatic people are also infectious
			S += h* (-(r/i)*(S/N)*infectious)
			E += h* ((r/i)*(S/N)*infectious - (1/l)*E)
			I += h* ((1/l)*E - (1/i)*I)
			R += h* (1/i)*I
		data['S'].append(S)
		data['E'].append(E)
		data['I'].append(I)
		data['R'].append(R)
	return data

def oriSEIR(N,r,i,l,time,E0=0,I0=1,R0=0):
	# Original version of SEIR, in which people in lateycy period are NOT infectious
	# initial state
	E = E0; I = I0; R = R0; S = N - (E + I + R)

	data = {'S':[S],'E':[E],'I':[I],'R':[R]}
	for t in range(time):
		h = 0.1 # h is the increment in Euler's method
		for j in range(int(1/h)):
			infectious = I # original SEIR model
			S += h* (-(r/i)*(S/N)*infectious)
			E += h* ((r/i)*(S/N)*infectious - (1/l)*E)
			I += h* ((1/l)*E - (1/i)*I)
			R += h* (1/i)*I
		data['S'].append(S)
		data['E'].append(E)
		data['I'].append(I)
		data['R'].append(R)
	return data

def Plot(ax,data,param):
        x = range(len(data['S']))
        ax.plot(x,data['I'],marker='.',linestyle='none',label=param)
        ax.set_xlabel('days')
        ax.set_ylabel('The number of people in the infected state each day')

top = tk.Tk()


L1 = Label(top, text="Parameters",).grid(row=0,column=1)
L2 = Label(top, text="Total population size",).grid(row=1,column=0)
L3 = Label(top, text="Average symptomatic period (days)",).grid(row=3,column=0)
L4 = Label(top, text="Average latency (asymptomatic) period (days)",).grid(row=2,column=0)
L5 = Label(top, text="Timesteps to simulate for (days)",).grid(row=4,column=0)
L6 = Label(top, text="Basic reproduction number",).grid(row=5,column=0)
#L7 = Label(top, text="Set y-axis as log scale").grid(row=7,column=0)
L8 = Label(top, text="Is latency period infectious?").grid(row=6,column=0)
E1 = Entry(top, bd =5)
E1.grid(row=1,column=1)
E1.insert(END,"100000")
E2 = Entry(top, bd =5)
E2.grid(row=3,column=1)
E2.insert(END,"10") # default average symptomatic period for coronavirus
E3 = Entry(top, bd =5)
E3.grid(row=2,column=1)
E3.insert(END,"5") # default average latency period
E4 = Entry(top, bd =5)
E4.grid(row=4,column=1)
E4.insert(END,"400") # default calculation timesteps
E5 = Entry(top, bd =5)
E5.grid(row=5, column=1)
E5.insert(END,"2.5,1") # default basic reproduction rate
var = IntVar()
C1 = Radiobutton(top, text="Yes (likely for COVID-19)", variable=var, value=1)
C1.grid(row=6,column=1)
C2 = Radiobutton(top, text="No (original SEIR model)", variable=var, value=2)
var.set(1) # give a default value on load-up so I can click "calculate" right away!
C2.grid(row=6,column=2)
vscale = IntVar()
C3 = Checkbutton(top, text="Set y-axis as log scale", variable=vscale, onvalue=1, offvalue=0)
C3.grid(row=7,column=1)

def _quit():
	top.destroy()
	top.quit()

def process():
	N = float(Entry.get(E1)) # total population size
	i = float(Entry.get(E2)) # average symptomatic period
	l = float(Entry.get(E3)) # average latency period
	time = int(Entry.get(E4))
	rn = Entry.get(E5) # basic reproduction number
	if ',' in rn:
		r_ls = map(float,rn.split(','))
	else:
		r_ls = [float(rn)]
	fig = plt.figure(figsize=(6,5))
	#if (var1.get() == 1) & (var2.get() == 0):
	if var.get() == 1:
		ax = fig.add_subplot(111)
		for r in r_ls:
			results = covid19SEIR(N,r,i,l,time)
			Plot(ax,results,r)
		ax.legend(title="basic reproduction number")
		if vscale.get() == 1:
			ax.set_yscale('log')
	#elif (var1.get() == 0) & (var2.get() == 1):
	elif var.get() == 2:
		ax = fig.add_subplot(111)
		for r in r_ls:
			results = oriSEIR(N,r,i,l,time)
			Plot(ax,results,r)
		ax.legend(title="basic reproduction number")
		if vscale.get() == 1:
			ax.set_yscale('log')
	#elif (var1.get() == 1) & (var2.get() == 1):
	#	ax1 = fig.add_subplot(1,2,1)
	#	for r in r_ls:
	#		results = covid19SEIR(N,r,i,l,time)
	#		Plot(ax1,results,r)
	#	ax1.set_title("Infectious latency period")
	#	ax2 = fig.add_subplot(1,2,2)
	#	for r in r_ls:
	#		results = oriSEIR(N,r,i,l,time)
	#		Plot(ax2,results,r)
	#	ax2.set_title("NonInfectious latency period")
	#	ax2.legend(title="basic reproduction number")
	else:
		return
	plt.suptitle("Press q to quit, c to close figure")
	output = FigureCanvasTkAgg(fig, master=top)
	output.draw()

	def on_key_press(event):
		if event.key == 'q':
			_quit()
		if event.key == 'c':
			output.get_tk_widget().destroy()
		key_press_handler(event,output)

	output.mpl_connect("key_press_event", on_key_press)
	#output.get_tk_widget().pack(side=tk.LEFT,fill=tk.BOTH) # can't use fill and grid in the same master window!
	output.get_tk_widget().grid(row=9,column=1)

B1 = Button(top, text="Calculate",command=process).grid(row=8,column=1,)
B2 = Button(top, text="Quit",command=_quit).grid(row=8,column=2) # for quality of life :)

tk.mainloop()

from math import exp

from math import tanh

class ../NN/MLP_Zbb_tt_EE:
	def value(self,index,in0,in1,in2,in3):
		self.input0 = (in0 - 20.9125)/1.08293
		self.input1 = (in1 - 21.6321)/1.05575
		self.input2 = (in2 - 21.6884)/0.800382
		self.input3 = (in3 - 65.8143)/37.6943
		if index==0: return self.neuron0x5361c30();
		return 0.
	def neuron0x535fa70(self):
		return self.input0
	def neuron0x535fd80(self):
		return self.input1
	def neuron0x5360090(self):
		return self.input2
	def neuron0x53603a0(self):
		return self.input3
	def neuron0x5360820(self):
		input = 3.49937
		input = input + self.synapse0x53089c0()
		input = input + self.synapse0x5360aa0()
		input = input + self.synapse0x5360ae0()
		input = input + self.synapse0x5360b20()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x5360b60(self):
		input = -2.31755
		input = input + self.synapse0x5360e70()
		input = input + self.synapse0x5360eb0()
		input = input + self.synapse0x5360ef0()
		input = input + self.synapse0x5360f30()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x5360f70(self):
		input = -0.403654
		input = input + self.synapse0x5361280()
		input = input + self.synapse0x53612c0()
		input = input + self.synapse0x5361300()
		input = input + self.synapse0x5361340()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x5361380(self):
		input = 0.254478
		input = input + self.synapse0x5361690()
		input = input + self.synapse0x53616d0()
		input = input + self.synapse0x5361710()
		input = input + self.synapse0x5361750()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x5361790(self):
		input = -0.165301
		input = input + self.synapse0x5361aa0()
		input = input + self.synapse0x4d6d220()
		input = input + self.synapse0x4d6d260()
		input = input + self.synapse0x5361bf0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x5361c30(self):
		input = 2.15354
		input = input + self.synapse0x5361f40()
		input = input + self.synapse0x5361f80()
		input = input + self.synapse0x5361fc0()
		input = input + self.synapse0x5362000()
		input = input + self.synapse0x5362040()
		return (input*1)+0
	def synapse0x53089c0(self):
		return (self.neuron0x535fa70()*0.968667)
	def synapse0x5360aa0(self):
		return (self.neuron0x535fd80()*0.585526)
	def synapse0x5360ae0(self):
		return (self.neuron0x5360090()*-1.19738)
	def synapse0x5360b20(self):
		return (self.neuron0x53603a0()*3.00339)
	def synapse0x5360e70(self):
		return (self.neuron0x535fa70()*-0.50648)
	def synapse0x5360eb0(self):
		return (self.neuron0x535fd80()*-0.917869)
	def synapse0x5360ef0(self):
		return (self.neuron0x5360090()*1.12753)
	def synapse0x5360f30(self):
		return (self.neuron0x53603a0()*-2.68942)
	def synapse0x5361280(self):
		return (self.neuron0x535fa70()*-0.793497)
	def synapse0x53612c0(self):
		return (self.neuron0x535fd80()*-0.114063)
	def synapse0x5361300(self):
		return (self.neuron0x5360090()*0.170865)
	def synapse0x5361340(self):
		return (self.neuron0x53603a0()*0.296807)
	def synapse0x5361690(self):
		return (self.neuron0x535fa70()*-0.010018)
	def synapse0x53616d0(self):
		return (self.neuron0x535fd80()*0.0670894)
	def synapse0x5361710(self):
		return (self.neuron0x5360090()*0.0886149)
	def synapse0x5361750(self):
		return (self.neuron0x53603a0()*-0.109301)
	def synapse0x5361aa0(self):
		return (self.neuron0x535fa70()*-0.76846)
	def synapse0x4d6d220(self):
		return (self.neuron0x535fd80()*-0.118074)
	def synapse0x4d6d260(self):
		return (self.neuron0x5360090()*-0.651483)
	def synapse0x5361bf0(self):
		return (self.neuron0x53603a0()*0.160447)
	def synapse0x5361f40(self):
		return (self.neuron0x5360820()*-1.24147)
	def synapse0x5361f80(self):
		return (self.neuron0x5360b60()*-0.110809)
	def synapse0x5361fc0(self):
		return (self.neuron0x5360f70()*-0.0577178)
	def synapse0x5362000(self):
		return (self.neuron0x5361380()*-1.48454)
	def synapse0x5362040(self):
		return (self.neuron0x5361790()*-0.181895)

from math import exp

from math import tanh

class FinalV5/MLP_DY_vs_TT_ZH125_comb_2_4_1000_Ptb1j40_Ptb2j25_Ptll20:
	def value(self,index,in0,in1,in2):
		self.input0 = (in0 - 20.0771)/1.45611
		self.input1 = (in1 - 20.9022)/1.93203
		self.input2 = (in2 - 22.264)/3.23887
		if index==0: return self.neuron0x174e4f50();
		return 0.
	def neuron0x17488210(self):
		return self.input0
	def neuron0x174e31f0(self):
		return self.input1
	def neuron0x174e3530(self):
		return self.input2
	def neuron0x174e39a0(self):
		input = 0.443761
		input = input + self.synapse0x1747a120()
		input = input + self.synapse0x17488120()
		input = input + self.synapse0x174884c0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x174e3c50(self):
		input = -0.743688
		input = input + self.synapse0x174e3f90()
		input = input + self.synapse0x174e3fd0()
		input = input + self.synapse0x174e4010()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x174e4050(self):
		input = 0.151966
		input = input + self.synapse0x174e4390()
		input = input + self.synapse0x174e43d0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x174e4410(self):
		input = -0.956538
		input = input + self.synapse0x174e4750()
		input = input + self.synapse0x174e4790()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x174e47d0(self):
		input = 6.18471
		input = input + self.synapse0x174e4b10()
		input = input + self.synapse0x174e4b50()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x174e4b90(self):
		input = -1.77205
		input = input + self.synapse0x174e4ed0()
		input = input + self.synapse0x174e4f10()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x174e4f50(self):
		input = -3.07214
		input = input + self.synapse0x174e3870()
		input = input + self.synapse0x174e5290()
		input = input + self.synapse0x174e52d0()
		input = input + self.synapse0x17478310()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def synapse0x1747a120(self):
		return (self.neuron0x17488210()*-0.401226)
	def synapse0x17488120(self):
		return (self.neuron0x174e31f0()*-0.32369)
	def synapse0x174884c0(self):
		return (self.neuron0x174e3530()*0.180795)
	def synapse0x174e3f90(self):
		return (self.neuron0x17488210()*-0.0260718)
	def synapse0x174e3fd0(self):
		return (self.neuron0x174e31f0()*-0.244625)
	def synapse0x174e4010(self):
		return (self.neuron0x174e3530()*2.73986)
	def synapse0x174e4390(self):
		return (self.neuron0x174e39a0()*1.92033)
	def synapse0x174e43d0(self):
		return (self.neuron0x174e3c50()*2.33217)
	def synapse0x174e4750(self):
		return (self.neuron0x174e39a0()*3.6486)
	def synapse0x174e4790(self):
		return (self.neuron0x174e3c50()*3.41052)
	def synapse0x174e4b10(self):
		return (self.neuron0x174e39a0()*-7.975)
	def synapse0x174e4b50(self):
		return (self.neuron0x174e3c50()*-4.67028)
	def synapse0x174e4ed0(self):
		return (self.neuron0x174e39a0()*4.69354)
	def synapse0x174e4f10(self):
		return (self.neuron0x174e3c50()*3.87672)
	def synapse0x174e3870(self):
		return (self.neuron0x174e4050()*0.373968)
	def synapse0x174e5290(self):
		return (self.neuron0x174e4410()*2.85367)
	def synapse0x174e52d0(self):
		return (self.neuron0x174e47d0()*-6.58874)
	def synapse0x17478310(self):
		return (self.neuron0x174e4b90()*3.96429)

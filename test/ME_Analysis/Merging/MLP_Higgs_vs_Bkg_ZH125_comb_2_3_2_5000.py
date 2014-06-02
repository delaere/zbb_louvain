from math import exp

from math import tanh

class MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_5000:
	def value(self,index,in0,in1,in2):
		self.input0 = (in0 - 0.445235)/0.307413
		self.input1 = (in1 - 0.487302)/0.29068
		self.input2 = (in2 - 0.530975)/0.330691
		if index==0: return self.neuron0xc2487d0();
		return 0.
	def neuron0xc235630(self):
		return self.input0
	def neuron0xc235970(self):
		return self.input1
	def neuron0xc246940(self):
		return self.input2
	def neuron0xc246c90(self):
		input = -3.00789
		input = input + self.synapse0xc21c020()
		input = input + self.synapse0xc246f40()
		input = input + self.synapse0xc246f80()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0xc246fc0(self):
		input = 3.15243
		input = input + self.synapse0xc247300()
		input = input + self.synapse0xc247340()
		input = input + self.synapse0xc247380()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0xc2473c0(self):
		input = -1.82836
		input = input + self.synapse0xc247700()
		input = input + self.synapse0xc247740()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0xc247780(self):
		input = -0.453903
		input = input + self.synapse0xc247ac0()
		input = input + self.synapse0xc247b00()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0xc247b40(self):
		input = 7.47677
		input = input + self.synapse0xc247e80()
		input = input + self.synapse0xc247ec0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0xc247f00(self):
		input = -3.97876
		input = input + self.synapse0xc248240()
		input = input + self.synapse0xc248280()
		input = input + self.synapse0xc2482c0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0xc248300(self):
		input = 6.39321
		input = input + self.synapse0xc248640()
		input = input + self.synapse0xc248680()
		input = input + self.synapse0xc1a7df0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0xc2487d0(self):
		input = 3.98922
		input = input + self.synapse0xc2489f0()
		input = input + self.synapse0xc248a30()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def synapse0xc21c020(self):
		return (self.neuron0xc235630()*0.529408)
	def synapse0xc246f40(self):
		return (self.neuron0xc235970()*0.284559)
	def synapse0xc246f80(self):
		return (self.neuron0xc246940()*0.633835)
	def synapse0xc247300(self):
		return (self.neuron0xc235630()*2.81423)
	def synapse0xc247340(self):
		return (self.neuron0xc235970()*0.565852)
	def synapse0xc247380(self):
		return (self.neuron0xc246940()*1.30298)
	def synapse0xc247700(self):
		return (self.neuron0xc246c90()*-2.0992)
	def synapse0xc247740(self):
		return (self.neuron0xc246fc0()*-3.69901)
	def synapse0xc247ac0(self):
		return (self.neuron0xc246c90()*-3.15759)
	def synapse0xc247b00(self):
		return (self.neuron0xc246fc0()*-9.53144)
	def synapse0xc247e80(self):
		return (self.neuron0xc246c90()*-10.4858)
	def synapse0xc247ec0(self):
		return (self.neuron0xc246fc0()*-4.64298)
	def synapse0xc248240(self):
		return (self.neuron0xc2473c0()*1.92283)
	def synapse0xc248280(self):
		return (self.neuron0xc247780()*3.23264)
	def synapse0xc2482c0(self):
		return (self.neuron0xc247b40()*14.8926)
	def synapse0xc248640(self):
		return (self.neuron0xc2473c0()*0.451754)
	def synapse0xc248680(self):
		return (self.neuron0xc247780()*-2.9629)
	def synapse0xc1a7df0(self):
		return (self.neuron0xc247b40()*-5.85746)
	def synapse0xc2489f0(self):
		return (self.neuron0xc247f00()*-11.8163)
	def synapse0xc248a30(self):
		return (self.neuron0xc248300()*10.2919)

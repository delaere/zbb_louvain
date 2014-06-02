from math import exp

from math import tanh

class MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_10000:
	def value(self,index,in0,in1,in2):
		self.input0 = (in0 - 0.445235)/0.307413
		self.input1 = (in1 - 0.487302)/0.29068
		self.input2 = (in2 - 0.530975)/0.330691
		if index==0: return self.neuron0x17eb9750();
		return 0.
	def neuron0x17ea65f0(self):
		return self.input0
	def neuron0x17ea6930(self):
		return self.input1
	def neuron0x17eb7900(self):
		return self.input2
	def neuron0x17eb7c50(self):
		input = -0.15607
		input = input + self.synapse0x17e6edc0()
		input = input + self.synapse0x17e8d350()
		input = input + self.synapse0x17eb7f00()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x17eb7f40(self):
		input = 1.1345
		input = input + self.synapse0x17eb8280()
		input = input + self.synapse0x17eb82c0()
		input = input + self.synapse0x17eb8300()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x17eb8340(self):
		input = 9.07702
		input = input + self.synapse0x17eb8680()
		input = input + self.synapse0x17eb86c0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x17eb8700(self):
		input = 3.29866
		input = input + self.synapse0x17eb8a40()
		input = input + self.synapse0x17eb8a80()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x17eb8ac0(self):
		input = -6.35498
		input = input + self.synapse0x17eb8e00()
		input = input + self.synapse0x17eb8e40()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x17eb8e80(self):
		input = 6.73508
		input = input + self.synapse0x17eb91c0()
		input = input + self.synapse0x17eb9200()
		input = input + self.synapse0x17eb9240()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x17eb9280(self):
		input = 8.61803
		input = input + self.synapse0x17eb95c0()
		input = input + self.synapse0x17eb9600()
		input = input + self.synapse0x17e19560()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x17eb9750(self):
		input = 12.5818
		input = input + self.synapse0x17eb9970()
		input = input + self.synapse0x17eb99b0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def synapse0x17e6edc0(self):
		return (self.neuron0x17ea65f0()*0.427614)
	def synapse0x17e8d350(self):
		return (self.neuron0x17ea6930()*0.223767)
	def synapse0x17eb7f00(self):
		return (self.neuron0x17eb7900()*0.0361055)
	def synapse0x17eb8280(self):
		return (self.neuron0x17ea65f0()*-2.69032)
	def synapse0x17eb82c0(self):
		return (self.neuron0x17ea6930()*2.83829)
	def synapse0x17eb8300(self):
		return (self.neuron0x17eb7900()*-0.629683)
	def synapse0x17eb8680(self):
		return (self.neuron0x17eb7c50()*-10.2648)
	def synapse0x17eb86c0(self):
		return (self.neuron0x17eb7f40()*-4.9344)
	def synapse0x17eb8a40(self):
		return (self.neuron0x17eb7c50()*-2.91887)
	def synapse0x17eb8a80(self):
		return (self.neuron0x17eb7f40()*-3.79877)
	def synapse0x17eb8e00(self):
		return (self.neuron0x17eb7c50()*14.825)
	def synapse0x17eb8e40(self):
		return (self.neuron0x17eb7f40()*4.12621)
	def synapse0x17eb91c0(self):
		return (self.neuron0x17eb8340()*5.98097)
	def synapse0x17eb9200(self):
		return (self.neuron0x17eb8700()*-7.19742)
	def synapse0x17eb9240(self):
		return (self.neuron0x17eb8ac0()*-5.29588)
	def synapse0x17eb95c0(self):
		return (self.neuron0x17eb8340()*0.715516)
	def synapse0x17eb9600(self):
		return (self.neuron0x17eb8700()*-10.2471)
	def synapse0x17e19560(self):
		return (self.neuron0x17eb8ac0()*-9.49324)
	def synapse0x17eb9970(self):
		return (self.neuron0x17eb8e80()*-12.6019)
	def synapse0x17eb99b0(self):
		return (self.neuron0x17eb9280()*-14.8207)

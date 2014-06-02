from math import exp

from math import tanh

class FinalV4/MLP_Higgs_vs_Bkg_3j_ZH125_comb_5_600_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_1:
	def value(self,index,in0,in1,in2):
		self.input0 = (in0 - 0.467176)/0.243159
		self.input1 = (in1 - 0.52708)/0.296356
		self.input2 = (in2 - 0.534793)/0.314261
		if index==0: return self.neuron0x2d8835c0();
		return 0.
	def neuron0x2d8817a0(self):
		return self.input0
	def neuron0x2d881ae0(self):
		return self.input1
	def neuron0x2d881e20(self):
		return self.input2
	def neuron0x2d882290(self):
		input = -7.90421
		input = input + self.synapse0x2d826930()
		input = input + self.synapse0x2d882540()
		input = input + self.synapse0x2d882580()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x2d8825c0(self):
		input = 2.18231
		input = input + self.synapse0x2d882900()
		input = input + self.synapse0x2d882940()
		input = input + self.synapse0x2d882980()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x2d8829c0(self):
		input = 1.70494
		input = input + self.synapse0x2d882d00()
		input = input + self.synapse0x2d882d40()
		input = input + self.synapse0x2d882d80()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x2d882dc0(self):
		input = 1.9539
		input = input + self.synapse0x2d883100()
		input = input + self.synapse0x2d883140()
		input = input + self.synapse0x2d883180()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x2d8831c0(self):
		input = -6.40271
		input = input + self.synapse0x2d883500()
		input = input + self.synapse0x2d883540()
		input = input + self.synapse0x2d883580()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x2d8835c0(self):
		input = -4.20094
		input = input + self.synapse0x2d883900()
		input = input + self.synapse0x2d883940()
		input = input + self.synapse0x2d816b40()
		input = input + self.synapse0x2d816b80()
		input = input + self.synapse0x2d826a40()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def synapse0x2d826930(self):
		return (self.neuron0x2d8817a0()*-1.81316)
	def synapse0x2d882540(self):
		return (self.neuron0x2d881ae0()*-2.79159)
	def synapse0x2d882580(self):
		return (self.neuron0x2d881e20()*0.382289)
	def synapse0x2d882900(self):
		return (self.neuron0x2d8817a0()*0.771404)
	def synapse0x2d882940(self):
		return (self.neuron0x2d881ae0()*-0.770748)
	def synapse0x2d882980(self):
		return (self.neuron0x2d881e20()*1.41563)
	def synapse0x2d882d00(self):
		return (self.neuron0x2d8817a0()*0.882241)
	def synapse0x2d882d40(self):
		return (self.neuron0x2d881ae0()*0.774728)
	def synapse0x2d882d80(self):
		return (self.neuron0x2d881e20()*-1.18669)
	def synapse0x2d883100(self):
		return (self.neuron0x2d8817a0()*-0.110115)
	def synapse0x2d883140(self):
		return (self.neuron0x2d881ae0()*2.03634)
	def synapse0x2d883180(self):
		return (self.neuron0x2d881e20()*-2.21034)
	def synapse0x2d883500(self):
		return (self.neuron0x2d8817a0()*1.57379)
	def synapse0x2d883540(self):
		return (self.neuron0x2d881ae0()*1.84907)
	def synapse0x2d883580(self):
		return (self.neuron0x2d881e20()*0.222873)
	def synapse0x2d883900(self):
		return (self.neuron0x2d882290()*-5.57171)
	def synapse0x2d883940(self):
		return (self.neuron0x2d8825c0()*2.76523)
	def synapse0x2d816b40(self):
		return (self.neuron0x2d8829c0()*4.52041)
	def synapse0x2d816b80(self):
		return (self.neuron0x2d882dc0()*-2.25213)
	def synapse0x2d826a40(self):
		return (self.neuron0x2d8831c0()*5.49871)

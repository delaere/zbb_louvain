from math import exp

from math import tanh

class ../NN/MLP_Zbb_tt_Comb_EE_TIGHT:
	def value(self,index,in0,in1,in2):
		self.input0 = (in0 - 20.2731)/1.05371
		self.input1 = (in1 - 20.9484)/1.00144
		self.input2 = (in2 - 21.8744)/11.3556
		if index==0: return self.neuron0xc8e4630();
		return 0.
	def neuron0xc8d1160(self):
		return self.input0
	def neuron0xc8d1470(self):
		return self.input1
	def neuron0xc8e22b0(self):
		return self.input2
	def neuron0xc8e2700(self):
		input = -2.34048
		input = input + self.synapse0xc89f370()
		input = input + self.synapse0xc8b9330()
		input = input + self.synapse0xc8d0f20()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0xc8e2980(self):
		input = 0.485312
		input = input + self.synapse0xc89f400()
		input = input + self.synapse0xc8e2c90()
		input = input + self.synapse0xc8e2cd0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0xc8e2d10(self):
		input = -1.20788
		input = input + self.synapse0xc8e3020()
		input = input + self.synapse0xc8e3060()
		input = input + self.synapse0xc8e30a0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0xc8e30e0(self):
		input = -1.72698
		input = input + self.synapse0xc8e33f0()
		input = input + self.synapse0xc8e3430()
		input = input + self.synapse0xc8e3470()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0xc8e34b0(self):
		input = -5.9007
		input = input + self.synapse0xc8e37c0()
		input = input + self.synapse0xc8e3800()
		input = input + self.synapse0xc8e3840()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0xc8e3880(self):
		input = 2.84982
		input = input + self.synapse0xc8e3b90()
		input = input + self.synapse0xc8e3bd0()
		input = input + self.synapse0xc56cc40()
		input = input + self.synapse0xc56cc80()
		input = input + self.synapse0xc8e3d20()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0xc8e3d60(self):
		input = 0.452289
		input = input + self.synapse0xc8e4070()
		input = input + self.synapse0xc8e40b0()
		input = input + self.synapse0xc8e40f0()
		input = input + self.synapse0xc8e4130()
		input = input + self.synapse0xc8e4170()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0xc8e41b0(self):
		input = 2.07118
		input = input + self.synapse0xc8e44f0()
		input = input + self.synapse0xc8e4530()
		input = input + self.synapse0xc8e4570()
		input = input + self.synapse0xc8e45b0()
		input = input + self.synapse0xc8e45f0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0xc8e4630(self):
		input = 0.290166
		input = input + self.synapse0xc8e2680()
		input = input + self.synapse0xc8e26c0()
		input = input + self.synapse0xc8e48b0()
		return (input*1)+0
	def synapse0xc89f370(self):
		return (self.neuron0xc8d1160()*2.2132)
	def synapse0xc8b9330(self):
		return (self.neuron0xc8d1470()*-0.594272)
	def synapse0xc8d0f20(self):
		return (self.neuron0xc8e22b0()*5.91654)
	def synapse0xc89f400(self):
		return (self.neuron0xc8d1160()*3.17722)
	def synapse0xc8e2c90(self):
		return (self.neuron0xc8d1470()*-4.86037)
	def synapse0xc8e2cd0(self):
		return (self.neuron0xc8e22b0()*-2.42604)
	def synapse0xc8e3020(self):
		return (self.neuron0xc8d1160()*0.199142)
	def synapse0xc8e3060(self):
		return (self.neuron0xc8d1470()*1.91832)
	def synapse0xc8e30a0(self):
		return (self.neuron0xc8e22b0()*-5.4752)
	def synapse0xc8e33f0(self):
		return (self.neuron0xc8d1160()*-0.324169)
	def synapse0xc8e3430(self):
		return (self.neuron0xc8d1470()*-0.672533)
	def synapse0xc8e3470(self):
		return (self.neuron0xc8e22b0()*8.84682)
	def synapse0xc8e37c0(self):
		return (self.neuron0xc8d1160()*0.131276)
	def synapse0xc8e3800(self):
		return (self.neuron0xc8d1470()*-0.346288)
	def synapse0xc8e3840(self):
		return (self.neuron0xc8e22b0()*4.19378)
	def synapse0xc8e3b90(self):
		return (self.neuron0xc8e2700()*-0.463377)
	def synapse0xc8e3bd0(self):
		return (self.neuron0xc8e2980()*2.28165)
	def synapse0xc56cc40(self):
		return (self.neuron0xc8e2d10()*2.56746)
	def synapse0xc56cc80(self):
		return (self.neuron0xc8e30e0()*1.18974)
	def synapse0xc8e3d20(self):
		return (self.neuron0xc8e34b0()*1.86594)
	def synapse0xc8e4070(self):
		return (self.neuron0xc8e2700()*4.07625)
	def synapse0xc8e40b0(self):
		return (self.neuron0xc8e2980()*-1.75436)
	def synapse0xc8e40f0(self):
		return (self.neuron0xc8e2d10()*-5.11615)
	def synapse0xc8e4130(self):
		return (self.neuron0xc8e30e0()*7.15315)
	def synapse0xc8e4170(self):
		return (self.neuron0xc8e34b0()*-0.7233)
	def synapse0xc8e44f0(self):
		return (self.neuron0xc8e2700()*1.99833)
	def synapse0xc8e4530(self):
		return (self.neuron0xc8e2980()*-0.0611633)
	def synapse0xc8e4570(self):
		return (self.neuron0xc8e2d10()*-1.96515)
	def synapse0xc8e45b0(self):
		return (self.neuron0xc8e30e0()*1.7151)
	def synapse0xc8e45f0(self):
		return (self.neuron0xc8e34b0()*1.36399)
	def synapse0xc8e2680(self):
		return (self.neuron0xc8e3880()*0.206597)
	def synapse0xc8e26c0(self):
		return (self.neuron0xc8e3d60()*1.21384)
	def synapse0xc8e48b0(self):
		return (self.neuron0xc8e41b0()*-0.729666)

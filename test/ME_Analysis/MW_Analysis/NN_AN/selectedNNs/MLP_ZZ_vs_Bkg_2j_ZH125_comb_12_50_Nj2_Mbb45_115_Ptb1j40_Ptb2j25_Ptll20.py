from math import exp

from math import tanh

class Final13/MLP_ZZ_vs_Bkg_2j_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20:
	def value(self,index,in0,in1):
		self.input0 = (in0 - 0.491067)/0.220463
		self.input1 = (in1 - 0.606248)/0.330761
		if index==0: return self.neuron0x41374c40();
		return 0.
	def neuron0x41371820(self):
		return self.input0
	def neuron0x41371b60(self):
		return self.input1
	def neuron0x41371fd0(self):
		input = -0.144035
		input = input + self.synapse0x41372280()
		input = input + self.synapse0x413722c0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x41372300(self):
		input = 0.597115
		input = input + self.synapse0x41372640()
		input = input + self.synapse0x41372680()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x413726c0(self):
		input = -0.160709
		input = input + self.synapse0x41372a00()
		input = input + self.synapse0x41372a40()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x41372a80(self):
		input = 0.410107
		input = input + self.synapse0x41372dc0()
		input = input + self.synapse0x41372e00()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x41372e40(self):
		input = 0.0559335
		input = input + self.synapse0x41373180()
		input = input + self.synapse0x413731c0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x41373200(self):
		input = -0.436213
		input = input + self.synapse0x41373540()
		input = input + self.synapse0x41373580()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x413735c0(self):
		input = 0.805806
		input = input + self.synapse0x41373900()
		input = input + self.synapse0x41373940()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x41373980(self):
		input = 0.491489
		input = input + self.synapse0x41373cc0()
		input = input + self.synapse0x41373d00()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x41373d40(self):
		input = 0.18814
		input = input + self.synapse0x41374080()
		input = input + self.synapse0x4132f0e0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x413741d0(self):
		input = -1.00563
		input = input + self.synapse0x4132f120()
		input = input + self.synapse0x41374480()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x413744c0(self):
		input = 0.114423
		input = input + self.synapse0x41374800()
		input = input + self.synapse0x41374840()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x41374880(self):
		input = -0.667612
		input = input + self.synapse0x41374bc0()
		input = input + self.synapse0x41374c00()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x41374c40(self):
		input = -0.483024
		input = input + self.synapse0x41374f80()
		input = input + self.synapse0x41374fc0()
		input = input + self.synapse0x41375000()
		input = input + self.synapse0x41375040()
		input = input + self.synapse0x41375080()
		input = input + self.synapse0x413750c0()
		input = input + self.synapse0x41375100()
		input = input + self.synapse0x41375140()
		input = input + self.synapse0x41375180()
		input = input + self.synapse0x4131e000()
		input = input + self.synapse0x4131e0e0()
		input = input + self.synapse0x413740c0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def synapse0x41372280(self):
		return (self.neuron0x41371820()*0.0398217)
	def synapse0x413722c0(self):
		return (self.neuron0x41371b60()*-0.537504)
	def synapse0x41372640(self):
		return (self.neuron0x41371820()*0.804773)
	def synapse0x41372680(self):
		return (self.neuron0x41371b60()*-0.348322)
	def synapse0x41372a00(self):
		return (self.neuron0x41371820()*-1.71855)
	def synapse0x41372a40(self):
		return (self.neuron0x41371b60()*1.73137)
	def synapse0x41372dc0(self):
		return (self.neuron0x41371820()*0.627778)
	def synapse0x41372e00(self):
		return (self.neuron0x41371b60()*-0.375924)
	def synapse0x41373180(self):
		return (self.neuron0x41371820()*0.107145)
	def synapse0x413731c0(self):
		return (self.neuron0x41371b60()*-0.12927)
	def synapse0x41373540(self):
		return (self.neuron0x41371820()*-0.556725)
	def synapse0x41373580(self):
		return (self.neuron0x41371b60()*-0.064672)
	def synapse0x41373900(self):
		return (self.neuron0x41371820()*-0.0221106)
	def synapse0x41373940(self):
		return (self.neuron0x41371b60()*0.602384)
	def synapse0x41373cc0(self):
		return (self.neuron0x41371820()*-0.819521)
	def synapse0x41373d00(self):
		return (self.neuron0x41371b60()*0.374839)
	def synapse0x41374080(self):
		return (self.neuron0x41371820()*0.0436693)
	def synapse0x4132f0e0(self):
		return (self.neuron0x41371b60()*0.547566)
	def synapse0x4132f120(self):
		return (self.neuron0x41371820()*-0.044613)
	def synapse0x41374480(self):
		return (self.neuron0x41371b60()*-0.545472)
	def synapse0x41374800(self):
		return (self.neuron0x41371820()*0.15246)
	def synapse0x41374840(self):
		return (self.neuron0x41371b60()*-0.433231)
	def synapse0x41374bc0(self):
		return (self.neuron0x41371820()*-0.984465)
	def synapse0x41374c00(self):
		return (self.neuron0x41371b60()*0.540921)
	def synapse0x41374f80(self):
		return (self.neuron0x41371fd0()*-1.24548)
	def synapse0x41374fc0(self):
		return (self.neuron0x41372300()*1.08568)
	def synapse0x41375000(self):
		return (self.neuron0x413726c0()*-1.95304)
	def synapse0x41375040(self):
		return (self.neuron0x41372a80()*1.20831)
	def synapse0x41375080(self):
		return (self.neuron0x41372e40()*-0.198044)
	def synapse0x413750c0(self):
		return (self.neuron0x41373200()*-0.609693)
	def synapse0x41375100(self):
		return (self.neuron0x413735c0()*1.79505)
	def synapse0x41375140(self):
		return (self.neuron0x41373980()*1.65336)
	def synapse0x41375180(self):
		return (self.neuron0x41373d40()*1.01976)
	def synapse0x4131e000(self):
		return (self.neuron0x413741d0()*-2.27322)
	def synapse0x4131e0e0(self):
		return (self.neuron0x413744c0()*-1.46106)
	def synapse0x413740c0(self):
		return (self.neuron0x41374880()*-1.23503)

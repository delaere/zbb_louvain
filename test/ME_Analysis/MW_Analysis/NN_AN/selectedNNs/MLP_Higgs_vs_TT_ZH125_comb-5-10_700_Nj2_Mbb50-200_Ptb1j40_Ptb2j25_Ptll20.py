from math import exp

from math import tanh

class FinalV4/MLP_Higgs_vs_TT_ZH125_comb-5-10_700_Nj2_Mbb50-200_Ptb1j40_Ptb2j25_Ptll20:
	def value(self,index,in0,in1,in2):
		self.input0 = (in0 - 22.2852)/3.17236
		self.input1 = (in1 - 24.6937)/1.64914
		self.input2 = (in2 - 13.2477)/2.49485
		if index==0: return self.neuron0x1feb9470();
		return 0.
	def neuron0x1feb6480(self):
		return self.input0
	def neuron0x1feb67c0(self):
		return self.input1
	def neuron0x1feb6b00(self):
		return self.input2
	def neuron0x1feb6f70(self):
		input = 1.05308
		input = input + self.synapse0x1c315ca0()
		input = input + self.synapse0x1feb7220()
		input = input + self.synapse0x1feb7260()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x1feb72a0(self):
		input = 2.30227
		input = input + self.synapse0x1feb75e0()
		input = input + self.synapse0x1feb7620()
		input = input + self.synapse0x1feb7660()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x1feb76a0(self):
		input = 0.560261
		input = input + self.synapse0x1feb79e0()
		input = input + self.synapse0x1feb7a20()
		input = input + self.synapse0x1feb7a60()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x1feb7aa0(self):
		input = 2.39589
		input = input + self.synapse0x1feb7de0()
		input = input + self.synapse0x1feb7e20()
		input = input + self.synapse0x1feb7e60()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x1feb7ea0(self):
		input = -4.39203
		input = input + self.synapse0x1feb81e0()
		input = input + self.synapse0x1feb8220()
		input = input + self.synapse0x1feb8260()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x1feb82a0(self):
		input = -0.561386
		input = input + self.synapse0x1feb85e0()
		input = input + self.synapse0x1feb8620()
		input = input + self.synapse0x1febf0f0()
		input = input + self.synapse0x1c315850()
		input = input + self.synapse0x1c315890()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x1feb8770(self):
		input = -0.385217
		input = input + self.synapse0x1feb8ab0()
		input = input + self.synapse0x1feb8af0()
		input = input + self.synapse0x1feb8b30()
		input = input + self.synapse0x1feb8b70()
		input = input + self.synapse0x1feb8bb0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x1feb8bf0(self):
		input = -1.63269
		input = input + self.synapse0x1feb8f30()
		input = input + self.synapse0x1feb8f70()
		input = input + self.synapse0x1feb8fb0()
		input = input + self.synapse0x1feb8ff0()
		input = input + self.synapse0x1feb9030()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x1feb9070(self):
		input = -0.232771
		input = input + self.synapse0x1feb93b0()
		input = input + self.synapse0x1feb93f0()
		input = input + self.synapse0x1feb9430()
		input = input + self.synapse0x1c315c50()
		input = input + self.synapse0x1c315ce0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x1feb9680(self):
		input = 0.23155
		input = input + self.synapse0x1feb99c0()
		input = input + self.synapse0x1feb9a00()
		input = input + self.synapse0x1feb9a40()
		input = input + self.synapse0x1feb9a80()
		input = input + self.synapse0x1feb9ac0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x1feb9b00(self):
		input = 0.164734
		input = input + self.synapse0x1feb9e40()
		input = input + self.synapse0x1feb9e80()
		input = input + self.synapse0x1feb9ec0()
		input = input + self.synapse0x1feb9f00()
		input = input + self.synapse0x1feb9f40()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x1feb9f80(self):
		input = -0.0622124
		input = input + self.synapse0x1feba2c0()
		input = input + self.synapse0x1feba300()
		input = input + self.synapse0x1feba340()
		input = input + self.synapse0x1feba380()
		input = input + self.synapse0x1feba3c0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x1feba400(self):
		input = -0.145791
		input = input + self.synapse0x1feba740()
		input = input + self.synapse0x1feba780()
		input = input + self.synapse0x1feba7c0()
		input = input + self.synapse0x1feba800()
		input = input + self.synapse0x1feba840()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x1feba880(self):
		input = 0.525667
		input = input + self.synapse0x1c3156a0()
		input = input + self.synapse0x1c3156e0()
		input = input + self.synapse0x1c315d20()
		input = input + self.synapse0x1c315d60()
		input = input + self.synapse0x1febabc0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x1febac00(self):
		input = -0.61746
		input = input + self.synapse0x1febaf40()
		input = input + self.synapse0x1febaf80()
		input = input + self.synapse0x1febafc0()
		input = input + self.synapse0x1febb000()
		input = input + self.synapse0x1febb040()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x1feb9470(self):
		input = 1.33348
		input = input + self.synapse0x1feb6e40()
		input = input + self.synapse0x1febb5b0()
		input = input + self.synapse0x1febb5f0()
		input = input + self.synapse0x1febb630()
		input = input + self.synapse0x1febb670()
		input = input + self.synapse0x1febb6b0()
		input = input + self.synapse0x1febb6f0()
		input = input + self.synapse0x1febb730()
		input = input + self.synapse0x1febb770()
		input = input + self.synapse0x1febb7b0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def synapse0x1c315ca0(self):
		return (self.neuron0x1feb6480()*-2.52939)
	def synapse0x1feb7220(self):
		return (self.neuron0x1feb67c0()*1.09034)
	def synapse0x1feb7260(self):
		return (self.neuron0x1feb6b00()*0.14284)
	def synapse0x1feb75e0(self):
		return (self.neuron0x1feb6480()*2.46768)
	def synapse0x1feb7620(self):
		return (self.neuron0x1feb67c0()*-1.22782)
	def synapse0x1feb7660(self):
		return (self.neuron0x1feb6b00()*-0.396988)
	def synapse0x1feb79e0(self):
		return (self.neuron0x1feb6480()*-1.94415)
	def synapse0x1feb7a20(self):
		return (self.neuron0x1feb67c0()*2.75575)
	def synapse0x1feb7a60(self):
		return (self.neuron0x1feb6b00()*-0.32658)
	def synapse0x1feb7de0(self):
		return (self.neuron0x1feb6480()*-1.44844)
	def synapse0x1feb7e20(self):
		return (self.neuron0x1feb67c0()*1.75343)
	def synapse0x1feb7e60(self):
		return (self.neuron0x1feb6b00()*1.90229)
	def synapse0x1feb81e0(self):
		return (self.neuron0x1feb6480()*1.8418)
	def synapse0x1feb8220(self):
		return (self.neuron0x1feb67c0()*-3.19946)
	def synapse0x1feb8260(self):
		return (self.neuron0x1feb6b00()*-0.291179)
	def synapse0x1feb85e0(self):
		return (self.neuron0x1feb6f70()*1.17416)
	def synapse0x1feb8620(self):
		return (self.neuron0x1feb72a0()*-2.02943)
	def synapse0x1febf0f0(self):
		return (self.neuron0x1feb76a0()*-0.601345)
	def synapse0x1c315850(self):
		return (self.neuron0x1feb7aa0()*1.87006)
	def synapse0x1c315890(self):
		return (self.neuron0x1feb7ea0()*0.568974)
	def synapse0x1feb8ab0(self):
		return (self.neuron0x1feb6f70()*-3.32266)
	def synapse0x1feb8af0(self):
		return (self.neuron0x1feb72a0()*1.25988)
	def synapse0x1feb8b30(self):
		return (self.neuron0x1feb76a0()*2.22746)
	def synapse0x1feb8b70(self):
		return (self.neuron0x1feb7aa0()*-1.20519)
	def synapse0x1feb8bb0(self):
		return (self.neuron0x1feb7ea0()*-3.05458)
	def synapse0x1feb8f30(self):
		return (self.neuron0x1feb6f70()*2.19755)
	def synapse0x1feb8f70(self):
		return (self.neuron0x1feb72a0()*-2.55671)
	def synapse0x1feb8fb0(self):
		return (self.neuron0x1feb76a0()*-0.597393)
	def synapse0x1feb8ff0(self):
		return (self.neuron0x1feb7aa0()*2.79433)
	def synapse0x1feb9030(self):
		return (self.neuron0x1feb7ea0()*0.361818)
	def synapse0x1feb93b0(self):
		return (self.neuron0x1feb6f70()*0.255753)
	def synapse0x1feb93f0(self):
		return (self.neuron0x1feb72a0()*-0.712838)
	def synapse0x1feb9430(self):
		return (self.neuron0x1feb76a0()*-0.529931)
	def synapse0x1c315c50(self):
		return (self.neuron0x1feb7aa0()*0.493946)
	def synapse0x1c315ce0(self):
		return (self.neuron0x1feb7ea0()*-0.593921)
	def synapse0x1feb99c0(self):
		return (self.neuron0x1feb6f70()*-1.21451)
	def synapse0x1feb9a00(self):
		return (self.neuron0x1feb72a0()*1.46038)
	def synapse0x1feb9a40(self):
		return (self.neuron0x1feb76a0()*1.68849)
	def synapse0x1feb9a80(self):
		return (self.neuron0x1feb7aa0()*-2.66613)
	def synapse0x1feb9ac0(self):
		return (self.neuron0x1feb7ea0()*-2.55601)
	def synapse0x1feb9e40(self):
		return (self.neuron0x1feb6f70()*-0.122763)
	def synapse0x1feb9e80(self):
		return (self.neuron0x1feb72a0()*0.413952)
	def synapse0x1feb9ec0(self):
		return (self.neuron0x1feb76a0()*-0.0931631)
	def synapse0x1feb9f00(self):
		return (self.neuron0x1feb7aa0()*-0.337579)
	def synapse0x1feb9f40(self):
		return (self.neuron0x1feb7ea0()*0.322298)
	def synapse0x1feba2c0(self):
		return (self.neuron0x1feb6f70()*0.768169)
	def synapse0x1feba300(self):
		return (self.neuron0x1feb72a0()*-1.00786)
	def synapse0x1feba340(self):
		return (self.neuron0x1feb76a0()*-1.19658)
	def synapse0x1feba380(self):
		return (self.neuron0x1feb7aa0()*1.36646)
	def synapse0x1feba3c0(self):
		return (self.neuron0x1feb7ea0()*2.41849)
	def synapse0x1feba740(self):
		return (self.neuron0x1feb6f70()*0.187899)
	def synapse0x1feba780(self):
		return (self.neuron0x1feb72a0()*-0.485648)
	def synapse0x1feba7c0(self):
		return (self.neuron0x1feb76a0()*-1.00856)
	def synapse0x1feba800(self):
		return (self.neuron0x1feb7aa0()*0.647257)
	def synapse0x1feba840(self):
		return (self.neuron0x1feb7ea0()*-0.0621195)
	def synapse0x1c3156a0(self):
		return (self.neuron0x1feb6f70()*-1.22343)
	def synapse0x1c3156e0(self):
		return (self.neuron0x1feb72a0()*1.53206)
	def synapse0x1c315d20(self):
		return (self.neuron0x1feb76a0()*3.45116)
	def synapse0x1c315d60(self):
		return (self.neuron0x1feb7aa0()*-4.29137)
	def synapse0x1febabc0(self):
		return (self.neuron0x1feb7ea0()*-3.45858)
	def synapse0x1febaf40(self):
		return (self.neuron0x1feb6f70()*1.42943)
	def synapse0x1febaf80(self):
		return (self.neuron0x1feb72a0()*-1.78329)
	def synapse0x1febafc0(self):
		return (self.neuron0x1feb76a0()*-0.841965)
	def synapse0x1febb000(self):
		return (self.neuron0x1feb7aa0()*1.68853)
	def synapse0x1febb040(self):
		return (self.neuron0x1feb7ea0()*0.121791)
	def synapse0x1feb6e40(self):
		return (self.neuron0x1feb82a0()*-2.54589)
	def synapse0x1febb5b0(self):
		return (self.neuron0x1feb8770()*5.25403)
	def synapse0x1febb5f0(self):
		return (self.neuron0x1feb8bf0()*-5.44708)
	def synapse0x1febb630(self):
		return (self.neuron0x1feb9070()*0.141637)
	def synapse0x1febb670(self):
		return (self.neuron0x1feb9680()*4.65298)
	def synapse0x1febb6b0(self):
		return (self.neuron0x1feb9b00()*0.66026)
	def synapse0x1febb6f0(self):
		return (self.neuron0x1feb9f80()*-2.66777)
	def synapse0x1febb730(self):
		return (self.neuron0x1feba400()*-0.278248)
	def synapse0x1febb770(self):
		return (self.neuron0x1feba880()*7.54434)
	def synapse0x1febb7b0(self):
		return (self.neuron0x1febac00()*-1.82458)

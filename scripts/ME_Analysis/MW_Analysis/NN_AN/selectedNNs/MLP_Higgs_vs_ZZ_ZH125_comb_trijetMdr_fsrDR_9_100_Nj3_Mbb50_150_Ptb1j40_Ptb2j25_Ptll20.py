from math import exp

from math import tanh

class FinalV7/MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_9_100_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20:
	def value(self,index,in0,in1,in2,in3,in4,in5):
		self.input0 = (in0 - 21.226)/1.24166
		self.input1 = (in1 - 10.9087)/1.03117
		self.input2 = (in2 - 24.8606)/1.19624
		self.input3 = (in3 - 13.2278)/1.29862
		self.input4 = (in4 - 8.4161)/32.0247
		self.input5 = (in5 - 1.80644)/0.815831
		if index==0: return self.neuron0x1dcb0ad0();
		return 0.
	def neuron0x1dcaccc0(self):
		return self.input0
	def neuron0x1dcad000(self):
		return self.input1
	def neuron0x1dcad340(self):
		return self.input2
	def neuron0x1dcad680(self):
		return self.input3
	def neuron0x1dcad9c0(self):
		return self.input4
	def neuron0x1dcadd00(self):
		return self.input5
	def neuron0x1dcae170(self):
		input = -0.566393
		input = input + self.synapse0x1dbfa800()
		input = input + self.synapse0x1dc9bf30()
		input = input + self.synapse0x1dcae420()
		input = input + self.synapse0x1dcae460()
		input = input + self.synapse0x1dcae4a0()
		input = input + self.synapse0x1dcae4e0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x1dcae520(self):
		input = -0.64416
		input = input + self.synapse0x1dcae860()
		input = input + self.synapse0x1dcae8a0()
		input = input + self.synapse0x1dcae8e0()
		input = input + self.synapse0x1dcae920()
		input = input + self.synapse0x1dcae960()
		input = input + self.synapse0x1dcae9a0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x1dcae9e0(self):
		input = 0.330788
		input = input + self.synapse0x1dcaed20()
		input = input + self.synapse0x1dcaed60()
		input = input + self.synapse0x1dcaeda0()
		input = input + self.synapse0x1dcaede0()
		input = input + self.synapse0x1dcaee20()
		input = input + self.synapse0x1dbfa770()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x1dcaef70(self):
		input = 0.441
		input = input + self.synapse0x1dbfa7b0()
		input = input + self.synapse0x1dcaf2b0()
		input = input + self.synapse0x1dcaf2f0()
		input = input + self.synapse0x1dcaf330()
		input = input + self.synapse0x1dcaf370()
		input = input + self.synapse0x1dcaf3b0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x1dcaf3f0(self):
		input = 0.765082
		input = input + self.synapse0x1dcaf730()
		input = input + self.synapse0x1dcaf770()
		input = input + self.synapse0x1dcaf7b0()
		input = input + self.synapse0x1dcaf7f0()
		input = input + self.synapse0x1dcaf830()
		input = input + self.synapse0x1dcaf870()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x1dcaf8b0(self):
		input = -4.36451
		input = input + self.synapse0x1dcafbf0()
		input = input + self.synapse0x1dcafc30()
		input = input + self.synapse0x1dcafc70()
		input = input + self.synapse0x1dc9c040()
		input = input + self.synapse0x1dc0a530()
		input = input + self.synapse0x1dbfab50()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x1dcafec0(self):
		input = -0.362429
		input = input + self.synapse0x1dcaeef0()
		input = input + self.synapse0x1dcaef30()
		input = input + self.synapse0x1dcb0050()
		input = input + self.synapse0x1dcb0090()
		input = input + self.synapse0x1dcb00d0()
		input = input + self.synapse0x1dcb0110()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x1dcb0150(self):
		input = -3.20514
		input = input + self.synapse0x1dcb0490()
		input = input + self.synapse0x1dcb04d0()
		input = input + self.synapse0x1dcb0510()
		input = input + self.synapse0x1dcb0550()
		input = input + self.synapse0x1dcb0590()
		input = input + self.synapse0x1dcb05d0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x1dcb0610(self):
		input = -0.478475
		input = input + self.synapse0x1dcb0950()
		input = input + self.synapse0x1dcb0990()
		input = input + self.synapse0x1dcb09d0()
		input = input + self.synapse0x1dcb0a10()
		input = input + self.synapse0x1dcb0a50()
		input = input + self.synapse0x1dcb0a90()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x1dcb0ad0(self):
		input = 0.686873
		input = input + self.synapse0x1dcb0cf0()
		input = input + self.synapse0x1dcb0d30()
		input = input + self.synapse0x1dcb0d70()
		input = input + self.synapse0x1dcb0db0()
		input = input + self.synapse0x1dcb0df0()
		input = input + self.synapse0x1dcb0e30()
		input = input + self.synapse0x1dcb0e70()
		input = input + self.synapse0x1dcb0eb0()
		input = input + self.synapse0x1dcb0ef0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def synapse0x1dbfa800(self):
		return (self.neuron0x1dcaccc0()*-0.126561)
	def synapse0x1dc9bf30(self):
		return (self.neuron0x1dcad000()*-0.246783)
	def synapse0x1dcae420(self):
		return (self.neuron0x1dcad340()*0.414073)
	def synapse0x1dcae460(self):
		return (self.neuron0x1dcad680()*-0.285194)
	def synapse0x1dcae4a0(self):
		return (self.neuron0x1dcad9c0()*-0.222319)
	def synapse0x1dcae4e0(self):
		return (self.neuron0x1dcadd00()*-0.411402)
	def synapse0x1dcae860(self):
		return (self.neuron0x1dcaccc0()*-0.633385)
	def synapse0x1dcae8a0(self):
		return (self.neuron0x1dcad000()*-0.40439)
	def synapse0x1dcae8e0(self):
		return (self.neuron0x1dcad340()*1.04567)
	def synapse0x1dcae920(self):
		return (self.neuron0x1dcad680()*-2.95414)
	def synapse0x1dcae960(self):
		return (self.neuron0x1dcad9c0()*-0.298041)
	def synapse0x1dcae9a0(self):
		return (self.neuron0x1dcadd00()*0.370507)
	def synapse0x1dcaed20(self):
		return (self.neuron0x1dcaccc0()*-0.26742)
	def synapse0x1dcaed60(self):
		return (self.neuron0x1dcad000()*-0.124502)
	def synapse0x1dcaeda0(self):
		return (self.neuron0x1dcad340()*-0.685238)
	def synapse0x1dcaede0(self):
		return (self.neuron0x1dcad680()*1.77335)
	def synapse0x1dcaee20(self):
		return (self.neuron0x1dcad9c0()*0.576958)
	def synapse0x1dbfa770(self):
		return (self.neuron0x1dcadd00()*-0.213641)
	def synapse0x1dbfa7b0(self):
		return (self.neuron0x1dcaccc0()*0.135909)
	def synapse0x1dcaf2b0(self):
		return (self.neuron0x1dcad000()*0.0309498)
	def synapse0x1dcaf2f0(self):
		return (self.neuron0x1dcad340()*-0.204472)
	def synapse0x1dcaf330(self):
		return (self.neuron0x1dcad680()*-0.287807)
	def synapse0x1dcaf370(self):
		return (self.neuron0x1dcad9c0()*-0.155076)
	def synapse0x1dcaf3b0(self):
		return (self.neuron0x1dcadd00()*-0.287008)
	def synapse0x1dcaf730(self):
		return (self.neuron0x1dcaccc0()*-1.20315)
	def synapse0x1dcaf770(self):
		return (self.neuron0x1dcad000()*0.452141)
	def synapse0x1dcaf7b0(self):
		return (self.neuron0x1dcad340()*-0.601491)
	def synapse0x1dcaf7f0(self):
		return (self.neuron0x1dcad680()*-1.18633)
	def synapse0x1dcaf830(self):
		return (self.neuron0x1dcad9c0()*-0.60432)
	def synapse0x1dcaf870(self):
		return (self.neuron0x1dcadd00()*-0.15516)
	def synapse0x1dcafbf0(self):
		return (self.neuron0x1dcaccc0()*-0.426349)
	def synapse0x1dcafc30(self):
		return (self.neuron0x1dcad000()*-2.49766)
	def synapse0x1dcafc70(self):
		return (self.neuron0x1dcad340()*1.99126)
	def synapse0x1dc9c040(self):
		return (self.neuron0x1dcad680()*1.0297)
	def synapse0x1dc0a530(self):
		return (self.neuron0x1dcad9c0()*-0.144313)
	def synapse0x1dbfab50(self):
		return (self.neuron0x1dcadd00()*0.541006)
	def synapse0x1dcaeef0(self):
		return (self.neuron0x1dcaccc0()*0.121397)
	def synapse0x1dcaef30(self):
		return (self.neuron0x1dcad000()*-0.235707)
	def synapse0x1dcb0050(self):
		return (self.neuron0x1dcad340()*0.154195)
	def synapse0x1dcb0090(self):
		return (self.neuron0x1dcad680()*-1.33835)
	def synapse0x1dcb00d0(self):
		return (self.neuron0x1dcad9c0()*-0.574202)
	def synapse0x1dcb0110(self):
		return (self.neuron0x1dcadd00()*0.532217)
	def synapse0x1dcb0490(self):
		return (self.neuron0x1dcaccc0()*1.14769)
	def synapse0x1dcb04d0(self):
		return (self.neuron0x1dcad000()*0.731311)
	def synapse0x1dcb0510(self):
		return (self.neuron0x1dcad340()*0.246479)
	def synapse0x1dcb0550(self):
		return (self.neuron0x1dcad680()*-2.87691)
	def synapse0x1dcb0590(self):
		return (self.neuron0x1dcad9c0()*0.102693)
	def synapse0x1dcb05d0(self):
		return (self.neuron0x1dcadd00()*-0.277343)
	def synapse0x1dcb0950(self):
		return (self.neuron0x1dcaccc0()*0.0110437)
	def synapse0x1dcb0990(self):
		return (self.neuron0x1dcad000()*-0.492624)
	def synapse0x1dcb09d0(self):
		return (self.neuron0x1dcad340()*0.804748)
	def synapse0x1dcb0a10(self):
		return (self.neuron0x1dcad680()*-0.316554)
	def synapse0x1dcb0a50(self):
		return (self.neuron0x1dcad9c0()*-0.0833357)
	def synapse0x1dcb0a90(self):
		return (self.neuron0x1dcadd00()*-0.301951)
	def synapse0x1dcb0cf0(self):
		return (self.neuron0x1dcae170()*-0.379318)
	def synapse0x1dcb0d30(self):
		return (self.neuron0x1dcae520()*1.23547)
	def synapse0x1dcb0d70(self):
		return (self.neuron0x1dcae9e0()*-0.727572)
	def synapse0x1dcb0db0(self):
		return (self.neuron0x1dcaef70()*0.399726)
	def synapse0x1dcb0df0(self):
		return (self.neuron0x1dcaf3f0()*-1.24247)
	def synapse0x1dcb0e30(self):
		return (self.neuron0x1dcaf8b0()*-3.7156)
	def synapse0x1dcb0e70(self):
		return (self.neuron0x1dcafec0()*0.486469)
	def synapse0x1dcb0eb0(self):
		return (self.neuron0x1dcb0150()*2.99347)
	def synapse0x1dcb0ef0(self):
		return (self.neuron0x1dcb0610()*-0.600311)

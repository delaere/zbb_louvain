from math import exp

from math import tanh

class FinalV7/MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_12_9_6_3_210_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20:
	def value(self,index,in0,in1,in2,in3,in4,in5):
		self.input0 = (in0 - 19.5959)/1.02856
		self.input1 = (in1 - 20.2647)/0.838707
		self.input2 = (in2 - 24.8357)/1.49412
		self.input3 = (in3 - 13.3413)/1.47218
		self.input4 = (in4 - 8.50219)/30.9864
		self.input5 = (in5 - 1.8064)/0.811333
		if index==0: return self.neuron0x1ca66330();
		return 0.
	def neuron0x1ca5a7c0(self):
		return self.input0
	def neuron0x1ca5aa70(self):
		return self.input1
	def neuron0x1ca5adb0(self):
		return self.input2
	def neuron0x1ca5b0f0(self):
		return self.input3
	def neuron0x1ca5b430(self):
		return self.input4
	def neuron0x1ca5b770(self):
		return self.input5
	def neuron0x1ca5bbe0(self):
		input = -0.259774
		input = input + self.synapse0x1ca5be90()
		input = input + self.synapse0x1ca5bed0()
		input = input + self.synapse0x1ca5bf10()
		input = input + self.synapse0x1ca5bf50()
		input = input + self.synapse0x1ca5bf90()
		input = input + self.synapse0x1ca5bfd0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x1ca5c010(self):
		input = 0.138746
		input = input + self.synapse0x1ca5c350()
		input = input + self.synapse0x1ca5c390()
		input = input + self.synapse0x1ca5c3d0()
		input = input + self.synapse0x1ca5c410()
		input = input + self.synapse0x1ca5c450()
		input = input + self.synapse0x1ca5c490()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x1ca5c4d0(self):
		input = 0.0672574
		input = input + self.synapse0x1ca5c810()
		input = input + self.synapse0x1ca5c850()
		input = input + self.synapse0x1ca5c890()
		input = input + self.synapse0x1ca5c8d0()
		input = input + self.synapse0x1ca5c910()
		input = input + self.synapse0x1c9a8270()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x1ca5ca60(self):
		input = -0.600926
		input = input + self.synapse0x1c9a82b0()
		input = input + self.synapse0x1ca5cda0()
		input = input + self.synapse0x1ca5cde0()
		input = input + self.synapse0x1ca5ce20()
		input = input + self.synapse0x1ca5ce60()
		input = input + self.synapse0x1ca5cea0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x1ca5cee0(self):
		input = -0.370899
		input = input + self.synapse0x1ca5d220()
		input = input + self.synapse0x1ca5d260()
		input = input + self.synapse0x1ca5d2a0()
		input = input + self.synapse0x1ca5d2e0()
		input = input + self.synapse0x1ca5d320()
		input = input + self.synapse0x1ca5d360()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x1ca5d3a0(self):
		input = 0.148826
		input = input + self.synapse0x1ca5d6e0()
		input = input + self.synapse0x1ca5d720()
		input = input + self.synapse0x1ca5d760()
		input = input + self.synapse0x1ca49b40()
		input = input + self.synapse0x1c9b8030()
		input = input + self.synapse0x1c9a8650()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x1ca5d9b0(self):
		input = 0.105755
		input = input + self.synapse0x1ca5c9e0()
		input = input + self.synapse0x1ca5ca20()
		input = input + self.synapse0x1ca5db40()
		input = input + self.synapse0x1ca5db80()
		input = input + self.synapse0x1ca5dbc0()
		input = input + self.synapse0x1ca5dc00()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x1ca5dc40(self):
		input = 1.97535
		input = input + self.synapse0x1ca5df80()
		input = input + self.synapse0x1ca5dfc0()
		input = input + self.synapse0x1ca5e000()
		input = input + self.synapse0x1ca5e040()
		input = input + self.synapse0x1ca5e080()
		input = input + self.synapse0x1ca5e0c0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x1ca5e100(self):
		input = -0.315596
		input = input + self.synapse0x1ca5e440()
		input = input + self.synapse0x1ca5e480()
		input = input + self.synapse0x1ca5e4c0()
		input = input + self.synapse0x1ca5e500()
		input = input + self.synapse0x1ca5e540()
		input = input + self.synapse0x1ca5e580()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x1ca5e5c0(self):
		input = 0.563446
		input = input + self.synapse0x1ca5e900()
		input = input + self.synapse0x1ca5e940()
		input = input + self.synapse0x1ca5e980()
		input = input + self.synapse0x1ca5e9c0()
		input = input + self.synapse0x1ca5ea00()
		input = input + self.synapse0x1ca5ea40()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x1ca5ea80(self):
		input = -0.876319
		input = input + self.synapse0x1c9a80c0()
		input = input + self.synapse0x1c9a8100()
		input = input + self.synapse0x1ca5eed0()
		input = input + self.synapse0x1ca5ef10()
		input = input + self.synapse0x1ca5ef50()
		input = input + self.synapse0x1ca5d7a0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x1ca5d7e0(self):
		input = 0.366995
		input = input + self.synapse0x1ca5d970()
		input = input + self.synapse0x1ca5f550()
		input = input + self.synapse0x1ca5f590()
		input = input + self.synapse0x1ca5f5d0()
		input = input + self.synapse0x1ca5f610()
		input = input + self.synapse0x1ca5f650()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x1ca5f690(self):
		input = -0.104546
		input = input + self.synapse0x1ca5f9d0()
		input = input + self.synapse0x1ca5fa10()
		input = input + self.synapse0x1ca5fa50()
		input = input + self.synapse0x1ca5fa90()
		input = input + self.synapse0x1ca5fad0()
		input = input + self.synapse0x1ca5fb10()
		input = input + self.synapse0x1ca5fb50()
		input = input + self.synapse0x1ca5fb90()
		input = input + self.synapse0x1ca5fbd0()
		input = input + self.synapse0x1ca5fc10()
		input = input + self.synapse0x1ca5fc50()
		input = input + self.synapse0x1ca5fc90()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x1ca5fcd0(self):
		input = 0.280206
		input = input + self.synapse0x1ca60010()
		input = input + self.synapse0x1ca60050()
		input = input + self.synapse0x1ca60090()
		input = input + self.synapse0x1ca600d0()
		input = input + self.synapse0x1ca60110()
		input = input + self.synapse0x1ca60150()
		input = input + self.synapse0x1ca60190()
		input = input + self.synapse0x1ca601d0()
		input = input + self.synapse0x1ca60210()
		input = input + self.synapse0x1ca60250()
		input = input + self.synapse0x1ca60290()
		input = input + self.synapse0x1ca602d0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x1ca60310(self):
		input = -0.36015
		input = input + self.synapse0x1ca60650()
		input = input + self.synapse0x1ca60690()
		input = input + self.synapse0x1ca606d0()
		input = input + self.synapse0x1ca60710()
		input = input + self.synapse0x1ca60750()
		input = input + self.synapse0x1ca60790()
		input = input + self.synapse0x1ca607d0()
		input = input + self.synapse0x1ca60810()
		input = input + self.synapse0x1ca60850()
		input = input + self.synapse0x1ca60890()
		input = input + self.synapse0x1ca608d0()
		input = input + self.synapse0x1ca60910()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x1ca60950(self):
		input = 0.464581
		input = input + self.synapse0x1ca60c90()
		input = input + self.synapse0x1ca60cd0()
		input = input + self.synapse0x1ca60d10()
		input = input + self.synapse0x1ca60d50()
		input = input + self.synapse0x1ca60d90()
		input = input + self.synapse0x1ca60dd0()
		input = input + self.synapse0x1ca60e10()
		input = input + self.synapse0x1ca60e50()
		input = input + self.synapse0x1ca60e90()
		input = input + self.synapse0x1ca60ed0()
		input = input + self.synapse0x1ca60f10()
		input = input + self.synapse0x1ca60f50()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x1ca60f90(self):
		input = 0.104663
		input = input + self.synapse0x1ca612d0()
		input = input + self.synapse0x1ca61310()
		input = input + self.synapse0x1ca61350()
		input = input + self.synapse0x1ca61390()
		input = input + self.synapse0x1ca613d0()
		input = input + self.synapse0x1ca61410()
		input = input + self.synapse0x1ca61450()
		input = input + self.synapse0x1ca61490()
		input = input + self.synapse0x1ca614d0()
		input = input + self.synapse0x1ca5ef90()
		input = input + self.synapse0x1ca5efd0()
		input = input + self.synapse0x1ca5f010()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x1ca5f050(self):
		input = -0.212921
		input = input + self.synapse0x1ca61d20()
		input = input + self.synapse0x1ca61d60()
		input = input + self.synapse0x1ca61da0()
		input = input + self.synapse0x1ca61de0()
		input = input + self.synapse0x1ca61e20()
		input = input + self.synapse0x1ca61e60()
		input = input + self.synapse0x1ca61ea0()
		input = input + self.synapse0x1ca61ee0()
		input = input + self.synapse0x1ca61f20()
		input = input + self.synapse0x1ca61f60()
		input = input + self.synapse0x1ca61fa0()
		input = input + self.synapse0x1ca61fe0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x1ca62020(self):
		input = 0.0120629
		input = input + self.synapse0x1ca62360()
		input = input + self.synapse0x1ca623a0()
		input = input + self.synapse0x1ca623e0()
		input = input + self.synapse0x1ca62420()
		input = input + self.synapse0x1ca62460()
		input = input + self.synapse0x1ca624a0()
		input = input + self.synapse0x1ca624e0()
		input = input + self.synapse0x1ca62520()
		input = input + self.synapse0x1ca62560()
		input = input + self.synapse0x1ca625a0()
		input = input + self.synapse0x1ca625e0()
		input = input + self.synapse0x1ca62620()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x1ca62660(self):
		input = 0.146341
		input = input + self.synapse0x1ca629a0()
		input = input + self.synapse0x1ca629e0()
		input = input + self.synapse0x1ca62a20()
		input = input + self.synapse0x1ca62a60()
		input = input + self.synapse0x1ca62aa0()
		input = input + self.synapse0x1ca62ae0()
		input = input + self.synapse0x1ca62b20()
		input = input + self.synapse0x1ca62b60()
		input = input + self.synapse0x1ca62ba0()
		input = input + self.synapse0x1ca62be0()
		input = input + self.synapse0x1ca62c20()
		input = input + self.synapse0x1ca62c60()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x1ca62ca0(self):
		input = -0.865624
		input = input + self.synapse0x1ca62fe0()
		input = input + self.synapse0x1ca63020()
		input = input + self.synapse0x1ca63060()
		input = input + self.synapse0x1ca630a0()
		input = input + self.synapse0x1ca630e0()
		input = input + self.synapse0x1ca63120()
		input = input + self.synapse0x1ca63160()
		input = input + self.synapse0x1ca631a0()
		input = input + self.synapse0x1ca631e0()
		input = input + self.synapse0x1ca63220()
		input = input + self.synapse0x1ca63260()
		input = input + self.synapse0x1ca632a0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x1ca632e0(self):
		input = -0.0821723
		input = input + self.synapse0x1ca63620()
		input = input + self.synapse0x1ca63660()
		input = input + self.synapse0x1ca636a0()
		input = input + self.synapse0x1ca636e0()
		input = input + self.synapse0x1ca63720()
		input = input + self.synapse0x1ca63760()
		input = input + self.synapse0x1ca637a0()
		input = input + self.synapse0x1ca637e0()
		input = input + self.synapse0x1ca63820()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x1ca63860(self):
		input = 0.315089
		input = input + self.synapse0x1ca63ba0()
		input = input + self.synapse0x1ca63be0()
		input = input + self.synapse0x1ca63c20()
		input = input + self.synapse0x1ca63c60()
		input = input + self.synapse0x1ca63ca0()
		input = input + self.synapse0x1ca63ce0()
		input = input + self.synapse0x1ca63d20()
		input = input + self.synapse0x1ca63d60()
		input = input + self.synapse0x1ca63da0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x1ca63de0(self):
		input = 0.0989284
		input = input + self.synapse0x1ca64120()
		input = input + self.synapse0x1ca64160()
		input = input + self.synapse0x1ca641a0()
		input = input + self.synapse0x1ca641e0()
		input = input + self.synapse0x1ca64220()
		input = input + self.synapse0x1ca64260()
		input = input + self.synapse0x1ca642a0()
		input = input + self.synapse0x1ca642e0()
		input = input + self.synapse0x1ca64320()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x1ca64360(self):
		input = -0.680248
		input = input + self.synapse0x1ca646a0()
		input = input + self.synapse0x1ca646e0()
		input = input + self.synapse0x1ca64720()
		input = input + self.synapse0x1ca64760()
		input = input + self.synapse0x1ca647a0()
		input = input + self.synapse0x1ca647e0()
		input = input + self.synapse0x1ca64820()
		input = input + self.synapse0x1ca64860()
		input = input + self.synapse0x1ca648a0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x1ca648e0(self):
		input = 0.0477673
		input = input + self.synapse0x1ca64c20()
		input = input + self.synapse0x1ca64c60()
		input = input + self.synapse0x1ca64ca0()
		input = input + self.synapse0x1ca64ce0()
		input = input + self.synapse0x1ca64d20()
		input = input + self.synapse0x1ca64d60()
		input = input + self.synapse0x1ca64da0()
		input = input + self.synapse0x1ca64de0()
		input = input + self.synapse0x1ca64e20()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x1ca64e60(self):
		input = 0.110013
		input = input + self.synapse0x1ca5edc0()
		input = input + self.synapse0x1ca5ee00()
		input = input + self.synapse0x1ca5ee40()
		input = input + self.synapse0x1ca5ee80()
		input = input + self.synapse0x1ca653b0()
		input = input + self.synapse0x1ca653f0()
		input = input + self.synapse0x1ca65430()
		input = input + self.synapse0x1ca65470()
		input = input + self.synapse0x1ca654b0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x1ca654f0(self):
		input = 0.271156
		input = input + self.synapse0x1ca65830()
		input = input + self.synapse0x1ca65870()
		input = input + self.synapse0x1ca658b0()
		input = input + self.synapse0x1ca658f0()
		input = input + self.synapse0x1ca65930()
		input = input + self.synapse0x1ca65970()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x1ca659b0(self):
		input = 0.0293537
		input = input + self.synapse0x1ca65cf0()
		input = input + self.synapse0x1ca65d30()
		input = input + self.synapse0x1ca65d70()
		input = input + self.synapse0x1ca65db0()
		input = input + self.synapse0x1ca65df0()
		input = input + self.synapse0x1ca65e30()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x1ca65e70(self):
		input = -0.0792383
		input = input + self.synapse0x1ca661b0()
		input = input + self.synapse0x1ca661f0()
		input = input + self.synapse0x1ca66230()
		input = input + self.synapse0x1ca66270()
		input = input + self.synapse0x1ca662b0()
		input = input + self.synapse0x1ca662f0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x1ca66330(self):
		input = -0.15943
		input = input + self.synapse0x1ca66550()
		input = input + self.synapse0x1ca66590()
		input = input + self.synapse0x1ca665d0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def synapse0x1ca5be90(self):
		return (self.neuron0x1ca5a7c0()*-0.353815)
	def synapse0x1ca5bed0(self):
		return (self.neuron0x1ca5aa70()*0.170272)
	def synapse0x1ca5bf10(self):
		return (self.neuron0x1ca5adb0()*1.00017)
	def synapse0x1ca5bf50(self):
		return (self.neuron0x1ca5b0f0()*-0.370854)
	def synapse0x1ca5bf90(self):
		return (self.neuron0x1ca5b430()*0.936689)
	def synapse0x1ca5bfd0(self):
		return (self.neuron0x1ca5b770()*0.344474)
	def synapse0x1ca5c350(self):
		return (self.neuron0x1ca5a7c0()*0.825059)
	def synapse0x1ca5c390(self):
		return (self.neuron0x1ca5aa70()*-0.676046)
	def synapse0x1ca5c3d0(self):
		return (self.neuron0x1ca5adb0()*-0.42661)
	def synapse0x1ca5c410(self):
		return (self.neuron0x1ca5b0f0()*-0.192055)
	def synapse0x1ca5c450(self):
		return (self.neuron0x1ca5b430()*1.25546)
	def synapse0x1ca5c490(self):
		return (self.neuron0x1ca5b770()*0.644279)
	def synapse0x1ca5c810(self):
		return (self.neuron0x1ca5a7c0()*0.654433)
	def synapse0x1ca5c850(self):
		return (self.neuron0x1ca5aa70()*1.66198)
	def synapse0x1ca5c890(self):
		return (self.neuron0x1ca5adb0()*-2.48814)
	def synapse0x1ca5c8d0(self):
		return (self.neuron0x1ca5b0f0()*-0.79154)
	def synapse0x1ca5c910(self):
		return (self.neuron0x1ca5b430()*0.499872)
	def synapse0x1c9a8270(self):
		return (self.neuron0x1ca5b770()*-0.137821)
	def synapse0x1c9a82b0(self):
		return (self.neuron0x1ca5a7c0()*-0.0489799)
	def synapse0x1ca5cda0(self):
		return (self.neuron0x1ca5aa70()*0.490612)
	def synapse0x1ca5cde0(self):
		return (self.neuron0x1ca5adb0()*0.518565)
	def synapse0x1ca5ce20(self):
		return (self.neuron0x1ca5b0f0()*-0.980488)
	def synapse0x1ca5ce60(self):
		return (self.neuron0x1ca5b430()*0.331811)
	def synapse0x1ca5cea0(self):
		return (self.neuron0x1ca5b770()*0.0148684)
	def synapse0x1ca5d220(self):
		return (self.neuron0x1ca5a7c0()*0.811245)
	def synapse0x1ca5d260(self):
		return (self.neuron0x1ca5aa70()*0.494022)
	def synapse0x1ca5d2a0(self):
		return (self.neuron0x1ca5adb0()*0.0317268)
	def synapse0x1ca5d2e0(self):
		return (self.neuron0x1ca5b0f0()*-1.21947)
	def synapse0x1ca5d320(self):
		return (self.neuron0x1ca5b430()*0.29712)
	def synapse0x1ca5d360(self):
		return (self.neuron0x1ca5b770()*-0.295108)
	def synapse0x1ca5d6e0(self):
		return (self.neuron0x1ca5a7c0()*-0.0331715)
	def synapse0x1ca5d720(self):
		return (self.neuron0x1ca5aa70()*-0.394247)
	def synapse0x1ca5d760(self):
		return (self.neuron0x1ca5adb0()*0.25673)
	def synapse0x1ca49b40(self):
		return (self.neuron0x1ca5b0f0()*0.836115)
	def synapse0x1c9b8030(self):
		return (self.neuron0x1ca5b430()*0.323178)
	def synapse0x1c9a8650(self):
		return (self.neuron0x1ca5b770()*-0.477245)
	def synapse0x1ca5c9e0(self):
		return (self.neuron0x1ca5a7c0()*0.115592)
	def synapse0x1ca5ca20(self):
		return (self.neuron0x1ca5aa70()*0.0919475)
	def synapse0x1ca5db40(self):
		return (self.neuron0x1ca5adb0()*0.147539)
	def synapse0x1ca5db80(self):
		return (self.neuron0x1ca5b0f0()*0.334577)
	def synapse0x1ca5dbc0(self):
		return (self.neuron0x1ca5b430()*-0.263489)
	def synapse0x1ca5dc00(self):
		return (self.neuron0x1ca5b770()*0.812386)
	def synapse0x1ca5df80(self):
		return (self.neuron0x1ca5a7c0()*0.86916)
	def synapse0x1ca5dfc0(self):
		return (self.neuron0x1ca5aa70()*0.641911)
	def synapse0x1ca5e000(self):
		return (self.neuron0x1ca5adb0()*-2.41273)
	def synapse0x1ca5e040(self):
		return (self.neuron0x1ca5b0f0()*0.395809)
	def synapse0x1ca5e080(self):
		return (self.neuron0x1ca5b430()*0.25692)
	def synapse0x1ca5e0c0(self):
		return (self.neuron0x1ca5b770()*-0.0212319)
	def synapse0x1ca5e440(self):
		return (self.neuron0x1ca5a7c0()*0.591311)
	def synapse0x1ca5e480(self):
		return (self.neuron0x1ca5aa70()*0.775978)
	def synapse0x1ca5e4c0(self):
		return (self.neuron0x1ca5adb0()*-2.30873)
	def synapse0x1ca5e500(self):
		return (self.neuron0x1ca5b0f0()*-0.815425)
	def synapse0x1ca5e540(self):
		return (self.neuron0x1ca5b430()*-0.125579)
	def synapse0x1ca5e580(self):
		return (self.neuron0x1ca5b770()*0.37859)
	def synapse0x1ca5e900(self):
		return (self.neuron0x1ca5a7c0()*-0.666062)
	def synapse0x1ca5e940(self):
		return (self.neuron0x1ca5aa70()*0.0652179)
	def synapse0x1ca5e980(self):
		return (self.neuron0x1ca5adb0()*-0.602585)
	def synapse0x1ca5e9c0(self):
		return (self.neuron0x1ca5b0f0()*2.13163)
	def synapse0x1ca5ea00(self):
		return (self.neuron0x1ca5b430()*-0.15076)
	def synapse0x1ca5ea40(self):
		return (self.neuron0x1ca5b770()*-0.415346)
	def synapse0x1c9a80c0(self):
		return (self.neuron0x1ca5a7c0()*-0.0708338)
	def synapse0x1c9a8100(self):
		return (self.neuron0x1ca5aa70()*0.876557)
	def synapse0x1ca5eed0(self):
		return (self.neuron0x1ca5adb0()*-0.0481722)
	def synapse0x1ca5ef10(self):
		return (self.neuron0x1ca5b0f0()*-1.53615)
	def synapse0x1ca5ef50(self):
		return (self.neuron0x1ca5b430()*0.0291664)
	def synapse0x1ca5d7a0(self):
		return (self.neuron0x1ca5b770()*-0.292204)
	def synapse0x1ca5d970(self):
		return (self.neuron0x1ca5a7c0()*0.119794)
	def synapse0x1ca5f550(self):
		return (self.neuron0x1ca5aa70()*-0.772332)
	def synapse0x1ca5f590(self):
		return (self.neuron0x1ca5adb0()*-1.22096)
	def synapse0x1ca5f5d0(self):
		return (self.neuron0x1ca5b0f0()*-0.611475)
	def synapse0x1ca5f610(self):
		return (self.neuron0x1ca5b430()*1.4446)
	def synapse0x1ca5f650(self):
		return (self.neuron0x1ca5b770()*0.323551)
	def synapse0x1ca5f9d0(self):
		return (self.neuron0x1ca5bbe0()*0.736745)
	def synapse0x1ca5fa10(self):
		return (self.neuron0x1ca5c010()*-0.0291903)
	def synapse0x1ca5fa50(self):
		return (self.neuron0x1ca5c4d0()*-0.0516619)
	def synapse0x1ca5fa90(self):
		return (self.neuron0x1ca5ca60()*0.328414)
	def synapse0x1ca5fad0(self):
		return (self.neuron0x1ca5cee0()*-0.356765)
	def synapse0x1ca5fb10(self):
		return (self.neuron0x1ca5d3a0()*0.105569)
	def synapse0x1ca5fb50(self):
		return (self.neuron0x1ca5d9b0()*-0.451963)
	def synapse0x1ca5fb90(self):
		return (self.neuron0x1ca5dc40()*0.267876)
	def synapse0x1ca5fbd0(self):
		return (self.neuron0x1ca5e100()*-0.026707)
	def synapse0x1ca5fc10(self):
		return (self.neuron0x1ca5e5c0()*-0.191121)
	def synapse0x1ca5fc50(self):
		return (self.neuron0x1ca5ea80()*-0.126975)
	def synapse0x1ca5fc90(self):
		return (self.neuron0x1ca5d7e0()*-0.563936)
	def synapse0x1ca60010(self):
		return (self.neuron0x1ca5bbe0()*0.361071)
	def synapse0x1ca60050(self):
		return (self.neuron0x1ca5c010()*-0.688781)
	def synapse0x1ca60090(self):
		return (self.neuron0x1ca5c4d0()*0.784987)
	def synapse0x1ca600d0(self):
		return (self.neuron0x1ca5ca60()*0.413866)
	def synapse0x1ca60110(self):
		return (self.neuron0x1ca5cee0()*0.228377)
	def synapse0x1ca60150(self):
		return (self.neuron0x1ca5d3a0()*0.227095)
	def synapse0x1ca60190(self):
		return (self.neuron0x1ca5d9b0()*0.0928625)
	def synapse0x1ca601d0(self):
		return (self.neuron0x1ca5dc40()*-1.30078)
	def synapse0x1ca60210(self):
		return (self.neuron0x1ca5e100()*0.812997)
	def synapse0x1ca60250(self):
		return (self.neuron0x1ca5e5c0()*-0.525417)
	def synapse0x1ca60290(self):
		return (self.neuron0x1ca5ea80()*-0.47495)
	def synapse0x1ca602d0(self):
		return (self.neuron0x1ca5d7e0()*0.381863)
	def synapse0x1ca60650(self):
		return (self.neuron0x1ca5bbe0()*0.588607)
	def synapse0x1ca60690(self):
		return (self.neuron0x1ca5c010()*-0.829706)
	def synapse0x1ca606d0(self):
		return (self.neuron0x1ca5c4d0()*0.173879)
	def synapse0x1ca60710(self):
		return (self.neuron0x1ca5ca60()*0.0724313)
	def synapse0x1ca60750(self):
		return (self.neuron0x1ca5cee0()*0.0915354)
	def synapse0x1ca60790(self):
		return (self.neuron0x1ca5d3a0()*0.281663)
	def synapse0x1ca607d0(self):
		return (self.neuron0x1ca5d9b0()*0.38661)
	def synapse0x1ca60810(self):
		return (self.neuron0x1ca5dc40()*-1.33952)
	def synapse0x1ca60850(self):
		return (self.neuron0x1ca5e100()*0.47519)
	def synapse0x1ca60890(self):
		return (self.neuron0x1ca5e5c0()*-0.213025)
	def synapse0x1ca608d0(self):
		return (self.neuron0x1ca5ea80()*-0.252472)
	def synapse0x1ca60910(self):
		return (self.neuron0x1ca5d7e0()*0.208455)
	def synapse0x1ca60c90(self):
		return (self.neuron0x1ca5bbe0()*-0.629453)
	def synapse0x1ca60cd0(self):
		return (self.neuron0x1ca5c010()*0.678428)
	def synapse0x1ca60d10(self):
		return (self.neuron0x1ca5c4d0()*-0.850422)
	def synapse0x1ca60d50(self):
		return (self.neuron0x1ca5ca60()*0.0511772)
	def synapse0x1ca60d90(self):
		return (self.neuron0x1ca5cee0()*-0.273791)
	def synapse0x1ca60dd0(self):
		return (self.neuron0x1ca5d3a0()*-0.185488)
	def synapse0x1ca60e10(self):
		return (self.neuron0x1ca5d9b0()*-0.231436)
	def synapse0x1ca60e50(self):
		return (self.neuron0x1ca5dc40()*1.18615)
	def synapse0x1ca60e90(self):
		return (self.neuron0x1ca5e100()*-0.414598)
	def synapse0x1ca60ed0(self):
		return (self.neuron0x1ca5e5c0()*-0.079186)
	def synapse0x1ca60f10(self):
		return (self.neuron0x1ca5ea80()*0.207305)
	def synapse0x1ca60f50(self):
		return (self.neuron0x1ca5d7e0()*-0.454743)
	def synapse0x1ca612d0(self):
		return (self.neuron0x1ca5bbe0()*0.115397)
	def synapse0x1ca61310(self):
		return (self.neuron0x1ca5c010()*0.164871)
	def synapse0x1ca61350(self):
		return (self.neuron0x1ca5c4d0()*0.258162)
	def synapse0x1ca61390(self):
		return (self.neuron0x1ca5ca60()*0.230612)
	def synapse0x1ca613d0(self):
		return (self.neuron0x1ca5cee0()*0.619123)
	def synapse0x1ca61410(self):
		return (self.neuron0x1ca5d3a0()*-0.632136)
	def synapse0x1ca61450(self):
		return (self.neuron0x1ca5d9b0()*-0.311799)
	def synapse0x1ca61490(self):
		return (self.neuron0x1ca5dc40()*0.0558619)
	def synapse0x1ca614d0(self):
		return (self.neuron0x1ca5e100()*0.432654)
	def synapse0x1ca5ef90(self):
		return (self.neuron0x1ca5e5c0()*-0.332534)
	def synapse0x1ca5efd0(self):
		return (self.neuron0x1ca5ea80()*-0.0443237)
	def synapse0x1ca5f010(self):
		return (self.neuron0x1ca5d7e0()*0.349896)
	def synapse0x1ca61d20(self):
		return (self.neuron0x1ca5bbe0()*0.861959)
	def synapse0x1ca61d60(self):
		return (self.neuron0x1ca5c010()*-0.159767)
	def synapse0x1ca61da0(self):
		return (self.neuron0x1ca5c4d0()*0.244556)
	def synapse0x1ca61de0(self):
		return (self.neuron0x1ca5ca60()*-0.106722)
	def synapse0x1ca61e20(self):
		return (self.neuron0x1ca5cee0()*0.341346)
	def synapse0x1ca61e60(self):
		return (self.neuron0x1ca5d3a0()*0.377302)
	def synapse0x1ca61ea0(self):
		return (self.neuron0x1ca5d9b0()*0.375653)
	def synapse0x1ca61ee0(self):
		return (self.neuron0x1ca5dc40()*-1.59955)
	def synapse0x1ca61f20(self):
		return (self.neuron0x1ca5e100()*0.98465)
	def synapse0x1ca61f60(self):
		return (self.neuron0x1ca5e5c0()*-0.538036)
	def synapse0x1ca61fa0(self):
		return (self.neuron0x1ca5ea80()*-0.70508)
	def synapse0x1ca61fe0(self):
		return (self.neuron0x1ca5d7e0()*-0.378267)
	def synapse0x1ca62360(self):
		return (self.neuron0x1ca5bbe0()*0.0145672)
	def synapse0x1ca623a0(self):
		return (self.neuron0x1ca5c010()*0.541401)
	def synapse0x1ca623e0(self):
		return (self.neuron0x1ca5c4d0()*0.424618)
	def synapse0x1ca62420(self):
		return (self.neuron0x1ca5ca60()*0.297554)
	def synapse0x1ca62460(self):
		return (self.neuron0x1ca5cee0()*0.358224)
	def synapse0x1ca624a0(self):
		return (self.neuron0x1ca5d3a0()*0.0685963)
	def synapse0x1ca624e0(self):
		return (self.neuron0x1ca5d9b0()*-0.135476)
	def synapse0x1ca62520(self):
		return (self.neuron0x1ca5dc40()*0.3224)
	def synapse0x1ca62560(self):
		return (self.neuron0x1ca5e100()*-0.101328)
	def synapse0x1ca625a0(self):
		return (self.neuron0x1ca5e5c0()*-0.467139)
	def synapse0x1ca625e0(self):
		return (self.neuron0x1ca5ea80()*0.559314)
	def synapse0x1ca62620(self):
		return (self.neuron0x1ca5d7e0()*-0.0820615)
	def synapse0x1ca629a0(self):
		return (self.neuron0x1ca5bbe0()*-0.118865)
	def synapse0x1ca629e0(self):
		return (self.neuron0x1ca5c010()*0.152673)
	def synapse0x1ca62a20(self):
		return (self.neuron0x1ca5c4d0()*0.396076)
	def synapse0x1ca62a60(self):
		return (self.neuron0x1ca5ca60()*-0.826773)
	def synapse0x1ca62aa0(self):
		return (self.neuron0x1ca5cee0()*0.529868)
	def synapse0x1ca62ae0(self):
		return (self.neuron0x1ca5d3a0()*-0.226547)
	def synapse0x1ca62b20(self):
		return (self.neuron0x1ca5d9b0()*-0.570651)
	def synapse0x1ca62b60(self):
		return (self.neuron0x1ca5dc40()*-0.200784)
	def synapse0x1ca62ba0(self):
		return (self.neuron0x1ca5e100()*0.0258732)
	def synapse0x1ca62be0(self):
		return (self.neuron0x1ca5e5c0()*-0.571443)
	def synapse0x1ca62c20(self):
		return (self.neuron0x1ca5ea80()*0.0347524)
	def synapse0x1ca62c60(self):
		return (self.neuron0x1ca5d7e0()*0.432986)
	def synapse0x1ca62fe0(self):
		return (self.neuron0x1ca5bbe0()*-0.551628)
	def synapse0x1ca63020(self):
		return (self.neuron0x1ca5c010()*1.60361)
	def synapse0x1ca63060(self):
		return (self.neuron0x1ca5c4d0()*-1.14716)
	def synapse0x1ca630a0(self):
		return (self.neuron0x1ca5ca60()*0.957502)
	def synapse0x1ca630e0(self):
		return (self.neuron0x1ca5cee0()*0.0991849)
	def synapse0x1ca63120(self):
		return (self.neuron0x1ca5d3a0()*-1.31208)
	def synapse0x1ca63160(self):
		return (self.neuron0x1ca5d9b0()*-1.326)
	def synapse0x1ca631a0(self):
		return (self.neuron0x1ca5dc40()*1.45022)
	def synapse0x1ca631e0(self):
		return (self.neuron0x1ca5e100()*-0.17163)
	def synapse0x1ca63220(self):
		return (self.neuron0x1ca5e5c0()*-2.04288)
	def synapse0x1ca63260(self):
		return (self.neuron0x1ca5ea80()*2.09757)
	def synapse0x1ca632a0(self):
		return (self.neuron0x1ca5d7e0()*-0.934316)
	def synapse0x1ca63620(self):
		return (self.neuron0x1ca5f690()*-0.210126)
	def synapse0x1ca63660(self):
		return (self.neuron0x1ca5fcd0()*0.114146)
	def synapse0x1ca636a0(self):
		return (self.neuron0x1ca60310()*-0.453747)
	def synapse0x1ca636e0(self):
		return (self.neuron0x1ca60950()*0.385174)
	def synapse0x1ca63720(self):
		return (self.neuron0x1ca60f90()*-0.503646)
	def synapse0x1ca63760(self):
		return (self.neuron0x1ca5f050()*-0.477515)
	def synapse0x1ca637a0(self):
		return (self.neuron0x1ca62020()*0.260288)
	def synapse0x1ca637e0(self):
		return (self.neuron0x1ca62660()*-0.179993)
	def synapse0x1ca63820(self):
		return (self.neuron0x1ca62ca0()*1.2239)
	def synapse0x1ca63ba0(self):
		return (self.neuron0x1ca5f690()*-0.554097)
	def synapse0x1ca63be0(self):
		return (self.neuron0x1ca5fcd0()*-0.517609)
	def synapse0x1ca63c20(self):
		return (self.neuron0x1ca60310()*-0.389608)
	def synapse0x1ca63c60(self):
		return (self.neuron0x1ca60950()*0.210168)
	def synapse0x1ca63ca0(self):
		return (self.neuron0x1ca60f90()*0.127572)
	def synapse0x1ca63ce0(self):
		return (self.neuron0x1ca5f050()*-0.299713)
	def synapse0x1ca63d20(self):
		return (self.neuron0x1ca62020()*-0.274208)
	def synapse0x1ca63d60(self):
		return (self.neuron0x1ca62660()*0.0707227)
	def synapse0x1ca63da0(self):
		return (self.neuron0x1ca62ca0()*0.657427)
	def synapse0x1ca64120(self):
		return (self.neuron0x1ca5f690()*-0.502835)
	def synapse0x1ca64160(self):
		return (self.neuron0x1ca5fcd0()*1.4006)
	def synapse0x1ca641a0(self):
		return (self.neuron0x1ca60310()*0.772327)
	def synapse0x1ca641e0(self):
		return (self.neuron0x1ca60950()*-1.81985)
	def synapse0x1ca64220(self):
		return (self.neuron0x1ca60f90()*0.218056)
	def synapse0x1ca64260(self):
		return (self.neuron0x1ca5f050()*1.76843)
	def synapse0x1ca642a0(self):
		return (self.neuron0x1ca62020()*-0.00238647)
	def synapse0x1ca642e0(self):
		return (self.neuron0x1ca62660()*-0.0835135)
	def synapse0x1ca64320(self):
		return (self.neuron0x1ca62ca0()*-4.54038)
	def synapse0x1ca646a0(self):
		return (self.neuron0x1ca5f690()*0.217003)
	def synapse0x1ca646e0(self):
		return (self.neuron0x1ca5fcd0()*-0.406905)
	def synapse0x1ca64720(self):
		return (self.neuron0x1ca60310()*0.154373)
	def synapse0x1ca64760(self):
		return (self.neuron0x1ca60950()*1.01441)
	def synapse0x1ca647a0(self):
		return (self.neuron0x1ca60f90()*0.283446)
	def synapse0x1ca647e0(self):
		return (self.neuron0x1ca5f050()*-0.826947)
	def synapse0x1ca64820(self):
		return (self.neuron0x1ca62020()*0.500192)
	def synapse0x1ca64860(self):
		return (self.neuron0x1ca62660()*-0.373014)
	def synapse0x1ca648a0(self):
		return (self.neuron0x1ca62ca0()*1.03667)
	def synapse0x1ca64c20(self):
		return (self.neuron0x1ca5f690()*1.03897)
	def synapse0x1ca64c60(self):
		return (self.neuron0x1ca5fcd0()*0.530599)
	def synapse0x1ca64ca0(self):
		return (self.neuron0x1ca60310()*0.181898)
	def synapse0x1ca64ce0(self):
		return (self.neuron0x1ca60950()*0.498963)
	def synapse0x1ca64d20(self):
		return (self.neuron0x1ca60f90()*0.0910804)
	def synapse0x1ca64d60(self):
		return (self.neuron0x1ca5f050()*0.233226)
	def synapse0x1ca64da0(self):
		return (self.neuron0x1ca62020()*0.895023)
	def synapse0x1ca64de0(self):
		return (self.neuron0x1ca62660()*0.104448)
	def synapse0x1ca64e20(self):
		return (self.neuron0x1ca62ca0()*0.146414)
	def synapse0x1ca5edc0(self):
		return (self.neuron0x1ca5f690()*-0.776394)
	def synapse0x1ca5ee00(self):
		return (self.neuron0x1ca5fcd0()*-1.23798)
	def synapse0x1ca5ee40(self):
		return (self.neuron0x1ca60310()*-1.18905)
	def synapse0x1ca5ee80(self):
		return (self.neuron0x1ca60950()*-1.08688)
	def synapse0x1ca653b0(self):
		return (self.neuron0x1ca60f90()*-0.262002)
	def synapse0x1ca653f0(self):
		return (self.neuron0x1ca5f050()*0.0941113)
	def synapse0x1ca65430(self):
		return (self.neuron0x1ca62020()*-0.103659)
	def synapse0x1ca65470(self):
		return (self.neuron0x1ca62660()*0.410103)
	def synapse0x1ca654b0(self):
		return (self.neuron0x1ca62ca0()*1.55839)
	def synapse0x1ca65830(self):
		return (self.neuron0x1ca632e0()*1.7456)
	def synapse0x1ca65870(self):
		return (self.neuron0x1ca63860()*1.0944)
	def synapse0x1ca658b0(self):
		return (self.neuron0x1ca63de0()*-3.81127)
	def synapse0x1ca658f0(self):
		return (self.neuron0x1ca64360()*0.675101)
	def synapse0x1ca65930(self):
		return (self.neuron0x1ca648e0()*-0.435656)
	def synapse0x1ca65970(self):
		return (self.neuron0x1ca64e60()*1.16258)
	def synapse0x1ca65cf0(self):
		return (self.neuron0x1ca632e0()*0.0115586)
	def synapse0x1ca65d30(self):
		return (self.neuron0x1ca63860()*-1.83135)
	def synapse0x1ca65d70(self):
		return (self.neuron0x1ca63de0()*2.86874)
	def synapse0x1ca65db0(self):
		return (self.neuron0x1ca64360()*-1.39902)
	def synapse0x1ca65df0(self):
		return (self.neuron0x1ca648e0()*1.12897)
	def synapse0x1ca65e30(self):
		return (self.neuron0x1ca64e60()*-2.73726)
	def synapse0x1ca661b0(self):
		return (self.neuron0x1ca632e0()*-0.422741)
	def synapse0x1ca661f0(self):
		return (self.neuron0x1ca63860()*-0.202768)
	def synapse0x1ca66230(self):
		return (self.neuron0x1ca63de0()*2.36101)
	def synapse0x1ca66270(self):
		return (self.neuron0x1ca64360()*-0.0427773)
	def synapse0x1ca662b0(self):
		return (self.neuron0x1ca648e0()*-0.252003)
	def synapse0x1ca662f0(self):
		return (self.neuron0x1ca64e60()*-0.252152)
	def synapse0x1ca66550(self):
		return (self.neuron0x1ca654f0()*4.69306)
	def synapse0x1ca66590(self):
		return (self.neuron0x1ca659b0()*-2.89429)
	def synapse0x1ca665d0(self):
		return (self.neuron0x1ca65e70()*-2.26607)

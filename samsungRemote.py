from samsungtv import SamsungTV

tv = SamsungTV('192.168.0.18')
#tv.power() # toggle powerfrom 

#print(dir(SamsungTV))
tv.guide()
tv.channel_list()

import wx
from cStringIO import StringIO

class AvoplotArtProvider(wx.ArtProvider):
    def __init__(self):
        wx.ArtProvider.__init__(self)

    def CreateBitmap(self, artid, client, size):
        bmp = wx.NullBitmap
        
        if size.width == -1:
            sizerq = wx.ArtProvider.GetSizeHint(client)
            
            if sizerq.width == -1:
                sizerq = wx.Size(64,64)
        
        else:
            sizerq = size.width

        pngfile = pngfiles.get(artid, {}).get(sizerq.width, None)
       
        if pngfile:
            bmp = makeBitmap(pngfile)

        return bmp



def makeBitmap(data):
    stream = StringIO(data)
    return wx.BitmapFromImage(wx.ImageFromStream(stream))

pngfiles = { 
            "AvoPlot": { \
                         16: '\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x10\x00\x00\x00\x10\x08\x06\x00\x00\x00\x1f\xf3\xffa\x00\x00\x01\x1cIDATx\x9c\x9d\xd2=J\x04A\x10\xc5\xf1_\xaf\x1f\x91\x83\x88\x1f\x91\x99\xb2\x06"\x88\x81\x81\x81\x070\xf2$\xde\xc3[x\x06A12\xd2\xc0\xc8\xc0\x15\xc1\x03h \x8a0\x8a\xa2\x0be03;3\xb8\xab\xb0\x0f\x8a~\x14\xd5\xff.\xe8G\xa10\xa6:\xe3^\xac4\xd9\xc6ea\xbd\xf4\xb3\xdf\\|\xa6\xff\x00\xd5@\xd8\xc8\n\xb7\xfaF7X\xc2\x14\x0e2\xe4#A\xed\r6s\xb6\xd1U\x00\xa6q\x95\xf3,\xec\x19\n\xa9\x01\xcb\x1fl)j\r\xf3e\xbf\x8fG\x9c\x0e\x87\xd4\x80\x95>+\x8aZ\xa8\x07\x02)\xf0A\x10\xc9\xf0M\x82,\\\n_\x02\x11\x8dBxj\xf7\xca~\xf3\x1b\xf3$\xe1d(],\x92\x8e\x7f\xf5\xa39\xc3\x99\xf0R\xbe\xd8|\xbd\xf2\x9d\x18\x9c\x03\xdf\x02\xec\n\xd7\xf5\xa5jpDM\xeaD\xa4\x06\xa0\xf0GB\x17;\x8d]\xcf\xd1\xc3e\xa27\xc3m\x9d\x8b\xdf\x00Y8\xcc\xeb\x1c\xbc\xe1\x01\xbd\xc4\xfd\x0c7^\xc9\xe7\xfe\x00\x94\x90\xfd\xf7\x120\xc1\xe34\xfdN\x91\x89\xbbv*G\x00\x1a\xa0\x81F\xc7\xb9\x02\x8c\xa5\x1f\xb3A\x86]\xdb@\xe4\xc6\x00\x00\x00\x00IEND\xaeB`\x82',
                         24: '\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x16\x00\x00\x00\x16\x08\x06\x00\x00\x00\xc4\xb4l;\x00\x00\x01\xcaIDATx\x9c\xdd\xd4\xcfjSA\x14\xc7\xf1\xcf\xbdmib\xbc\xa5\xad\x82DDmue\xe9\xc2\x97p\xa1\x08\xee\x04W>\x83\x08>\x81;\x1f\xc1\xb5k7\xfe\xd9\xba\x14\x04\x91\x16q\x13\xc5M\x17\xa2E\x08i\x8aIs\\dB\x92{\x13\xad\xae\xc4\x03\x87\x99\xb9\xf7\x9c\xef\xfc\xe6\xcf\x19\xfe\x13+\xbeR\xc4\xd0\xff\xce\xb2\x12\xb0o\xcb\x82<\rO\x1c\xb1\xde\xe3E\r\xed\xac\x9c||\xf0vRx\xb2\xc7\xc6!M\xacb\x19\x81\x07\x8d\x1ft\x96\xff\x10\xdc\x08\xdb9\xa7\x0f\xd9\xeaq\x11g\x13\xb8\x9e\xc0\x1d\xdc,\x8e\xa5~q\xdc\xcd)zC\xe8\x15l\xaa*\xee\xe2M\x9b]\xe1ny\x1b\xe7\x82\xb1y\xc8F\x82n$pQ\xcaXE\r\xcf\x84\x1b\xf3\xe1\x13\xe0v\xa6)4\x13\xb0\x89\x95Rt`-\xf5\xbb\x04\x91U.\xc0\xd0\xf2\xa9\xd1\x1aN\xa5ve\xcc\x1a\xb5\x91\r\xddjrP\x0c&\xe6\x8dH)\xd3\xe0~Zf\xbd*t\xca\xb2aL\xf6\x98H\x07\x19\x13aQ\xdd\xc0b\xe0\x95\xf0e(PR0\xcf\xbd\x14\x9fk\xb3\xffM+>\x7f9\xd75<\xfd\tq#\x1f\xd9\xedQ\xe7z\xb8p\x7f"6\x8f\xe5\x8c\xec\xdb\xb9K3\xf6\xfd\x89\xf0N\xb83V-\x8fi\'\xbc\x9e\xf1}\xfc\x7f\x96\x15\xe1\xb9\xf0\xa1\x04.O \xc2C\xe1V>\x13\xbeX\x05\xb73\x9f\xd2A\xbc\xc5U\x0c\xd2\xcaF\xedS\xb4\xf0\x1e\x1f\xeb\x0cV\x94\xabq\xce\x05o\x84G\x1d\xce`\xdd\xb8\xf2:\xf8\x8e\xbd\x04\xde\xadq\xb0\xc4N\xb5\xc4\x7fQ\x96\x8dp\xafS-\xe9}\xece\xb4\xea\x1c-\xb0\xa3\xa2\xf67`(\xc2\xb5\xee\x04x\x81\xfdE\xfa\xe92\x1d\xa05\xfbA:\xe6\x1b[\x84\xed\x89\xe1\x0eX\xa2\xdd\x9f\x97\x91\x99QX\xff\xb4\xfd\x04\x19\xa6\xcc\xf2|g\x0b\xdd\x00\x00\x00\x00IEND\xaeB`\x82',
                         64: '\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00@\x00\x00\x00@\x08\x06\x00\x00\x00\xaaiq\xde\x00\x00\t,IDATx\x9c\xed\x9bm\xa8\x1dG\x19\xc7\x7f\xb3\xe7\x9es\xcf\xbd{\xf6\xf6\xe6\xa5*\x12\xbd\xd6\xd6\xc4\x944&\xa0\xd4~\xb2\x82\xafi\x91Z\xd1\x0f\xb5\x05\xb5\xfa\xa1\x82\t*B\xf0\x83XA1`\xc5\x98\x1a\xbfD-\xbe\x10PTLQ\x8bB\xa0\xda*\x8d\xad\xa6\x8d%\xa1-\xdeTcJ\xd5\xd4\x9b\xbb\xf7\xfd\x9c\xb3\xe3\x87g\xe6\xec\x9c=\xfbv^\x92+\xa4\x7f\x98\xbb{fg\x9f\x99\xff\x7f\x9eyvvv.\xf4B\x9btE\xc0[\xef\x06\xac7^\x16`\xbd\x1b\xb0\xdexY\x80\xa1\xee\x9e\xd9\r\x04\r\x08\x1e\x87\xe0Q\x08>\r\xc15\xa3i\xda\xfa\xa1\xe4S 8\x0f\x81\xceI\x11\x04O0\xb3\xebR\xb7w(\xa8\x94<\x9ds\r!\x07l\x06^I\xbe\x0f=\x0b\xac\x98\xf3\x99k\x15\xcf\x9f\x1c\xa0\x89\x97\x16}\x08`\x88{\xc0v\x8a\x07\xcfX\x04U\r\xb5\x08\x1e\xa9Z\xbb\xef\x86\xf0\xb7C\xb4w\xe4(!@\xf0k\xe0=\\\r\xbc\xaa\xc0\xdax\x1b&#\xa8\x19\xe2U-BT4T\x80\xa3\rS0\xcc\xf0\xae\xcb\x8f\x02\x01\xfc\xfb\xc0\xfb\x0c7\xe4X\x88\x80\x8964\xda0\x1e\xc9\xf9\xb8\x16\x11\xaa\xc0\x18B^!^\xf3\xbd:,VA\xbc\xe17#\xe42\x10\n\x04\x08"n\xc8\x88\x05Q\x04\xbe\x86\xc9\xb6\xa4\x86!>\x01\xd4\x80q\x84|\x95n\x01@D\xfbb \'\xaf}\x83\xe2\xef\'G\xc7\xa8O\x14\t\xa03{\xbf\xd1\x84\xa96L\xb6\x8c\x10\x08\xf9:"@\r!o\x05H\xc6\x8c6\xf0\xa5q\xf8o\r`\x12\xc2\xe5!\xb9\x0c\x84\x1c\x01\x82_\xb2\x81[\xd8\x92\xb8Zi\xc3tSz|*\x82\x06B\xdcG\xc8\xdb\xe4z\x80"\x16!2v\xda&\xb5\x80\x8f\x1bo\x98\xd9\xaax\xfe/#\xa4W\x8c<\x01`\'\xdd3\x82J[z}C\xd3<\xe6\x11\x01&\x9dd\xc9\xd7\x10\x01l\x0c\xf0\x9c\xda4\xdd\x024\x81;|S\xe8\xf2\x06\xc8|\x01\\\xf7\xaf\x18\xe2W\xb5`Z\x0b\xf1)b\x0f\x08\x10\xe2n\x0cH\x0b\x82 ^\xd06\xc7&"\xc2\x1a\xf0\x04po\x00\xb0\r\xc2gF\xc62\x07%\x05\x88`\xba\x05\x1b\x9b\xe2\xf6\xd3r\x99\xab\x88{\xbeA,@\x9dx\xfc\x17y\x80+\xc0\xaaT\xc5\x1e\x1f\xe0\xbb\xb0x\xf7\xc8\x98f\xa0\x9c\x00\x8d&lh\xc1\xc6\x96\xf4\xfa4r\x0c\x90\xb1\xef\xd3\x1b\x04\xeb\x94\x1b\x02\xae\x00\xcb\x88\x08\x1ax\xa7\x0fp;,\xfe|Td\xd3P,@\xad\r\x9b\x9b\xe2\x01\x9b\xb4\xf4\xfa\xb4\\\xee\x89\x01\x13\xc4C\xc0\xc6\x00\xeb\x05*QCd\xd2\x1a"\x82\xf5\x80U`\tX\x04\xf6\x04\xc8\xd5\xb06*\xc2I\x14\xbf\r\xdag|C\xf7\x06\xbcF\xc6\xf9$\xe2\x15\rb\xef\xb0\xbf\x1b\x05\xf9\xae\xbd\x87B\x80*\xf8\xf7\x8e\x84m\n\xf2=\xe0\xc66l\\\x83W\xb4\xa4\xd77I6\xd3\x88\'\x04t\x93\x1f7Gw\x1eP$q\x8b\xee\x18\xb0\x82x\xc0\x12\xb0`\xd2\x9e\x00\x88\x96aqr0\x9a\xd9\xc8o\xde\xa4\x99\xdb\xbb\xcfw\xf7qWw\xce\'\xe8\x1e\x06\xa7\x81\xeb\x80\r\xc0\x9b\x80\xa73\xea\x18s\xee\xaf;\xf7\xbb\xb6\x8e\x85\x807\x01\xfe\xad\x03\xf2\xccD\x8e\x00\x11\xd4\x8d\x006\xd0\xf9N\xe3\x92\xc1\xcf=V\x81\xdd\xc0,0\x07<\x05\xec@\xfcM\x017\xa6TWu\xec\xb9\xb6\xacw\xfd,\x04\xbc\x07W\xe0\x17C\xf0\xedA\x8e\x00\xdeC\xbc\xa0\xc4\xadm\xaa\x11\xf7\x94\xcdsg~u2W\x11\xbap\xc2\x94\xdb\x9b\xd2\x1a\xd7v"iB\xc6\xe1}%\xb9\x95B\x8e\x00\xe1{9Y\xef%\xeb6j\x82n\x11*\xe5*\xedL.\x0f\x81N\nfEp\x85\xb6\xbf;\xf0#F\x84\xe2\xa7@-\'\x8d9\xe7o\xee\xbf\xf2\x8e\x10\np\xe7}\xf6\xd1i\x03\xa9=vPQ\xf2\x066\x1c4\xe8"\x01t\xc7\xf5\xf3\xc8W\x81\x8cw\x98\xacV\xf6\xe4o\x03~\xe5\xfcN\x92wg\x02\x87\xe7\xb1}\xa7A\xeb\x8cj\xdc\xfc\xac2E\x02(\x1eV\xe2\xda\x15\xe2Y]\x85\xf85\xb7\x02|\xa3\xc0\x8a\xc1.\xf2\x05\xd1\xb78\x19\xb6.{t\x05\xa8\x00\x9f\x0fSI%\xf3\xb2\x88[\x14\tp\'\x7fht7d\x8c\xde\xc6}6\xfdf\x9d8/\xf5\xa2\xeb\xc6\x04Gd\xbd\xdb\xc9\xaf\x81\xfeJ\x19c\x9d\xba\xb59~$y\xad@\x80\xf0G@<\x97\xb7\xf3y\x9b<\x12c\xb3\xab\xd2\xd4\xf32\xe8\x04F\x05\xfajz\x82\xab\xfeh\x9f\x06cLi8\xe2f\x94\xfb0\x92$\xed\x8aq$\xfb\x96\xb4\xf3"t\xc4\xfav\xdc:]\xf2S\x8b\x86\xdb\xcd1K\xf3\x83\xc0\xddn\xdc(#\xc0c\x1c%\xdb\xe4\xb3\xa5\x1a\x96\x8bO\xa5\xdd\xf3\xc9\xde\xbck\xbe\x06\xeaX\xae\xa9\x9f\x16\xb7\xa6\x1b%\x04\x08\xdf\xca\xef}\xd3*\xe2\xb7\xb8\xc8\xfc\xbe\xa9\xdf*{\xf1\xcd\x8c|\x9dx\x07<\xfb\x96\xe1\xebJ\xa2\xe4\xb7A/&mWr\xac\x18\xb7e\xdf\xd5\x8f\xeb\x97*k\xd7\x10\xfa\xc7>\xe0\x13\xc4+\x92\xc7\x01\x94\xa7\xfb\xf88\xfaGb\xf2m\'\xad\xe4\xdd\xd4\x9f\x08\x996\xfedN"\xe0\x03\xe9\x03*\xeb\xf1\xa7\xa4\t\xdfQpD\xc5\xe1t\x96>b\x00\xc0\x878\x1c\xc4\x0b\x986\xd9\xdfeH\x90.F2\xef\x8e\xb4\xb2\xbe\xf4\x16\xefJ\'\xaf\xbc8\xff\xc2\x96k\xbbMzZ+Y^qq@y\xf2\xac))@\xf8\x13@\xde\xd9[t\xbf\xc3\xb7\x80W\x97\xb3\x92\xd6\xe0\xae|\xe0\xa8\xfb\xfb\x01s\xd2J\x94;\x00\xea\xab\xa0n{{\xd2\xc4\xc1\xcd\xe7\x9f+|\xea*\'t\xf7\xb3?@wH\xdb\xc5\x0b{\xfe\xb7\xc2\n{\xce\x15F\x08O\xc7\xd7\x93\xc2\xdc\n\xea\x0c\xb2V\x984x\x118v\x9c\x13\xe3N\xb6\xa7\xf7\x01\xbc\xb4\xe5:e\x8a\xf5x\x03\xf0\xf5\xae\xac\xfc\xa6w\xe1&>\xec\xc7\xebv\xee\x1a^X\xe2nC\xb6\x87\xa4{\xdd-\x07\xb2\x96p\xbd\x86\xd9\xa0\xbb\xec~\r\x07\xa4\xcc\xfd\xe6\xc3\x8d".\xb3\xe9\xdcs\x00O\xb2}\xd6\xda\xd4\x86<\xca\xd3\xe7\\S}\xee\x0f\x084\xdf\x0f\xd3\x17E\x1f\x00\xbe\x90\xce\xad\x8b`YD\xc0_\x15\xec,y_4\x05\xde\xbc\xfd5I\xa4\x96-\xe9<\xf4\xb9E&\x92\x99\xdf*\xf1\x12\xf6\xb2I\x1f\xeb\xcfR!<b\xf2\xf6\xe1u\xa8\xf43e\tO?i\xce3&\xebq5\xfd\xb4\xca\xe3w\xbe,T\xdaEK\xbb\x84\xbd\x08\xfc\xbb?k]\x88r\xc8\x1d1\xd7\x16\x80\xfd\x19\xe5\xd4\xbc\xb5c\x0b\xec4\xbf[l\x9bU\x9d|9\x9e\xb1\xb7\xf5)@\xa8\xc1\x83\x7f\x10\xaf\xdc.!\x1e\xb0\x04\\\xc8\xb8-\xe9\xfe.\xd9H\xf5\x92?\xa1\xe0a\x93\xf7\xb9w\xc8\xf1>\x15\xd7\x07\xb0\'\xd1\xb1\xae\x89mg\xbb\r\x9e~\xbd\x1c\xdf8kE\xd8\x9ev\x9bE\xc1\x1e!\x00_\xf3\xad\xc5\xdeeq\xbb\x8a\xbb#\xfb\xce\x0e\xac(I\xf2g\x80\x17\xe8^\x16\x9fG\x02\xed\x1c\x12\xfd/x\xf0R\xd5|Z_\x81Su\x06\xfd\xa8:\xe069\x0f\xf6M\xc6\r\x0c\x9d\xe3<\xf0\xe7\x12&\xd2z\xfeq\xe0<\xb1\xdd\x05dh\xb9\xbf\x17\x14,T`\xc9L\xea\xa2\xba\x1cgv3\x08\xc6\x06\xba\x8bP\xd1\n4!\xf1\xa4\xa8\x89\xf4\xfe\x1a2=~\xd4X\xff\x01p\x7f\t\x93\xc7\x81\x17\x91\xc0\xbahl\xcc#\x9e0o\xd2\x9c\x82\x8bc0W\x85U#\x806\x7f\x07\xdcW0\xe0\x10\x00\xf0\xf7\x82w\x90/\x87\xbd\xdf\x06\x93ky\n\x11c\x15\xd8\x0f<fL\x1c\x02\xb6\x92\xfeeh\x19\xf1\xa8%\xc4\xed\xe7\x81\xb91\x11 t\xb6\x9c\x9c\x02\xe0\x1c\x84\xaf\xe9\x83w\x07C\x08\x00\xe0G\xbcnMqW3\xde!\x92\xf6q\xd4\xa3{U\xa7\xcc\xc7Q+\xc0\x02pQ\t\xe9\xb91X\xa8\xc6\x03W!\x1f]\x86\xd8T1\xe0\x10\xb0X\xf48\x1bh\xfe\xd3\x94^\\A\x08\x94\xdd aw\x88$?\x8f/\xe3\x8c\x7fC>\x1c\x93\xb1\xefF\xad\xa7\x00\t\x8d\x03cH\x0f\x00\x08\xf6Bt\x90{\x16{w\x88\xa4\xed\x12K\xdb#d_\xaa\xac\x00\x8b\x98\xf9\x85\'\xa4/V`\xb9\xda\x1b\xb2O\xc1\xb0[jF \x00\x80\xffA\xf0~\xcc\x9da\xfa\x06\t;\x04\x94c=)@\x13!\xbd\xaa`Y\xc1\x92\x07\x0b\xa6\xd7\xd3>_\xc8\xd8\xbf\x0b\xc2\x1f\x96og/F$\x00\x80\xbf\x02\xde8\xef_\x80\xba\xee\xdd$\x95\x16\x03\xec\x0e\x915\xa0\xa9`\xa5b\x82\xe0\x18,{q\xa4O\xe2<p\x01\r\xe1\xd0\xdb\xfdG(\x00\x80\x7f\x18\xbc{\xb8yMv\x8dv\xb6\xca\x92\xb1I\xca\x13\xe2-`\xcd\x10^Q\xd0\xca\xe1\xd5B>\xbd\x8fh7\xd9\x88\x05\x00\xf0O\x81\xb7\x83]\x91\xec\x1c\xadFf\x088\xd3a\x8d\x99\x08!\xc4\x9b\x05\xa4A\xca>\r\x10i\t\x0e\xa3\xc1%\x10\xc0\xc2\xec.\x9f\x02f\x88\x83\x9fE?\x14N\xd9\x93\xe8\x19f\xb6n\x1b\xe5f\xcaK(\x80E\x10w\xfdV\xcam\x9bQ\xc0?q_\xaeNCx\xfdh\xdaS\x0c\xcd\xa8\xffopf\x17\x10\xbc\xad\xe0?L\x12\xc9\x7fd\xa4m\xc8\xc0e\xf0\x80\x04fv#.\x1cl\x05n\x86h;xu\xe0_\xc0a\x08_\xbc$\xf5f\xc0}2_\x91\xb8\xe2\xffm.\r\xa3\x8f\x01\xff\xc7\xb8\xe2=\xe0e\x01\xd6\xbb\x01\xeb\x8d\xff\x01\xeeX\xf5nW\xd9w\x8d\x00\x00\x00\x00IEND\xaeB`\x82'\
                        },
            "grid": {\
                         16: '\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x10\x00\x00\x00\x10\x08\x06\x00\x00\x00\x1f\xf3\xffa\x00\x00\x00UIDATx\x9cc|\xf1\xe2\xc9\xffK\x97X\x19\xf4\xf4~3\xc0\x00)|&\x06\x06\x06\x06771\x06d@\x12\x7f\xf3\xe6W\xff\x19\x18\xfe\x93\x8dYLM\x7f10000\xbcx\xf1\x14n\xa8\x84\x844\xd1|&\x06\n\x01\xc5\x06\x8c\x86\x01\xc3h\x1800\x0c\x820\x00\x00\xb5\x19\xcb\x83fm\xd6\xc3\x00\x00\x00\x00IEND\xaeB`\x82',
                         24: '\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x16\x00\x00\x00\x16\x08\x06\x00\x00\x00\xc4\xb4l;\x00\x00\x00tIDATx\x9cc|\xf1\xe2\xc9\x7f\x06\x06\x06\x06\x0f\x0fQ\x86\x1d;^3 \x83K\x97X\x19~\xfedd05\xfd\x85"N\x8cZF\x98\xc1\x12\x12\xd2\x0c/^<EQ,!!\xcd\xc0\xc0\xc0\x80U\x9c\x90Z&\x06Z\x81\xcd\x9b_\xfdg`\xf8Ou\xcc\xc4\xce\xfe\x9f&\x0e\x1eza<\xf4\x0cf00\xf8I\x93T1\x1ay\xb47x4K\x8f\xa6\n,`\xc8ei\x00D<\x17 \x86:\xfa\xf0\x00\x00\x00\x00IEND\xaeB`\x82',
                         64: '\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00@\x00\x00\x00@\x08\x06\x00\x00\x00\xaaiq\xde\x00\x00\x01^IDATx\x9c\xed\x9b1j\xc30\x18F\x7f\x87v3\xb4t\nt\xd5\x01\xbch\xf3\x89r\x80d\xcb1r\x11m>F\xe6\x8c-8)\x14Z2TIA\x1d\xba\xb8\xc9$\x0c}(\xfe\x1eh1\xf9\xc5\xc7\x8bA\xd1\x07\xa9\xfa\xfe%\xd9\x80\xed\xf6\xde\x96\xcbG\xab\xebd\xab\xd5\xa7y\x7f\xb2\x1cJ\x9b\xbf\xbb|\xb0X<\xd9n\xf7\xfb8\xc6\x07\x0b\xe1-+@i\xf3\xd5\xe5\x1b0\x9f?\xff\xf9@\xdf\xbff\x05(m~\x96\xb5\xfb\r"\x01t\x00\x1a\t\xa0\x03\xe0\x84pH\xde\xc7d\x96&\xb5\x9c;\xa7\xae\xdb\'k\xdb/<\x0c\xb5\x9a&\xa6\xd9\xf1X\xd1/!F]\'\xb3\xae\xdb\'\xe7\xce\xf8\xb7\xf1\xdf\xcb\xfb\x98B8$\xfd\x12\xcc\xda\xfd\x06\x91\x00:\x00\x8d\x04\xd0\x01h$\x80\x0e@#\x01t\x00\x1a\t\xa0\x03\xe0\xa8\x0fP\x1f\xa0>@}\xc0\xd0Ji\xf7\xf9\xb1\xf3\x93?\x05$\x80\x0e@#\x01t\x00\x1a\t\xa0\x03\xd0H\x00\x1d\x80F\x02\xe8\x008\xea\x03\xd4\x07\xa8\x0fP\x1f0\xb4R\xda}~\xec\xfc\xe4O\x01\t\xa0\x03\xd0H\x00\x1d\x80F\x02\xe8\x004\x12@\x07\xa0\x91\x00:\x00\x8e\xfa\x00\xf5\x01\xea\x03\xd4\x07\x0c\xad\x94v\x9f\x1f;?\xf9S\xe0J\xc0\xf0\xdf\xd6\xce}goX\xda\xfc\x95\x80\xf5\xfa\xc3\xda6Z\xd3\x9cl\xb3y\xcf\x0eP\xda\xfc\x0f\xe4\x05\xd4\x8d\xd1\x19\xade\x00\x00\x00\x00IEND\xaeB`\x82'\
                         },
            "add": {\
                    16: '\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x10\x00\x00\x00\x10\x08\x06\x00\x00\x00\x1f\xf3\xffa\x00\x00\x01\x15IDATx\x9c\xc5\x92=N\xc40\x10F_~v\x13VH\xdb!DGGM\xc1E\xe0\x12(\xc7@\x1ca\x95\x1a\x89\x03p\x03\n\n\xa4\xf4{\x05\n:\x16%\xb1\xc7\xce\x86\xc6\x89\x9c\rQV4\x8c4\xc5x\xc6o\xbe\x19\x1b\xfe\xdb\x82\xa9\xc4\xc7\xd7S\xeb\xc7\x0f\xcf\x1b\xf2\xac\x18\xd5\xc7S\x80\xb65\xecT1\xab`\x12`\x1b\x8d\xb5\xf6\xef\x001\nm\xcc\xf1\x80\xfb\xcd\xcd`f\xb15\xe2\x01\xc20\x1a\xd5\xe4Y\x11\xf4Ky\xdd\xde\x0e\x92s\xb6^]q}\xf9\x18\xf4\nD\xe6\xe5\xfa\xa6\xe3\x1a\xf0F8f\xde\x01@\x0e\x00\xcb\xe8lP v\x87\xd8\xef>>M/\xf0\xbf\x8d\x92\n\xf8\xfd#E\xc0\xe2\xe5\xfd\xae\xae\xf4g\x7f\xf8\xb6U\xe4Y\x91\x00\x06\xe8\xf7\xe5?\xe3\x89\xf3\x04Hk]\xa2\xc7{9\x074\xa0\x80\x1a\x90\x0e\x90\xba\xcb\xab\xce\x95\xae\x10\xeb\x03B\x805Pz\xca\xdb\x0e`\x9d4q#\x84\x95.i\xf6> \xc1u\x16Wk\x00{\xb8\x83\x05\xb0t\x1e\xbb\xb6\x01\xb0\x07\x1a\xd7H\x9c7\x00?>\xcan,=\x9c\xae\xea\x00\x00\x00\x00IEND\xaeB`\x82',
                    24: '\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x18\x00\x00\x00\x18\x08\x06\x00\x00\x00\xe0w=\xf8\x00\x00\x01iIDATx\x9c\xedT1N\xc40\x10\x9c\xd8\xe68\xa1\x93\x80\x0e\xd1@KGu=\xbf\xb8/\x9c\xf8\x05\xbc!\xa2F\xe2\x07\xbc\x80\x0e\xa8\xef\x07H\x886  \xb1\xd7g\n\xec\xc48N\xb0\x0ct\x8c4J\xb4\xf2\xce\xecn6\x06\xfe\xf1\r\x8a\x94C\x8f\xd5\xa5\x89\xc5\xcf\xafJ\\\x9c\xde\x8fj\x88\xa42\x8cFU\xdf&\x1d\r\xc1\x92\xf4\xa1\xb3\xc4\x81\xc4\x0eHK\x10\xd1_\x1a((\x9d\xd7E\xa2A\xf3\xf3\x0e\x96\xe5<\xba)\x9f\x06\n\x14\xe9\x801>\x98\xe7\xb6\xab]\xb1e97\x8b\x93\x83\xac*Clo\x1d\xe1\xf8\xf0\xac\x00\x82\x11\x91\xce\x1bC\x08\xd2\xb2}\xffj@\xf9\xeb\xe8C\xd1\x90\xc1ou@M\xdc w\x15C\xc8\xa1\x11M\xc5^<\x81\x9e!\xe9\xa5\x17\x9fM\xf7\x11\xbb\xce\x94\xea\x0c\x92.\xbb\xeb\xbb\x85y\xad\x9fz\xf1\x9b\xd5[\xd6e\xc7m\xdc\x91+\x92\xd1\xff\xc0b\x17\x00yTC\x06\x1c\xc0\xc4r\xc3g\xa3\xde\xa1\x86\xff\xe4\x1d+\xea(=\xb6\x06\x1c\xc0\xa6\x15\x0f\x9f\x139\xde\xc1\xcc\x8a5V\x87\xa1\x1b\xbdt\x06.\xe8?\x99M\xe0R\xd5\x03+,\\q\xcc\xa3\x9f_8\x03\n\x0e\xb8\n\x0c\x00-U\x03\xbd\x8eu \x00\xa0\x0e\xc6\xe2FE\x00\x8c\xf0\x84\x1a\x00\x1a\xdd\x87\x92VA\xac\x1e\x98\x9dX\x14\x95\x97C\x9e\x89\x01\xc6\xd7\x94\x07,\x82\xf3k\x8f\xae\xb0\xde\xcd\xfa\x01\xe4\x1a\xa4\xc0Z\xc5\xe5\xf5\x00\x00\x00\x00IEND\xaeB`\x82',
                    64: '\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00@\x00\x00\x00@\x08\x06\x00\x00\x00\xaaiq\xde\x00\x00\x03\x88IDATx\x9c\xed[Kn\x13A\x10}\xd3c98R\x94=Kv\x1c\x80,\xb8\x00\x0b\x8b\x1b\xb0GQ\xce\xc0\x8a3D\xb9\x00\x17\x00\xc4\x15\x10p\x01\x10\x07 Rv\x01ap\x98\xaef1\xd3qOMO\xcfL\x7f\x9cX\xee\'Y\xe3r\xbb?US\xf5\xba\xba\xc6\x06222222\xf6\x16E\xca\xc1O\xcfOT\xac\xb1.\xce\xbe$Y\xeb,\xc5\xa0&^\xbd8\x0b\xea\xff\xfa\xcdy\xa4\x95\xd8!\x92\x8e\xbe\x03H\xee\x01@\x1d\x05\xd7\x7f>N\xeey\xbcx\x1a{1\x1d\xa47\x80\xa2\xbb\xe9;\x12\xc9\r\xa0\xe0\xafDH\xdf\xb1\xc8\x1c\x90~\x8a\x90\x9d0\xda.\xda\x8b\xe4\x06 \x92\xcdu\xba;\xeb\xbe)\x91\xde\x00*\xc0\x00*\xbd\x012\x07\xa4\x9e@\xdfyI\xd3\xe3\xd9\xc7k\xa6b{!\xe0\xb1\xa7o#\x04\xf6\x9e\x043\x07\xa4\x9e\x80TU_\xbdv\x81*\xf6r:\xd8\x82\x01\xa8\xb9z\x90\xe0]\x9e\x05b\x143\x84(\x839@\x882\xdazlE\x95\xcc\x01\xae\xc6\xd3\xe7\xcb\xe0\t~\xaf/\x01\x00\xd2\xc3\x03V\xebK\xbc\\>k\xa4\xb0\x8a\xd8\xc5\xfb\x0f\xd6\xcf\x9d\x06 \x92\xb8^}\r\x9a8\x04\xab\xf5\x15V\xeb\xab\xa01\x8e\x0f\x1f;\xdb\xdd\x06Pr+D\x94\x12C\xc9T\xe6\x00W#\x91\xdcJ>\x9e\x12C\xd9\xa4\xd3\x00\x92\xaa\x9d7\x80$w25\xe0\x01\x04\xf28\xc5\xdd\'\x0c\xdd\xc0\xcc\x01\xaeF\xa2j\xf7w\x81\xb0\x10\xd8{\x12$\xafJ\xce}\xc2P\x06\x9a9\xc0\xd5(\xd5\xees\x80\x1c\xa8)\xe4<\xc0\xd5H\x92p8\x7f\x18\xb4\x80\x9b\xeags\xfd5\xb9\xef|v\x84\xf9\xec\xa8\x91\xfcN\x83$3\x078\xe1\xf4\x80\xb7\x9f\xc2\x8e\xc2E!\xb0|\xf2\x08\x00@t=\xb9\x7f)\x16x\xf7\xf9;\x00@%\xe2\xa2^\x03\xc4\xf8M\xce\xe9\xf9\x89\xd2\x1c\xe2W\x12\xa3[\xc5\xef\xebo\x84\nl\xc2H0\xb9\x006$\xe4\xb3\x9b0\x02[\xa0~\\\xac\x07\xd2\xefMy22\x07L\xfc~\x89\xf6\x1d\x17\x0e\xb9\x006\xae\xefs\xaada\xc3=\x80\xd0\xf6\x00.\x8fz\xac4d\x80\x02\xb5\xd2@\xadX\xc9da\x91M\x83\xa0\x92\xff\xea\xd5xp\x80\xee\xdb`\x01\xbb\xc2\xb2G\x96L\xb6\xde\x01\x97\x01J\xb4\x15\xe6\xb2V^\x18\xed\xdc \x1b\x0e\xf00\x00\xe3\x80\x07\xe8*\xac\x95\x04\xba\n\xcb\xe6%\x98\xdcB\xe6\x00&\x9b.?\xe4\x01c<\xe4\xd6\xf5}\x1e\x8d\xb1\xb09\x80\xfd\x0ekY4\xef\xf5vY\x18/Sn\x85\x047\x80\x19\xc3\\\xa1\x19\xec\n\xcfz\xbe_\xd6JD\x0b\x819\xda.\xad\xd7\xeaR\x98Ca\xc3\x05\x12h\x1b@\xef\xe1\xc2!\xf3}\x9f\x93^\xc7\x00$\x03\x9e\x0e\xcb\x96\x01J\xd6\xac\x95\x11L\xd6\x13\xe9\xb5j\x85\xc9"\xab\xcc\x01\xa9\'\xa8\x022\xc1j\xe0(\x1b\x03\xa6\x01\xb4\xfb\xe8\xd8\x11\x16\x99\xbbX\xc1\xe4\xce6#\x9b\x9a\x9cOi\xad(Z\xc3q\xd2\xebK\x84\xf4D\xb6T\xb9\x93:s\x0f0\x15\xb6eR&\x89(&[31\x19\xc0\x01\x12\x15\x8c\x9d\xfa\x06\xee]`\x8cl\xae\x0f@\xce\x03:\x1e\xa0\x00T\xc6\xfb1w\\[\xd8\x9a\t\xb2tv\x12\xea\xbe\x07Z\\\xb3\xf9\xc6f\x82\\n\xc1E\x82\xdce$<\xce\x02\xdf~\xdc*\x10\x8a\xbf\xb0\xc7|\xd0Y`j\x91a\xeai\xb0S\x1f\xb0\\M\x98\x1e\xa6ebmQO\x83{\xcf\x01\xa1e\xa6\xa1\x8a\x90)\x9b\x9f\xb9\xa0\xd8\xb5\xcf\x03\xa2T\x84\x92\xfeo\x90\x8d\xcfC\xa1\x0f\xa6"\xd4\xf3y4\xfc\x07N?\x05\xe8\x9a\x00c:\x00\x00\x00\x00IEND\xaeB`\x82'
                    },
            "remove":{\
                      16: '\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x10\x00\x00\x00\x10\x08\x06\x00\x00\x00\x1f\xf3\xffa\x00\x00\x00vIDATx\x9c\xed\x90\xcb\n@`\x10\x85\xbf\xdf\xdd\xc6J\xf1\n\xca\x1a\xef\xe2\xf9\xbc\x0b\x8f\xa3(\xb7\xb0p\x89\xe5\xd8(9ujf\xea|3\r\xfcz_\xea(\x8a4[\xa4\xe1\xbc*\x95q4I\xe8\x89\xc2N\x14CUr\x02\x86\xa6\x17\x01\xf4\xba\x01x\x0e\xd0\xea\xf6\x06p4?\x10\x01\x86\xed\x02C]f\x16\xe0\x02\xf6n\x13\xd0\xd9\x1e=\x03\x130\x02=\xd0\xed\x9eD[?\xaa\x15Cr\x1a\x13\xe2`\x92\x93\x00\x00\x00\x00IEND\xaeB`\x82',
                      24: '\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x18\x00\x00\x00\x18\x08\x06\x00\x00\x00\xe0w=\xf8\x00\x00\x00\x9eIDATx\x9c\xed\x93A\n\xc20\x10E_l\xd4n\xdd)x\x02qo\xef\xe2\xf9z\x97\xf6B\xa51\x13\xebfRJ\xab+\x93]\x1e|\x12B\xf8\x8f\x81\x04\n\x85BvL\xdc\xb4\x8ffJY\xfc\xec;\x03`\x97\x87\xcd\xf5\x94\xa4\xbc\xbe\xdd\xa1\xef\xd8\x08d\xf4I\x042\xb8y\x9fE\x10\x86\xf1\x97@\x92\x08|\xee\t\xe4\xcb\x04\x16\xc0\x9e/)\x055\xe0\xe235\xc0\x018\xea\x1a\xb3\xd7\xd5jvz\x7f\x02\x02 \x80\xd7\xbcVq\x80\xcc\xff`\x81\xd1\xe2XZi\xccJ\x10%o\x15\x05-\x0e\x7f\x8d_(l\xf8\x00|\xce4\xfb\xd3\x1b!\xd4\x00\x00\x00\x00IEND\xaeB`\x82',
                      64: '\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00@\x00\x00\x00@\x08\x06\x00\x00\x00\xaaiq\xde\x00\x00\x01\x83IDATx\x9c\xed\x98MN\xc3@\x0c\x85\x9d\xb4B\x1c\xa2\'@\xeca\x0b[\x8e\xd0\xf3q\x04\xb6\xb0\x85}\xc5\x1d\x908\x00\xea\xccx\xd8\xe0b\x9c\xf9i\x81L\ty\x9f4j^\x9c&\xb6c;\xd2\x10\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00`.t9\xc3\xed\xc5el\xe9H\x0b\xd6O\x8f\x83x\xfbc8\xf2\x97X\x96\x8c\xd77W\xad\xfc\x18\x9d\xfb\xbb\x87\xe4\xf9b\x02\xd8yz{\xde\x8c\xe2P+N\xcf\xce\x8b\xf6J\x02\x02\xb1\x0f\xbf\xeaPk\xd8\x95\xfd\xc7\x0c(\x19\xd9yb\xcf\xad|\x19\x05v\xbehG\x02J\xc6\xe8\xfc\xe4g@\xac$\x003\xa0d\x0c\xff\xa0\x05\xc2\xcff@\x98|\x02j\x9f\xc1=\x86\xe0\xb4g@m\x08b\x06\x94\x8cs\xfc\x0cvD\xb4\xd8\xfdy\xeb\xa6\xdf\x02[\xa7\xe5\x92\x88$\xa0(\'\x04\t~w\x8e}\xa0\x93\xd5jd\x17\xc7\xc5\xbc@\x1do \xa2\x88\x19P2n^_Z\xf9q4\xec\x16\x91\x9e\x01\xd2\x0eZ/*\xbaOh\xa929\x96g\xa6\xb6\xe3\xe2\xc7""b\xb5D\x07\xfa\xeca\xabCE{\xa3c\xce\tA\x92!\x01\xd8\x80{cO\xe9N\xe9N\xad\xdc\xb3u\x02\xe4\x98\x95\xd6\t\t\x19m\x13\xa0\xed\x83}\xce\xd9\xcf\x80R\x05\xe4\xae\xb7\x15!\xf7\xe8\xe9k\xc9w4\xac\x80\xd4\xafFW\x80h66\xdd\x12\xac\xae\xb7o|\xaf]\xedC\x13p\xc8=S%\xafu\x0e\xdb\x029\r\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0-\xde\x01\x1cA\xa7\n\xdf\x988\xcf\x00\x00\x00\x00IEND\xaeB`\x82'
                      },
            "select_cols" : {16: '\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x10\x00\x00\x00\x10\x08\x06\x00\x00\x00\x1f\xf3\xffa\x00\x00\x00\x04gAMA\x00\x00\xd6\xd8\xd4OX2\x00\x00\x00\x19tEXtSoftware\x00Adobe ImageReadyq\xc9e<\x00\x00\x00\x18tEXtCopyright\x00Stella Schulze\xd4b}\xbe\x00\x00\x01TIDATx\xdab\xfc\xff\xff?\x03%\x00 \x80\x98\x18(\x04\x00\x01\xc4\xd21m\t\x86\x13\x9ed\xc7bU,3u1\x86\x18@\x00\xb1\xfc\xfb\xf7\x8f!%:\x10E\xb0?\x9b\x81\xa1=-\rE\xacr\xd6,\x86\xa4H\x7f\x14\xb19K\xd73\x00\x04\x10\xcb\xdf\xbf\x7f\x19>~\xfd\x81"\xc1\x0f"\x80\x1a\xd0\xc5\xd0\xd5\x81\xf4\x02\x04\x10\xcb? \xb1c\xcfa\x14\t. \x9e\x84\xe6T\x90\x18\xba:\x90^\x80\x00b\xf9\xf3\xe77\x83\xb7\x9b\x1d\x8a\xc46 \xce\x11\x12B\x11\x9b\xf2\xee\x1d\x83\x17\x9a\xba\xf9KV3\x00\x04\x10\xd8\x0bLLX"\x83\x9f\x1f\x95\x0f4\x00]\x1dH/@\x00\x81]\xb0u\xf7a\x0c\xfdS\xee\xdf\xc7\x10CW\x07\xd2\x0b\x10@@\x03\xfe0\x04z:\xa0H\xac\x03y\xc1\xd3\x13\xd5\xc0\xed\xdb1\xd4\xf5L\xbe\xc5\x00\x10@,\x7f~\xfff`\xc6\xe6\x0511\x0c!tu \xbd\x00\x01\x04\x0e\x835[\xf7aza\xe1B\x0c1tu \xbd\x00\x01\x04\x0e\x83\xd8`w\x14\x89Eq@/,X\x80j`B\x02\x86\xba\xd2\x0bg\x19\x00\x02\x08\x98\x0e\xfe1\xb0`\xf3\x82\x94\x14f\xb2ES\x07\xd2\x0b\x10@\x8c\x899\xe5\x18y\xc1hJ\'\xd6\xbcp.\xa7\x1cC\x0c \x80\x18\x81\xd8\x98\x92\xdc\x08\x10`\x004\xa2}\xc6\x01\x18\t\x10\x00\x00\x00\x00IEND\xaeB`\x82',
                             24: '\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x18\x00\x00\x00\x18\x08\x06\x00\x00\x00\xe0w=\xf8\x00\x00\x01WIDATx\x9c\xbdU=K\x03A\x10}9\xafJs\x90"E\xf0Wh/VJ\xb4\x90`%\x12\x89"ir\xad\x04\x7f\x81\n\x82\xa0\xab\xc5!\x98h\xac\x14\xadb\x04\xc5\xc6Z\xb1\xb6Ic}`!\x08\xb7\xb3gq\x82\x16;\x13R\xdcn;\xefc\xe6\xcd\xb2[H\xd3\x14y\x1e/Wu\x17\x06\xfe\xeeIO\xcc\xe8\xa3U\x1f)2y|\xc1\xd6\xf2\x9f\xc0\x18\x03\x00\xd8\\\xadY\x01\x07-`\xa7\xd9d\x05\xb6\xa3\x08\x1b+K\xd6\xda\xe9\xe5\xad\x83\t\x88\x08\x00\xf0\xf9\xf5m\x05\x04\x00\x10E\xac@ p\x89\x08\xbe\xf95\xb8\x7f|\xb6\x82\x8a\x00\x0e\x85\x0e\x8b\x02\xd7\x10\xc1\xd7:\x01\x00,\xce\xcdXAw\x00\xc2R\x895Pq\x8c\x05\x86{\xd6\xbbr\xb8\x03\xcf\x13\xbc\x82\x80\xaf\xc51\xcb\xa5\xff\x11\xf5\x1f\xec9\x02\x80\x1a\x0e\xc5.9\xae\xd6\x89\x83\x88\xb4\xd6\x00\x80Zu\xd6\n\xb8\x01\x10V\xab\xac\x80\x1a\x0cX\xee\xfe\xd1\xbb\x8b\t\x92l\x07\x13\xd2\x92\xcbeQ\x84\xe3\xea$\xf9\xbbE\xd7\xfd\'V@u\xbb\xa2\x01\xc7%"\'K\xce"\xaa/\xcf[\x01\xe7k@\xd8\xe9\xb0\x02\xaa\xd1`\xb9[o/\xf0\re\xcf\xb5/\xed\xa0R\x91\xbbd\xb8\x86L\xfe\x11\x15\xd6\xc3\xb6\xf8eN\xa9\xbd\x91"\xafa\x9b7\x000=v[c\x9c\x1fx\xf5}\xd6\xba\x14h\xa1\x00\x00\x00\x00IEND\xaeB`\x82'
                             }}


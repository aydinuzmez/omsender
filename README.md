
# what is the omsender

omsender is a Output Messenger sending. You can send message to anyone person on Blackmagic Fusion. actually, it just has been pulling filename from Loader and Saver where blackmagic fusion and then it sends message with API of that connect

# installation
 1. install [Output Messenger](http://www.outputmessenger.com/lan-messenger-downloads/)
 2. make a API ([Api-Helper](http://support.outputmessenger.com/output-messenger/api-helper/))
 3. of course, you must install Python. ([Python](https://www.python.org/downloads/))
 4. install package `pip install omsender` (but if you have a common harddisk. you should download the omsender and you can put to a harddisk)
 
## configuration

you go to output .py then you should see **IP**, **API_KEY**, **USER**, **TRANSFER**, **COMP_PATHMAP**, **PATH_PATHMAP**, You have to fill blank correcly.

## usage

    from omsender import omsender as om
    om.run()


# preview

![Press Hotkey on the Fusion](https://lh3.googleusercontent.com/ndaGKKsbCVtlUnVAYN8ksgDMur8SDjX_eqLNN4GipoJ9qsh-w5tytM4ZDdK3tqR0ZSwP8k-RKWPI83B7wL1Mx22MMjIeGhoN0MVlXFPCRBZ33eH3oVPiMIGyaMtBWVGer1OVq74bW8lrzM_VygIZRzJtM5Zn0x1dTWPus9rEs4du7yyHLCGJMrLNP1f26LD0gPw6uhW4bO_suBaXI52UYSMANMP6d9ZvgJ2Zuka04B5rq0Ov1SxD3nLFNEeNBT5w5T0UUOEoo6V7trd-MLRA1ai5-tA1ZxZbdVwlTDDUX78P984kqqmhnmreXdXOD4ab6-4vjpd6mkizLgaF-GN3ENqKdzXrdS1A075PdSoGOwCXuM8wjIhEj2Diulskt824ongF8lxvCUyuWLSdJkjK_HMzeELSV00HzCznC3LciHruPK23yUFx8jkkVUSug2p1SFij495NWMr4JSIeeX_Ca9sAbCEQyYnexKK5dNFvAH0TcT0w2-HrjSWp4EyXGiIbGvamTzm7lXyD2Gh_MeWfGYEJRS1xiKbFfqse9Kxi1Go0HLR_JURw5HKKKZhVwGSEJ6ht5fwTyid0NnCscV9JJBlNq8sBv0wtjjCwj4A=w424-h217-no)

![OMSENDER Photo](https://lh3.googleusercontent.com/10pBvPKv5Q81wH0gYcPqsmlRqavcGaJDynk_vCP7w9_sG75_UgFGN4avxkC4CtYVU_vhGx33xhJEoK_otBG57F5cEtcGZ3BIw6mMv2hbnk53af1iEVA9ZlMKN0xGb4-cDSRcx38h4Eim2rrSVYz-r3wL8L-n5bg5DDcpnoVttCJmrrvlxR6R_SIqXSCc12BhQP2MlVPNKnSAcs7GAwPgp1HghQ0uAjO-LYbdxbBWH_imqWTPJUkhJbm-vllv4eMKDKWaqQCc3mwA0yfnQIKhUQxJomk9ddWD0x4OgX-dRmdxyIrBVwifm19o0RZHJwoLy72T6ushGhTzhJjYV4DcDStxMX8aEIwFoCz-GL5Buqx8j9yYp876vThNtDRRVTTWhbUny3y3Ds9t3HaXkb83glewree3lXgSeBnfSAu8SbRIjnlR1G5EwQOWKYGONUVVjYRypIOAHIJpFz1y7Pe8h6vR2emTm3cxjdZQ9Bw6MdFRoZrv25RRtDar7CqYJqkm_7UbQg8twZ60-ceXMKeVRyLLtSVdQ_xVJKxG7DXOav54Sj7McC-QQCrcN8cdixkyKqTLEiz__pLKcS7cRvF_Kd_-s1RXkHkGidFnGX4=w450-h399-no)
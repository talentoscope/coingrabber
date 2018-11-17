import os.path
import lxml.html
import requests
import time
import re
import pandas as pd
import matplotlib.pyplot as plt
from selenium import webdriver
driver = webdriver.Chrome()
df = pd.DataFrame(columns=['time','amount'])
df.loc[0] = [0,0]
counter = 0
plt.switch_backend("TkAgg")
plt.ion()
plt.show()

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

scrivwallet = ""
rvnwallet = ""
btcwallet = ""
ginwallet = ""
luxwallet = ""
grvwallet = ""
hthwallet = ""
dgbwallet = ""
vtcwallet = ""
xshwallet = ""
xmnwallet = ""
manowallet = ""
xdnawallet = ""
bcdwallet = ""
gbxwallet = ""
suqawallet = ""
xvgwallet = ""
gtmwallet = ""
argwallet = ""
crswallet = ""
ifxwallet = ""
monawallet = ""
abswallet = ""
resqwallet = ""
linxwallet = ""
eliwallet = ""
tlmwallet = ""
glynowallet = ""
mctwallet = ""
privwallet = ""
mdexwallet = ""
gxxwallet = ""
ultrawallet = ""
almnwallet = ""
toscwallet = ""
mngwallet = ""


while True:
	print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
	print("Coin          Balance          Amount($)")
	print("====          =======          =========")
	try:
		#SCRIV
		scrivexplorer = "https://explorer.scriv.network/ext/getbalance/"
		scrivcmc = "https://coinmarketcap.com/currencies/scriv-network/"
		driver.get(scrivexplorer+scrivwallet)
		time.sleep(10)
		scrivbalance = float(driver.find_elements_by_xpath('/html/body')[0].text)
		html = requests.get(scrivcmc)
		doc = lxml.html.fromstring(html.content)
		span1 = doc.xpath('//span[@id="quote_price"]')
		scrivprice = float(span1[0][0].text)
		scrivtotal = scrivprice*scrivbalance
		print("SCRIV        ",round(scrivbalance,6),"       ",round(scrivtotal,6))
	except (KeyboardInterrupt, SystemExit):
		raise
	except:
		scrivtotal = 0
		print("Error getting SCRIV")
		pass

	try:
		#RVN
		rvnexplorer = "https://explorer.ravencoin.world/address/"
		rvncmc = "https://coinmarketcap.com/currencies/ravencoin/"
		driver.get(rvnexplorer+rvnwallet)
		time.sleep(10)
		rvnbalance = float(driver.find_elements_by_xpath('/html/body/div[3]/div[1]/table/tbody/tr/td[3]')[0].text)
		html = requests.get(rvncmc)
		doc = lxml.html.fromstring(html.content)
		span1 = doc.xpath('//span[@id="quote_price"]')
		rvnprice = float(span1[0][0].text)
		rvntotal = rvnprice*rvnbalance
		print("RVN          ",round(rvnbalance,6),"       ",round(rvntotal,6))
	except (KeyboardInterrupt, SystemExit):
		raise
	except:
		rvntotal = 0
		print("Error getting RVN")
		pass

	try:
		#BTC
		btcexplorer = "https://www.blockchain.com/btc/address/"
		btccmc = "https://coinmarketcap.com/currencies/bitcoin/"
		driver.get(btcexplorer+btcwallet)
		time.sleep(20)
		btcbalance = float(re.sub('BTC','',driver.find_elements_by_xpath('//*[@id="final_balance"]/font/span')[0].text))
		html = requests.get(btccmc)
		doc = lxml.html.fromstring(html.content)
		span1 = doc.xpath('//span[@id="quote_price"]')
		btcprice = float(span1[0][0].text)
		btctotal = btcprice*btcbalance
		print("BTC          ",round(btcbalance,6),"       ",round(btctotal,6))
	except (KeyboardInterrupt, SystemExit):
		raise
	except:
		btctotal = 0
		print("Error getting BTC")
		pass

	try:
		#GRV
		grvexplorer = "https://grv.ccore.online/address/"
		grvcmc = "https://www.coingecko.com/en/coins/gravium"
		driver.get(grvexplorer+grvwallet)
		time.sleep(10)
		grvbalance = float(re.sub('GRV','',driver.find_elements_by_xpath('/html/body/div/div[3]/table/tbody/tr[2]/td[1]')[0].text))
		driver.get(grvcmc)
		time.sleep(10)
		grvprice = float(re.sub('\$','',driver.find_elements_by_xpath('//*[@id="wrapper"]/div[4]/div[3]/div[1]/div[2]/div[1]/span')[0].text))
		grvtotal = grvprice*grvbalance
		print("GRV          ",round(grvbalance,6),"       ",round(grvtotal,6))
	except (KeyboardInterrupt, SystemExit):
		raise
	except:
		grvtotal = 0
		print("Error getting GRV")
		pass

	try:
		#HTH
		hthexplorer = "https://explorer.hthcoin.world/address/"
		hthcmc = "https://coinmarketcap.com/currencies/help-the-homeless-coin/"
		driver.get(hthexplorer+hthwallet)
		time.sleep(10)
		hthbalance = float(driver.find_elements_by_xpath('/html/body/div[3]/div[1]/table/tbody/tr/td[3]')[0].text)
		driver.get(hthcmc)
		time.sleep(10)
		hthprice = float(re.sub('\$','',driver.find_elements_by_xpath('//*[@id="quote_price"]/span[1]')[0].text))
		hthtotal = hthprice*hthbalance
		print("HTH          ",round(hthbalance,6),"       ",round(hthtotal,6))
	except (KeyboardInterrupt, SystemExit):
		raise
	except:
		hthtotal = 0
		print("Error getting HTH")
		pass

	try:
		#xdna
		xdnaexplorer = "http://explorer.xdna.io/address/"
		xdnacmc = "https://coinmarketcap.com/currencies/xdna/"
		driver.get(xdnaexplorer+xdnawallet)
		time.sleep(10)
		xdnabalance = float(driver.find_elements_by_xpath('/html/body/div[3]/div[1]/table/tbody/tr/td[3]')[0].text)
		driver.get(xdnacmc)
		time.sleep(10)
		xdnaprice = float(re.sub('\$','',driver.find_elements_by_xpath('//*[@id="quote_price"]/span[1]')[0].text))
		xdnatotal = xdnaprice*xdnabalance
		print("XDNA         ",round(xdnabalance,6),"       ",round(xdnatotal,6))
	except (KeyboardInterrupt, SystemExit):
		raise
	except:
		xdnatotal = 0
		print("Error getting XDNA")
		pass

	try:
		#suqa
		suqaexplorer = "http://suqaexplorer.com/address/"
		suqacmc = "https://coinmarketcap.com/currencies/suqa/"
		driver.get(suqaexplorer+suqawallet)
		time.sleep(10)
		suqabalance = float(driver.find_elements_by_xpath('/html/body/div[2]/div[3]/div[1]/table/tbody/tr/td[3]')[0].text)
		driver.get(suqacmc)
		time.sleep(10)
		suqaprice = float(re.sub('\$','',driver.find_elements_by_xpath('//*[@id="quote_price"]/span[1]')[0].text))
		suqatotal = suqaprice*suqabalance
		print("SUQA         ",round(suqabalance,6),"       ",round(suqatotal,6))
	except (KeyboardInterrupt, SystemExit):
		raise
	except:
		suqatotal = 0
		print("Error getting SUQA")
		pass

	try:
		#xvg
		xvgexplorer = "https://verge-blockchain.info/address/"
		xvgcmc = "https://coinmarketcap.com/currencies/verge/"
		driver.get(xvgexplorer+xvgwallet)
		time.sleep(10)
		xvgbalance = float(driver.find_elements_by_xpath('/html/body/div[3]/div[1]/table/tbody/tr/td[3]')[0].text)
		driver.get(xvgcmc)
		time.sleep(10)
		xvgprice = float(re.sub('\$','',driver.find_elements_by_xpath('//*[@id="quote_price"]/span[1]')[0].text))
		xvgtotal = xvgprice*xvgbalance
		print("XVG          ",round(xvgbalance,6),"       ",round(xvgtotal,6))
	except (KeyboardInterrupt, SystemExit):
		raise
	except:
		xvgtotal = 0
		print("Error getting XVG")
		pass

	try:
		#gtm
		gtmexplorer = "https://explorer.gtmcoin.io/address/"
		gtmcmc = "https://coinmarketcap.com/currencies/gentarium/"
		driver.get(gtmexplorer+gtmwallet)
		time.sleep(10)
		gtmbalance = float(driver.find_elements_by_xpath('/html/body/div[4]/table/tbody/tr/td[3]')[0].text)
		driver.get(gtmcmc)
		time.sleep(10)
		gtmprice = float(re.sub('\$','',driver.find_elements_by_xpath('//*[@id="quote_price"]/span[1]')[0].text))
		gtmtotal = gtmprice*gtmbalance
		print("GTM          ",round(gtmbalance,6),"       ",round(gtmtotal,6))
	except (KeyboardInterrupt, SystemExit):
		raise
	except:
		gtmtotal = 0
		print("Error getting GTM")
		pass

	try:
		#arg
		argexplorer = "https://chainz.cryptoid.info/arg/address.dws?"
		argcmc = "https://coinmarketcap.com/currencies/argentum/"
		driver.get(argexplorer+argwallet+".htm")
		time.sleep(10)
		argbalance = float(re.sub('ARG','',(driver.find_elements_by_xpath('//*[@id="balance"]')[0].text)))
		driver.get(argcmc)
		time.sleep(10)
		argprice = float(re.sub('\$','',driver.find_elements_by_xpath('//*[@id="quote_price"]/span[1]')[0].text))
		argtotal = argprice*argbalance
		print("ARG          ",round(argbalance,6),"       ",round(argtotal,6))
	except (KeyboardInterrupt, SystemExit):
		raise
	except:
		argtotal = 0
		print("Error getting ARG")
		pass

	try:
		#abs
		absexplorer = "http://explorer.absolutecoin.net/address/"
		abscmc = "https://coinmarketcap.com/currencies/absolute/"
		driver.get(absexplorer+abswallet)
		time.sleep(10)
		absbalance = float(driver.find_elements_by_xpath('/html/body/div[3]/div[1]/table/tbody/tr/td[3]')[0].text)
		driver.get(abscmc)
		time.sleep(10)
		absprice = float(re.sub('\$','',driver.find_elements_by_xpath('//*[@id="quote_price"]/span[1]')[0].text))
		abstotal = absprice*absbalance
		print("ABS          ",round(absbalance,6),"       ",round(abstotal,6))
	except (KeyboardInterrupt, SystemExit):
		raise
	except:
		abstotal = 0
		print("Error getting ABS")
		pass

	try:
		#resq
		resqexplorer = "http://explorer.resqchain.org:3001/address/"
		resqcmc = "https://www.coingecko.com/en/coins/resq-chain"
		driver.get(resqexplorer+resqwallet)
		time.sleep(10)
		resqbalance = float(driver.find_elements_by_xpath('/html/body/div[3]/div[1]/table/tbody/tr/td[3]')[0].text)
		driver.get(resqcmc)
		time.sleep(10)
		resqprice = float(re.sub('\$','',driver.find_elements_by_xpath('//*[@id="wrapper"]/div[4]/div[3]/div[1]/div[2]/div[1]/span')[0].text))
		resqtotal = resqprice*resqbalance
		print("RESQ         ",round(resqbalance,6),"       ",round(resqtotal,6))
	except (KeyboardInterrupt, SystemExit):
		raise
	except:
		resqtotal = 0
		print("Error getting RESQ")
		pass

	try:
		#linx
		linxexplorer = "https://chainz.cryptoid.info/linx/address.dws?"
		linxcmc = "https://coinmarketcap.com/currencies/linx/"
		driver.get(linxexplorer+linxwallet+".htm")
		time.sleep(10)
		linxbalance = float(re.sub('LINX','',driver.find_elements_by_xpath('//*[@id="balance"]')[0].text))
		driver.get(linxcmc)
		time.sleep(10)
		linxprice = float(re.sub('\$','',driver.find_elements_by_xpath('//*[@id="quote_price"]/span[1]')[0].text))
		linxtotal = linxprice*linxbalance
		print("LINX         ",round(linxbalance,6),"       ",round(linxtotal,6))
	except (KeyboardInterrupt, SystemExit):
		raise
	except:
		linxtotal = 0
		print("Error getting LINX")
		pass

	try:
		#priv
		privexplorer = "https://explorer.privcy.io/address/"
		privcmc = "https://coinmarketcap.com/currencies/privcy/"
		driver.get(privexplorer+privwallet)
		time.sleep(10)
		privbalance = float(driver.find_elements_by_xpath('/html/body/div[3]/div[1]/table/tbody/tr/td')[0].text)
		driver.get(privcmc)
		time.sleep(10)
		privprice = float(re.sub('\$','',driver.find_elements_by_xpath('//*[@id="quote_price"]/span[1]')[0].text))
		privtotal = privprice*privbalance
		print("PRIV         ",round(privbalance,6),"       ",round(privtotal,6))
	except (KeyboardInterrupt, SystemExit):
		raise
	except:
		privtotal = 0
		print("Error getting PRIV")
		pass

	try:
		#mdex
		mdexexplorer = "http://explorer.moondexcoin.org/address/"
		mdexcmc = "https://www.livecoinwatch.com/price/MoonDEX-MDEX"
		driver.get(mdexexplorer+mdexwallet)
		time.sleep(10)
		mdexbalance = float(driver.find_elements_by_xpath('/html/body/div[3]/div[1]/table/tbody/tr/td[3]')[0].text)
		driver.get(mdexcmc)
		time.sleep(10)
		mdexprice = float(re.sub('Price\n\$','',driver.find_elements_by_xpath('//*[@id="usd"]')[0].text))
		mdextotal = mdexprice*mdexbalance
		print("MDEX         ",round(mdexbalance,6),"       ",round(mdextotal,6))
	except (KeyboardInterrupt, SystemExit):
		raise
	except:
		mdextotal = 0
		print("Error getting MDEX")
		pass

	try:
		#almn
		almnexplorer = "https://ex.allmn.org/address/"
		almncmc = "https://www.worldcoinindex.com/coin/allmn"
		driver.get(almnexplorer+almnwallet)
		time.sleep(10)
		almnbalance = float(driver.find_elements_by_xpath('/html/body/div[3]/div/div/div[1]/table/tbody/tr/td[3]')[0].text)
		driver.get(almncmc)
		time.sleep(10)
		almnprice = float(re.sub('\$','',driver.find_elements_by_xpath('/html/body/div[2]/div[3]/div[3]/div[2]/div[2]/div/div/table/tbody/tr/td[3]')[0].text))
		almntotal = almnprice*almnbalance
		print("ALMN         ",round(almnbalance,6),"       ",round(almntotal,6))
	except (KeyboardInterrupt, SystemExit):
		raise
	except:
		almntotal = 0
		print("Error getting ALMN")
		pass

	amount = grvtotal + btctotal + scrivtotal + rvntotal + hthtotal + almntotal + mdextotal + privtotal + linxtotal + resqtotal + abstotal + gtmtotal + argtotal + xvgtotal + suqatotal + xdnatotal
	print('====          =======          =========')
	print('                              ',round(amount,6))
	# store current time quickly
	now = int(time.time())
	plt.gcf().clear()

	if os.path.isfile("store.csv"):
		df = pd.read_csv("store.csv", header=0, index_col=0)
		counter = 1
	else:
		pass
	
	if counter < 1:
		df.loc[0] = [now, amount]
		plt.plot(df['time'].iloc[-50:],df['amount'].iloc[-50:])
		df.to_csv("store.csv")
	
	else:
		# add data to bottom of dataframe
		df.loc[df.index[-1]+1] = [now,amount]
		plt.plot(df['time'].iloc[-50:],df['amount'].iloc[-50:])
		df.to_csv("store.csv")

	plt.draw()
	plt.pause(0.0001)
	counter += 1
	time.sleep(60)

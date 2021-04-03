print('Enter either Daily or Weekly')
DailyOption = ['daily' , 'D' , 'd' , 'Daily', 'DAILY']
WeeklyOption = ['Weekly' , 'w' , 'weekly' , 'W' ,'WEEKLY']
dpc = input('Enter Daily or weekly ')
et = str(dpc)
if et in DailyOption :
		dh = input ('Work hour:  ')
		dr = input ('Rate per hour:  ')
		try :
			fdh = float(dh)
			fdr = float(dr)
		except :
			print('enter numerical value')
			quit()
		dpm = fdh*fdr
		if fdh > 24 :
			print('A day has only 24 hours')
		elif fdh > 8 :
			try :
				owr = input('% charge for extra hour:  ')
				fwr = float(owr)
				tdp = dpm + (fdh-8)*(fwr/10)
				print ('Payment for the day: ' , tdp )
			except :
				print ('Error , put numerical value')
				quit()
		else :
			print('Payment for the day: ', dpm )
elif et in WeeklyOption :
	sh = input('Work Hour(w): ')
	sr = input('per hour rate: ')
	try:
	  fh = float(sh)
	  fr = float(sr)
	except:
		print('Error, put numerical value')
		quit()
	pm = fh * fr
	if fh >168 :
		print('there are only 168 hours in a week')
	elif fh > 40 :
		try:
			ser = input('% charge for extra hours: ')
			fer = float(ser)
			otpm = (pm) +(fh-40)*(fer/10)
			print('Pay: ', otpm)
		except:
			print('Error, put numerical value')
			quit()
	else :
		print('Payment for the week', pm)
else :
	print('invalid input')